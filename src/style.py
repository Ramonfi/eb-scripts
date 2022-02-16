import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import src.utilities as ut 

# ======== Standard parameters ==========
def set_rc_eb_standard(spines=False):
    #New fontsizes
    SMALL_SIZE = 9
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12

    plt.rc("figure", figsize=(10,6))
    plt.rc("figure", titlesize=BIGGER_SIZE)
    plt.rc("figure", titleweight='bold')

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('font', family='Arial')

    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', titleweight = 'bold')
    plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
    plt.rc('axes.spines', left=spines)
    plt.rc('axes.spines', right=spines)
    plt.rc('axes.spines', top=spines)
    plt.rc('axes.spines', bottom=spines)

    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels

    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('legend', frameon=True)
    plt.rc('legend', loc = 'best')

    plt.rc('lines', linewidth = 0.5)
    plt.rc('lines', markersize = .8)


# ======== Standard BBOX ==========
bbox = {
            'boxstyle':'square',
            'alpha':0.8,
            "facecolor":"white", 
            'edgecolor':'0.8', 
            "pad":0.4
            }

eb_bbox = {
            'boxstyle':'square',
            'alpha':0.8,
            "facecolor":"white", 
            'edgecolor':'0.8', 
            "pad":0.4
            }

# ======== Standard BBOX ==========

def cm(inch):return inch*2.54
def inch(cm):return cm/2.54

# figsize(float, float), default: rcParams["figure.figsize"] (default: [6.4, 4.8])
# Width, height in inches.

din_a4 = (inch(21), inch(29.7))
din_a4_landscape = (inch(29.7), inch(21))

in_doc = (10,6)

din_a3 = (inch(29.7), inch(2*21))
din_a3_landscape = (inch(2*21), inch(29.7))

### Colors:
c_temp = ut.truncate_colormap('Reds_r' ,minval=0 ,maxval=0.8)
c_hum = ut.truncate_colormap('Blues_r',minval=0.2,maxval=0.8)
c_co2 = ut.truncate_colormap('Greens_r', minval=0,maxval=0.8)