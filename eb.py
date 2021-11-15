#import datetime as dt
import os
import math as m

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import smtplib, ssl
import urllib.parse
from getpass import getpass
import platform

################################################ TOOLS ################################################
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    if isinstance(cmap,str):
        cmap=plt.get_cmap(cmap)
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap
    
def recolor_lines(ax,cmap,minint=0,maxint=1):
    num_plots = len(ax.lines)
    cmap = truncate_colormap(cmap,minint,maxint,100)
    new_colors = [plt.get_cmap(cmap)(1. * i/num_plots) for i in range(num_plots)]
    for c, line in enumerate(ax.lines):
        line.set_color(new_colors[c])

def get_labels(dfp):
    labels = dfp.columns.values

    if len(labels)==1:
        labels = ''.join(labels[0])
    else:
        for l, label in enumerate(labels):
            labels[l] = ''.join(label)

    return labels

def send_email(who,sender,subject,text,password,smtp):
    RCPT_TO = ', '.join(who)
    subject = subject
    MAIL_FROM = sender  # Enter receiver address
    DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (MAIL_FROM, RCPT_TO, subject, text)

    port = 465  # For SSL
    smtp_server = smtp
    sender_email = sender.rsplit(' ',1)[-1].replace('<','').replace('>','')  # Enter your address
    receiver_email = [who[i].split(' ')[-1].replace('<','').replace('>','') for i in range(len(who))]  # Enter receiver address
    password = password
    message = DATA.encode()

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Message sent!')

def export(fig,filepath,filename,extlist = list(),extsubfolder=False,show=False):
    for ext in extlist:
        exportname = os.path.join(filepath,filename + '.' + ext)
        if extsubfolder:
            exportname = os.path.join(filepath,ext,filename + '.' + ext)
        if os.path.isdir(os.path.dirname(exportname)) == False:
            os.makedirs(os.path.dirname(exportname))
        fig.savefig(os.path.join(exportname),bbox_inches="tight",dpi=300)
        print(exportname,'saved!')
    if show == False:
        plt.close()

### Wasserdampfsättungsdruck
def psat(t):
    if t >= 0:
        return 610.5*m.exp((17.269*t)/(237.3+t))
    if t < 0:
        return 610.5*m.exp((21.875*t)/(265.5+t))

### Luftdichte in Abhängigkeit von der Temperatur in kg/m³
def roh(t):
    # Temperatur in Kelvin
    T = 273.15 + t
    # atmosphärischer Luftdruck in Pa:
    p = 101325   
    # spezifische Gaskonstante in J/(kg*K) 
    Rs = 287.058 

    return p/(Rs*T) 

#Umrechnung spezifische Feuchte zu absoluter Feuchte
def x_to_g(g, t):
    # x: spezifische Luftfeuchte in g/kg Luft
    # g: absolute Luftfeuchte in g/m³ Luft
    # roh: Dichte von Luft, abhängig von der Temperatur t:
    def roh(t):
        # Temperatur in Kelvin
        T = 273.15 + t
        # atmosphärischer Luftdruck in Pa:
        pamb = 101325   
        # spezifische Gaskonstante in J/(kg*K) 
        Rs = 287.058 

        return pamb/(Rs*T)

    return g/roh(t)

# absolute Luftfeuchtigkeit in g/kg von temperatur und luftfeuchte
def g_abs(rh:float,t:float):
    # atmosphärischer Luftdruck in Pa:
    p = 101325
    # Wasserdampfsättigungsdruck
    def psat(t):
        if t >= 0:
            return 610.5*m.exp((17.269*t)/(237.3+t))
        if t < 0:
            return 610.5*m.exp((21.875*t)/(265.5+t))

    rh=rh/100

    return round( 0.622 * (rh*psat(t))/(p-rh*psat(t)) * 1000 ,2)

# relative feuchte von absoluter feuchte und temperatur
def RH(g:float,t:float):
    # atmosphärischer Luftdruck in Pa:
    p = 101325
    # Wasserdampfsättigungsdruck
    def psat(t):
        if t >= 0:
            return 610.5*m.exp((17.269*t)/(237.3+t))
        if t < 0:
            return 610.5*m.exp((21.875*t)/(265.5+t))
    #absoulte Feuchte in kg/kg
    g = g/1000
    return round( (g*p/(psat(t)*(0.622+g))*100), 1)


################################################ READ DATABASES ###############################################    

################################################ LOAD BUI FILE ################################################
def load_bui(path):
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
        try:
            t = col.strip().split(' (')[0].split('_',4)
            #print(len(t))
            whg = t[2]
            rm = t[3]
            sensor = t[4].strip().replace('  ',' ')

        except:
            try:
                t = col.strip().split(' (')[0].split('_',3)
                whg = t[2]
                rm = 'Strom'
                sensor = t[3] + ' (' + col.strip().split(' (')[1]
            except:
                whg = ''
                rm = ''
                sensor = col

        idx.append((whg,rm,sensor))

    df.columns = pd.MultiIndex.from_tuples(idx)
    df.sort_index(axis=1,inplace=True)
    df.drop('',level=0,axis=1,inplace=True)

    return df

################################################ LOAD PYRANOMETER FILE ################################################

def load_pm(path):

    df = pd.read_csv(
        path, 
        decimal='.', 
        na_values = '#N/V',
        parse_dates = ['Datetime'],
        infer_datetime_format=True,
        index_col='Datetime',
        dayfirst=True
        )
    df = df.abs()
    df.columns = df.columns.str.split(' ',expand=True).droplevel(level=1).str.lower()

    return df

################################################ LOAD WEATHER FILE ################################################

def load_amb(path):
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

################################################ PLOT TEMPLATES ################################################

################################################ HX DIAGRAMM ################################################

def hx_diagramm(t1, rh1, ax, t2=None,rh2=None, cmap='Blues_r',minint=0,maxint=1):

    # absolute Luftfeuchtigkeit in g/kg
    def g_abs(t: float, rh: float):
        # atmosphärischer Luftdruck in Pa:
        p = 101325
        # Wasserdampfsättigungsdruck
        def psat(t):
            if t >= 0:
                return 610.5*m.exp((17.269*t)/(237.3+t))
            if t < 0:
                return 610.5*m.exp((21.875*t)/(265.5+t))

        rh=rh/100

        return round( 0.622 * (rh*psat(t))/(p-rh*psat(t)) * 1000 ,2)

    def t_for_g(g, rh):
        A = 23.1964
        B = 3816.44
        C = 273.15 - 46.13
        pamb = 101325

        blub = ((29*g)/18000)/(1+29*g/18000)

        p_0 = blub*(100/rh)*pamb

        return B/(A-m.log(p_0))-C

    new_colors = [truncate_colormap(cmap,minint,maxint)(1. * i/2) for i in range(2)]

    # Wertebereich für Chart
    drybulb_graph = np.linspace(-20,40, 601)
    rh_graph = np.linspace(10,100,10)

    # Komfortbereich
    minrf = 30
    maxrf = 65
    maxaf = 11.5
    t_min = 20
    t_max = 26

    #Ränder der Grafik
    min_x = -20
    min_y = 0
    max_x = 40
    max_y = 20

    #Achsen Minima und Maxima
    ax.set_xlim(min_x,max_x)
    ax.set_ylim(min_y,max_y)             
 
    # Linien für das HX-Diagramm erstellen
    for item in rh_graph:
        ax.plot(drybulb_graph, [g_abs(t,item) for t in drybulb_graph], 'k-')
        if g_abs(40,item) <= max_y:
            ax.text(40,g_abs(40,item), '  {}%'.format(int(item)), ha = 'left', va = 'bottom')
        if g_abs(40,item) > max_y:
            ax.text(t_for_g(max_y,item),max_y, s='{}%'.format(int(item)), ha = 'left', va = 'bottom', rotation = 45)
    
    if isinstance(t2,(pd.Series, pd.DataFrame)) and isinstance(rh2, (pd.Series, pd.DataFrame)):
        df = pd.concat([t2, rh2],axis=1)
        df.columns = ['t', 'Rh']
        df.dropna(inplace=True)
        df = df.astype(float, errors='raise')
        if len(df)==0:
            return
        df['G_abs'] = df.dropna().apply(lambda x: g_abs(x['t'], x['Rh']), axis = 1)
        n_comf = df[(df.t > t_min) & (df.t < t_max) & (df.Rh < maxrf) & (df.Rh > minrf) & (df.G_abs < maxaf)].shape[0]

        per_comf_t2 = round(n_comf/min(len(t2), len(rh2))*100,0)
        ax.plot(
            df['t'],
            df['G_abs'], 
            marker = '.',
            c=new_colors[1],
            linestyle ='none', 
            label = 'Außenluftfeuchte',
            alpha = 0.75
            )

    df = pd.concat([t1, rh1],axis=1)
    df.columns = ['t', 'Rh']
    df.dropna(axis=0,inplace=True)
    df = df.astype(float, errors='raise')
    if len(df)==0:
        return
    df['G_abs'] = df.dropna().apply(lambda x: g_abs(x['t'], x['Rh']), axis = 1)

    n_comf = df[(df.t > t_min) & (df.t < t_max) & (df.Rh < maxrf) & (df.Rh > minrf) & (df.G_abs < maxaf)].shape[0]

    per_comf_t1 = round(n_comf/min(len(t1), len(rh1))*100,0)

    ax.plot(
        df['t'],
        df['G_abs'], 
        marker = '.',
        c=new_colors[0],
        linestyle ='none', 
        label = 'Raumluftfeuchte',
        alpha = 0.75
        )

    tx = np.linspace(t_min,t_max,21)
    y1 = [g_abs(t,minrf) for t in tx]
    y2 = [min(g_abs(t,maxrf),maxaf) for t in tx]

    ax.fill_between(
        x = tx,
        y1=y1,
        y2=y2,
        color='k',
        alpha=0.2, 
        label = 'Behaglichkeitsbereich nach DIN 1946-6'
        )

    ax.annotate(r"$\bf{" + str(int(per_comf_t1)) + str('\%') + "}$" + ' der Messpunkte\nim Behaglichkeitsbereich',
            xy=(20, min(y2)), xycoords='data',
            xytext=(0.55, 0.6), textcoords='axes fraction',
            arrowprops=dict(arrowstyle="->"),bbox=dict(boxstyle="round", fc="w"),
            horizontalalignment='center', verticalalignment='top')

    ax.set_xlabel(
        'Lufttemperatur [°C]',
        )

    ax.set_ylabel(
        'Absolute Luftfeuchte\n[g/kg]', 

        ) 

    ax.xaxis.set_major_formatter('{x:.0f}')
    ax.yaxis.set_major_formatter('{x:.0f}')

    ax.set_title(
        'H,x - Diagramm', 
        fontweight = 'bold', 
        )

    ax.legend(
        loc='upper left',
        markerscale = 3,
        frameon=False)

    for spine in ax.spines:
        ax.spines[spine].set_visible(False)

################################################ Thermischer Komfort nach DIN  ################################################

def thermal_comfort_2(TAMBG24, TOP, axs, KAT={'I':2,'II':3,'III':4}):
    def komfortstunden(df):
        results={}
        KAT={'I':2,'II':3,'III':4}
        df.columns = ['Tamb_g24', 'TOP']    
        for idx, row in df.iterrows():
            for key in KAT:
                t_op = row.TOP
                t = row.Tamb_g24
                if t > 10:
                    lower = (t/3)+18.8-KAT[key]-1
                    upper = (t/3)+18.8+KAT[key]
                    if (lower < t_op < upper) == False:
                        if t_op < min(lower, upper):
                            if 'lower' not in results:
                                results['lower'] = {}
                            if key not in results['lower']:
                                results['lower'][key] = 0
                            results['lower'][key] += 1
                        if t_op > max(lower, upper):
                            if 'upper' not in results:
                                results['upper'] = {}
                            if key not in results['upper']:
                                results['upper'][key] = 0
                            results['upper'][key] += 1
        return results

    df = pd.concat([TAMBG24,TOP],axis=1)
    df.columns = ['Tamb_g24', 'TOP']
    df.dropna(inplace=True)
    df=df[(df.Tamb_g24 >10) & (df.Tamb_g24 < 30)]
    df
    linestyle = ['dashdot','dotted','solid']
    KAT={'I':2,'II':3,'III':4}

    for k, key in enumerate(KAT):
        x1 = np.linspace(10,30)
        x2 = np.linspace(10,30)

        y1 = [(t/3)+18.8-KAT[key]-1 for t in x1]
        y2 = [(t/3)+18.8+KAT[key] for t in x2]

        axs.plot(x1, y1, c='k',ls = linestyle[k])
        axs.plot(x2, y2, c='k',ls = linestyle[k])

        axs.annotate(
            f'KAT {key}',
            xy=(min(x1), 
            min(y1)), 
            xycoords='data',
            xytext=(-5, 0), 
            textcoords='offset points',
            horizontalalignment='right', 
            verticalalignment='center'
            )

        axs.annotate(
            f'KAT {key}',
            xy=(min(x2), 
            min(y2)), 
            xycoords='data',
            xytext=(-5, 0), 
            textcoords='offset points',
            horizontalalignment='right', 
            verticalalignment='center'
            )

    x = np.linspace(10,30)
    y = [(t/3)+18.8 for t in x]
    axs.plot(x, y, c='k',ls = 'dashed', label = 'Komforttemperatur')

    axs.plot(df['Tamb_g24'], df['TOP'],color =truncate_colormap('Reds_r',0,0.8)(0.1),
                    marker = '.', 
                    linestyle='None',
                    alpha=0.75,
                    label = 'Raumlufttemperatur im Verhältnis zur Außenlufttemperatur'
                    )

    results = komfortstunden(df)
    text2 = r"$\bf{" + str('Untergradstunden') + "}$" + '\n'
    text1 = r"$\bf{" + str('Übergradstunden') + "}$" + '\n'
    for key in results:
        if key == 'upper':
            for kat in results[key]:
                if results[key][kat] > 0:
                    text1 += 'KAT {}: {}\n'.format(kat, results[key][kat]) 
            axs.text(
                0.1,
                0.95, 
                text1.strip(),      
                style='normal', 
                ha = 'left', 
                va = 'top',
                transform=axs.transAxes,
                bbox=dict(boxstyle="round", fc="w"), 
                )
        if key == 'lower':
            for kat in results[key]:
            
                if results[key][kat] > 0:
                    text2 += 'KAT {}: {}\n'.format(kat, results[key][kat]) 
            axs.text(
                0.9,
                0.15, 
                text2.strip(),      
                style='normal', 
                ha = 'right', 
                va = 'bottom',
                transform=axs.transAxes,
                bbox=dict(boxstyle="round", fc="w"), 
                )
                
    axs.set_xlabel('gleitender Mittelwert der Außenlufttemperatur [°C]')
    axs.set_xlim(8,32)
    axs.set_ylabel('Raumtemperatur\n[°C]')
    axs.set_title('Adaptives Komfortmodell nach DIN EN 16798-1 - Anhang B2.2', fontweight = 'bold')
    axs.legend(loc='lower right',markerscale = 3)


#########################################################  USER INPUTS  #############################################################################
def mount_ls(mount):
    server = 'nas.ads.mwn.de'
    share = '/tuar/l15/private/DATA/FORSCHUNG/04_Projekte/2021/Einfach_Bauen_3/Daten/'

    print(f'\ntrying to mount \n\t{server}{share}\non\n\t{mount}\n')
    user = input(f'Enter the username on {server}:\n')
    password = getpass(f'Enter the password for user {user} on {server}:\n')
    pw = urllib.parse.quote_plus(password)

    os.system(f'mount_smbfs -o automounted -N "//{user}:{pw}@{server}{share}" "{mount}"')

    if os.path.ismount(mount):
        print(f'{mount}: successfully mounted.\n')

def unmount_ls(mount):
    os.system(f'umount {mount}')
    if os.path.ismount(mount) == False:
        print(f'{mount}: successfully unmounted.\n')

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
        mount_ls(mount)

    if os.path.ismount(mount):
        dir_db_ls = os.path.join(mount,'2_datenbank')
        dir_results_ls = os.path.join(mount,'3_auswertung')
        em_path = os.path.join(mount,'1_rohdaten','EM','RmCU')
        tf_path = os.path.join(mount,'1_rohdaten')
        tf_archive = os.path.join(mount,'ARCHIV','1_rohdaten')

### prepare config file for email support
config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.py')
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        f.write('sender = "email-adress"\npassword = ""\nsmtp=""emails={"name":"name <name@email.com>"}')
        f.close()

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


#############################################STYLE GUIDE ##############################################

figsize = (15,10)
height = 15
width = 10

def cm(inch):return inch*2.54
def inch(cm):return cm/2.54

din_a4 = (inch(21), inch(29.7))
din_a4_landscape = (inch(29.7), inch(21))

din_a3 = (inch(29.7), inch(2*21))
din_a3_landscape = (inch(2*21), inch(2*29.7))

figsize = (width,height)

### Colors:
c_temp = truncate_colormap('Reds_r' ,minval=0 ,maxval=0.8)
c_hum = truncate_colormap('Blues_r',minval=0.2,maxval=0.8)
c_co2 = truncate_colormap('Greens_r', minval=0,maxval=0.8)

def set_rc_eb():
    #fontsizes
    SMALL_SIZE = 9
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12

    plt.rc("figure", figsize=(10,6))
    plt.rc("figure", titlesize=BIGGER_SIZE)

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes

    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
    plt.rc('axes.spines', left=False)
    plt.rc('axes.spines', right=False)
    plt.rc('axes.spines', top=False)
    plt.rc('axes.spines', bottom=False)

    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels

    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('legend', frameon=False)
    plt.rc('legend', loc = 'best')
    plt.rc('lines', linewidth = 1)
    plt.rcParams['lines.markersize']  = 1.5