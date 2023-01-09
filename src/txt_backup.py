from datetime import datetime
from pathlib import Path
from src.appSetting import appSettings
## Bernecker Thomas
# Class zum erstellen deiner backupdatei
#

class txt_backup():
    appSettings = appSettings()
    ## Kontruktor
    def __init__(self):
        self.ifExist()
        self.appSettings = appSettings()
        self.appSettings.loadSettings()
    # funktion zum testen ob die datei vorhanden ist
    def ifExist(self):
        fileName = self.appSettings.settingList["txtSettings"]["Pfad"] +"\\"+ self.appSettings.settingList["txtSettings"]["NameDerTxTDatei"]+self.appSettings.settingList["txtSettings"]["DateiEndung"]
        fileObj = Path(fileName)
        if fileObj.is_file() == False:
            print("Keine Backup-Datei im verzeichniss gefunden...")
            print("erstelle.....")
            self.creating()
    # funktion zum zeilen hinzufügen
    def adding(self, Liste):
        with open(f'{self.appSettings.settingList["txtSettings"]["Pfad"]}\\{self.appSettings.settingList["txtSettings"]["NameDerTxTDatei"]}{self.appSettings.settingList["txtSettings"]["DateiEndung"]}', 'a') as f:
            f.write("\n")
            for element in Liste:
                f.write( element + '\t' )
        f.close()

    # funktion zum erstellen der backupdatei
    def creating(self):
        self.appSettings.loadSettings()
        print(f'{self.appSettings.settingList["txtSettings"]["Pfad"]}\\{self.appSettings.settingList["txtSettings"]["NameDerTxTDatei"]}{self.appSettings.settingList["txtSettings"]["DateiEndung"]}')
        with open(f'{self.appSettings.settingList["txtSettings"]["Pfad"]}\\{self.appSettings.settingList["txtSettings"]["NameDerTxTDatei"]}{self.appSettings.settingList["txtSettings"]["DateiEndung"]}', 'w') as f:
            f.write("Automatisch erzeugte Backupdatei\n")
            f.write("Generiert am :\n")
            f.write(datetime.today().strftime('%d.%m.%Y\n'))
            f.write('*'*20+"\n")
            f.write("Index\t\t\tDatum\t\t\tName\t\t\tSN\t\t\tModell\t\t\tBetriebsystem\t\t\tHinweis")
            f.close()