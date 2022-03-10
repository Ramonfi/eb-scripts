# **Auswertung Einfach Bauen Messdaten**

In diesem Ordner befinden sich die Auswertungen der Messdaten aus dem Projekt Einfach Bauen 3.
## 1. Allgemeines



## 2.1  Energieverbrauch
## 2.2  Raumklima
## 2.3  Nutzungsprofile
## 2.4  Sonstiges
### 2.4.1   Sensorstatus
### 2.4.2   Abweichung trh
### 2.4.3   Sensorliste
### 2.5 Simulationsergebnisse

## 3. src
### stylesheets
    In diesem Ordner befinden sich die Formatierungsvorlagen für die Graphen.
### config.py
    Diese Datei enthält die Zugangsdaten zum Versand der Status eMails.
### energymeter.config
    Diese Datei enthält die Übersetzungen die Benötigt werden um die MollineSensoren korrekt auszulesen.
### graphs.py
    Diese Datei enthält die Vorlagen für die Komfort-Graphen.
### physics.py
    Diese Datei enthält einige nütztliche physikalische Funktionen.
### profect_definitions.py
    Diese Datei enthält einige allgemeine Informationen zum Projekt wie:
        - Übersetzungen zwischen Abkürzungen (Bauweisen, Wohnungsbezeichnungen, Sensoren, etc.)
        - Dateipfade zu den neuen Datensätzen sowie zum Datenbank-Speicherort
        - Grundflächen
### sensor_reader.py
    Diese Datei enthält die Funktionen zum einlesen der Datenbanken in ein Skript.
        - TinkerForge: load_tf_bui()
        - Pyranometer: load_tf_pm()
        - Wetter: load_tf_weather()
        - Molline: load_energy_data()
### style.py
    Diese Datei entählt einige zusätzliche Formatierungen wie z.B.:
        - Formate (din_a4, etc.)
        - ...
### update_databases.py
    Diese Datei erstellt die Datenbanken aus den einzelnen Datensheets aus Bad Aibling. Wenn diese Datei in ein anderes Sript importiert wird, wird überprüft, ob es heute schon ein Update gab und wenn nicht, ein Datenbank-Update durchgeführt. Achtung! Das kann einige Zeit in Anspruch nehmen, wenn man nicht im Uni-Netzwerk ist.
### utilities.py
    In dieser Datei sind einige weitere nützliche Funktionen.
        - truncate_colormaps()
            Schneide mpl.colormaps in eine gewünschte range.
        - recolor_lines()
            Färbe alle Line-Graphs einer AX mit den Farben einer gewünschen Colormap um.
        - tick_to_hours()
            Diese Funktion rechnet die y-label eines Graphen von Minuten in Stunden um.
        - get_labels():
            extrahiert die Spaltennamen aus einem MultiIndex (nützlich wenn man pd.plot() in verbindung mit einem Multiindex verwendet)
        - export()
            Speichert einen Graphen in einer gewünschten Anzahl an Dateiformaten ab.
        - running_bar()
            plottet eine Fortschritsanzeige in das Terminal
        - send_email()
            versendet eine eMail. 
        - set_ticks()
            Stellt die Achsenskalierung nach Wunsch ein.