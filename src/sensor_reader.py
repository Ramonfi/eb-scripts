import pandas as pd
import numpy as np

import src.project_definitions as eb

def load_tf_bui(bui, timestep='60min'):
    path = eb.files['tf'][bui][timestep]
    df = pd.read_csv(
            path, 
            decimal='.', 
            na_values = '#N/V',
            parse_dates = ['Datetime'],
            infer_datetime_format=True,
            index_col='Datetime',
            dayfirst=True
            )

    df.replace([' ','  '],np.NAN,inplace=True)
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
                name = '_'.join(sensor)

            elif len(sensor) < 4:
                if len(sensor[0]) == 1:
                    whg = sensor[0]
                    room = ''
                    name = '_'.join(sensor[1:])
                else:
                    whg = ''
                    room = ''
                    name = '_'.join(sensor)

            elif len(sensor) >= 4:
                whg = sensor[0]
                if whg in ['N', 'S', 'O']:
                    room = sensor[1]
                    name = '_'.join(sensor[2:])
                elif whg in ['TH']:
                    room = ''
                    name = '_'.join(sensor[1:])

        else:
            if sensor == '-->Extra-Sensors-->':
                whg == ''
                room == ''
                name = ''
            else:
                whg = 'DA'
                room = ''
                name = sensor.split('-')[1].split('_', 2)[2]
        index = (whg,room,name)
        idx.append(index)
        
    df.columns = pd.MultiIndex.from_tuples(idx)
    df.sort_index(axis=1,inplace=True)
    return df

################################################ LOAD PYRANOMETER FILE ################################################

def load_tf_pm(timestep='60min'):
    path = eb.files['tf']['PM'][timestep]
    df = pd.read_csv(
        path, 
        decimal='.', 
        na_values = '#N/V',
        parse_dates = ['Datetime'],
        infer_datetime_format=True,
        index_col='Datetime',
        dayfirst=True
        )
    df['Direct W/m^2'][df['Direct W/m^2'] < 0] = 0
    df['Diffuse W/m^2'] = df['Global W/m^2'] - df['Direct W/m^2']
    #df = df.abs()
    
    df.columns = df.columns.str.split(' ',expand=True).droplevel(level=1).str.lower()

    return df

################################################ LOAD WEATHER FILE ################################################

def load_tf_weather(timestep='60min'):
    path = eb.files['tf']['WD'][timestep]
    df = pd.read_csv(
        path, 
        decimal='.', 
        na_values = '#N/V',
        parse_dates = ['Datetime'],
        infer_datetime_format=True,
        index_col='Datetime',
        dayfirst=True
        )
    df.columns = ['ID', 'T_amb', 'Rh_amb','windspeed','gustspeed','rain','winddir','btry']
    df.drop(['ID', 'btry'],axis = 1,inplace=True)
    df['rain'].replace(0,np.nan,inplace=True)
    return df

################################################ LOAD MOILNE FILEs ################################################

def load_energy_data(bui, ts='1min'):
    df = pd.read_csv(eb.files['em'][bui][ts], index_col = [0], header=[0,1,2])
    df.index = pd.to_datetime(df.index)
    df.drop('TPID',axis=1,level=2,inplace=True)
    meters = {'HQ':'Energie','VW':'Volumen','H':'Heizung','W':'Wasser'}
    idx = []
    for col in df.columns:
        t = '_'.join(col)
        try:
            app = eb.wohnungen3[t.split('_')[0]]
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