import pandas as pd
import numpy as np
import os
from src.project_definitions import BUID, dir_db
import datetime as dt

# Scanne das Projektverzeichnis nach den Datenbanken und speichere die Pfade ab.
files ={}
for meter in ['tf','em']:
    if meter not in files:
        files[meter] = {} 
    for bui in ['LB','MW','MH','WD','PM']:
        path = os.path.join(dir_db,bui)
        if not os.path.isdir(path):
            os.makedirs(path)
        for fn in os.listdir(path):
            names = fn.split('_')
            if names[1] == meter:
                if bui not in files[meter]:
                    files[meter][bui] = {}
                files[meter][bui][fn.rsplit('_',1)[-1].split('.')[0]] = os.path.join(os.path.join(path), fn)


def load_tf_bui(bui, timestep='60min',multiindex=True):
    '''
    Öffne die TinkerForge Messdatenbank als pd.DataFrame.

    Args:
    ----
        bui: Bauweise ['LB', 'MW' oder 'MH']
        timestep: '1min', '15min' oder '60min'
        multiindex: Return DataFrame with Multiindex vereinfacht das Durchsuchen und filtern. (default = True)
    '''
    path = files['tf'][bui][timestep]
    df = pd.read_csv(
            path, 
            decimal='.', 
            na_values = '#N/V',
            low_memory=False
            )
    df.replace([' ','  '],np.NAN,inplace=True)
    df.set_index( pd.to_datetime(df['Datetime'], utc=True).dt.tz_convert('Europe/Berlin'), inplace=True)
    df.drop('Datetime',axis=1,inplace=True)
    if multiindex:
        idx = []
        for col in df.columns:
            sensor = ' '.join(col.split(' '))
            # Für alle Sensorbezeichnungen die jetzt mit der Gebäude ID Anfangen:
            if sensor.startswith(bui):
                # Entferne Gebäudebezeichnung...
                sensor = sensor.split('_',2)[1:]
                # Setze Stochwerksbezeichnung
                loc = sensor[0]
                sensor = sensor[1].split('_')

                if loc == 'Dach':
                    whg = 'DA'
                    room = ''
                    name = '_'.join(sensor).strip()

                elif len(sensor) < 4:
                    if len(sensor[0]) == 1:
                        whg = sensor[0]
                        room = ''
                        name = '_'.join(sensor[1:]).strip()
                    else:
                        whg = ''
                        room = ''
                        name = '_'.join(sensor).strip()

                elif len(sensor) >= 4:
                    whg = sensor[0]
                    if whg in ['N', 'S', 'O']:
                        room = sensor[1]
                        name = '_'.join(sensor[2:]).strip()
                    elif whg in ['TH']:
                        room = ''
                        name = '_'.join(sensor[1:]).strip()

            else:
                if sensor == '-->Extra-Sensors-->':
                    whg == ''
                    room == ''
                    name = ''
                else:
                    whg = 'DA'
                    room = ''
                    name = sensor.split('-')[1].split('_', 2)[2].strip()
            index = (whg,room,name)
            idx.append(index)
        df.columns = pd.MultiIndex.from_tuples(idx)
    else:
        df.columns = df.columns.str.strip()
    df.sort_index(axis=1,inplace=True)
    return df

################################################ LOAD PYRANOMETER FILE ################################################

def load_tf_pm(timestep='60min'):
    path = files['tf']['PM'][timestep]
    df = pd.read_csv(
        path, 
        decimal='.', 
        na_values = '#N/V',
        low_memory=False
        )
    df.set_index( pd.to_datetime(df['Datetime'], utc=True).dt.tz_convert('Europe/Berlin'), inplace=True)
    df.drop('Datetime',axis=1,inplace=True)
    df['Direct W/m^2'][df['Direct W/m^2'] < 0] = 0
    df['Diffuse W/m^2'] = df['Global W/m^2'] - df['Direct W/m^2']
    #df = df.abs()
    
    df.columns = df.columns.str.split(' ',expand=True).droplevel(level=1).str.lower()

    return df

################################################ LOAD WEATHER FILE ################################################

def load_tf_weather(timestep='60min'):
    path = files['tf']['WD'][timestep]
    df = pd.read_csv(
        path, 
        decimal='.', 
        na_values = '#N/V',
        low_memory=False
        )
    df.set_index( pd.to_datetime(df['Datetime'], utc=True).dt.tz_convert('Europe/Berlin'), inplace=True)
    df.drop('Datetime',axis=1,inplace=True)
    df.columns = ['ID', 'T_amb', 'Rh_amb','windspeed','gustspeed','rain','winddir','btry']
    df.drop(['ID', 'btry'],axis = 1,inplace=True)
    df['rain'].replace(0,np.nan,inplace=True)
    return df

################################################ LOAD MOILNE FILEs ################################################

def load_energy_data(bui, ts='1min'):
    df = pd.read_csv(files['em'][bui][ts], index_col = [0], header=[0,1,2],low_memory=False)
    df.index = pd.to_datetime(df.index, utc=True).tz_convert('Europe/Berlin')
    df.drop('TPID',axis=1,level=2,inplace=True)
    meters = {'HQ':'Energie','VW':'Volumen','H':'Heizung','W':'Wasser'}
    idx = []
    for col in df.columns:
        t = '_'.join(col)
        try:
            app = {'2OG-Nord' : 'N','2OG-Ost':'O','2OG-Sued':'S'}[t.split('_')[0]]
        except:
            app = t
        meter = t.split('_')[-2]
        unit = t.split('_')[-1]
        clmn = (app,unit,meter)
        idx.append(clmn)

    df.columns = pd.MultiIndex.from_tuples(idx)
    for col in df.filter(like='HQ').columns:
        df[col] = df[col]/1000 #kWh

    return df

def import_data(mode = 'all', startdate = '2021-06-01', timestep = '1min'):
    '''
    args:
    -----
        mode: {'all', 'IND', 'AMB','EM', 'tinkerforge'} (default = 'all')
            -- 'all' returns IND, AMB, EM
            -- 'tinkerforge' retruns IND, AMB
        startdate: (default = '2021-06-01')
        timestep: {'1min', '15min', '60min'} (default = '1min')
    '''
    if mode == 'IND':
        IND = pd.concat({bui: load_tf_bui(bui, timestep).loc[startdate:] for bui in BUID},axis=1)
        return IND
    elif mode == 'AMB':
        AMB = pd.merge(load_tf_weather(timestep).loc[startdate:], load_tf_pm(timestep).loc[startdate:], left_index=True, right_index=True)
        return AMB
    elif mode == 'EM':    
        EM = pd.concat({bui: load_energy_data(bui) for bui in BUID}, axis=1)
        return EM
    elif mode == 'all':
        IND = pd.concat({bui: load_tf_bui(bui, timestep).loc[startdate:] for bui in BUID},axis=1)
        AMB = pd.merge(load_tf_weather(timestep).loc[startdate:], load_tf_pm(timestep).loc[startdate:], left_index=True, right_index=True)
        EM = pd.concat({bui: load_energy_data(bui) for bui in BUID}, axis=1)
        return IND, AMB, EM
    elif mode == 'tinkerforge':
        IND = pd.concat({bui: load_tf_bui(bui, timestep).loc[startdate:] for bui in BUID},axis=1)
        AMB = pd.merge(load_tf_weather(timestep).loc[startdate:], load_tf_pm(timestep).loc[startdate:], left_index=True, right_index=True)
        return IND, AMB
    else:
        print('mode ungültig...')