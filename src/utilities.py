import smtplib, ssl
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# ======== costum colormap ==========
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    if isinstance(cmap,str):
        cmap=plt.get_cmap(cmap)
    new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

# ======== recolor lineplots ==========
def recolor_lines(ax,cmap,minint=0,maxint=1):
    num_plots = len(ax.lines)
    cmap = truncate_colormap(cmap,minint,maxint,100)
    new_colors = [plt.get_cmap(cmap)(1. * i/num_plots) for i in range(num_plots)]
    for c, line in enumerate(ax.lines):
        line.set_color(new_colors[c])

# ======== ticks to hours ==========
def ticks_to_hours(ax):
    ### Diese Funktion rechnet die y-label eines Graphen von Minuten in Stunden um.
    ticks = ax.get_yticks()
    n_ticks = len(ticks)
    max_ticks = round((ticks.max()/60/1000),0)*1000
    new_ticks = range(0,int(max_ticks),int(n_ticks))
    ax.set_yticklabels(new_ticks)

# ======== get clean labels from multiindex df ==========
def get_labels(df):
    labels = df.columns.values
    if len(labels)==1:
        labels = ''.join(labels[0])
    else:
        for l, label in enumerate(labels):
            labels[l] = ''.join(label)
    return labels

# ======== export graphs to subfolders ==========
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

# ======== running bar command line print ==========
def running_bar(m, m_max):
    m_max = m_max-1
    n = int((m/m_max)*100)
    s = 'loading <' + (n)*'|' + (100-n) * '-' + f'> {n} %       '
    if m < m_max:
        print(s,end='\r',flush=True)
    if m == m_max:
        print(s,end='\r',flush=True)
        s2 = 'finished!'
        s = s2 + (len(s)-len(s2))*' '
        print(s,end='\r')


# ======== send email to receipient ==========
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

# ======== set_ticks ==========
def set_ticks(ax:plt.axes, min:float, max:float, step:float=None, axes:str='y') -> None:
    '''
    Passt die Grenzen und Schrittweite Achse an.

    Args:
    ---
    ax: Plot auf den die Funktion angewendet werden soll
    min: Untere Grenze der Achse.
    max: Obere Grenze der Achse.
    axes: Welche Achse soll angepasst werden? 'x' oder 'y' (default = 'y')
    step: Manuelle Schrittweite. None bedeutet automatische Schrittweite (defaul: None).
    '''
    if axes == 'y':
        ax.set_ylim(min,max)
        if step:
            ax.set_yticks(np.arange(min, max+step, step))
    elif axes == 'x':
        ax.set_xlim(min,max)
        if step:
            ax.set_xticks(np.arange(min, max+step, step))
    else:
        raise ValueError('Achse nicht korrekt angegeben. Bitte "x" für die x-Achse und "y" für die y-Achse übergeben')

# ======== calcTOP ==========
def calcTOP(Tair, Tsk, E:float=0.94, D:float=0.07):
    '''
    Berechne die operative Raumtemperatur aus der Luft- und der Schwarzkugeltemperatur

    args:
    -----
        Tair:   Raumlufttemperatur  [°C]
        Tsk:    Schwarzkugeltemperatur [°C]
        E:      Emissionsfaktor der Schwarzkugel [-]
        D:      Durchmesser der Schwarzkugel [m]

    returns:
    ----
        Top:    operative Raumtemperatur [°C]
    '''
    if isinstance(Tair, pd.DataFrame):
        Tair = Tair.max(axis=1)
    if isinstance(Tsk, pd.DataFrame):
        Tsk = Tsk.max(axis=1)
        
    ## MRT,sk
    MRT_sk = (( ( (Tsk + 273)**4 ) + ( (0.25*10**8) / E ) * ( abs(Tsk - Tair) / D )**(1/4) * (Tsk - Tair) )**(1/4) - 273)

    ## Top,sk
    return ((MRT_sk + Tair) / 2)

# ======== Kompass ==========
KOMPASS = {'n': 'Nord', 'o':'Ost', 's': 'Süd', 'w': 'West'}

# ======== DIN Formate ==========
def cm(inch):return inch*2.54
def inch(cm):return cm/2.54

din_a4 = (inch(21), inch(29.7))
din_a4_landscape = (inch(29.7), inch(21))

din_a3 = (inch(29.7), inch(2*21))
din_a3_landscape = (inch(2*21), inch(29.7))

# ======== Vorlage BBOX f. Annotationen ==========
eb_bbox = {
            'boxstyle':'square',
            'alpha':0.8,
            "facecolor":"white", 
            'edgecolor':'0.8', 
            "pad":0.4
            }

# ======== Temperaturgradstunden DIN 16789 ==========
def Temperaturgradstunden(Tamb_g24:pd.DataFrame=None, Top:pd.DataFrame=None, Kat:str=None, Ret:str='df'):
    '''
    Berechnet die Über- bzw. Untergradstunden bezogen auf das Komfortband nach DIN EN 16789-1, Anhang 2. 

    Args:
    ----------
        Tambg_24:   Gleitender Mittelwert der Außenlufttemperatur. Übergabe als pd.Series oder pd.DataFrame mit DatetimeIndex.
                    Wenn ein DataFrame übergeben wird, wird für die untere Grenze das Minimum und für die obere Grenze das Maximum je Zeitschritt betrachtet.

        Top:        Operative Raumtemperatur. Übergabe als pd.Series oder pd.DataFrame mit DatetimeIndex
                    Wenn ein DataFrame übergeben wird, wird für die untere Grenze das Minimum und für die obere Grenze das Maximum je Zeitschritt betrachtet.

        Kat:        Kategorie nach DIN EN 16789-1 ['I', 'II' oder 'III] (default = all)

        Ret:        'df' = DataFrame, 'dict' = Dict (default = DataFrame)

    Returns:
    ---
        pd.DataFrame oder dict
    
    '''
    KAT={'I':2,'II':3,'III':4}
    if Kat:
        for kat in Kat:
            if kat in KAT:
                KAT = {kat: KAT[kat]}

    Tamb_g24 = Tamb_g24[Tamb_g24 > 10]

    results = {'UTGS':{}, 'ÜTGS':{}}
    for key, item in KAT.items():

        if isinstance(Tamb_g24, pd.DataFrame):
            TrefLower = (Tamb_g24.min(axis=1)/3) + 18.8 - item - 1
            TrefUpper = (Tamb_g24.max(axis=1)/3) + 18.8 + item
        elif isinstance(Tamb_g24, pd.Series):
            TrefLower = (Tamb_g24/3) + 18.8 - item - 1
            TrefUpper = (Tamb_g24/3) + 18.8 + item
        else:
            raise ValueError('Tamb_g24 muss entweder pd.DataFrame oder pd.Series sein.')
        
        if isinstance(Top, pd.DataFrame):
            TopUpper = Top.max(axis=1)
            TopLower = Top.min(axis=1)
        elif isinstance(Top, pd.Series):
            TopUpper = Top
            TopLower = Top
        else:
            raise ValueError('Top muss entweder pd.DataFrame oder pd.Series sein.')

        deltaT = TopUpper - TrefUpper
        results['ÜTGS'][key] = deltaT[deltaT > 0].sum().round(2)

        deltaT = TopLower - TrefLower
        results['UTGS'][key] = deltaT[deltaT < 0].mul(-1).sum().round(2)
    if Ret == 'dict': 
        return results
    else:
        return pd.DataFrame(results)

def Temperaturgradstunden_1(TAMB:pd.Series, TROOM:pd.Series):
    '''
    Berechne die Über- und Untertemperaturgradstunden nach DIN 15251:2012 - NA

    ARGS:
    ----
        TAMB    Außentemperatur
        TROOM   Raumtemperatur
        
    RETURNS:
    ----
        UTGS, ÜTGS
    '''
    df = pd.DataFrame({'TAMB': TAMB, 'TROOM': TROOM})
    UTGS = 0
    ÜTGS = 0

    UTGS += (20 - df[(df['TAMB'] < 16) & (df['TROOM'] < 20)]['TROOM']).round(1).sum()
    ÜTGS += (df[(df['TAMB'] < 16) & (df['TROOM'] > 24)]['TROOM'] - 24).round(1).sum()

    dummy = df[(df['TAMB'] >= 16) & (df['TAMB'] <= 32) & (df['TROOM'] < 16 + 0.25 * df['TAMB'])]
    UTGS += ((16 + 0.25 * dummy['TAMB']) - dummy['TROOM']).round(1).sum()

    dummy = df[(df['TAMB'] >= 16) & (df['TAMB'] <= 32) & (df['TROOM'] > 20 + 0.25 * df['TAMB'])]
    ÜTGS += (dummy['TROOM'] - (20 + 0.25 * dummy['TAMB'])).round(1).sum()

    UTGS += (24 - df[(df['TAMB'] > 32) & (df['TROOM'] < 24)]['TROOM']).round(1).sum()
    ÜTGS += (df[(df['TAMB'] > 32) & (df['TROOM'] > 28)]['TROOM'] - 28).round(1).sum()

    return UTGS, ÜTGS