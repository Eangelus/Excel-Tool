import json
import os.path

#klass für stettings die in einer json geladen wird und gespeichtert

class appSettings():

    def __init__(self):
        self.loadSettings()
        #20.12



        self.settingListDefault = {"txtSettings":{"Pfad": "C:\\LegacyApp\\Dell_Hardware_Rollout\\Backup",
                                     "NameDerTxTDatei" : "Dell Rollout Backup Ausgabe",
                                    "DateiEndung": ".txt",
                                                  },
                                                        "ExcelSettings": {  "Log_Erzeugen": True,
                                                                        "AutomatischesEintragenIn2Excel" : True,
                                                                        "Sheet2SpalteBereichsAuswahl" : "E",
                                                                          "BereichIm2SheetA": 2,
                                                                          "BereichIm2SheetE" : 12,
                                                                          "PrüfSpalteFürSN" : "Y",
                                                                          "DropDownMenue1" : "H",
                                                                          "DropDownMenue2" : "W",
                                                                          "DropdownMenuAuswahl1": "Win10",
                                                                        "DropdownMenuAuswahl2":"Win11",
                                                                        "Später" : "Q",
                                                                        "Q1" : "P",
                                                                         "Q4": "O",
                                                                        "Überschrift": "Excel Tool",
                                                                          "TextFürLabelÄndernIn" : "Bestelltes Modell ggf. ändern in:",
                                                                          "UnterOrdnerErstellung": "C:\\LegacyApp\\Dell_Hardware_Rollout\\Backup\\",
                                                                          "DateiEndung" : ".xlsx",
                                                                          "LadeLieferueberSicht":"I:\\cs_ls_projekt\\Dell_Hardwarerollout\\Dell Rollout Lieferübersicht.xlsx",
                                                                          "SpeicherOrt": "I:\\cs_ls_projekt\\Dell_Hardwarerollout\\",
                                                                          "ExportName" :  "Dell Rollout Ausgabe Datei",
                                                                          "ExportOrt" : "I:\\cs_ls_projekt\\Dell_Hardwarerollout",
                                                                          "SpeicherName" : "Dell Rollout Ausgabe",
                                                                          "BackupOrt" : "C:\\LegacyApp\\Dell_Hardware_Rollout\\Backup",
                                                                          "BackupName": "Dell Rollout Ausgabe Backup",
                                                                          "BackupNameLiefer": "Dell Rollout Lieferübersicht Backup",
                                                                          "LadeOrt": "C:\\LegacyApp\\Dell_Hardware_Rollout\\Backup",
                                                                          "LadeName": "Dell Rollout Backup Ausgabe",
                                                                          "ImportVerzeichnis": "I:\\cs_ls_projekt\\Dell_Hardwarerollout",
                                                                          "ImportName": "Dell Rollout Ausgabe Datei",
                                                                          "SpalteKostenstelle": "J",
                                                                          "SpalteHinweis": "AB",
                                                                          "SpalteAlterHinweis": "S",
                                                                          "Worksheet_2": "Pivot Q4-22",
                                                                          "SpalteName": "H",
                                                                          "SpalteHost": "I",
                                                                          "SpalteUID": "W",
                                                                          "SpalteModell": "E",
                                                                          "SpalteEntwickler": "K",
                                                                          "Betriebssystem": "AA",
                                                                          "SpalteSN": "Y",
                                                                          "SpalteNotiz": "AB",
                                                                          "SpalteAusModell": "AC",
                                                                          "SpalteDatum": "Z",
                                                                          "BestelteModell": "",
                                                                          "BestelltesWin": "",
                                                                          "BestelltesModellSpalte": "M",
                                                                          "BestellesWinSpalte": ""},
                                   "Excel2Einstellungen":{"PrüfSpalte": "A",  "Eintrag1" : "B", "Eintrag2": "L", "Eintrag3": "J", "Eintrag4" : "G","Eintrag5" :"I", "Eintrag6": "K", "Eintrag7": "D","Eintrag8":"M" }}


        self.settingList =  {"txtSettings": {"Pfad": "",
                         "NameDerTxTDatei": "",
                         "DateiEndung": ".txt"},

         "ExcelSettings": {                                       "Log_Erzeugen": None,
                                                                  "AutomatischesEintragenIn2Excel" : None,
                                        "Sheet2SpalteBereichsAuswahl" : "",
                                                                          "BereichIm2SheetA": 2,
                                                                          "BereichIm2SheetE" : 12,
             "PrüfSpalteFürSN" : "",
                                                                        "DropDownMenue1" : "",
                                                                          "DropDownMenue2" : "","DropdownMenuAuswahl1": "",
                                                                        "DropdownMenuAuswahl2":"",
                                                                        "Später" : "",
                                                                        "Q1" : "",
                                                                         "Q4": "",
                                                                        "Überschrift": "",
                                                                          "TextFürLabelÄndernIn" : "",
                                                                          "UnterOrdnerErstellung": "",
                                                                          "DateiEndung" : ".xlsx",
                                                                          "LadeLieferueberSicht":"",
                                                                          "SpeicherOrt": "",
                                                                          "ExportName" :  "",
                                                                          "ExportOrt" : "",
                                                                          "SpeicherName" : "",
                                                                          "BackupOrt" : "",
                                                                          "BackupName": "",
                                                                          "BackupNameLiefer": "",
                                                                          "LadeOrt": "",
                                                                          "LadeName": "",
                                                                          "ImportVerzeichnis": "",
                                                                          "ImportName": "",
                                                                          "SpalteKostenstelle": "",
                                                                          "SpalteHinweis": "",
                                                                          "SpalteAlterHinweis": "",
                                                                          "Worksheet_2": "",
                                                                          "SpalteName": "",
                                                                          "SpalteHost": "",
                                                                          "SpalteUID": "",
                                                                          "SpalteModell": "",
                                                                          "SpalteEntwickler": "",
                                                                          "Betriebssystem": "",
                                                                          "SpalteSN": "",
                                                                          "SpalteNotiz": "",
                                                                          "SpalteAusModell": "",
                                                                          "SpalteDatum": "",
                                                                          "BestelteModell": "",
                                                                          "BestelltesWin": "",
                                                                          "BestelltesModellSpalte": "",
                                                                          "BestellesWinSpalte": ""}}

    # settings werden gespeichert ( settings gui eingaben )
    def saveSettings(self):
        filename = "settings.json"
        with open(filename, 'w') as f:
            settings = json.dump(self.settingList, f)


    # defaultsettings werden beim erstellen der datei geladen
    def saveDefaultSettings(self):
        filename = "settings.json"
        with open(filename, 'w') as f:
            json.dump(self.settingListDefault, f)


    # f. zum laden der settings
    def loadSettings(self):
        filename = "settings.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.settingList = json.load(f)

                #self.settingListTxtExport = json.load(f)
    # f. zum speicher der stettings fals nicht vorhanden
    def inputSettings(self):
        print( "-- Settings können später verändert werden --")
        self.settingListDefault["ImportVerzeichnis"] = "I:\\cs_ls_projekt\\Dell_Hardwarerollout\\"
        self.settingListDefault["ImportName"] = "Dell Rollout Ausgabe Datei"
        self.settingListDefault["LadeLieferueberSicht"] = "I:\\cs_ls_projekt\\Dell_Hardwarerollout\\Dell Rollout Lieferübersicht.xlsx"
