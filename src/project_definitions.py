#import datetime as dt
import os
import math as m
import datetime as dt
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import smtplib, ssl
import urllib.parse
from getpass import getpass
import platform

from eblib import style
import eblib.utilities as ut

#########################################################  USER INPUTS  #############################################################################
def mount_ls(server='nas.ads.mwn.de', share='/tuar/l15/private/DATA/FORSCHUNG/04_Projekte/2021/Einfach_Bauen_3/Daten/', local_mount=None):

    print(f'\ntrying to mount \n\t{server}{share}\non\n\t{local_mount}\n')
    user = input(f'Enter the username on {server}:\n')
    password = getpass(f'Enter the password for user {user} on {server}:\n')
    pw = urllib.parse.quote_plus(password)

    os.system(f'mount_smbfs -o automounted -N "//{user}:{pw}@{server}{share}" "{local_mount}"')

    if os.path.ismount(local_mount):
        print(f'{local_mount}: successfully mounted.\n')

def unmount_ls(local_mount=os.path.join(os.path.dirname(os.path.dirname(__file__)),'eb-remote')):
    os.system(f'umount {local_mount}')
    if os.path.ismount(local_mount) == False:
        print(f'{local_mount}: successfully unmounted.\n')

### short name of buildings
buid = {'MH': 'Massivholz','MW': 'Mauerwerk','LB': 'Leichtbeton'}

# ID of room based on sensor-naming, which should be analysed
wohnungen = {'N':'Nord','S':'Süd','O':'Ost'}
wohnungen2 = {'WE1': 'N', 'WE3': 'S', 'WE2': 'O'}
ori = {'WE1':'Nord','WE2':'Ost','WE3':'Süd'}
wohnungen3 = {'2OG-Nord' : 'N','2OG-Ost':'O','2OG-Sued':'S'}
rooms = {'B':'Bad', 'F':'Flur', 'K':'Küche', 'SZ':'Schlafzimmer', 'WZ':'Wohnzimmer', 'SWK':'1-Zimmer-Appartment'}
meters = {'HQ':'Energie','VW':'Volumen','H':'Heizung','W':'Wasser'}
airnodes = ['A1_WE1_Wohnen','A2_WE1_Innenflur','A3_WE1_Diele','A4_WE1_Schlafen','A5_WE1_Kueche','A6_WE1_Bad','A16_TH_gesamt','A18_DG_gesamt','A17_TH_gesamt','A7_WE2_Schlafen','A8_WE2_Innenflur','A9_WE2_Bad','A10_WE3_Wohnen','A11_WE3_Innenflur','A12_WE3_Diele','A13_WE3_Schlafen','A14_WE3_Kueche','A15_WE3_Bad','A19_DG_gesamt']

### path to datasheets
dir_db = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'eb-data','database')
dir_db_ls = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\2_datenbank'

### paths for exporting graphs and results
dir_results = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'eb-data','Results')
dir_results_ls = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\3_auswertung'

### paths where (new) raw data is stored
## 1) Energy Monitoring
em_path = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\1_rohdaten\EM\RmCU'

## 2) Tinkerforge Dropbox Sync
tf_path = os.path.join(r'\\nas.ads.mwn.de','tuar','l15','private','DATA','FORSCHUNG','04_Projekte','2021','Einfach_Bauen_3','Daten','1_rohdaten')

## 3) Archiv: Daten vor September (ohne Dropbox-Sync)
tf_archive = r'\\nas.ads.mwn.de\tuar\l15\private\DATA\FORSCHUNG\04_Projekte\2021\Einfach_Bauen_3\Daten\ARCHIV\1_rohdaten'

if platform.system() == 'Darwin':
    dir = os.path.dirname(os.path.dirname(__file__))
    mount = os.path.join(dir,'eb-remote')

    if not os.path.exists(mount):
        os.makedirs(mount)

    if os.path.ismount(mount) == False:
        mount_ls(local_mount = mount)

    if os.path.ismount(mount):
        dir_db_ls = os.path.join(mount,'2_datenbank')
        dir_results_ls = os.path.join(mount,'3_auswertung')
        em_path = os.path.join(mount,'1_rohdaten','EM','RmCU')
        tf_path = os.path.join(mount,'1_rohdaten')
        tf_archive = os.path.join(mount,'ARCHIV','1_rohdaten')

### Construct filepaths to databases
files ={}
for meter in ['tf','em']:
    if meter not in files:
        files[meter] = {} 
    for bui in list(buid.keys()) + ['WD','PM']:
        path = os.path.join(dir_db,bui)
        if not os.path.isdir(path):
            os.makedirs(path)
        for fn in os.listdir(path):
            names = fn.split('_')
            if names[1] == meter:
                if bui not in files[meter]:
                    files[meter][bui] = {}
                files[meter][bui][fn.rsplit('_',1)[-1].split('.')[0]] = os.path.join(os.path.join(path), fn)

### prepare config file for email support
config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.py')
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        f.write('sender = "email-adress"\npassword = ""\nsmtp=""emails={"name":"name <name@email.com>"}')
        f.close()

### prepare readme file
readme = os.path.join(dir_db,'readme.txt')
if not os.path.exists(readme):
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
resampled = nachberarbeitete Datensätze. Haben einen durchgehenden Zeitindex (1min, 15min oder 60min). Zwischenwerte werden allerdings einfach gelöscht. Heißt nicht alle Werte sind Aussagekräftig (z.B. Fenster und Bewegungsmelder nicht!)')
        f.close()

### Construct dict with room areas....
idx = [(item.split('_')[1], item.split('_')[0]) for item in airnodes]
A = pd.Series([21.775,2,6.46,17.85,8.8775, 4.8,0, 0, 0,17.85,2,4.8,15.075,2.0,12.92,17.85,8.8775,4.8,0],pd.MultiIndex.from_tuples(idx))

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

### Colors:
cmap_temp = ut.truncate_colormap('Reds_r' ,minval=0 ,maxval=0.8)
cmap_hum = ut.truncate_colormap('Blues_r',minval=0.2,maxval=0.8)
cmap_co2 = ut.truncate_colormap('Greens_r', minval=0,maxval=0.8)