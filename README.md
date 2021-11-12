# eb-scripts
 Skripte um die Messdaten der Einfach-Bauen Häuser auszuwerten

eb.py
    Dieses Modul enthält generelle Daten und Funktionen die von den anderen Skripten abgerufen werden.

config.py
    Diese Datei enthält sensible Daten zum versand von automatisierten emails, die nicht synchronisiert werden und nur local gespeichert werden.

update_energy_database.py:
    Erstellt eine Datenbanken der Daten der Wärmemängenzähler und updated sie forwährend mit den neuen Datensätzen aus der Dropbox.
    Braucht die Datei 'energymeter.config'
    Es wird ein neuer im Mutterverzeichnis des aktuellen Ordners 'eb-data' erstellt. In diesem wird die Datenbank abgelegt. Alternativ können die Daten direkt auf dem Lehrstuhllaufwerk abgelegt werden.

update_tinkerforge_database.py:
    Fügt neue Datensätze aus der Dropbox zur Datenbank hinzu. Wenn die Datenbank noch nicht vorhanden ist oder nicht gefunden wurde, wird eine neue Datenbank aus dem Archiv erstellt.
    Es wird ein neuer im Mutterverzeichnis des aktuellen Ordners 'eb-data' erstellt. In diesem wird die Datenbank abgelegt. Alternativ können die Daten direkt auf dem Lehrstuhllaufwerk abgelegt werden.

