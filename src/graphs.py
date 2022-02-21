import pandas as pd
import numpy as np
import math as m
import src.style as style
import src.utilities as ut
import matplotlib.pyplot as plt

################################################ Thermischer Komfort nach DIN 15251 - NA.1 ################################################

def thermal_comfort_1(TAMB, TROOM, ax=None, mode='op',ms=None,legend_ms=None):
    """Erstelle ein Diagramm zur Evaluation des thermischen Komoforts nach DIN 15251 - NA.1

    Keyword arguments:
    :param TAMBG -- Außentemperatur, mittelwert in stündlichen Schritten. Übergabe als pd.Series oder pd.DataFrame.
    :param TROOM -- Raumtemperatur. stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.
    :param ax -- plt.axes instanz zum plotten des graphen
    :param mode -- 'air' für Lufttemperatur, 'op' für operative Temperatur
    """
    df = pd.concat([TAMB,TROOM],axis=1)
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

    comf = ((
        df[(df.TAMB < 16) & (df.TROOM > 20) & (df.TROOM < 24)].shape[0]
        +df[((df.TAMB >= 16) & (df.TAMB <= 32)) & (df.TROOM < 20 + 0.25*df.TAMB) & (df.TROOM > 16 + 0.25*df.TAMB)].shape[0]
        +df[(df.TAMB > 32) & (df.TROOM > 24) & (df.TROOM < 28)].shape[0]
        ) / length_data) * 100

    untertemperaturstunden = (
        df[(df.TAMB < 16) & (df.TROOM < 20)].shape[0] 
        + df[((df.TAMB >= 16) & (df.TAMB <= 32)) & (df.TROOM < 16 + 0.25*df.TAMB)].shape[0]
        +df[(df.TAMB > 32) & (df.TROOM < 24)].shape[0])

    uebertemperaturstunden = (
        df[(df.TAMB < 16) & (df.TROOM > 24)].shape[0] 
        + df[((df.TAMB >= 16) & (df.TAMB <= 32)) & (df.TROOM > 20 + 0.25*df.TAMB)].shape[0]
        +df[(df.TAMB > 32) & (df.TROOM > 28)].shape[0])
    if not ax:
        fig, ax = plt.subplots()
    ax.plot(x, y, c='k',ls = 'dashed', label = 'Komforttemperatur')
    #ax.plot(x, [(t+2,t-2) for t in y], c='k',ls = 'solid')
    ax.fill_between(
        x, 
        [t+2 for t in y], 
        [t-2 for t in y], 
        color="0.8",
        label = 'Komfortbereich')

    ax.annotate(
        r"$\bf{" + str(int(comf)) + str('\%') + "}$" + f' der Messpunkte\nim Komfortbereich',
        xy=(df.TAMB.mean(), df.TROOM.mean()), 
        xycoords='data',
        xytext=(0.4, 0.85), 
        textcoords='axes fraction',
        arrowprops=dict(arrowstyle="->"),
        bbox=style.eb_bbox,
        horizontalalignment='center', 
        verticalalignment='top')

    if uebertemperaturstunden > 0:
        text1 = r"$\bf{" + str('Übertemperaturstunden') + "}$" + f':\n{uebertemperaturstunden}'
        ax.text(
            -13,
            28, 
            text1.strip(),      
            style='normal', 
            ha = 'left', 
            va = 'top',
            #transform=ax.transAxes,
            bbox=style.eb_bbox, 
            )
    if untertemperaturstunden > 0:
        text2 = r"$\bf{" + str('Untertemperaturstunden') + "}$" + f':\n{untertemperaturstunden}'
        ax.text(
            40,
            16, 
            text2.strip(),      
            style='normal', 
            ha = 'right', 
            va = 'bottom',
            #transform=ax.transAxes,
            bbox=style.eb_bbox, 
            )

    ax.plot(
        df['TAMB'], df['TROOM'],
        color=ut.truncate_colormap('Reds_r',0,0.8)(0.1),
        marker = 'o',
        mfc='none',
        linestyle='None',
        ms=ms,
        alpha=0.75,
        label = 'Raumlufttemperatur im Verhältnis zur Außenlufttemperatur'
        )

    ax.set_xlim(-15, 40)
    ax.set_ylim(15, 30)

    ax.set_xlabel('Außenlufttemperatur [°C]')

    if mode == 'op':
        ax.set_ylabel('operative Raumtemperatur\n[°C]')
    if mode == 'air':
        ax.set_ylabel('Raumlufttemperatur\n[°C]')

    ax.set_title('Adaptives Komfortmodell nach DIN EN 15251-1 - NA.1', fontweight = 'bold', loc='left')
    
    ax.legend(
        #loc='lower right',
        loc='upper left',
        markerscale = legend_ms,
        ncol=99,
        #bbox_to_anchor=(1,1.1),
        frameon=False)


################################################ Thermischer Komfort nach DIN EN 16798-1 - Anhang B2.2 ################################################

def thermal_comfort_2(TAMBG24, TROOM, ax, mode='air',ms=None,legend_ms=None):
    """Erstelle ein Diagramm zur Evaluation des thermischen Komoforts nach DIN EN 16798-1 - Anhang B2.2

    Keyword arguments:
    TAMBG24 -- gleitender Mittelwert der Außentemperatur über 24h in stündlichen Schritten. Übergabe als pd.Series oder pd.DataFrame.
    TROOM -- Raumtemperatur. stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.
    ax -- plt.axes instanz zum plotten des graphen
    mode -- 'air' für Lufttemperatur, 'op' für operative Temperatur
    """
    def komfortstunden(df):
        results={}
        KAT={'I':2,'II':3,'III':4}
        df.columns = ['Tamb_g24', 'TROOM']    
        for idx, row in df.iterrows():
            for key in KAT:
                t_op = row.TROOM
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

    df = pd.concat([TAMBG24,TROOM],axis=1)
    df.columns = ['Tamb_g24', 'TROOM']
    df.dropna(inplace=True)

    # Definiere Wertebereich des Graphen.
    df=df[(df.Tamb_g24 >10) & (df.Tamb_g24 < 30)]
    if df.shape[0] == 0:
        ax.text(0.5,0.5, 'Alle Datenpunkte außerhalb des Definitionsbereich:\n' + r'$10°C < T_{amb,g24} < 30°C$',style='normal', 
                ha = 'center', 
                va = 'center',
                transform=ax.transAxes,
                bbox=style.eb_bbox, 
                )
    else:
        linestyle = ['dashdot','dotted','solid']
        KAT={'I':2,'II':3,'III':4}

        for k, key in enumerate(KAT):
            x1 = np.linspace(10,30)
            x2 = np.linspace(10,30)

            y1 = [(t/3)+18.8-KAT[key]-1 for t in x1]
            y2 = [(t/3)+18.8+KAT[key] for t in x2]

            ax.plot(x1, y1, c='k',ls = linestyle[k])
            ax.plot(x2, y2, c='k',ls = linestyle[k])

            ax.annotate(
                f'KAT {key}',
                xy=(min(x1), 
                min(y1)), 
                xycoords='data',
                xytext=(-5, 0), 
                textcoords='offset points',
                horizontalalignment='right', 
                verticalalignment='center'
                )

            ax.annotate(
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

        ax.plot(x, y, c='k',ls = 'dashed', label = 'Komforttemperatur')

        sct = ax.plot(df['Tamb_g24'], df['TROOM'],color = ut.truncate_colormap('Reds_r',0,0.8)(0.1),
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
                item.set_label('operative Raumtemperatur')

        results = komfortstunden(df)
        text2 = r"$\bf{" + str('Untertemperaturstunden') + "}$" + '\n'
        text1 = r"$\bf{" + str('Übertemperaturstunden') + "}$" + '\n'
        for key in results:
            if key == 'upper':
                for kat in results[key]:
                    if results[key][kat] > 0:
                        text1 += 'KAT {}: {}\n'.format(kat, results[key][kat]) 
                ax.text(
                    9,
                    31, 
                    text1.strip(),      
                    style='normal', 
                    ha = 'left', 
                    va = 'top',
                    #transform=ax.transAxes,
                    bbox=style.eb_bbox, 
                    )
            if key == 'lower':
                for kat in results[key]:
                
                    if results[key][kat] > 0:
                        text2 += 'KAT {}: {}\n'.format(kat, results[key][kat]) 
                ax.text(
                    30,
                    17, 
                    text2.strip(),      
                    style='normal', 
                    ha = 'right', 
                    va = 'bottom',
                    #transform=ax.transAxes,
                    bbox=style.eb_bbox, 
                    )
            
        ax.legend(
            #loc='lower right',
            loc='upper left',
            ncol=2,
            markerscale = legend_ms,
            #bbox_to_anchor=(0.025,1,1,0.125),
            #bbox_transform=fig.transFigure,
            frameon=False)
             
    ax.set_xlabel('gleitender Mittelwert der Außenlufttemperatur [°C]')
    ax.set_xlim(8,30)
    if mode=='air':
        ax.set_ylabel('Raumlufttemperatur\n[°C]')
    if mode=='op':
        ax.set_ylabel('operative Raumtemperatur\n[°C]')

    # ax.text(
    #     0.025,
    #     1.15, 
    #     'Adaptives Komfortmodell nach DIN EN 16798-1, B2.2',      
    #     fontweight = 'bold',
    #     fontsize = 8, 
    #     ha = 'left', 
    #     va = 'top',
    #     transform=ax.transAxes,
    #     )
    ax.set_title('Adaptives Komfortmodell nach DIN EN 16798-1 - Anhang B2.2',
       fontweight = 'bold',
       loc='left',
       #pad = 20
       )

    
################################################ HX DIAGRAMM ################################################

def comfort_hx_diagramm(t1, rh1, ax, t2=None,rh2=None, cmap='Blues_r', ms=None,legend_ms=None):
    """Erstelle ein Diagramm zur Evaluation des thermich hygrischen Komoforts nach DIN 1946-6.

    Keyword arguments:
    :param t1 -- Temperatur, Datensatz A, stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.
    :param rh1 -- rel. Luftfeuchte, Datensatz A, stündliche Mittelwerte. Übergabe als pd.Series oder pd.DataFrame.
    ax -- plt.axes instanz zum plotten des graphen
    t2, rh2 -- optional: zweiter Datensatz zum gegenplotten.
    cmap -- Farbschema des plots. Standart ist 'Blues_r'
    minint -- Untergrenze für Farbschema
    maxint -- Obergrenze für Farbschema
    """
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

    new_colors = [ut.truncate_colormap(cmap,0,1)(1. * i/2) for i in range(2)]

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
    
    tx = np.linspace(t_min,t_max,21)
    y1 = [g_abs(t,minrf) for t in tx]
    y2 = [min(g_abs(t,maxrf),maxaf) for t in tx]

    ax.fill_between(
        x = tx,
        y1=y1,
        y2=y2,
        color='0.8',
        label = 'Behaglichkeitsbereich nach DIN 1946-6'
        )

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
            marker = 'o',
            linestyle = 'None',
            ms=ms,
            mfc='none',
            color=new_colors[1],
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
        marker = 'o',
        mfc='none',
        ms=ms,
        linestyle='None',
        color=new_colors[0],
        label = 'Raumluftfeuchte',
        alpha = 0.75
        )

    ax.annotate(
        r"$\bf{" + str(int(per_comf_t1)) + str('\%') + "}$" + ' der Messpunkte\nim Behaglichkeitsbereich',
        xy=(20, min(y2)), 
        xycoords='data',
        xytext=(0.35, 0.6), 
        textcoords='axes fraction',
        arrowprops=dict(arrowstyle="->"),
        bbox=style.eb_bbox,
        horizontalalignment='center', 
        verticalalignment='top')

    ax.set_xlabel(
        'Lufttemperatur [°C]',
        )

    ax.set_ylabel(
        'Absolute Luftfeuchte\n[g/kg]', 
        ) 

    ax.xaxis.set_major_formatter('{x:.0f}')
    ax.yaxis.set_major_formatter('{x:.0f}')

    # ax.text(
    #     0.025,
    #     1.15, 
    #     'H,x - Diagramm',      
    #     fontweight = 'bold',
    #     fontsize = 8, 
    #     ha = 'left', 
    #     va = 'top',
    #     transform=ax.transAxes,
    #     )
    ax.set_title(
        'H,x - Diagramm',
        fontweight = 'bold',
        loc='left',
    )

    ax.legend(
        loc='upper left',
        ncol=2,
        #bbox_to_anchor=(0.025,1,1,0.125),
        markerscale = legend_ms,
        frameon=False)