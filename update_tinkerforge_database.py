
import os
import datetime as dt
import pandas as pd
import numpy as np
import eb
import config

##############################################################___Input Daten___##############################################################
#############################################################################################################################################
lehrstuhl = False

send=True

# Export Ordner
db_loc = eb.dir_db
if lehrstuhl:
    db_loc = eb.dir_db_ls

#Speicherort für neue Datensätze:
dropbox = eb.tf_path

#Speicherort von allen alten Datensätzen (Vor der Dropbox...)
arch_loc = eb.tf_archive

#Dateikürzel im Archiv
buid = ['LB','MH','MW','WD']
buid_long ={'LB':'Leichtbetonhaus','MH':'Massivholzhaus','MW':'Ziegelhaus', 'WD':'Wetterstation', 'PM':'Pyranometer'}

#Erstelle Pfade zu den Datenbanken
db = {bui : os.path.join(db_loc,bui,'{}_tf_raw.csv'.format(bui)) for bui in buid_long}
for bui in db:
    if os.path.isdir(os.path.dirname(db[bui])) == False:
        os.makedirs(os.path.dirname(db[bui]))

###############################################################___Functions___###############################################################
#############################################################################################################################################
def load_tf_file(path):
    df = pd.read_csv(
        file,
        engine='python',
        sep=';',
        na_values=['-','#N/V','#NV'],
        decimal=',')
    
    df = df[df.iloc[:, 0] != df.columns[0]]

    not_empty_cols = [(col, df.columns.get_loc(col)) for col in df.replace(' ', np.NaN).filter(like='Unnamed:').dropna(axis=1).columns]
    empty_cols = [(col, df.columns.get_loc(col)) for col in df.columns if df[col].replace(' ',np.NaN).isnull().all() and not 'Unnamed:' in col]

    cols = list(df.columns)
    if len(not_empty_cols) == len(empty_cols):
        for i in range(len(empty_cols)):
            id1 = empty_cols[i][1]
            id2 = not_empty_cols[i][1]
            delta = id1-id2
            for n in range(delta):
                cols[id2+n],cols[id2+n+1] = cols[id2+n+1],cols[id2+n]
                print('Headers: {} - {} switched!'.format(cols[id2+n],cols[id2+n+1]))
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
                d=c
                date=col
                drop.append(col)
            if col == 'Time' or col =='Uhrzeit':
                t=c
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

################################################################___Skript___#################################################################
#############################################################################################################################################

#Falls noch nicht vorhanden, erstelle eine neue Datenbank aus dem Archiv.
print('1_ Datenbanken checken und ggf. erstellen...')
files = {}
master_df={}
for bui in buid:
    if os.path.isfile(db[bui]):
        print('{}: Datenbank vorhanden...'.format(bui))
        continue
    else:
        print('{}: Keine Datenbank gefunden - erstelle neue aus dem Archiv...'.format(bui))
        bui_path = os.path.join(arch_loc, bui)
        files[bui] = [os.path.join(bui_path, fn) for fn in os.listdir(bui_path) if fn.endswith('.csv') ]
        files[bui].sort(key=lambda x: os.path.getmtime(x))
        print('loading {}...'.format(bui))

        df = []
        for file in files[bui]:
            df.append(eb.load_tf_file(file))

        master_df[bui] = pd.concat(df)
        if master_df[bui].index.is_unique == False:
            master_df[bui] = master_df[bui][~master_df[bui].index.duplicated(keep='first')]
            if master_df[bui].index.is_unique:
                print('{}: Datenbank bereinigt!'.format(bui))
        if len(master_df[bui].filter(like='.1').columns) >0:
            print('{}: Spalten dupliziert...'.format(bui))
        master_df[bui].dropna(axis=1, how='all',inplace=True)
        if master_df[bui].index.has_duplicates:
            print('{}: Achtung! Duplikate vorhanden!'.format(bui))
        print('...postprocessing complete, exporting database now...')
        master_df[bui].to_csv(db[bui], index=True)
        print('...export finished, starting next building now.')
    print("Mom! I'm done!")

#öffne vorhandene Datenbanken...
print('2_ Datenbanken öffnen...')
database = {}
for bui in db:
    try:
        database[bui] = pd.read_csv(db[bui], parse_dates=['Datetime'], dayfirst=True, index_col='Datetime')
    except:
        if bui == 'PM':
            database[bui] = database['LB'].filter(like='DA')
            database[bui].columns = ['Global W/m^2','Direct W/m^2','Diffuse W/m^2']
    if database[bui].index.is_unique:
        print('{} index ok!'.format(bui))
    else:
        try:
            database[bui] = database[bui][~database[bui].index.duplicated(keep='first')]
        except:
            print('{} Fehler!'.format(bui))
        finally: 
            if database[bui].index.is_unique:
                print('{} index ok!'.format(bui))


#Öffne Messdaten aus Dropbox die noch nicht in der Datenbank sind...
print('3_ Lade neue Daten aus Dropbox...')
dropbox_files = {}
dropbox_df = {}
notification = {}
offline = {}
database = {}
for bui in buid_long:
    print('------------{}------------'.format(bui))
    print('{}: Öffne vorhandene Datenbank.'.format(bui))
    try:
        database[bui] = pd.read_csv(db[bui], parse_dates=['Datetime'], dayfirst=True, index_col='Datetime')
    except:
        if bui == 'PM':
            database[bui] = database['LB'].filter(like='DA')
            database[bui].columns = ['Global W/m^2','Direct W/m^2','Diffuse W/m^2']
    if database[bui].index.is_unique == False:
        try:
            database[bui] = database[bui][~database[bui].index.duplicated(keep='first')]
            if database[bui].indes.is_unique:
                print('{}: Datenbank bereinigt!'.format(bui))
            else:
                print('{}: Datenbankfehler, überspringe Gebäude!'.format(bui))
                continue
        except:
            print('{}: Datenbankfehler!'.format(bui))

    cols_db = len(database[bui].columns)
    dropbox_path = os.path.join(dropbox, bui)
    dropbox_files[bui] = [os.path.join(dropbox_path, fn) for fn in os.listdir(dropbox_path) if fn.endswith('.csv') ]
    dropbox_files[bui].sort(key=lambda x: os.path.getmtime(x))

    last_day = pd.to_datetime(os.path.basename(dropbox_files[bui][-1]).rsplit('_',1)[0],format='%Y_%m_%d')
    last_day_soll = dt.datetime.today().date()-dt.timedelta(1)

    if last_day == dt.date.today():
        last_file = dropbox_files[bui].pop(-1)
        print('{}: Datei von Heute ({}) wird übersprungen!'.format(bui, os.path.basename(last_file)))
    if last_day.date() < last_day_soll:
        offline[bui] = '{} liefert seit {} ({} Tage(n)) keine neuen Daten mehr.'.format(buid_long[bui],last_day.to_pydatetime().strftime('%d.%m.%Y'),((dt.datetime.today()-last_day.to_pydatetime()).days))
        print(offline[bui])

    print('{}: Durchsuche Dropbox nach neuen Datensätzen.'.format(bui))
    
    df1 = []
    for file in dropbox_files[bui]:
        test = pd.read_csv(
                file,
                engine='python',
                sep=';',
                nrows=1,
                na_values=['-','#N/V','#NV'],
                decimal=',')
        test.reset_index(drop=True)
        test.dropna(axis=1, how='all',inplace=True)
        test.drop(list(test.filter(like='named').columns), axis=1, inplace=True)
        test.drop_duplicates(ignore_index=True, inplace=True)
        #test = test[test.iloc[:, 0] != tes.columns[0]]

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
            newday = load_tf_file(file)
            if len(newday.columns) != cols_db:
                print('---{}: Neue Datei gefunden, {} Spalten mehr als in der Datenbank!'.format(newdate, len(newday.columns)-cols_db))
            else:
                print('---{}: Neue Datei gefunden!'.format(newdate))
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
    try:        
        dropbox_df[bui] = pd.concat(df1)
        if dropbox_df[bui].index.has_duplicates:
            dropbox_df[bui] = dropbox_df[bui][~dropbox_df[bui].index.duplicated(keep='first')]
            print('{}: Datenbank von Duplikaten bereinigt!'.format(bui))
        if len(dropbox_df[bui].filter(like='.1').columns) >0:
            for col in dropbox_df[bui].filter(like='.1'):
                print('Achtung: {} wurde dupliziert statt ergänzt...'.format(col))
        print('...saving data in dict and continue with next building.')
    except:
        print('{}: Keine neue Datei(en) gefunden.'.format(bui))
        continue
#print("Mom! I am ready!")

# send missing data report
for bui in list(notification):
    for key in list(notification[bui]):
        if 'named' in key:
            notification[bui].pop(key)
            print(key, 'removed!')

if len(offline) == 0 and len(notification) == 0:
    print('Keine neuen Datensätze oder alles läuft einwandfrei...')
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
            print(text)

    if len(notification) > 0 and send==True:
        eb.send_email(who=[config.emails['roman']],sender=config.emails['sender'],subject='EINFACH MESSEN: SENSORS NOT WORKING!',text=text,password=config.password,smtp=config.smtp)

# send offline notification            
who=['Roman Ficht <Roman.Ficht@tum.de>']

if len(offline) == 0:
    print('Keine neuen Datensätze oder alles läuft einwandfrei...')
else:
    text = 'Hallo,\ndas ist eine automatisch erzeugte Fehlermeldung der Einfach-Bauen-Haeuser:\n\n'

    for bui in offline:
        text += 'Das ' + offline[bui]

    if send==False:
        print(text)

    if len(offline) > 0 and send==True:
        eb.send_email(who=[config.emails['roman']],sender=config.emails['sender'],subject='EINFACH MESSEN: OFFLINE ALERT!',text=text,password=config.password,smtp=config.smtp)

# Füge neue Daten der Datenbank hinzu und speichere die aktualisierte Datenbank ab.
print('4_ Speichere aktualisierte Datenbank...')
if len(dropbox_df)==0:
    print('Keine neuen Dateien...')
else:
    for bui in dropbox_df:
        print('{}: Überprüfe neue Datensätze aus Dropbox...'.format(bui))
        if dropbox_df[bui].index.has_duplicates:
            print('{}: Indexfehler!'.format(bui))
            try:
                dropbox_df[bui] = dropbox_df[bui][~dropbox_df[bui].index.duplicated(keep='first')]
                print('{}: Datensatz bereinigt!'.format(bui))
            except:
                print('{}: Leider stimmt immer noch was nicht...Überspringe Datensatz'.format(bui))
                continue
            finally: 
                if dropbox_df[bui].index.is_unique:
                    print('{}: Jetzt passts!'.format(bui))

        print('{}: Füge neue Einträge zur Datenbank hinzu...'.format(bui))

        df = pd.concat([database[bui], dropbox_df[bui]])
        df.dropna(axis=1, how='all', inplace=True)
        df.sort_index(axis=0, inplace=True)
        
        if df.index.is_unique == False:
                print('{}: Versuche doppelte Einträge zu löschen...'.format(bui))
                df = df[~df.index.duplicated(keep='first')]
                if df.index.is_unique:
                    print('{}: Erfolgreich bereinigt!'.format(bui))
                else:
                    print('{}: Index Fehler!'.format(bui))
                    continue
        if len(df.filter(like='.1').columns)>0:
            for col in df.filter(like='.1').columns:
                print(col, 'wurde dupliziert...')
        else:
            print('{}: Super! Keine doppelten Einträge in der Datenbank. Starte Export...'.format(bui))

        
        database[bui] = df

        anfang = database[bui].index.min()
        ende = database[bui].index.max()

        database[bui].to_csv(db[bui])
        print('{}: Datenbank exportiert! Zeitraum von {} bis {}.'.format(bui, anfang, ende))
        for ts in ['1min', '15min', '60min']:
            if os.path.isdir(os.path.join(db_loc,bui)) == False:
                os.makedirs(os.path.join(db_loc,bui))
            
            df_resampled = database[bui].resample(ts).last().asfreq(ts)
            
            df_resampled.to_csv(os.path.join(db_loc,bui,'{}_tf_database_resampled_{}.csv'.format(bui, ts)))

            print('{}: Resampled auf {} und exportiert! Zeitraum on {} bis {}.'.format(bui, ts, df_resampled.index.min(), df_resampled.index.max()))
print('Fertig!')