# **Einfach Bauen Messdaten**
# **Handbuch**

In diesem Ordner befinden sich die Auswertungen der Messdaten aus dem Projekt Einfach Bauen 3.
## 1. Allgemeines

### **Schritte zur Vorbereitung**
1. VS Code Installation (s. Mail: anaconda3, virtual environment, vs code)
2. EB-SCRIPTS Ordner über GitHub lokal auf die Festplatte klonen

    2.1 Ggf. config.py anpassen (Zugangsdaten google mail)

    2.2 Ggf. Speicherort für Datenbank und Results anpassen (standardmäßig beides auf LS-Laufwerk)

### **GitHub**

### **Datenbankmanagment**
Datenbank mit den neuen Daten aus der Drop-Box zu aktualisieren: 

    Funktion up() aus src.update_databases in Anwendung-script importieren und ausführen
    -> neue Datenbank wird aktualisiert

Für komplett neue Datenbank: 

    (a) alten Datenbank-Ordner löschen und Funktion up() ausführen
    (b) Funktion tinkerforge_update aus src.update_databases importieren und anpassen: tinkerforge_update(OverwriteDatabase='all')

### **Speicherort der Datenbank ändern**
Definiert als 'dir' in project_definitions.py. Möglichkeit a) lokale Kopie im Projektverzeichnis 'eb-scripts', b) Datenbank+Results auf dem Lehrstuhllaufwerk.


### **Arbeiten mit der Datenbank**
1. Import der Datenbank mit 

        from src.sensor_reader import import_data

        IND, AMB, EM = import_data()
    
    default: Import in minütlichen Zeitschritt mit Startzeitpunkt 01.06.2021. Um einen anderen Zeitschritt ('15min', '60min') zu importieren, schreibe

        IND, AMB, EM = import_data(timestep = '15min')

    Der Startzeitpunkt lässt sich deaktivieren: (None bedeutet ALLE Daten)

        IND, AMB, EM = import_data(timestep = '15min', startdate = None)

    oder z.B.

        IND, AMB, EM = import_data(timestep = '15min', startdate = '2021-05-01')


    IND = TinkerForge (Indoor)
    AMB = Wetterstation + Pyranometer
    EM = Molline Wärmemengen + Wasserzähler

        # Nur Tinkerforge Daten importieren:
        IND = import_data(mode='IND')

        # nur Wetterdaten Importieren:
        AMB = import_data(mode='AMB')

        ....

3. Filtern der Daten:

    2.1 TinkerForge (IND):
    
    Die Tinkerforge Datensätze haben eine 4-fache Spaltenhirachie in der Reihenfolge [<BAUWEISE>][<WOHNUNG>][<RAUM>][<SENSOR>]

    Ein einzelner Sensor kann, wenn der Name bekannt ist gezielt aufgerufen werden:

    Beispiel:

        IND['MH']['S']['WZ']['n_trh_Tair (°C)']

    Wenn die genaue Sensorbezeichnung unbekannt ist, hilft die Funktion .filter()

    Beispiel:

        IND['MH']['S']['WZ'].filter(like='trh_Tair')

    Will man z.B. alle trh Sensoren einer Wohnung aufrufen, so schreibt man:

        IND['MH']['S'].filter(like='trh_Tair')

    Zum Aufrufen der Stromzähler:

        IND['MH']['S']['']
        
    Um den Zeitraum der Ergebnisse einzuschrenken, wird die Funktion .loc[] verwendet.

    Filtern nach einem bestimmten Jahr, Monat oder Tag:

    Jahr:

        IND['MH']['S'].filter(like='trh_Tair').loc['2021']


    Monat:

        IND['MH']['S'].filter(like='trh_Tair').loc['2021-10']

    Tag:

        IND['MH']['S'].filter(like='trh_Tair').loc['2021-10-10']

    Filtern nach einem beliebigen Zeitraum. Syntax: .loc[startzeitpunkt:endzeitpunkt]

    Beispiel:

        IND['MH']['S'].filter(like='trh_Tair').loc['2021-10-10':'2021-11-01']


    2.2 Wetterstation + Pyranometer (AMB):
    
    Indexing wie bei IND, nur dass es nur ein Spaltenlevel gibt.

        AMB[<Sensorbezeichnung>]

        oder 

        AMB.filter(like='T_amb')

2. Korrektur der trh-Sensoren

        from src.project_definitions import KORREKTUR_RH, KORREKTUR_T

    Die Korrekturfaktoren werden fortlaufend durch ausführen des Skripts '7_Abweichung_trh.ipynb' bestimmt. KORREKTUR_RH und KORREKTUR_T sind Dicts: Für jede Bauweise ist ein Wert hinterlegt. Dieser muss anhand der 'bui' aufgerufen werden und dann vom Messwert substrahiert werden. 

    Beispiel:

        IND['MH']['S'].loc['2021-12-5 12:00':'2021-12-8 18:00'].filter(like='trh_RH') - KORREKTUR_RH['MH']



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
    Sie wird nicht mit Github synchronisiert und muss nach dem erneuten Klonen der Repository manuell angepasst oder kopiert werden.
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
            z.B.:   - DIN['A4'] für DIN A4 Hochformat
                    - DIN['A4L'] für DIN A4 Querformat
        - INDOC
            Größe für einbettung in Word-Dokument (16 x 12 cm²)
        - eb_bbox
            Vorlage für die Standard-Beschriftungsbox
        - Temperaturgradstunden
            Berechnet die Über- bzw. Untergradstunden nach DIN 16789 Anhang B
        - Temperaturgradstunden_1
            Berechnet die Über bzw. Untergradstunden nach DIN 15251:2012 NA
            