# eb-scripts
 Skripte um die Messdaten der Einfach-Bauen Häuser auszuwerten
-----
outdated ::: NEEDS UPDATE!!!

## eb.py
Dieses Modul enthält generelle Daten und Funktionen die von den anderen Skripten abgerufen werden.

- Nützliche Tools zum plotten von Graphen:
    - truncate_colormaps(): schneidet matplotlib.cmap()-Instanzen in einen bereich von min bis max zu.
    - recolor_lines(): Färbt alle Linien in einem Plot mit einer colormap ein. Die Colormaps können durch die parameter minint und maxint zurecht geschnitten werden.
    - get_labels(): Verschönert die label in der Legende bei der Verwendung von Multi-Index Spalten
    - send_email(): Sended eine Email.
    - ticks_to_hours(ax): Diese Funktion rechnet die y-label eines Graphen von Minuten in Stunden um.
    - export(): exportiert Figures in einer Reihe gewünschter Dateiformate (extlist) in einen bestimmten Ordner.
    - diverese Gleichungen zur Berechnung von Wasserdampf und Luftfeuchtigkeitsbeziehungen: (psat(t),roh(t), x_to_g(g,t),g_abs(rh,t),RH(g,t))

- Funktionen um die Datensätze aus den Datenbanken zu laden:
    - load_bui(path): Öffnet die Datensätze der Tinkerforge-Sensoren der drei Häuser und lädt sie in einen Pandas DataFrame. 
        - Known Issues:
            - Fenster sind teilweise doppelt, da sich die Header Bezeichnung geändert hat.
            - ...
    - load_pm(path): Öffnet die Daten der Pyranometer und lädt sie in einen Pandas DataFrame.
    - load_amb(path): Öffnet die Daten der Wetterstation und lädt sie in einen Pandas DataFrame.

- Vorlagen zur erstellung von spezifischen Graphen:
    - hx_diagram(t1,rh1,ax, (t2,rh2,cmap,minint,maxint,fontsite)): plottet ein HX-Diagramm in eine vorher zu definierende plt.axes Instanz.
        - das plotten eines zweiten Datensatzes (z.B. Außenluft) ist optional.
        - zu verwendende colormap kann über die aus truncate_colormap bekannten parameter variiert werden.
    - thermal_comfort_2(TAMBG24, TOP, ax, fontsize): plottet das Komfortband nach DIN EN 16798-1 ein eine plt.axes Instanz.

- User Inputs:
    - Datenpfade zu den localen Ordnern:
        - Das Programm erstellt die Datenbänke und Ergebnisse standardmäßig in einem neuen Ordner 'eb-data' im übergeordneten Verzeichnis des aktuellen skripts. 
        - Die Pfade zu den Speicherorten auf dem Lehrstuhlaufwerk sind für Windowsbetriebssysteme hinterlegt.
        - MacOS und Linux Systeme müssen den entsprechenden Ordner erst als Netzlaufwerk mounten. Das Programm erledigt das für den Nutzer über die Funktion mount_ls(mountpoint). Über die Funktion unmount_ls(mountpoint) wird die Verbindung wieder getrennt.
    - config_file: locale Datei in der die Zugangsdaten zum versenden von eMails abgespeichert werden. Diese Datei wird nicht synchronisiert und muss vom Nutzer manuell angelegt werden. Eine Vorlage wird automatisch erstellt.
    - diverse nutzliche dictionarys um die Sensorbezeichnungen lesbarer zu machen.
    - files: erzeugt ein dictionary mit allen Pfaden zu den erstellten Datenbanken. Die Pfade sind wie folgt abrufbar:
        files['tf' oder 'em']['MH' od. 'MW' od. 'LB' od. 'WD' od. 'PM']['raw' od. '1min' od. '15min' od. '60min']

- Style Guide:
    - gibt ein paar Vorgaben, damit die Graphen einheitlicher aussehen. tbc....



## config.py
Diese Datei enthält sensible Daten zum versand von automatisierten emails, die nicht synchronisiert werden und nur local gespeichert werden.

## update_energy_database.py:
- Erstellt eine Datenbanken der Daten der Wärmemängenzähler und updated sie forwährend mit den neuen Datensätzen aus der Dropbox.
- Braucht die Datei 'energymeter.config'
- Es wird ein neuer im Mutterverzeichnis des aktuellen Ordners 'eb-data' erstellt. In diesem wird die Datenbank abgelegt. Alternativ können die Daten direkt auf dem Lehrstuhllaufwerk abgelegt werden.

## update_tinkerforge_database.py:
- Fügt neue Datensätze aus der Dropbox zur Datenbank hinzu. Wenn die Datenbank noch nicht vorhanden ist oder nicht gefunden wurde, wird eine neue Datenbank aus dem Archiv erstellt.

- Es wird ein neuer im Mutterverzeichnis des aktuellen Ordners 'eb-data' erstellt. In diesem wird die Datenbank abgelegt. Alternativ können die Daten direkt auf dem Lehrstuhllaufwerk abgelegt werden.

