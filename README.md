# **Auswertung Einfach Bauen Messdaten**

In diesem Ordner befinden sich die Auswertungen der Messdaten aus dem Projekt Einfach Bauen 3.
## 1. Allgemeines



## 2.1 Energieverbrauch
    Erstellt Übersichtsgrafiken zum Energieverbrauch
        Wärmeenergie:
        - Tatsächlicher Verbrauch
        - Spezifischer Verbrauch
        - Lastkurve
        Stromverbrauch (nach Zählerablesung)
        - spezifisch
        - Hochrechnung auf Beobachtungszeitraum
## 2.2 Raumklima
    Erstllt auswertungen des Raumklimas:
        Messdatenverläufe
        - Täglich (nach Raum)
        - Monatlich (nach Wohneinheit und Raum)
        Thermischer Komofort
        - operativ / Lufttemperatur
        - Monatlich / Jährlich / Gesamt
## 2.3 Wetter
    Erstellt Auswertungen der Wetterstation
## 2.4 Nutzungsprofile
    Erstellt durchschnittliche Nutzungsprofile basierend auf den Bewegungsmeldern und Fensterkontakten.
## 2.5 Simulationsergebnisse
    Wertet die Ergebnisse der Simulation aus EB2 aus. 
    ACHTUNG! Ergebnisse müssen noch aufs Lehrstuhllaufwerk kopiert weren!!
### 2.6 Sensorstatus
    Erstellt Übersichtsgrafiken zur Überprüfung der Sensorfunktionalität
### 2.7 Abweichung trh
    Berechnet den Korrekturfaktor für die Luftfeuchte und die Temperatur.
### 2.8 Sensorliste
    Beinhaltet die Python Vorlage für die Sensorliste. 

## 3. src
### stylesheets
    In diesem Ordner befinden sich die Formatierungsvorlagen für die Graphen.
### config.py
    Diese Datei enthält die Zugangsdaten zum Versand der Status eMails.
### energymeter.config
    Diese Datei enthält die Übersetzungen die Benötigt werden um die MollineSensoren korrekt auszulesen.
### graphs.py
    Diese Datei enthält die Vorlagen für die Komfort-Graphen.

    - thermal_comfort_1()
        Adaptives Comfortmodell nach DIN 15251:2012 NA

    - thermal_comfort_2()
        Adaptives Komfortmodell nach DIN 16789 Anhang B
    - comfort_hx_diagramm()
        HX Diagramm nach DIN 1946-1
### KorrekturFaktoren.csv
    Diese Datei enthält die Korrekturfaktoren für die trh-Sensoren.
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
        
        - import_data(mode, startdate, timestep)
### Sensoruebersicht_template.xlsx
    Vorlage für die Sensorüberischt
### Stromzähler.csv
    Datei zum Eintragen der Stromzählerstände.
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
        - calcTOP()
            Berechne die operative Temperatur aus der Schwarzkugel- und der Lufttemperatur
        - KOMPASS
            Übersetzungen der Kurzfassungen der Himmelsrichtungen
        - DIN Formate
        - eb_bbox
            Vorlage für die Standard-Beschriftungsbox
        - Temperaturgradstunden
            Berechnet die Über- bzw. Untergradstunden nach DIN 16789 Anhang B
        - Temperaturgradstunden_1
            Berechnet die Über bzw. Untergradstunden nach DIN 15251:2012 NA
            