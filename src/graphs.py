from email.mime import text
import pandas as pd
import numpy as np
import math as m
from src.utilities import eb_bbox, truncate_colormap, Temperaturgradstunden, Temperaturgradstunden_1, INDOC
from src.physics import g_abs, t_for_g
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import operator as op

from geopy import geocoders
from meteostat import Stations, Hourly
from timezonefinder import TimezoneFinder

def getRollingTamb(df, a=0.8):
    return df.resample('D').mean().ewm(alpha=a, min_periods=1, ignore_na=True).mean().reindex(df.index, method='ffill')

def fill_weather_gaps(df, location, dataset):
    '''
    Ersetze Datenlücken durch die Daten der nächsten Wetterstation. 
    ---
    args:
        df  (pd.Series):    
            Messdaten
        location:           
            Messort
        dataset:            
            Name des Datensatz der zum Auffüllen verwerndet werden soll.  
    '''
    loc = geocoders.Nominatim(user_agent="EinfachBauen").geocode(location)
    station = Stations().nearby(loc.latitude, loc.longitude).fetch(1)
    timezone = TimezoneFinder().timezone_at(lng=loc.longitude, lat=loc.latitude)
    start = df.resample('D').mean().index.min().tz_convert('utc').to_pydatetime().replace(tzinfo=None)
    ende = df.resample('D').mean().index.max().tz_convert('utc').to_pydatetime().replace(tzinfo=None)
    refdata = Hourly(station, start, ende).fetch().tz_localize('utc').tz_convert(timezone)
    if dataset in refdata.columns:
        #print(f'{df.isna().mean():.1%}')
        df = df.fillna(refdata[dataset])
        #print(f'{df.isna().mean():.1%}')
        #print(f'Lücken im Datensatz mit dem Daten der DWD Wetterstation in {station.name[0]} aufgefüllt.')
        return df
    else:
        print(f'Dataset [{dataset}] nicht gefunden. Mögliche Werte: {refdata.columns.to_list()}')

################################################ Thermischer Komfort nach DIN EN 16798-1/NA:2021-06 ################################################

def thermal_comfort_1(TAMB, TROOM, ax=None, mode='air',ms=None, legend_ms=5.0, fillna=False, title=True, annotateComf=False):

    """
    Erstelle ein Diagramm zur Evaluation des thermischen Komoforts nach DIN EN 16798-1/NA:2021-06 (ehem. DIN EN 15251:2012 - NA).

    Wenn ax = None: returns fig, ax

    Args:
    ----

    TAMBG --        Außentemperatur, mittelwert in stündlichen Schritten. Übergabe als pd.Series oder pd.DataFrame.
    TROOM --        Raumtemperatur. stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.
    ax --           plt.axes instanz zum plotten des graphen (default = None)
    mode --         'air' für Lufttemperatur, 'op' für operative Temperatur (default = 'air')
    ms =            Markersize im Plot
    legend_ms:      Markerscale in der Legende
    title:          Deaktiviert den Titel im Plot
    annotateComf:   Plottet eine Box mit dem prozentualen Anteil der Messpunkte im Comfortbereich (Beta)

    Returns:
    ----

    fig, ax         
    """
    if fillna:
        df = pd.concat([fill_weather_gaps(TAMB, 'Mietraching', 'temp'),TROOM],axis=1)
    else:
        df = pd.concat([TAMB, TROOM],axis=1)
    df.columns = ['TAMB', 'TROOM']
    df.dropna(inplace=True)
    length_data = df.shape[0]
    x = np.linspace(-30,40)
    y=[]

    for t in x:
        if t < 16:
            y.append(22)
        if 16 <= t <= 32:
            y.append(18 + 0.25*t)
        if t > 32:
            y.append(26)
    try:
        comf = ((
            df[(df.TAMB < 16) & (df.TROOM > 20) & (df.TROOM < 24)].shape[0]
            +df[((df.TAMB >= 16) & (df.TAMB <= 32)) & (df.TROOM < 20 + 0.25*df.TAMB) & (df.TROOM > 16 + 0.25*df.TAMB)].shape[0]
            +df[(df.TAMB > 32) & (df.TROOM > 24) & (df.TROOM < 28)].shape[0]
            ) / length_data) * 100
    except ZeroDivisionError:
        print('No Data to plot...')

    UTGS, ÜTGS = Temperaturgradstunden_1(df['TAMB'], df['TROOM'])

    if not ax:
        fig, ax = plt.subplots(figsize=INDOC)
        ret = True
    else:
        ret = False

    # Erstellung Punktewolke und Legende

    #top_cloud, = 
        ax.plot(
            df['TAMB'], df['TROOM'],
            color=truncate_colormap('Reds_r',0,0.8)(0.1),
            marker = 'o',
            mfc='none',
            linestyle='None',
            ms=ms,
            alpha=0.75,
            label = 'Stündlicher Messwert bei Anwesenheit'
            )

    #comf_line, = 
        ax.plot(
            #0.07,    #0.03^=-13,
            #-0.3,    #0.90^=28,
            x, y, c='k',
            ls = 'dashed', 
            label = 'Komfortbereich nach DIN EN 16798-1/NA:2021-06'
            )
    
        ax.set_xlim(-15, 40),
        ax.set_ylim(16, 32),

        ax.fill_between(
            x, 
            [t+2 for t in y], 
            [t-2 for t in y],
            color="0.8"
            #label = 'Komfortbereich'
            )

        ax.legend( 
            loc='upper left',
            markerscale = legend_ms,
            #columnspacing = 2.0,
            ncol=1,
            #bbox_to_anchor=(-0.02,-0.15),
            #bbox_transform=fig.transFigure,
            frameon=False)
    
    #comf_area = mpatches.Patch(color="0.8")
        #first_legend = ax.legend(handles=[comf_area],bbox_to_anchor=(0.11,0.89),frameon=False)
        #ax.add_artist(first_legend)
        #first_legend = ax.legend(handles=[top_cloud],bbox_to_anchor=(0.60,0.97),frameon=False, markerscale=legend_ms)
        #ax.add_artist(first_legend)
        #second_legend = ax.legend(handles=[comf_line],bbox_to_anchor=(0.22,0.97),frameon=False)
        #ax.add_artist(second_legend)

  
    # Erstellung Bewertungskriterien und Platzierung
    
    if annotateComf:
            ax.annotate(
            r"$\bf{" + str(int(comf)) + str('\%') + "}$" + f' der Messpunkte\nim Komfortbereich',
            xy=(df.TAMB.mean(), df.TROOM.mean()), 
            xycoords='data',
            xytext=(0.85, 0.23), 
            textcoords='axes fraction',
            arrowprops=dict(arrowstyle="->"),
            bbox=eb_bbox,
            horizontalalignment='center', 
            verticalalignment='top')

    if ÜTGS > 0:
            text1 = r"$\bf{" + str('ÜTGS') + "}$" + f'\n{ÜTGS:.1f} Kh'
            ax.text(
                0.03,    #0.03^=-13,
                0.65,    #0.90^=28, 
                text1.strip(),   
                ha = 'left', 
                va = 'top',
                transform=ax.transAxes,
                #bbox=eb_bbox, 
                )
    if UTGS > 0:
            text2 = r"$\bf{" + str('UTGS') + "}$" + f'\n{UTGS:.1f} Kh'
            ax.text(
                0.03,
                0.21, 
                text2.strip(),  
                ha = 'left', 
                va = 'top',
                transform=ax.transAxes,
                #bbox=eb_bbox, 
                )

    # Achsenbeschriftung

    ax.set_xlabel('Außenlufttemperatur [°C]')

    if mode == 'op':
            ax.set_ylabel('operative Raumtemperatur [°C]')
    if mode == 'air':
            ax.set_ylabel('Raumlufttemperatur [°C]')
    '''
    if title:
            ax.set_title('Adaptives Komfortmodell nach DIN EN 16798-1/NA:2021-06', fontweight = 'bold', loc='left')
    '''
    if ret:
        return fig, ax


################################################ Thermischer Komfort nach DIN EN 16798-1:2021-B.2.2 ################################################

def thermal_comfort_2(TAMB:pd.Series, TROOM:pd.Series, ax:plt.Axes = None, fillna=False, mode:str='air', kat:list = ['II'], ms:float=None, legend_ms:float=5.0, title:bool=True):
    """Erstelle ein Diagramm zur Evaluation des thermischen Komoforts nach DIN EN 16798-1:2021-B.2.2

    Args:
    -----

        TAMBG24:    gleitender Mittelwert der Außentemperatur über 24h in stündlichen Schritten. Übergabe als pd.Series oder pd.DataFrame.
    
        TROOM:      Raumtemperatur. stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.
    
        ax:         plt.axes instanz zum plotten des graphen
    
        mode:       'air' für Lufttemperatur, 'op' für operative Temperatur

        kat:        Komfortkategorie nach DIN EN 16798-1 - Anhang B ['I', 'II' oder 'III'] (default = 'II')

        ms:         Größe der Marker im Plot (optional)

        legend_ms:  Skalierungsfaktor der Marker in der Legende (optional)

        title:      Plotte die Überschrift des Graphen (default = True)
    """
    if not ax:
        fig, ax = plt.subplots(figsize=INDOC)
        ret = True
    else:
        ret = False
        
    if fillna:
        TAMB = getRollingTamb(fill_weather_gaps(TAMB, 'Mietraching', 'temp'))
    else:
        TAMB = getRollingTamb(TAMB)

    df = pd.concat([TAMB,TROOM],axis=1)
    df.columns = ['Tamb_g24', 'TROOM']
    df.dropna(inplace=True)

    # Definiere Wertebereich des Graphen.
    df=df[(df.Tamb_g24 >10) & (df.Tamb_g24 < 30)]
    if df.shape[0] == 0:
        ax.text(0.5,0.5, 'Alle Datenpunkte außerhalb des Definitionsbereich:\n' + r'$10°C < T_{amb,g24} < 30°C$',style='normal', 
                ha = 'center', 
                va = 'center',
                transform=ax.transAxes,
                bbox=eb_bbox, 
                )
    else:
        linestyle = {'I':'dashdot','II':'dotted','III':'solid'}
        _KAT={'I':2,'II':3,'III':4}
        KAT = {}
        for ikat in kat:
            KAT[ikat] = _KAT[ikat]

        for k, key in enumerate(KAT):
            x1 = np.linspace(10,30)
            x2 = np.linspace(10,30)

            y1 = [(t/3)+18.8-KAT[key]-1 for t in x1]
            y2 = [(t/3)+18.8+KAT[key] for t in x2]

            ax.plot(x1, y1, c='k',ls = linestyle[key])
            ax.plot(x2, y2, c='k',ls = linestyle[key])

            '''ax.annotate(
                f'KAT {key}',
                xy=(min(x1), 
                min(y1)), 
                xycoords='data',
                xytext=(-0.5, 0.0), 
                textcoords='offset points',
                horizontalalignment='left', 
                verticalalignment='top'
                )

            ax.annotate(
                f'KAT {key}',
                xy=(min(x2), 
                min(y2)), 
                xycoords='data',
                xytext=(-0.5, 0.0), 
                textcoords='offset points',
                horizontalalignment='left', 
                verticalalignment='bottom'
                )'''

        x = np.linspace(10,30)
        y = [(t/3)+18.8 for t in x]

        sct = ax.plot(df['Tamb_g24'], df['TROOM'],color = truncate_colormap('Reds_r',0,0.8)(0.1),
                        marker = 'o',
                        mfc='none', 
                        ms=ms,
                        linestyle='None',
                        alpha=0.75,
                        )
        if mode == 'air':
            for item in sct:
                item.set_label('Raumlufttemperatur')
        if mode == 'op':
            for item in sct:
                item.set_label('Stündlicher Messwert bei Anwesenheit')

        ax.plot(x, y, c='k',ls = 'dashed', label = 'Komfortbereich nach DIN EN 16798-1:2021-B.2.2')

        results = Temperaturgradstunden(df['Tamb_g24'],df['TROOM'],Kat=kat, Ret='dict')
    
        text1 = r"$\bf{" + str('ÜTGS') + "}$" + '\n'
        text2 = r"$\bf{" + str('UTGS') + "}$" + '\n'
        text3 = r" Kh" + '\n'

        for key in results:
            for kat in results[key]:
                if key == 'ÜTGS':
                    if results[key][kat] > 0:
                        text1 += f'KAT {kat}: {results[key][kat]:.1f}' + text3
                        ax.text(
                            0.03,
                            0.75, 
                            text1.strip(),
                            ha = 'left', 
                            va = 'top',
                            transform=ax.transAxes,
                            )
                if key == 'UTGS':
                    if results[key][kat] > 0:
                        text2 += f'KAT {kat}: {results[key][kat]:.1f}' + text3
                        ax.text(
                            0.03,
                            0.13, 
                            text2.strip(),      
                            ha = 'left', 
                            va = 'top',
                            transform=ax.transAxes,
                            )
            
        ax.legend(
            loc='upper left',
            ncol=1,
            markerscale = legend_ms,
            #bbox_to_anchor=(0.025,1,1,0.125),
            #bbox_transform=fig.transFigure,
            frameon=False)
             

    ax.set_xlabel('gleitender Mittelwert der Außenlufttemperatur [°C]')
    ax.set_ylim(16,32)
    ax.set_xlim(6,30)
    if mode=='air':
        ax.set_ylabel('Raumlufttemperatur [°C]')
    if mode=='op':
        ax.set_ylabel('operative Raumtemperatur [°C]')
    '''
    if title:
        ax.set_title('Adaptives Komfortmodell nach DIN EN 16798-1:2021-B.2.2',
        fontweight = 'bold',
        loc='left',
        #pad = 20
        )
    '''
    if ret:
        return fig, ax
    
################################################ HX DIAGRAMM ################################################

def comfort_hx_diagramm(t1, rh1, ax= None, t2=None,rh2=None, cmap='Blues_r', ms=None,legend_ms=5.0, xlim = (-20, 40), ylim = (0, 20)):
    """Erstelle ein Diagramm zur Evaluation des thermisch hygrischen Komoforts nach DIN 1946-6.

    Args:
    ------
        t1: Temperatur, Datensatz A, stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.

        rh1: rel. Luftfeuchte, Datensatz A, stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.

        ax: plt.axes instanz zum plotten des Graphen

        t2 : Zweiter Temperatur Datensatz (optional)

        rh2 : Zweiter rH Datensatz (optional)

        cmap: Farbschema des plots. (default 'Blues_r')
    """
    if not ax: 
        fig, ax = plt.subplots(figsize=INDOC)
        ret = True
    else:
        ret = False
    # absolute Luftfeuchtigkeit in g/kg

    new_colors = [truncate_colormap(cmap,0,1)(1. * i/2) for i in range(2)]

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
    min_x = 0
    min_y = 0
    max_x = 40
    max_y = 20

    # Temp
    min_x = xlim[0]
    max_x = xlim[1]

    # g
    min_y = ylim[0]
    max_y = ylim[1]

    #Achsen Minima und Maxima
    ax.set_xlim(min_x,max_x)
    ax.set_ylim(min_y,max_y)             
 
    # Linien für das HX-Diagramm erstellen
    for item in rh_graph:
        ax.plot(drybulb_graph, [g_abs(t,item) for t in drybulb_graph], 'k-')
        if g_abs(max_x,item) <= max_y:
            if g_abs(max_x,item) > min_y:
                ax.text(max_x, g_abs(max_x,item), '  {}%'.format(int(item)), ha = 'left', va = 'bottom')
        if g_abs(max_x,item) > max_y:
            ax.text(t_for_g(max_y,item),max_y, s='{}%'.format(int(item)), ha = 'left', va = 'bottom', rotation = 45)
    
    tx = np.linspace(t_min,t_max,21)
    y1 = [g_abs(t,minrf) for t in tx]
    y2 = [min(g_abs(t,maxrf),maxaf) for t in tx]

    ax.fill_between(
        x = tx,
        y1=y1,
        y2=y2,
        color='0.8',
        label = 'Komfortbereich nach DIN 1946-6'
        )

    if isinstance(t2,(pd.Series, pd.DataFrame)) and isinstance(rh2, (pd.Series, pd.DataFrame)):
        df = pd.concat([t2, rh2],axis=1)
        df.columns = ['t', 'Rh']
        df.dropna(inplace=True)
        df = df.astype(float, errors='raise')
        if len(df)!=0:            
            df['G_abs'] = df.dropna().apply(lambda x: g_abs(x['t'], x['Rh']), axis = 1)
            n_comf = df[(df.t > t_min) & (df.t < t_max) & (df.Rh < maxrf) & (df.Rh > minrf) & (df.G_abs < maxaf)].shape[0]
            per_comf_t2 = round(n_comf/min(len(t2), len(rh2))*100,0)
            ax.plot(
                df['t'],
                df['G_abs'], 
                marker = 'o',
                linestyle = 'None',
                ms=ms,
                mfc='none',
                color=new_colors[1],
                label = 'Stündl. Messwert der Außenluftfeuchte',
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
        marker = 'o',
        mfc='none',
        ms=ms,
        linestyle='None',
        color=new_colors[0],
        label = 'Stündl. Messwert der Raumluftfeuchte',
        alpha = 0.75
        )

    ax.annotate(
        r"$\bf{" + str(int(per_comf_t1)) + str('\%') + "}$" + ' der Messpunkte\nim Komfortbereich',
        xy=(20, min(y2)), 
        xycoords='data',
        xytext=(0.32, 0.62), 
        textcoords='axes fraction',
        arrowprops=dict(arrowstyle="->"),
        bbox=eb_bbox,
        horizontalalignment='center', 
        verticalalignment='top')

    ax.set_xlabel(
        'Lufttemperatur [°C]',
        )

    ax.set_ylabel(
        'Absolute Luftfeuchte [g/kg]', 
        ) 

    ax.xaxis.set_major_formatter('{x:.0f}')
    ax.yaxis.set_major_formatter('{x:.0f}')
    ax.tick_params(labelleft=True, labelright=False, left=True, right=False)
    '''
    ax.set_title(
        'H,x - Diagramm',
        fontweight = 'bold',
        loc='left',
    )'''

    ax.legend(
        loc='upper left',
        ncol=1,
        #bbox_to_anchor=(0.025,1,1,0.125),
        markerscale = legend_ms,
        frameon=False)
    if ret:
        return fig, ax