
import pandas as pd
import datetime as dt
import os
import matplotlib.pyplot as plt
import eb

##############################################################___Input Daten___##############################################################
#############################################################################################################################################

lehrstuhl = False
em_path = eb.em_path
db_loc = eb.dir_db
if lehrstuhl:
    db_loc = os.path.join(eb.dir_db_ls,'EM')

name_file = 'energymeter.config'
name_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),name_file)

if not os.path.isfile(name_file):
    print('config file nicht gefunden...!')
    quit()

meters = pd.read_csv(name_file,sep=';')

filenames = os.listdir(em_path)
files = [os.path.join(em_path,name) for name in os.listdir(em_path)]

start = dt.datetime(2021,9,2)

################################################################___Skript___#################################################################
#############################################################################################################################################
data = []
print(f'-start reading files from Database...')
for fn in files:
    datasheet =         pd.read_csv(fn,  
        engine='python',
        sep=';',
        dayfirst=True,
        infer_datetime_format=True,
        na_values=['-','#N/V','#NV'],
        decimal= ','
    )
    datasheet.insert(0,'Datetime',pd.to_datetime(datasheet['Timestamp'],yearfirst=True,dayfirst=False,infer_datetime_format=True))
    datasheet = datasheet.drop(axis=1,labels = 'Timestamp')
    data.append(datasheet)

df = pd.concat(data,ignore_index=True)
print(f'--finished reading files. Starting postprocessing...')
df = df[df['Datetime']>start]
df = df.dropna(axis = 1,how='all')
df = df.drop(axis=1,labels=['ID','SN','IP','State'])
df = df.sort_values(by=['Datetime'])

df['HQ'] = pd.to_numeric(df.HQ, errors='coerce')
df['VW'] = pd.to_numeric(df.VW, errors='coerce')

counts = df.TPID.value_counts()

dth = (df['Datetime'].max()-df['Datetime'].min()).total_seconds()/60/60*12
dtw = (df['Datetime'].max()-df['Datetime'].min()).total_seconds()/60/60*8

for i, tpid in enumerate(meters.TPID):
    df.loc[df.TPID.str.contains(str(tpid)), 'type']=meters.Medium[i]
    df.loc[df.TPID.str.contains(str(tpid)), 'bui']=meters.Haus[i]
    df.loc[df.TPID.str.contains(str(tpid)), 'app']=meters.Wohnung[i]

    for item in counts.index:
        if str(tpid) in str(item):
            if meters.loc[i, 'Medium'] == 'H':
                meters.loc[i, 'n [%]'] = round(counts[item]/dth,2)

            if meters.loc[i, 'Medium'] == 'W':
                meters.loc[i, 'n [%]'] = round(counts[item]/dtw,2)

            meters.loc[i, 'TPID'] = item
            
meters = meters.dropna(subset=['n [%]'])

meters.set_index(['Haus', 'Wohnung', 'Medium']).sort_index()

df = df.set_index(['bui','app', 'type', 'Datetime']).sort_index()

variants = {}

variants['wohnung'] = list(meters.Wohnung.unique())
variants['haus'] = list(meters.Haus.unique())
variants['meter'] = list(meters.Medium.unique())

for key in variants:
    variants[key].sort()
print(f'---starting export to {db_loc}...')
export = {bui : os.path.join(db_loc, bui) for bui in variants['haus']}
for bui in export:
    if os.path.isdir(export[bui]) == False:
        os.makedirs(export[bui])

database = {}
for name, group in df.groupby(level=0):
    if group.index.is_unique == False:
        group = group[~group.index.duplicated(keep='first')]
    database[name] = group.droplevel(0).unstack(level=[0,1]).swaplevel(0,-1,axis=1).swaplevel(0,1,axis=1).sort_index(axis=1).dropna(axis=1, how='all').sort_index(axis=0)
    database[name].to_csv(os.path.join(export[name], '{}_em_database.csv'.format(name)))
    for ts in ['1min']:
        database[name].resample(ts).fillna('pad').to_csv(os.path.join(export[name], '{}_em_resampled_{}.csv'.format(name,ts)))

print(f'---creating overview graph...')
level_values = df.index.get_level_values

result = (df.groupby([level_values(i) for i in [0,1,2]]
                      +[pd.Grouper(freq='D', level=-1)]).size())
result = pd.DataFrame(result, columns=['n_data'])

result.reset_index(level=[0,1,2],inplace=True)

result['meter'] = result['bui'] + '_' + result['app'] + '_' + result['type']
result.drop(['bui','app','type'],axis=1,inplace=True)

f, ax = plt.subplots(figsize=(15,10))

ax.plot(result.index, result.meter, linestyle='None')

sc = ax.scatter(result.index, result.meter, c=result.n_data, s=len(result.index.unique())*1.4, marker = 's', cmap='RdYlGn')

cbar = f.colorbar(sc)
cbar.set_label("Observations per day ", loc='top')

exdir = os.path.join(eb.dir_results,'Results','Allgemein')
if lehrstuhl:
    exdir = os.path.join(eb.dir_results_ls,'Allgemein')
if not os.path.isdir(exdir):
    os.makedirs(exdir)
f.savefig(os.path.join(exdir,f'EM_Monitoring_Datenempfang_Übersicht.png'),dpi=300)
print(f'finished!')