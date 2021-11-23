
import pandas as pd
import datetime as dt
import os
import matplotlib.pyplot as plt
import eb
import logging as log



def main(lehrstuhl=False):
    log.basicConfig(
        format='%(asctime)s -- %(levelname)s -- %(message)s', 
        datefmt='%d.%m.%Y %H:%M:%S', 
        level=log.INFO,
        encoding='utf-8',
        handlers=[
            log.FileHandler("debug.log"),
            log.StreamHandler()]
        )

    log.info(f'Start Wärmemengenzähler')
    log.info(f'Export to Lehrstuhl = {lehrstuhl}')
    ##############################################################___Input Daten___##############################################################
    #############################################################################################################################################
    #paths
    em_path = eb.em_path    #new datasheets
    files = [os.path.join(em_path,name) for name in os.listdir(em_path)]
    n_files = len(files)

    db_loc = eb.dir_db      #database location
    if lehrstuhl:
        db_loc = os.path.join(eb.dir_db_ls,'EM')

    #open name-file to assign meter ID to building/app/meter
    name_file = 'energymeter.config'
    name_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),name_file)
    if not os.path.isfile(name_file):
        log.warning('name-file nicht gefunden...!')
        quit()
    meters = pd.read_csv(name_file,sep=';')

    #startdate of regular observations
    start = dt.datetime(2021,9,2)

    ################################################################___Skript___#################################################################
    #############################################################################################################################################
    data = []
    # reading datasheets
    log.info(f'Start reading files from Database.')

    for nf, fn in enumerate(files):
        eb.running_bar(nf,n_files)
        datasheet =         pd.read_csv(fn,  
            engine='python',
            sep=';',
            na_values=['-','#N/V','#NV'],
            decimal= ','
        )
        datasheet.insert(0,'Datetime',pd.to_datetime(datasheet['Timestamp'],yearfirst=True,dayfirst=False,infer_datetime_format=True))
        datasheet = datasheet.drop(axis=1,labels = 'Timestamp')
        data.append(datasheet)
    df = pd.concat(data,ignore_index=True)

    # postprocessing data
    log.info(f'finished reading files. Starting postprocessing.')

    df = df[df['Datetime']>start]       #set start date
    df = df.dropna(axis = 1,how='all')  #drop empty columns
    df = df.drop(axis=1,labels=['ID','SN','IP','State'])    #drop irelevant columns
    df = df.sort_values(by=['Datetime'])    # sort by time

    df['HQ'] = pd.to_numeric(df.HQ, errors='coerce')    #convert to float
    df['VW'] = pd.to_numeric(df.VW, errors='coerce')    #convert to float

    for i, tpid in enumerate(meters.TPID):
        df.loc[df.TPID.str.contains(str(tpid)), 'type']=meters.Medium[i]    # rename meter (type)
        df.loc[df.TPID.str.contains(str(tpid)), 'bui']=meters.Haus[i]       # rename meter (building)
        df.loc[df.TPID.str.contains(str(tpid)), 'app']=meters.Wohnung[i]    # rename meter (appartment)
    df = df.set_index(['bui','app', 'type', 'Datetime']).sort_index()       # sort DataFrame

    ## extracting variants
    buids_em = list(meters.Haus.unique())

    # exporting database
    log.info(f'starting export to {db_loc}.')

    ## creating paths to database
    export = {bui : os.path.join(db_loc, bui) for bui in buids_em}
    for bui in export:
        if os.path.isdir(export[bui]) == False:
            os.makedirs(export[bui])

    ## exporting DataFrames
    database = {}
    for bui, group in df.groupby(level=0):     #group by building
        if group.index.is_unique == False:
            group = group[~group.index.duplicated(keep='first')]    # remove duplicates
        database[bui] = group.droplevel(0).unstack(level=[0,1]).swaplevel(0,-1,axis=1).swaplevel(0,1,axis=1).sort_index(axis=1).dropna(axis=1, how='all').sort_index(axis=0)    #reshaping datastructure
        database[bui].to_csv(os.path.join(export[bui], f'{bui}_em_database.csv'))   # saving raw database
        for ts in ['1min']:
            database[bui].resample(ts).fillna('pad').to_csv(os.path.join(export[bui], f'{bui}_em_resampled_{ts}.csv'))  # saving reshaped database

    # plotting graph...
    log.info(f'creating overview graph.')

    ## preparing data
    timemax = max([database[bui].index.max().date() for bui in eb.buid])
    level_values = df.index.get_level_values
    result = (df.groupby([level_values(i) for i in [0,1,2]]
                        +[pd.Grouper(freq='D', level=-1)]).size())  # count observations
    result = pd.DataFrame(result, columns=['n_data'])   # make DataFrame of it
    result.reset_index(level=[0,1,2],inplace=True)      # clean up DataFrame
    result['meter'] = result['bui'] + '_' + result['app'] + '_' + result['type']    #clean up index
    result.drop(['bui','app','type'],axis=1,inplace=True)   # remove unneeded columns

    ## plotting
    f, ax = plt.subplots(figsize=(15,10))
    ax.plot(result.index, result.meter, linestyle='None')
    sc = ax.scatter(result.index, result.meter, c=result.n_data, s=len(result.index.unique()), alpha=0.75,marker = 's', cmap='RdYlGn')
    cbar = f.colorbar(sc)
    cbar.set_label("Observations per day ", loc='top')
    f.suptitle(f'Übersicht Datenempfang Wärmemengenzähler\nStand: {timemax}')
    f.tight_layout()

    ## exporting graph.
    exdir = os.path.join(eb.dir_results,'Allgemein')
    if lehrstuhl:
        exdir = os.path.join(eb.dir_results_ls,'Allgemein')
    if not os.path.isdir(exdir):
        os.makedirs(exdir)
    f.savefig(os.path.join(exdir,f'EM_Monitoring_Datenempfang_Übersicht.png'),dpi=300)
    log.info(f'finished!')

if __name__ == "__main__":
    main()