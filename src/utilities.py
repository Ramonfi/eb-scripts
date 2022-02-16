import smtplib, ssl
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
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