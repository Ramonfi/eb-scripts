import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
#import src.project_definitions as eb
import logging as log
import src.config as config
import sys
import src.utilities as ut

###############################################################___Functions___###############################################################
#############################################################################################################################################

def load_tf_file(path, nrows=None, debug = False):
    df = pd.read_csv(
        path,
        engine='python',
        encoding= 'latin-1',
        sep=';',
        nrows=nrows,
        na_values=['-',' ','#N/V','#NV'],
        decimal=',',
        index_col=False)
    
    df = df[df.iloc[:, 0] != df.columns[0]].copy()

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
            if debug:
                print(f'{cols[i+n]} <-> {cols[i+n+1]}')
        df.columns = cols

    df.drop(list(df.filter(like='named').columns), axis=1, inplace=True)
    if '-->Extra-Sensors-->' in df.columns:
        df.drop(['-->Extra-Sensors-->'], axis=1, inplace=True)
    df.columns = df.columns.str.replace('HM', 'MH')
    df.columns = df.columns.str.replace('(Â°C)', '(°C)', regex=False)
    df.columns = df.columns.str.replace('[Black Globe] ', '', regex=False)
    df.columns = df.columns.str.replace(f'[LB_Black Globe] ', '', regex=False)
    df.columns = df.columns.str.replace(f'[MW_Black Globe] ', '', regex=False)
    df.columns = df.columns.str.replace(f'[MH_Black Globe] ', '', regex=False)
    df.columns = df.columns.str.replace(f'[HM_Black Globe] ', '', regex=False)
    df.columns = df.columns.str.replace(f'[LB_Black Globe_Metal] ', '', regex=False)

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

## Dateipfade

# Datenbanken
dir_db = './eb-data/database'

# Ordner für Auswertungen
dir_results = './eb-data/Results'

### Rohdaten (Dropbox, Archiv & co)
## 1) Energy Monitoring
em_dropbox = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\1_rohdaten\EM\RmCU'

## 2) Tinkerforge Dropbox Sync
tf_dropbox = os.path.join(r'\\nas.ads.mwn.de','tuar','l15','private','DATA','FORSCHUNG','04_Projekte','2021','Einfach_Bauen_3','Daten','1_rohdaten')

## 3) Archiv: Daten vor September (ohne Dropbox-Sync)
tf_archive = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\ARCHIV\1_rohdaten'

# Kürzel der Messdaten
buid ={'LB':'Leichtbetonhaus','MH':'Massivholzhaus','MW':'Ziegelhaus', 'WD':'Wetterstation', 'PM':'Pyranometer'}


########################################################## Set environmental values #########################################################
#############################################################################################################################################

#Dateikürzel im Archiv
#buid = ['LB','MH','MW','WD']
#buid_long ={'LB':'Leichtbetonhaus','MH':'Massivholzhaus','MW':'Ziegelhaus', 'WD':'Wetterstation', 'PM':'Pyranometer'}

################################################################ MAIN SCRIPT ################################################################
#############################################################################################################################################

def energymeter_update(send=True, plot=False):
    log.info(f'------ EnergyMeter ------')

    # Speicherort für neue Moiline Datensätze
    files = [os.path.join(em_dropbox,name) for name in os.listdir(em_dropbox)]
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
    log.info(f'Starting export to directory: {dir_db}.')

    ## creating paths to database
    export = {bui : os.path.join(dir_db, bui) for bui in list(meters.Haus.unique())}
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
        timemax = max([database[bui].index.max().date() for bui in buid])
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
        exdir = os.path.join(dir_results,'Allgemein')
        if not os.path.isdir(exdir):
            os.makedirs(exdir)
        f.savefig(os.path.join(exdir,f'EM_Monitoring_Datenempfang_Übersicht.png'),dpi=300)
    log.info(f'EnergyMeter: FINISHED')


def tinkerforge_update(send=True, OverwriteDatabase=[], skip=[]):
    log.info(f'------ Starte TinkerForge ------')
    ## Erstelle Pfade zu den tinkerforge Datenbanken
    db = {bui : os.path.join(dir_db,bui,'{}_tf_raw.csv'.format(bui)) for bui in buid}
    ## Falls der Datenbank-Ordner noch nicht existiert, erstelle ihn.
    for bui in db:
        if os.path.isdir(os.path.dirname(db[bui])) == False:
            os.makedirs(os.path.dirname(db[bui]))

    files = {}                                                          #dict with path to archived datasheets
    master_df={}                                                        #dict with database as DataFrame


    log.info(f'Suche vorhandene Datenbank.')
    for bui in buid:                                                        # Starte Import Datensheet. Iteration über die Einheiten (LB, MH, MW, PM, WD)
        if bui not in skip:                                                 # Skippe benutzerdefinierte Varianten.
            export_databases = False
            tf_drop_bui = os.path.join(tf_dropbox,bui)                      # Konstruiere den Pfad zum Dropbox Ordner der aktuellen Einheit
            if os.path.isfile(db[bui]) and bui not in OverwriteDatabase:    # Hysterese: Wenn Datenbank schon vorhanden ist und Bauweise nicht in der Liste der zu überschreibenden Bauweisen ist, dann öffne die Vorhandene Datenbank
                master_df[bui] = pd.read_csv(db[bui], low_memory=False, index_col='Datetime')   # Öffne die vorhandene Datenbank aus dem Ordner
                last_data = pd.to_datetime(master_df[bui].index).max().date()-dt.timedelta(10)  # Konstruiere den Datenstand der Datenbank. Ziehe Toleranz von 10 Tagen ab.
                log.info(f'{bui}: Vorhandene Datenbank geöffnet!')
                # Suche nach neuen Datensätzen in der Dropbox
                dropbox_files = {}
                offline = {}
                notification = {}

                dropbox_path = os.path.join(tf_dropbox, bui)    # Konstruiere den Dateipfad zum DropboxOrdner der aktuellen Einheit 
                dropbox_files[bui] = [os.path.join(dropbox_path, fn) for fn in os.listdir(dropbox_path) if fn.endswith(f'{bui}.csv') and dt.datetime.fromtimestamp(os.path.getmtime(os.path.join(dropbox_path, fn))).date() > last_data]  # Konstruiere die Pfade zu den einzelnen Datensheets
                dropbox_files[bui].sort(key=lambda x: os.path.getmtime(x))  # sortiere die Dateipfade nach deren letztem Bearbeitungsdatum

                last_day = pd.to_datetime(os.path.basename(dropbox_files[bui][-1]).rsplit('_',1)[0],format='%Y_%m_%d')  # Extrahiere das Datum der neusten Datei im DropBox-Ordner aus deren Dateiname
                last_day_soll = dt.datetime.today().date()-dt.timedelta(1)                                              # Konstruiere das Soll-Datum, sprich gestern

                if last_day.date() == dt.date.today():                                                                  # Vergleiche das Datum der neusten Datei mit dem Datum von Heute
                    last_file = dropbox_files[bui].pop(-1)                                                              # Überspriche die Datei von Heute, da so noch fortgeschrieben wird.
                    log.info(f'{bui}: Datei von Heute ({os.path.basename(last_file)}) wird übersprungen!')
                if last_day.date() < last_day_soll:                                                                     # Wenn die neuste Datei mehr als einen tag zurück liegt funktioniert der Dropbox Abgleich nicht.
                    offline[bui] = f'{buid[bui]} liefert seit {last_day.to_pydatetime().strftime("%d.%m.%Y")} ({((dt.datetime.today()-last_day.to_pydatetime()).days)} Tage(n)) keine neuen Daten mehr.'   # Erstelle eine Benachrichtigung
                    log.info(offline[bui])

                log.info(f'{bui}: Durchsuche Dropbox nach neuen Datensätzen.')

                df1 = []                                                                # Definiere eine Liste in der die gefundenen neuen Datensätze gespeichert werden.
                n_files = len(dropbox_files[bui])                                       # Zähle alle gefundenen Datensätze (Für die Fortschrittsanzeige während des Ladens)
                for n, file in enumerate(dropbox_files[bui]):                           # Iteration über alle Dateien in der Dropbox
                    ut.running_bar(n,n_files)                                           # Plotte die Fortschrittsanzeige
                    try:                                                                # Fange Exceptions ein und überspringe damit fehlerhafte Dateien
                        test = load_tf_file(file, nrows=1)                              # Lade die erste Zeile jedes Sheets
                        if test.index.isin(master_df[bui].index) == False:              # Prüfe ob diese Zeile bereits in der bestehenden Datenbank vorhanden ist.
                            newdate = pd.to_datetime(test.index.values.min()).date()    # Wenn es sich um eine neue Zeile handelt, extrahiere das Datum von dem die Aufzeichnungen stammen
                            log.info(f'--- {newdate}: Neue Datei gefunden!')            # Plotte eine kurze Info
                            newday = load_tf_file(file)                                 # Lade den kompletten Sheet
                            for sensor, data in newday.iteritems():                     # Für den neuen Sheet: Gehe Spalte für Spalte durch und zähle die Fehlerhaften Beobachtungen
                                check = data.isna().sum()/len(data.index)               # Berechne den Anteil der fehlenden Messpunkte
                                if check > 0.1:                                         # Wenn mehr als 10% Datenpunkte fehlen sollten
                                    if bui not in notification:                         # Erstelle eine Benachrichtigung...
                                        notification[bui] = {}
                                    if sensor in notification[bui]:
                                        notification[bui][sensor][newdate] = int((1-check)*100)     # Dazu: Berechne den Anteil an fehlenden Punkten und speichere ihn in einem Dict
                                    else:
                                        notification[bui][sensor] = {newdate : int((1-check)*100)}
                            df1.append(newday)
                    except Exception as e:                                              # Speichere die Exception im log....
                        log.warning(e)
                if len(df1) > 0:
                    export_databases = True
                    master_df[bui] = pd.concat([master_df[bui]] + df1,axis=0)               # Nachdem alle Datensheets überprüft wurden, hänge die neuen Datensätze der Datenbank an
                    master_df[bui].to_csv(db[bui], index=True)                              # exportiere die aktualisierte (Roh-)Datenbank
                
            elif not os.path.isfile(db[bui]) or bui in OverwriteDatabase:               # Falls die Bedingung vom Eingang nicht zutrifft, sprich: Entweder wurde keine Datenbank gefunden oder die Datenbank SOLL überschrieben werden
                log.info(f'{bui}: Keine Datenbank gefunden - erstelle neue aus dem Archiv.')
                bui_path = os.path.join(tf_archive, bui)                                # Konstruiere den Pfad zum Ordner der entsprechenden Einheit im Archiv-Ordner
                if os.path.exists(bui_path):                                            # Wenn der Archivordner existiert (...tut er z.B. für das Pyranometer nicht...)
                    files[bui] = [os.path.join(bui_path, fn) for fn in os.listdir(bui_path) if fn.endswith('.csv')]    # Speichere die Dateipfade zu den Datensätzen im einem Dict ab.
                else:
                    files[bui] = []                                                     # Wenn das Archiv nicht existiert erstelle wenigstens eine leere Liste
                files[bui].extend([os.path.join(tf_drop_bui, fn) for fn in os.listdir(tf_drop_bui) if fn.endswith(f'{bui}.csv')])   # Nun gehe in den Dropbox Ordner und hänge alle Datensheets der Liste an. Achtung: nur Dateien die auf {bui}.csv enden werden berücksichtigt. Damit werden die "Test" Dateien in der Dropbox direkt aussortiert
                files[bui].sort(key=lambda x: os.path.getmtime(x))                      # Sortiere alle Datasheets nach dem Datum.
                # files[bui].pop(-1)                                                      # Zum testen: entferne den neusten Datensatz... Kann deaktiviert werden
                n_files = len(files[bui])                                               # Zähle die Sheets (Für die Fortschrittsanzeige)
                dfs = []                                                                # Erstelle eine Leere Liste in die die Datensheets abgespeichert werden
                for nf, file in enumerate(files[bui]):                                  # Gehe alle Datensheets durch
                    try:                                                                # Fange FileNotFound Exceptions ein um nicht jedes mal von neuem anfangen zu müssen, falls eine Datei nicht gefunden wurden....
                        df = load_tf_file(file)                                         # Öffne den Datensheet
                        if isinstance(df, pd.DataFrame):                                # Die Funktion load_tf_file() gibt None zurück, wenn die Datei z.B. Leer ist. Nur wenn ein pd.DataFrame geladen wurde, soll dieser der Liste hinzugefügt werden
                            dfs.append(df)
                    except FileNotFoundError:
                        print(f'{file} wurde nicht geladen.')
                    ut.running_bar(nf,n_files)                                          # Fortschrittsanzeige

                df = pd.concat(dfs)                                                     # Vereine alle Datensheets zu einem großen
                log.info(f'{bui}: Lesen der Datensätze erfolgreich. Exportiere die Datenbank.')
                if bui == 'LB':                                                         # In der LB-Datei waren am Anfang auch die Pyranometer-Daten. Diese müssen extrahiert werden.
                    master_df['PM'] = df.filter(like='DA').copy()                       # Dazu wird im master_df-dict eine Kopie der Pyranometer-Daten gespeichert 
                    master_df['PM'].columns = [col.rsplit('_',1)[-1] for col in master_df['PM'].columns]    # Deren Spaltenbezeichnugn wird noch vereinheitlicht
                    master_df[bui] = df.drop(df.filter(like='DA').columns,axis=1).copy()    # Am Ende werden die Einträge der Pyranometer noch aus dem Bauweisen-dict gelöscht
                elif bui == 'PM':                                                       # Für das Pyranometer wird das ganze jetzt andersrum gemacht. Erst werden die aus den LB-Daten extrahierten Datensätze geöffnet und die neuen Datensätze aus der Dropbox werden hinzugefügt.
                    if bui in master_df and isinstance(master_df[bui], pd.DataFrame):   # Prüfe ob Daten aus dem Import eines LB-Sheets vorhanden sind.
                        master_df[bui] = pd.concat([master_df[bui],df], axis = 0)       # Wenn dem so ist, dann füge Vereine sie mit dem neuen Datensatz
                    else:
                        master_df[bui] = df                                             # Wenn nicht, dann lade einfach nur den neuen Datensatz
                else:
                    master_df[bui] = df.copy()                                          # für alle anderen Datensätze: Speichere die neu geladenen Datensätze in dem master_df-dict
                
                master_df[bui].to_csv(db[bui], index=True)                              # und exportiere die Rohdaten als csv Datei
                log.info(f'{bui}: Export der Datenbank erfolgreich.')
                export_databases = True
            if export_databases:                                                        # Hier beginnt das PostProcessing
                master_df[bui].index = pd.to_datetime(master_df[bui].index)                 # Forme zuerst alle Indizes in das Datetime Format um.
                if not master_df[bui].index.max().date() == dt.date.today():                # Nun Prüfe ob alle Datenbanken Aktuell sind, wenn nicht
                    log.warning(f'{bui}: Datenbank ist nicht aktuell. Vermutlich funktioniert der Dropbox-abgleich aktuell nicht.')
                for name, data in master_df[bui].iteritems():                               # Nun forme alle numerischen Daten in Float-Werte um
                    master_df[bui][name] = pd.to_numeric(data, errors='ignore')
                if not master_df[bui].columns.is_unique:                                    # Warne wenn duplizierte Spalten vorhanden sind
                    log.warning(f'{bui}: Duplizierte Spalten!')
                start, ende = master_df[bui].index.min(), master_df[bui].index.max()        # Extrahiere das Start und Enddatum des gesamten Datensatzes                             
                log.info(f'{bui}: Starte Export!')
                allgood = True                                                              # Prüfwert, dass alle Datensätze korrekt exportiert wurden
                for ts in ['1min', '15min', '60min']:                                       # Definiere die Zeitschritte für den Export
                    if os.path.isdir(os.path.join(dir_db,bui)) == False:                    # Falls der Export-Ordner nicht existieren sollte, erstelle ihn
                        os.makedirs(os.path.join(dir_db,bui))
                    
                    df_resampled = master_df[bui].resample(ts).last().asfreq(ts)            # Führe Resampling auf den gewünschten Zeitschritt durch.
                    if df_resampled.index.is_unique:                                        # Wenn der Index jetzt keine Fehler mehr enthält, exportiere den Datensatz
                        df_resampled.to_csv(os.path.join(dir_db,bui,'{}_tf_database_resampled_{}.csv'.format(bui, ts)))
                        log.debug(f'{bui}: Resampled auf {ts}')
                    else:
                        log.warning(f'{bui}: Resampling auf {ts} hat nicht geklappt! Es wurde nichts exportiert...')    # Falls Fehler enthalten sind, Schreibe eine Warnung ins Log 
                        allgood = False                                                     # Setze den Prüfwert auf Falsch
                if allgood:                                                                 # Wenn alle exporte Geklappt haben, schreibe das ins log. 0
                    log.info(f'{bui}: TinkerForge Datenbanken exportiert! | {start} | {ende} |')

    # send missing data report
    for bui in list(notification):                                                      # Räume die Notifications auf.
        for key in list(notification[bui]):
            if 'named' in key:                                                          # Es kann passieren, dass die "leeren"-Spalten hier landen, die müssen erst aussortiert werden
                notification[bui].pop(key)
                log.warning(f'{bui}: unnamed column in data.')

    if len(offline) == 0 and len(notification) == 0:                                    # Wenn nichts offline ist und alle Sensoren mehr als 90% Daten aufgezeichnet haben passt alles. Schreibe das ins Log und beende das Programm
        log.info('Keine neuen Datensätze oder alles läuft einwandfrei...')
    else:                                                                               # Wenn das nicht der Fall ist erstelle eine Benachrichtigungs-Mail
                                                                                        # Beginne mit dem Einleitungstext der eMail    
        text = 'Hallo,\ndie folgenden Sensoren haben in den vergangenen Tagen ungewöhnlich wenige Daten aufgezeichnet:\n\nHinweis:\nDie Liste führt Tage auf, an denen ein Sensor weniger als 90% der Datensätze aufgezeichnet hat. Fehlende Tage in der Aufzählung bedeuten, dass an diesen Tagen mehr als 90% der Daten aufgezeichnet wurden\n'

                                                                                        # Wenn alle Häuser "Online" sind - Sprich wir von allen Häusern aktuelle Datensheets haben, Schreibe das in die Mail
        if len(offline)==0:
            text += '\n\n---------ALLE HÄUSER ONLINE - DROPBOX-SYNC FUNKTIONIERT---------\n\n'
                                        
        for bui in buid:                                                                # Liste Haus für Haus, Tag für Tag die Fehlermeldungen auf
            if bui in offline or bui in notification:
                text +='\n------'+ buid[bui] + ':------\n'
            if bui in offline:
                text += '\n!!! ' + offline[bui] + ' !!!\n'
            if bui in notification:
                for sensor in notification[bui]:
                    text += '\n' + sensor + ':\n'
                    for day in notification[bui][sensor]:
                        text += '\t{}: {}% Messwerte vorhanden.\n'.format(day, notification[bui][sensor][day])                                                                        
            if send==False:                                                             # Wenn keine Mail versendet werden soll, schreibe die Infos ins Logbuch
                log.debug(text)
                                                                                        
        if len(notification) > 0 and send==True:                                        # Wenn Benachrichtigungen da sind und sie auch versendet werden sollen, bereite die Mail vor
                                                                                        
            try:                                                                        # Der Versand der eMails erfolgt über eine vorgefertigte Funktion unter src.utilities. Darüber hinaus wird die config.py mit den Zugangsdaten zum eMail Provider benötigt.
                ut.send_email(who=[config.emails['roman']],sender=config.emails['sender'],subject='EINFACH MESSEN: SENSORS NOT WORKING!',text=text,password=config.password,smtp=config.smtp)
                log.info(f'Sensordaten-Übersicht gesendet')
                                                # Schreibe was ins logbuch, wenn es nicht funktioniert hat
            except Exception as e:
                log.warning(f'Senden der Nachricht fehlgeschlagen: {e}')

    # Versnde eine Extra Mail, wenn Häuser offline sind.            
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

    log.info('TinkerForge: FINISHED')                                           # Schreibe ins Log, dass das Skript druchgelaufen ist. !Achtung: Nach diesem Eintrag wird entschieden, ob ein Datenbank update notwendig ist oder nicht. Wenn dieser Eintrag mit heutigem Datum im Log steht, wird die DAtenbank nicht aktualisiert, wenn das nicht der Fall ist, wird ein Update angestoßen.

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
    tinkerforge_update()

if Stand_EnergyMeter.date() == dt.date.today():
    print('EnergyMeter up-to-date')
else:
    energymeter_update()
    print('EnergyMeter Nessesarry')