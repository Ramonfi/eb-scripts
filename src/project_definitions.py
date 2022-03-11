#import datetime as dt
import os
import math as m
import datetime as dt
import numpy as np
import pandas as pd

import numpy as np
from src.utilities import truncate_colormap

#########################################################  USER INPUTS  #############################################################################

# Ein paar Namen und Kurzbezeichnungen
### Kurzbezeichnung Häuser
BUID = {'MH': 'Massivholz','MW': 'Mauerwerk','LB': 'Leichtbeton'}
buid = {'MH': truncate_colormap('Greens_r',0, 0.6), 'MW': truncate_colormap('Oranges_r',0, 0.7), 'LB': truncate_colormap('Blues_r',0, 0.6)}
### Kurzbezeichnung Wohnungen (Messdaten)
WOHNUNGEN = {'N':'Nord','S':'Süd','O':'Ost'}
### Kurzbezeichnung Wohnungen (Simulation)
ori = {'WE1':'Nord','WE2':'Ost','WE3':'Süd'}
### Überzetzung Wohnungsbezeichnungen (Simulation in Messdaten)
wohnungen2 = {'WE1': 'N', 'WE3': 'S', 'WE2': 'O'}
### Übersetzung Wohungsbezeichnungen (Moline in Kurzbezeichnung Messdaten)
wohnungen3 = {'2OG-Nord' : 'N','2OG-Ost':'O','2OG-Sued':'S'}
### Kurzbezeichnung Räume
ROOMS = {'B':'Bad', 'F':'Flur', 'K':'Küche', 'SZ':'Schlafzimmer', 'WZ':'Wohnzimmer', 'SWK':'1-Zimmer-Appartment'}
### Kurzbezeichnungen Moiline Zähler
meters = {'HQ':'Energie','VW':'Volumen','H':'Heizung','W':'Wasser'}
### Airnodes aus der Simulation
airnodes = ['A1_WE1_Wohnen','A2_WE1_Innenflur','A3_WE1_Diele','A4_WE1_Schlafen','A5_WE1_Kueche','A6_WE1_Bad','A16_TH_gesamt','A18_DG_gesamt','A17_TH_gesamt','A7_WE2_Schlafen','A8_WE2_Innenflur','A9_WE2_Bad','A10_WE3_Wohnen','A11_WE3_Innenflur','A12_WE3_Diele','A13_WE3_Schlafen','A14_WE3_Kueche','A15_WE3_Bad','A19_DG_gesamt']

# Datenbanken
### Lokaler Pfad in Projektverzeichnis
dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'eb-data')
dir_db = os.path.join(dir,'database')
### Pfad auf Lehrstuhl-Laufwerk
dir_db_ls = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\2_datenbank'

# Ordner für Auswertungn
### Lokaler Pfad in Projektverzeichnis
dir_results = os.path.join(dir,'Results')
### Pfad auf Lehrstuhl-Laufwerk
dir_results_ls = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\3_auswertung'

### Rohdaten (Dropbox, Archiv & co)
## 1) Energy Monitoring
em_dropbox = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\1_rohdaten\EM\RmCU'

## 2) Tinkerforge Dropbox Sync
tf_dropbox = os.path.join(r'\\nas.ads.mwn.de','tuar','l15','private','DATA','FORSCHUNG','04_Projekte','2021','Einfach_Bauen_3','Daten','1_rohdaten')

## 3) Archiv: Daten vor September (ohne Dropbox-Sync)
tf_archive = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\ARCHIV\1_rohdaten'

# Erstelle eine Vorlage für die config-File die zum eMail Versand notwendig ist.
config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.py')
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        f.write('sender = "email-adress"\npassword = ""\nsmtp=""emails={"name":"name <name@email.com>"}')
        f.close()

em_name_file = config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'energymeter.config')

# Erstelle eine ReadMe File im Projektverzeichnis
readme = os.path.join(dir_db,'readme.txt')
with open(readme, "w") as f:
    f.write(f'Stand: {dt.date.today()-dt.timedelta(days=1)}\n\n\
Abkürzungsverzeichnis:\n\
gesamt = Wärmemengenzähler am Hausanschluss\n\
LB = Leichtbetonhaus\n\
MH/HM = Massivholzhaus\n\
MW = Ziegelhaus\n\
PM = Pyranometer\n\
WD = Wetterstation\n\n\
em = Wärmemengenzähler\n\
tf = TinkerForge Sensoren\n\n\
raw/database = unverarbeitete Datensätze. Enthalten Lücken wenn Sensoren ausfallen.\n\
resampled = nachberarbeitete Datensätze. Sie haben einen durchgehenden Zeitindex (1min, 15min oder 60min), Zwischenwerte werden gelöscht. Dadurch sind nichtmehr alle Werte Aussagekräftig (z.B. Fenster und Bewegungsmelder).')


# Berechne die Flächen der Airnodes für die Simulation
idx = [(item.split('_')[1], item.split('_')[0]) for item in airnodes]

A = pd.Series([21.775,2,6.46,17.85,8.8775, 4.8,0, 0, 0,17.85,2,4.8,15.075,2.0,12.92,17.85,8.8775,4.8,0],pd.MultiIndex.from_tuples(idx))

# Berechne die Fläche pro Wohneinheit für die Simulation
area = {}
for app in ['WE1','WE2','WE3']:
    try:
        if app not in area:
            area[wohnungen2[app]] = {}
        area[wohnungen2[app]]['array'] = A[app]
        area[wohnungen2[app]]['sum'] = A.groupby(level=0).sum()[app]
        area[wohnungen2[app]]['%']=(area[wohnungen2[app]]['array']/area[wohnungen2[app]]['sum'])
    except:
        continue

AREA = (pd.DataFrame(A.groupby(level=0).sum()).T)[['WE1','WE2','WE3']]
AREA.columns = ['N','O','S']


TIR = {'LB': {
    'm_tir3_obj (°C)':'Küchenzeile [WEST]',
    'm_tir4_obj (°C)':'Außenwand [OST]',
    'm_tir6_obj (°C)':'Nachbarwohnung [SÜD]',
    'm_tir5_obj (°C)':'Treppenhaus [NORD]',
    'm_tir2_obj (°C)':'Decke',
    'm_tir1_obj (°C)':'Fußboden'
    },'MW': {
    'm_tir1_obj (°C)':'Küchenzeile [WEST]', 
    'm_tir2_obj (°C)':'Außenwand [OST]',
    'm_tir3_obj (°C)':'Nachbarwohnung [SÜD]',
    'm_tir4_obj (°C)':'Treppenhaus [NORD]',
    'm_tir5_obj (°C)':'Decke',
    'm_tir6_obj (°C)':'Fußboden'
    },'MH': {
    'm_tir1_obj (°C)':'Küchenzeile [WEST]', 
    'm_tir3_obj (°C)':'Außenwand [OST]',
    'm_tir2_obj (°C)':'Nachbarwohnung [SÜD]',
    'm_tir4_obj (°C)':'Treppenhaus [NORD]',
    'm_tir5_obj (°C)':'Decke',
    'm_tir6_obj (°C)':'Fußboden'
    }
}

WANDFLÄCHEN = {
    'Fußboden': 17.9,
    'Decke':17.9,
    'Küchenzeile [WEST]':7.5,
    'Außenwand [OST]':10.5,
    'Treppenhaus [NORD]':16.3,
    'Nachbarwohnung [SÜD]':16.3
    }

df = pd.read_csv('.\src\KorrekturFaktoren.csv', index_col=[0])
df.index = df.index.str.split('_', expand=True)

KORREKTUR_RH = df.unstack().droplevel(0,axis=1).dropna(axis=1).round(1).to_dict()['deltaRH'] #{'MH': 4.2,'MW': 13.5,'LB':5.3}
KORREKTUR_T = df.unstack().droplevel(0,axis=1).dropna(axis=1).round(1).to_dict()['deltaT']