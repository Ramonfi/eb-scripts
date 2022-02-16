import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import src.project_definitions as eb
import logging as log
import src.config as config
import sys
import src.utilities as ut

###############################################################___Functions___###############################################################
#############################################################################################################################################

def load_tf_file(path):
    df = pd.read_csv(
        path,
        engine='python',
        encoding= 'unicode_escape',
        sep=';',
        na_values=['-',' ','#N/V','#NV'],
        decimal=',',
        index_col=False)
    
    df = df[df.iloc[:, 0] != df.columns[0]]

    if len(df) < 1:
        return

    not_empty_cols = [(col, df.columns.get_loc(col)) for col in df.replace(' ', np.NaN).filter(like='Unnamed:').dropna(axis=1).columns]
    cols = df.columns.to_list()
    for not_empty_col in not_empty_cols:
        i = not_empty_col[1]
        j = not_empty_col[1]
        while True:
            j+=1
            if len(df.iloc[:,j].dropna()) == 0:
                break
        delta = (j - not_empty_col[1])
        for n in range(delta):
            cols[i+n],cols[i+n+1] = cols[i+n+1],cols[i+n]
            print(f'{cols[i+n]} <-> {cols[i+n+1]}')
        df.columns = cols

    df.drop(list(df.filter(like='named').columns), axis=1, inplace=True)

    df.columns = df.columns.str.replace('HM', 'MH')

    df.drop_duplicates(ignore_index=True, inplace=True)

    if len(df)<1:
        return
    else:
        drop=[]
        for c, col in enumerate(df.columns):
            if col == 'Date' or col == 'Datum':
                date=col
                drop.append(col)
            if col == 'Time' or col =='Uhrzeit':
                time=col
                drop.append(col)

        df.insert(0,'Datetime',pd.to_datetime(df[date] +' '+ df[time],dayfirst=True))
        df.drop(drop,axis=1,inplace=True)

        if df.Datetime.is_unique != True:
            df.drop_duplicates(ignore_index=True, inplace=True, keep='last')
        df.dropna(axis=1, how='all', inplace=True)
        df.set_index('Datetime',inplace=True)
        df.sort_index(axis=0, inplace=True)
        return df

########################################################## Set environmental values #########################################################
#############################################################################################################################################

log.basicConfig(
    format='%(asctime)s -- %(levelname)s -- %(message)s', 
    datefmt='%d.%m.%Y %H:%M:%S', 
    level=log.INFO,
    encoding='utf-8',
    handlers=[
        log.FileHandler(f"logs/{dt.date.today().strftime('%y_%m_%d')}_einfach-bauen.log"),
        log.StreamHandler()]
    )


#Speicherort für neue Tinker-Forge Datensätze:
dropbox = eb.tf_path

#Speicherort von allen alten (TinkerForge-)Datensätzen (Vor der Dropbox...)
arch_loc = eb.tf_archive

########################################################## Set environmental values #########################################################
#############################################################################################################################################


#Dateikürzel im Archiv
buid = ['LB','MH','MW','WD']
buid_long ={'LB':'Leichtbetonhaus','MH':'Massivholzhaus','MW':'Ziegelhaus', 'WD':'Wetterstation', 'PM':'Pyranometer'}

################################################################ MAIN SCRIPT ################################################################
#############################################################################################################################################

def energymeter(send=True, plot=False):
    log.info(f'------ EnergyMeter ------')

    # Speicherort für neue Moiline Datensätze
    files = [os.path.join(eb.em_path,name) for name in os.listdir(eb.em_path)]
    n_files = len(files)

    # Öffne Config-File zur Zuordnung der Moiline Senoren zu den Wohneinheiten
    name_file = './src/energymeter.config'
    if not os.path.isfile(name_file):
        print('name-file für EnergyMeter nicht gefunden...!')
        sys.exit
    meters = pd.read_csv(name_file,sep=';')

    #startdate of regular observations for energymeter
    start = dt.datetime(2021,9,2)

    data = []
    # reading datasheets
    log.info(f'Reading files.')

    # Speicherort der Einfach-Bauen-Datenbanken
    db_loc = eb.dir_db

    # Lese die einzelnen Datensheets ein...
    for nf, fn in enumerate(files):
        # Die Datensheets werden importiert...
        datasheet = pd.read_csv(fn,  
            engine='python',
            sep=';',
            na_values=['-','#N/V','#NV'],
            decimal= ',')
        # ...und einer Liste hinzugefügt.
        data.append(datasheet)
        ut.running_bar(nf,n_files)

    # Anschließend werden alle Datensheets in der Liste in einen Pandas-DataFrame übersetzt.
    df = pd.concat(data,ignore_index=True)
    # Nun müssen noch die Zeitstempel vereinheitlicht werden...
    df.insert(0,'Datetime', pd.to_datetime(df['Timestamp']))
    df['Datetime'] = df['Datetime'].dt.tz_localize(None)
    df = df.drop(axis=1,labels='Timestamp')
    log.info(f'Reading files finished.')

    # Die Datenbank wird jetzt noch etwas aufgeräumt...
    
    log.info(f'Starting postprocessing.')
    df = df[df['Datetime']>pd.Timestamp(start)]             # Alle Datensätze vor dem Startdatum werden aussoritiert
    df = df.dropna(axis = 1,how='all')                      # Leere Spalten werden gelöscht
    df = df.drop(axis=1,labels=['ID','SN','IP','State'])    # Uninteressante Spalten werden gelöscht
    df = df.sort_values(by=['Datetime'])                    # Die Datensätze werden nach Zeitstempel soriert

    df['HQ'] = pd.to_numeric(df.HQ, errors='coerce')        # Die Messdaten werden vom str() in einen float() Wert übersetzt
    df['VW'] = pd.to_numeric(df.VW, errors='coerce')        # Die Messdaten werden vom str() in einen float() Wert übersetzt

    for i, tpid in enumerate(meters.TPID):
        df.loc[df.TPID.str.contains(str(tpid)), 'type']=meters.Medium[i]    # rename meter (type)
        df.loc[df.TPID.str.contains(str(tpid)), 'bui']=meters.Haus[i]       # rename meter (building)
        df.loc[df.TPID.str.contains(str(tpid)), 'app']=meters.Wohnung[i]    # rename meter (appartment)
    df = df.set_index(['bui','app', 'type', 'Datetime']).sort_index()       # sort DataFrame
    log.info(f'Postprocessing finished.')

    # exporting database
    log.info(f'Starting export to directory: {db_loc}.')

    ## creating paths to database
    export = {bui : os.path.join(db_loc, bui) for bui in list(meters.Haus.unique())}
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

    if plot:
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
        if not os.path.isdir(exdir):
            os.makedirs(exdir)
        f.savefig(os.path.join(exdir,f'EM_Monitoring_Datenempfang_Übersicht.png'),dpi=300)
    log.info(f'EnergyMeter: FINISHED')

def tinkerforge(send=True, OverwriteDatabase=False):
    log.info(f'------ Starte TinkerForge ------')
    # Export Ordner
    db_loc = eb.dir_db      #database location

    #Erstelle Pfade zu den tinkerforge Datenbanken
    db = {bui : os.path.join(db_loc,bui,'{}_tf_raw.csv'.format(bui)) for bui in buid_long}
    for bui in db:
        if os.path.isdir(os.path.dirname(db[bui])) == False:
            os.makedirs(os.path.dirname(db[bui]))

    files = {}      #dict with path to archived datasheets
    master_df={}    #dict with database as DataFrame
    log.info(f'Suche vorhandene Datenbank.')
    for bui in buid:
        if not OverwriteDatabase and os.path.isfile(db[bui]):
            log.info(f'{bui}: Datenbank gefunden!')
            continue
        else:
            log.info(f'{bui}: Keine Datenbank gefunden - erstelle neue aus dem Archiv.')
            bui_path = os.path.join(arch_loc, bui)  # path to current bui-folder
            files[bui] = [os.path.join(bui_path, fn) for fn in os.listdir(bui_path) if fn.endswith('.csv') ]    # create paths to current bui's datasheets
            files[bui].sort(key=lambda x: os.path.getmtime(x))  # sort datasheets
            n_files = len(files[bui])
            df = []
            for nf, file in enumerate(files[bui]):
                ut.running_bar(nf,n_files)
                df.append(load_tf_file(file))

            master_df[bui] = pd.concat(df)  # concainate datasheets to one big DataFrame
            log.info(f'{bui}: Archivierte Datensätze geladen. Erstelle Datenbank.')
            ## remove duplicates...
            if master_df[bui].index.is_unique == False: 
                master_df[bui] = master_df[bui][~master_df[bui].index.duplicated(keep='first')]
                if master_df[bui].index.is_unique:
                    log.warning(f'{bui}: Doppelte Zeilen entfernt.')
            ## remove duplicated columns
            if len(master_df[bui].filter(like='.1').columns) >0:
                log.warning(f'{bui}: Doppelte Spalten entfernt.')
            ## warn if there is still a problem...
            master_df[bui].dropna(axis=1, how='all',inplace=True)
            if master_df[bui].index.has_duplicates:
                log.warning(f'{bui}: Indexfehler in der (Archiv)-Datenbank!')
            ## finally saving database...
            log.info(f'{bui}: Erstellen der neuen Datenbank abgeschlossen. Exportiere die Datenbank.')
            master_df[bui].to_csv(db[bui], index=True)
            log.info(f'{bui}: Speichern der Datenbank erfolgreich.')

    #Öffne Messdaten aus Dropbox die noch nicht in der Datenbank sind...
    log.info('Lade neue Datensätze aus Dropbox.')
    dropbox_files = {}
    dropbox_df = {}
    notification = {}
    offline = {}
    database = {}
    for bui in buid_long:
        log.info(f'{bui}: Öffne vorhandene Datenbank.')
        try:
            database[bui] = pd.read_csv(db[bui], parse_dates=['Datetime'], dayfirst=True, index_col='Datetime')
        except:
            if bui == 'PM':
                database[bui] = database['LB'].filter(like='DA')
                database[bui].columns = ['Global W/m^2','Direct W/m^2','Diffuse W/m^2']
        if database[bui].index.is_unique == False:
            log.warning(f'{bui}: Achtung! Datensatz enthält Duplikate.')
            try:
                database[bui] = database[bui][~database[bui].index.duplicated(keep='first')]
                if database[bui].indes.is_unique:
                    log.warning(f'{bui}: Datenbank bereinigt!')
                else:
                    log.warning(f'{bui}: Datenbankfehler, überspringe Gebäude!')
                    continue
            except Exception as e:
                log.warning(f'{bui}: Datenbankfehler {e}')
                log.warning(f'{bui}: Überspringe Gebäude!')

        cols_db = len(database[bui].columns)
        dropbox_path = os.path.join(dropbox, bui)
        dropbox_files[bui] = [os.path.join(dropbox_path, fn) for fn in os.listdir(dropbox_path) if fn.endswith(f'{bui}.csv') ]
        dropbox_files[bui].sort(key=lambda x: os.path.getmtime(x))

        last_day = pd.to_datetime(os.path.basename(dropbox_files[bui][-1]).rsplit('_',1)[0],format='%Y_%m_%d')
        last_day_soll = dt.datetime.today().date()-dt.timedelta(1)

        if last_day.date() == dt.date.today():
            last_file = dropbox_files[bui].pop(-1)
            log.info(f'{bui}: Datei von Heute ({os.path.basename(last_file)}) wird übersprungen!')
        if last_day.date() < last_day_soll:
            offline[bui] = f'{buid_long[bui]} liefert seit {last_day.to_pydatetime().strftime("%d.%m.%Y")} ({((dt.datetime.today()-last_day.to_pydatetime()).days)} Tage(n)) keine neuen Daten mehr.'
            log.info(offline[bui])

        log.info(f'{bui}: Durchsuche Dropbox nach neuen Datensätzen.')
        
        df1 = []
        n_files = len(dropbox_files[bui])
        for n, file in enumerate(dropbox_files[bui]):
            ut.running_bar(n,n_files)
            try:
                test = pd.read_csv(
                        file,
                        encoding= 'unicode_escape',
                        engine='python',
                        sep=';',
                        nrows=1,
                        na_values=['-','#N/V','#NV'],
                        decimal=',')
                test.reset_index(drop=True)
                test.dropna(axis=1, how='all',inplace=True)
                test.drop(list(test.filter(like='named').columns), axis=1, inplace=True)
                test.drop_duplicates(ignore_index=True, inplace=True)

                drop=[]
                for c, col in enumerate(test.columns):
                    if col == 'Date' or col == 'Datum':
                        d=c
                        date=col
                        drop.append(col)
                    if col == 'Time' or col =='Uhrzeit':
                        t=c
                        time=col
                        drop.append(col)
                test.insert(0,'Datetime',pd.to_datetime(test[date] +' '+ test[time],dayfirst=True))
                test.drop(drop,axis=1,inplace=True)
                test.set_index('Datetime',inplace=True)
                test.sort_index(axis=0, inplace=True)

                test.columns = test.columns.str.replace('HM', 'MH')
                
                if test.index.isin(database[bui].index) == False:
                    newdate = pd.to_datetime(test.index.values.min()).date()
                    log.info(f'--- {newdate}: Neue Datei gefunden!')
                    newday = load_tf_file(file)

                    for sensor in newday:
                        check = newday[sensor].isna().sum()/len(newday.index)
                        if check > 0.1:
                            if bui not in notification:
                                notification[bui] = {}
                            if sensor in notification[bui]:
                                notification[bui][sensor][newdate] = int((1-check)*100)
                            else:
                                notification[bui][sensor] = {newdate : int((1-check)*100)}
                    df1.append(newday)
            except Exception as e:
                log.warning(e)
        try:        
            dropbox_df[bui] = pd.concat(df1)
            if dropbox_df[bui].index.has_duplicates:
                log.warning(f'{bui}: Datenbank enthält Duplikate!')
                dropbox_df[bui] = dropbox_df[bui][~dropbox_df[bui].index.duplicated(keep='first')]
                log.warning(f'{bui}: Duplikate bereinigt.')
            if len(dropbox_df[bui].filter(like='.1').columns) >0:
                for col in dropbox_df[bui].filter(like='.1'):
                    log.warning(f'Achtung: {col} wurde dupliziert statt ergänzt...')
            log.info(f'{bui}: Speichere neue Datensätze in Dictionary und fahre fort...')
        except:
            log.info(f'{bui}: Keine neue Datei(en) gefunden.')
            continue

    # send missing data report
    for bui in list(notification):
        for key in list(notification[bui]):
            if 'named' in key:
                notification[bui].pop(key)
                log.warning(f'{bui}: unnamed column in data.')

    if len(offline) == 0 and len(notification) == 0:
        log.info('Keine neuen Datensätze oder alles läuft einwandfrei...')
    else:
        text = 'Hallo,\ndie folgenden Sensoren haben in den vergangenen Tagen ungewöhnlich wenige Daten aufgezeichnet:\n\nHinweis:\nDie Liste führt Tage auf, an denen ein Sensor weniger als 90% der Datensätze aufgezeichnet hat. Fehlende Tage in der Aufzählung bedeuten, dass an diesen Tagen mehr als 90% der Daten aufgezeichnet wurden\n'

        if len(offline)==0:
            text += '\n\n---------ALLE HÄUSER ONLINE - DROPBOX-SYNC FUNKTIONIERT---------\n\n'

        for bui in buid_long:
            if bui in offline or bui in notification:
                text +='\n------'+ buid_long[bui] + ':------\n'
            if bui in offline:
                text += '\n!!! ' + offline[bui] + ' !!!\n'
            if bui in notification:
                for sensor in notification[bui]:
                    text += '\n' + sensor + ':\n'
                    for day in notification[bui][sensor]:
                        text += '\t{}: {}% Messwerte vorhanden.\n'.format(day, notification[bui][sensor][day])
            if send==False:
                log.debug(text)

        if len(notification) > 0 and send==True:
            try:
                ut.send_email(who=[config.emails['roman']],sender=config.emails['sender'],subject='EINFACH MESSEN: SENSORS NOT WORKING!',text=text,password=config.password,smtp=config.smtp)
                log.info(f'Sensordaten-Übersicht gesendet')
            except Exception as e:
                log.warning(f'Senden der Nachricht fehlgeschlagen: {e}')

    # send offline notification            
    if len(offline) == 0:
        log.info('Keine neuen Datensätze oder alles läuft einwandfrei...')
    else:
        text = 'Hallo,\ndas ist eine automatisch erzeugte Fehlermeldung der Einfach-Bauen-Haeuser:\n\n'

        for bui in offline:
            text += '-> Das/Die ' + offline[bui] + '\n'

        if send==False:
            log.debug(text)

        if len(offline) > 0 and send==True:
            try:
                ut.send_email(who=[config.emails['roman']],sender=config.emails['sender'],subject='EINFACH MESSEN: OFFLINE ALERT!',text=text,password=config.password,smtp=config.smtp)
                log.info(f'Offline Benachrichtigung gesendet!')
            except Exception as e:
                log.warning(f'Senden der Nachricht fehlgeschlagen: {e}')

    # Füge neue Daten der Datenbank hinzu und speichere die aktualisierte Datenbank ab.
    log.info('4_ Speichere aktualisierte Datenbank...')
    if len(dropbox_df)==0:
        log.info('Keine neuen Datensätze...')
    else:
        for bui in dropbox_df:
            log.info(f'{bui}: Überprüfe neue Datensätze aus Dropbox...')
            if dropbox_df[bui].index.has_duplicates:
                log.warning(f'{bui}: Index enthält Duplikate!')
                try:
                    dropbox_df[bui] = dropbox_df[bui][~dropbox_df[bui].index.duplicated(keep='first')]
                    log.info(f'{bui}: Duplikate erfolgreich bereinigt!')
                except Exception as e:
                    log.info(f'{bui}: Leider stimmt immer noch was nicht')
                    log.warning(f'{bui}: {e}')
                    log.info(f'{bui}: Überspringe Datensatz')
                    continue
                finally: 
                    if dropbox_df[bui].index.is_unique:
                        log.info(f'{bui}: Duplikate bereinigt. Datenbank in Ordnung.')

            log.info(f'{bui}: Füge neue Einträge zur Datenbank hinzu.')

            df = pd.concat([database[bui], dropbox_df[bui]])
            df.dropna(axis=1, how='all', inplace=True)
            df.sort_index(axis=0, inplace=True)

            sensors = []

            for col in df.columns:
                sensor = col
                for i, name in enumerate(sensor.split(' ')):
                    # Unerwünschte Strings vom Anfang der Sensorbezeichnung abschneiden (z.B. [Black Globe], o.ä.)
                    if name.startswith(bui):
                        sensor = ' '.join(sensor.split(' ')[i:])
                sensors.append(sensor)
            df.columns = sensors

            raw_sensor_id = df.columns.str.split(' ',expand=True).get_level_values(level=0)

            for col in df.columns[raw_sensor_id.duplicated()]:
                dupes = df.filter(like=col.split(' ')[0]).columns.tolist()
                for dupe in dupes:
                    if dupe == col:
                        dupes.remove(dupe)
                for dupe in dupes:
                    df[col].fillna(df[dupe])
                    df.drop(dupe,axis=1,inplace=True)

            if df.index.is_unique == False:
                    log.warning(f'{bui}: Index hat Duplikate.')
                    log.info(f'{bui}: Versuche doppelte Einträge zu löschen...')
                    df = df[~df.index.duplicated(keep='first')]
                    if df.index.is_unique:
                        log.info(f'{bui}: Erfolgreich bereinigt!')
                    else:
                        log.info(f'{bui}: Index Fehler!')
                        continue
            if len(df.filter(like='.1').columns)>0:
                for col in df.filter(like='.1').columns:
                    log.info(f'Spalte: {col} wurde dupliziert.')
            else:
                log.info(f'{bui}: Super! Keine doppelten Einträge mehr in der Datenbank. Starte Datenbankexport...')

            
            database[bui] = df

            anfang = database[bui].index.min()
            ende = database[bui].index.max()

            database[bui].to_csv(db[bui])
            log.info(f'{bui}: Aktueller Datenzeitraum: {anfang} bis {ende}.')
            for ts in ['1min', '15min', '60min']:
                if os.path.isdir(os.path.join(db_loc,bui)) == False:
                    os.makedirs(os.path.join(db_loc,bui))
                
                df_resampled = database[bui].resample(ts).last().asfreq(ts)
                
                df_resampled.to_csv(os.path.join(db_loc,bui,'{}_tf_database_resampled_{}.csv'.format(bui, ts)))
                log.debug(f'{bui}: Resampled auf {ts}')
            log.info(f'{bui}: Datenbanken exportiert!')
    log.info('TinkerForge: FINISHED')

logpath = './logs'
onlyfiles = [os.path.join(logpath, f) for f in os.listdir(logpath) if os.path.isfile(os.path.join(logpath, f))]
onlyfiles.sort(key=lambda x: os.path.getmtime(x))
for logfile in onlyfiles:
    with open(logfile,encoding='latin-1') as f:
        f = f.read().splitlines()
        data = []
        for line in f:
            line = line.split(' -- ')
            if line[1] == 'INFO' and (line[2] == '------ EnergyMeter finished! ------'or line[2] == 'EnergyMeter: FINISHED'):
                Stand_EnergyMeter = dt.datetime.strptime(line[0], '%d.%m.%Y %H:%M:%S')
            if line[1] == 'INFO' and (line[2] == 'TinkerForge Update komplett!' or line[2] == 'TinkerForge: FINISHED'):
                Stand_TinkerForge = dt.datetime.strptime(line[0], '%d.%m.%Y %H:%M:%S')
if Stand_TinkerForge.date() == dt.date.today():
    print('Tinkerforge up-to-date')
else:
    tinkerforge()

if Stand_EnergyMeter.date() == dt.date.today():
    print('EnergyMeter up-to-date')
else:
    energymeter()
    print('EnergyMeter Nessesarry')