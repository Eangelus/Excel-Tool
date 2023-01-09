#Bernecker Thomas
# Programm für Excel zur Anzeige  und zu einscannen von infos
# 15.11.2022
import os.path
import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor

import src.appSetting
from gui.main_frm import Ui_frm_main
from gui.settings_frm import Ui_Settings_frm
from src.excel_convert import excelImport
from src.appSetting import appSettings
from src.txt_backup import txt_backup
from src.snExport import snExport

# inizalisieren der objekte
#TODO Lade oder Speicher optionen durch ein Dialogfenster ersetzen!
# TODO Settingfester erweiter..



class setings_window(QMainWindow, Ui_Settings_frm):
    # normaler konstruktor
    def __init__(self):
        super().__init__()
        self.appSetings = appSettings()
        self.setupUi(self)
        #self.btn_setting_ok.pressed.connect(self.saveSettings)
        self.appSetings.loadSettings()
        self.lb_activ_wb2_import.setText(self.appSetings.settingList["ExcelSettings"]["LadeLieferueberSicht"])
        self.lb_activ_log_name.setText(
        self.appSetings.settingList["txtSettings"]["Pfad"] + "/" + self.appSetings.settingList["txtSettings"][
                "NameDerTxTDatei"])
        self.lb_activ_wb2_save_2.setText(self.appSetings.settingList["ExcelSettings"]["BackupOrt"] + "/" +
                                         self.appSetings.settingList["ExcelSettings"]["BackupNameLiefer"])

        self.lb_activ_Name.setText(self.appSetings.settingList["ExcelSettings"]["SpalteName"])
        self.lb_activ_Kostenstelle.setText(self.appSetings.settingList["ExcelSettings"]["SpalteKostenstelle"])
        self.lb_activ_UID.setText(self.appSetings.settingList["ExcelSettings"]["SpalteUID"])

        self.lb_activ_Entwickler.setText(self.appSetings.settingList["ExcelSettings"]["SpalteEntwickler"])

        self.lb_activ_Notiz.setText(self.appSetings.settingList["ExcelSettings"]["SpalteNotiz"])

        self.lb_load_pfad.setText(self.appSetings.settingList["ExcelSettings"]["LadeOrt"]+
                                                  self.appSetings.settingList["ExcelSettings"]["SpeicherName"])

        self.lb_activ_Alter_Hinweis.setText(self.appSetings.settingList["ExcelSettings"]["SpalteAlterHinweis"])
        self.lb_aktiver_speicherOrt_Name.setText((self.appSetings.settingList["ExcelSettings"]["SpeicherOrt"]+
                                                  self.appSetings.settingList["ExcelSettings"]["SpeicherName"]))
        self.lb_aktiv_Qartale.setText(self.appSetings.settingList["ExcelSettings"]["Später"]+ ", "+
                                      self.appSetings.settingList["ExcelSettings"]["Q1"] + ", "+
                                      self.appSetings.settingList["ExcelSettings"]["Q4"])
        self.lb_activ_DD_auswahl1.setText(self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl1"])
        self.lb_activ_DD_auswahl2.setText(self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl2"])
        self.lb_dmEA_save_in.setText(self.appSetings.settingList["ExcelSettings"]["Betriebssystem"])
        self.lb_activ_2Sheet.setText(self.appSetings.settingList["ExcelSettings"]["Worksheet_2"])
        self.lb_activ_2SBereichAuswahl.setText(self.appSetings.settingList["ExcelSettings"]["Sheet2SpalteBereichsAuswahl"])
        self.lb_aktiv_Sheet2SpalteBereichsAuswahl.setText(self.appSetings.settingList["ExcelSettings"]["Sheet2SpalteBereichsAuswahl"] + " von "+
                                                         str(self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetA"]) + " bis "+
                                                         str(self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetE"]))
        self.lb_aktiv_aus_db_save_in.setText(self.appSetings.settingList["ExcelSettings"]["SpalteAusModell"])

        self.lb_activ_backupV.setText(self.appSetings.settingList["ExcelSettings"]["BackupOrt"])

        ###############  -------- seite 2 in settings -------  #############
        ####
        ##
        self.lb_wb2_active_suchSpalte.setText(self.appSetings.settingList["Excel2Einstellungen"]["PrüfSpalte"])
        self.lb_wb2_activ_datum.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag7"])
        self.lb_wb2_activ_name.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag4"])
        self.lb_wb2_activ_uid.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag5"])
        self.lb_wb2_activ_Eintrag4.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag2"])
        self.lb_wb2_activ_Eintrag5.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag3"])
        self.lb_wb2_activ_Eintrag6.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag6"])
        self.lb_wb2_activ_Eintrag7.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag7"])
        self.lb_wb2_activ_Eintrag8.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag8"])
        self.btn_importOpen.clicked.connect(self.open_import)
        self.btn_importSave.clicked.connect(self.save_import)
        self.btn_wb2_open.clicked.connect(self.open_wb2)
        self.btn_wb2_save.clicked.connect(self.save_wb2)

        self.btn_log_save.clicked.connect(self.save_log)
        self.btn_backup_open.clicked.connect(self.pic_BackupV)
        self.buttonBox.accepted.connect(self.saveSettings)
        self.buttonBox_2.accepted.connect(self.saveSettings)
        self.buttonBox_3.accepted.connect(self.saveSettings)
        self.buttonBox_4.accepted.connect(self.saveSettings)

        self.buttonBox.rejected.connect(self.close)
        self.buttonBox_2.rejected.connect(self.close)
        self.buttonBox_3.rejected.connect(self.close)
        self.buttonBox_4.rejected.connect(self.close)


        #self.lb_activ_BeSys.setText(self.appSetings.settingList["ExcelSettings"]["Betriebssystem"])
        #self.lb_name_datei_load.setText('Dell Rollout Backup Ausgabe.xlsx')
        #self.lb_activ_Datum.setText(self.appSetings.settingList["ExcelSettings"]["SpalteDatum"])
        #self.lb_activ_BeModell.setText(self.appSetings.settingList["ExcelSettings"]["BestelltesModellSpalte"])
        #self.lb_.setText(self.appSetings.settingList["ExcelSettings"]["SpalteModell"])
        #self.lb_activ_SN.setText(self.appSetings.settingList["ExcelSettings"]["SpalteSN"])
    def kombiPfad(self, list):
        pfad = ""
        i = 0
        print("liste erhalten")
        print(list)
        while i <= len(list)-2:
            if i == 0:
                pfad = list[0]
                i = 1
            pfad = pfad + "/" + list[i]
            i = i +1
        print(pfad)
        return pfad


    def pic_BackupV(self):
        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            self.appSetings.settingList["ExcelSettings"]["BackupOrt"] = filename[0]
            self.lb_activ_wb2_import.setText(filename[0])
        else:
            pass

    def open_import(self):

        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            filename = filename[0].split("/")

            self.appSetings.settingList["ExcelSettings"]["ImportVerzeichnis"] = self.kombiPfad(filename)
            self.appSetings.settingList["ExcelSettings"]["ImportName"] = filename[-1]
        else:
            pass

    def save_import(self):
        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            filename = filename[0].split("/")

            self.appSetings.settingList["ExcelSettings"]["ExportOrt"] = self.kombiPfad(filename)
            self.appSetings.settingList["ExcelSettings"]["ExportName"] = filename[-1]
        else:
            pass

    def open_wb2(self):
        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            self.appSetings.settingList["ExcelSettings"]["LadeLieferueberSicht"] = filename[0]
            self.lb_activ_wb2_import.setText(filename[0])
        else:
            pass
    def save_wb2(self):
        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            filename = filename[0].split("/")

            self.appSetings.settingList["ExcelSettings"]["BackupOrt"] = self.kombiPfad(filename)
            self.appSetings.settingList["ExcelSettings"]["BackupNameLiefer"] = filename[-1]
            self.lb_activ_wb2_save_2.setText(self.appSetings.settingList["ExcelSettings"]["BackupOrt"]+"/"+self.appSetings.settingList["ExcelSettings"]["BackupNameLiefer"])
        else:
            pass
    def open_log(self):

        filename = QFileDialog.getOpenFileName()
        if len(filename) > 0:
            self.appSetings.settingList["ExcelSettings"]["UnterOrdnerErstellung"] = filename[0]
            self.lb_activ_backupV.setText(filename[0])
        else:
            pass

    def save_log(self):
        filename = QFileDialog.getOpenFileName()
        if len(filename)> 0:
            filename = filename[0].split("/")

            self.appSetings.settingList["txtSettings"]["Pfad"] = self.kombiPfad(filename)
            self.appSetings.settingList["txtSettings"]["NameDerTxTDatei"] = filename[-1]
            self.lb_activ_log_name.setText(self.appSetings.settingList["txtSettings"]["Pfad"]+"/"+self.appSetings.settingList["txtSettings"]["NameDerTxTDatei"])
        else:
            pass
    # funktion zum speicher der einstellungen von der Settings GUI in die Json
    def saveSettings(self):

        # hier wird geprüft ob die einstelungs text boxen leer sind

        # Setting gui seite 1
        if len(self.le_Name_Suche.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["SpalteName"]= self.le_Name_Suche.text().upper()
        if len(self.le_Anzeige1.text())>0:
            self.appSetings.settingList["ExcelSettings"]["SpalteKostenstelle"] = self.le_Anzeige1.text().upper()
        if len(self.le_UID_Suche.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["SpalteUID"] = self.le_UID_Suche.text().upper()
        if len(self.le_q_nr1.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["Q1"] = self.le_q_nr1.text().upper()
        if len(self.le_q_nr2.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["Q4"] = self.le_q_nr2.text().upper()
        if len(self.le_q_nr3.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["Später"] = self.le_q_nr3.text().upper()
        if len(self.le_Anzeige_nr2.text()) >0:
            self.appSetings.settingList["ExcelSettings"]["SpalteAlterHinweis"] = self.le_Anzeige_nr2.text().upper()
        if len(self.le_spalte_pf_JN.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["SpalteEntwickler"] = self.le_spalte_pf_JN.text().upper()
        if len(self.le_db_Eintrag1.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl1"] = self.le_db_Eintrag1.text()
        if len(self.le_db_Nr2.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl2"] = self.le_db_Nr2.text()
        if len(self.le_db_schreiben_in.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["Betriebssystem"] = self.le_db_schreiben_in.text().upper()
        if len(self.le_name_sh2.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["Worksheet_2"] = self.le_name_sh2.text()
        if len(self.le_sh2_aBereich.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetA"] = self.le_sh2_aBereich.text()
        if len(self.le_sh2_eBereich.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetE"] = self.le_sh2_eBereich.text()
        if len(self.le_db_sh2_speicher_in.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["SpalteAusModell"] = self.le_db_sh2_speicher_in.text()
        if len(self.el_sh2_le_sh2_spalte_bereich.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["Sheet2SpalteBereichsAuswahl"] = self.el_sh2_le_sh2_spalte_bereich.text()
        if len(self.le_ersterSpaltenEintrag.text()) > 0:
            self.appSetings.settingList["ExcelSettings"]["SpalteNotiz"] = self.le_ersterSpaltenEintrag.text()

        #######################################################################################################
        #####
        ###
        #

        # Setting gui seite 2
        if self.cb_uebertragen.isChecked():
            self.appSetings.settingList["ExcelSettings"]["AutomatischesEintragenIn2Excel"] = True
        else:
            self.appSetings.settingList["ExcelSettings"]["AutomatischesEintragenIn2Excel"] = False

        if self.cb_logerzeugen.isChecked():
            self.appSetings.settingList["ExcelSettings"]["Log_Erzeugen"] = True
        else:
            self.appSetings.settingList["ExcelSettings"]["Log_Erzeugen"] = False

        if len(self.el_wb2_suchspalte.text() ) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["PrüfSpalte"] = self.el_wb2_suchspalte.text()
        if len(self.el_wb2_Datum_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag7"] = self.el_wb2_Datum_in.text()
        if len(self.el_wb2_Name_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag4"] = self.el_wb2_Name_in.text()
        if len(self.el_wb2_uid_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag5"] = self.el_wb2_uid_in.text()

        if len(self.el_wb2_eintrag4_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag2"] = self.el_wb2_eintrag4_in.text()
        if len(self.el_wb2_eintrag5_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag3"] = self.el_wb2_eintrag5_in.text()
        if len(self.el_wb2_eintrag6_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag6"] = self.el_wb2_eintrag4_in.text()
        if len(self.el_wb2_eintrag7_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag7"] = self.el_wb2_eintrag5_in.text()
        if len(self.el_wb2_eintrag8_in.text()) > 0:
            self.appSetings.settingList["Excel2Einstellungen"]["Eintrag8"] = self.el_wb2_eintrag5_in.text()

        # hier werden die eigegebenen einstellungen aus den textboxen in die json gesetzt
        self.lb_activ_Name.setText(self.appSetings.settingList["ExcelSettings"]["SpalteName"])
        self.lb_activ_Kostenstelle.setText(self.appSetings.settingList["ExcelSettings"]["SpalteKostenstelle"])
        self.lb_activ_UID.setText(self.appSetings.settingList["ExcelSettings"]["SpalteUID"])
        self.lb_aktiv_Qartale.setText(self.appSetings.settingList["ExcelSettings"]["Q4"] +", " +
                                      self.appSetings.settingList["ExcelSettings"]["Q1"] +", "+
                                      self.appSetings.settingList["ExcelSettings"]["Später"])
        self.lb_activ_Alter_Hinweis.setText(self.appSetings.settingList["ExcelSettings"]["SpalteAlterHinweis"])
        self.lb_activ_Notiz.setText(self.appSetings.settingList["ExcelSettings"]["SpalteNotiz"])
        self.lb_activ_Entwickler.setText(self.appSetings.settingList["ExcelSettings"]["SpalteEntwickler"])
        self.lb_activ_DD_auswahl1.setText(self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl1"])
        self.lb_activ_DD_auswahl2.setText(self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl2"])
        self.lb_dmEA_save_in.setText(self.appSetings.settingList["ExcelSettings"]["Betriebssystem"])
        self.lb_activ_2Sheet.setText(self.appSetings.settingList["ExcelSettings"]["Worksheet_2"])
        self.lb_activ_2SBereichAuswahl.setText(self.appSetings.settingList["ExcelSettings"]["Sheet2SpalteBereichsAuswahl"])
        self.lb_aktiv_Sheet2SpalteBereichsAuswahl.setText(self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetA"] +" bis "+
                                                          self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetE"])
        self.lb_aktiv_aus_db_save_in.setText(self.appSetings.settingList["ExcelSettings"]["SpalteAusModell"])

        self.lb_wb2_active_suchSpalte.setText(self.appSetings.settingList["Excel2Einstellungen"]["PrüfSpalte"])
        self.lb_wb2_activ_datum.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag7"])
        self.lb_wb2_activ_name.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag4"])
        self.lb_wb2_activ_uid.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag5"])
        self.lb_wb2_activ_Eintrag4.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag2"])
        self.lb_wb2_activ_Eintrag5.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag3"])
        self.lb_wb2_activ_Eintrag6.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag6"])
        self.lb_wb2_activ_Eintrag7.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag7"])
        self.lb_wb2_activ_Eintrag8.setText(self.appSetings.settingList["Excel2Einstellungen"]["Eintrag8"])
        self.appSetings.saveSettings()
        self.appSetings.loadSettings()


        #####################################  EditLines Clear
        ####
        ##
        self.le_Name_Suche.setText("")
        self.le_Anzeige1.setText("")
        self.le_UID_Suche.setText("")
        self.le_q_nr1.setText("")
        self.le_q_nr2.setText("")
        self.le_q_nr3.setText("")
        self.le_Anzeige_nr2.setText("")
        self.le_spalte_pf_JN.setText("")
        self.le_db_Eintrag1.setText("")
        self.le_db_Nr2.setText("")
        self.le_db_schreiben_in.setText("")
        self.le_name_sh2.setText("")
        self.le_sh2_aBereich.setText("")
        self.le_sh2_eBereich.setText("")
        self.le_db_sh2_speicher_in.setText("")
        self.el_sh2_le_sh2_spalte_bereich.setText("")
        self.le_ersterSpaltenEintrag.setText("")




# Hauptfenster klasse
class main_window(QMainWindow, Ui_frm_main):
    #public atribute

    Spalte = ""
    index = []
    name =""
    hostname =""
    ausgabeliste = []
    sn= ""
    notiz = ""
    listeModellAuswahl = []

    listeModelle = {}
    ex = None
    ex2 = None
    appSettings = src.appSetting.appSettings()
    appSettings.loadSettings()
    # Konstruktor
    def __init__(self):

        super().__init__()
        self.listeDropBoxIndexWahl = {}
        self.listeModelleDropBoxAnzeige = {}
        self.setupUi(self)
        self.indexListe = []

        self.cb_mehr_eintrag.setHidden(True)
        self.lb_mehr_eintrag.setHidden(True)
        self.cb_MehrfachNamen.setHidden(True)
        self.lb_AushabeHinweis.setHidden(True)
        # verstecke teile der gui wen die eingabe kürzer als 3 zeichen hat
        if len(self.tb_suche_name.text()) < 3:
            self.cb_mehr_eintrag.setHidden(True)
            self.lb_mehr_eintrag.setHidden(True)
            self.cb_MehrfachNamen.setHidden(True)
        # lade settings json
        fileName = r".\settings.json"
        fileObj = Path(fileName)
        self.appSetings = appSettings()
        # überprüfe ob die datei vorhanden ist wen nein erstelllt es automatisch
        if fileObj.is_file() == False:
            print("Keine Settings gefunden!")
            print("Erstelle Settings.json....  ")
            self.appSetings.inputSettings()
            self.appSetings.saveDefaultSettings()
            self.appSetings.loadSettings()

        self.appSetings.loadSettings()
        self.listeBetriebsysteme = [f'{self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl2"]}',
                               f'{self.appSetings.settingList["ExcelSettings"]["DropdownMenuAuswahl1"]}']
        try:
            self.snE = snExport()
        except:
            print("Es besteht keine verbindung zu den Import Verzeichnis!")
        if self.appSetings.settingList["ExcelSettings"]["Log_Erzeugen"] == True:
            self.backup = txt_backup()
            self.backup.ifExist()
        else:
            print("Einstellungen sagen es wird kein Backup benötigt \n Aufeigene Gefahr ! ;)")
        self.cb_mehr_eintrag.setDuplicatesEnabled(False)

        self.comboBox.addItems(self.listeBetriebsysteme)
        try:
            self.ex = excelImport()
            self.ex.loadExcel()
        except:
            print("Datei nicht vorhanden, überpürfen sie die Einstellungen")

        self.tb_suche_uid.textChanged.connect(self.uidübergabe)
        self.tb_suche_name.textChanged.connect(self.nameübergabe)
        self.lb_datum_anzeige.setText(datetime.today().strftime('%d.%m.%Y'))
        try:
            self.dropdaownmenuAdd()
        except:
            print("Fehler beim Import!")
        self.cb_modelauswahl.addItems(self.listeModellAuswahl)
        self.btn_settings.pressed.connect(self.setingsAnzeigen)
        self.btn_export.pressed.connect(self.exportToExcel)
        self.tb_suche_name.textChanged.connect(self.dropdownMehrfach)
        self.tb_suche_name.textChanged.connect(self.textClear)
        self.tb_suche_name.textChanged.connect(self.dropNamen)
        self.cb_MehrfachNamen.currentTextChanged.connect(self.indexPicDurchCB)
        self.cb_MehrfachNamen.currentTextChanged.connect(self.dropdownMehrfach)
        #self.cb_MehrfachNamen.currentTextChanged.connect(self.indexwahldurchcb)
        self.cb_mehr_eintrag.currentTextChanged.connect(self.indexwahldurchcb)
        self.tb_suche_sn.setDisabled(False)
        self.tb_suche_name.textChanged.connect(self.dbClear)

        ## 20.12
        try:
            self.label.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteUID"]}1'].value)
            self.label_2.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteName"]}1'].value)
            self.label_9.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteKostenstelle"]}1'].value)
            self.label_3.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteAlterHinweis"]}1'].value)
            self.label_4.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteSN"]}1'].value)
            self.label_5.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteEntwickler"]}1'].value)
            self.lb_8.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Betriebssystem"]}1'].value)
            self.lb_9.setText(f'{self.appSetings.settingList["ExcelSettings"]["TextFürLabelÄndernIn"]}')
            self.label_6.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteHinweis"]}1'].value)
            self.label_8.setText(f'{self.appSetings.settingList["ExcelSettings"]["Überschrift"]}')
        except:
            print("Kein Internet... Standart einstellungen werden übernommen")


    ## funktion zum clearen der textzeilen in der gui
    def dbClear(self):

        if len(self.tb_suche_name.text()) < 4:
            self.index = 2
            self.indexListe = []
            self.lb_mehr_eintrag.setHidden(True)
            self.cb_MehrfachNamen.setHidden(True)
            self.cb_mehr_eintrag.setHidden(True)
            self.lb_quatal.setText("")
            self.lb_kostenstelle.setText("")
            self.lb_name_ausgabe.setText("")
            self.lb_hinweis.setText("")
            self.lb_uid_ausgabe.setText("")
            self.notiz_eingabe.setText("")


    ## funktion zum auswählen des index durch die combobox
    def indexPicDurchCB(self):
        self.dbClear()
        text = self.cb_MehrfachNamen.currentText()
        splitttext = text.split()
        text = splitttext[0] +" "+ splitttext[1]
        self.indexListe = self.ex.sucheNachName(text, self.appSetings.settingList["ExcelSettings"]["SpalteName"])
        self.index = self.indexListe[0]
        self.texteSetzen(self.index)

        # gleiche wie oben nur andere combobox
    def indexwahldurchcb(self):
        self.dbClear()
        try:


            text = self.cb_mehr_eintrag.currentText()
            self.index = self.indexListe[self.cb_mehr_eintrag.currentIndex()]
            self.cb_modelauswahl.setCurrentText(text)
            self.indexListe = set(self.indexListe)
            self.indexListe = list(self.indexListe)
            ##################20.12
            self.pruefenObHinweiss(self.index)
            self.pruefungObSn(self.index)
            #################################################
            self.texteSetzen(self.index)

        except:
            pass
    # funktionb zur anzeige des settings fensters
    def setingsAnzeigen(self):
        sWindow.show()

    #funktion für die combobox der namen inc. index wechsel
    def dropNamen(self):
        self.dbClear()
        self.cb_MehrfachNamen.clear()
        ListeName = []
        self.indexListe = set(self.indexListe)
        self.indexListe = list(self.indexListe)

        if len(self.indexListe) > 1:
            self.cb_MehrfachNamen.setHidden(False)
            for element in self.indexListe:
                if self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteName"]}{element}'].value != None:

                    ListeName.append(str(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["DropDownMenue1"]}{element}'].value) +
                                          " " + str(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["DropDownMenue2"]}{element}'].value))
            ListeName = set(ListeName)

            self.cb_MehrfachNamen.addItems(ListeName)

        else:
            self.cb_MehrfachNamen.setHidden(True)
            self.cb_mehr_eintrag.setHidden(True)
            self.lb_mehr_eintrag.setHidden(True)

        self.texteSetzen(self.index)
    # funktion der namessuche
    def nameübergabe(self):
        self.dbClear()
        # 20.12
        # versuch die UID TEXT box zu leeren wen ein name eingegeben wird
        self.tb_suche_uid.setText("")
        ########################################
        text = self.tb_suche_name.text()
        spalte = self.appSetings.settingList["ExcelSettings"]['SpalteName']

        self.indexListe = self.ex.sucheNachName(text, spalte)

        if self.indexListe == None or len(self.indexListe) == 0:
            teile = text.split(" ")
            text= teile[1] + " " + teile[0]
            self.indexListe = self.ex.sucheNachName(text, spalte)
        if len(self.indexListe) > 0 and self.indexListe != None:
            self.texteSetzen(self.indexListe[0])

        self.texteSetzen(self.index)
    def pruefungObSn(self, index):

        if self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["PrüfSpalteFürSN"]}{index}'].value != None:
            self.tb_suche_sn.setHidden(True)
            self.lb_WenSnVorhanden.setDisabled(False)
            self.cb_modelauswahl.setHidden(True)
            self.comboBox.setHidden(True)
            self.btn_export.setHidden(True)
            self.btn_export.setDisabled(True)
            self.lb_WenSnVorhanden.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["PrüfSpalteFürSN"]}{index}'].value)
        elif self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["PrüfSpalteFürSN"]}{index}'].value == None:
            self.tb_suche_sn.setHidden(False)
            self.btn_export.setHidden(False)
            self.btn_export.setDisabled(False)
            self.lb_WenSnVorhanden.setText("")
            self.lb_WenSnVorhanden.setDisabled(True)
            self.notiz_eingabe.setHidden(False)
            self.lb_AushabeHinweis.setHidden(True)
            self.cb_modelauswahl.setHidden(False)
            self.comboBox.setHidden(False)
            self.lb_AushabeHinweis.setText("")
            self.lb_WenSnVorhanden.setText("")

    # funktion zum label setzen auf der gui aus der excel
    def uidübergabe(self):
        # 20.12 versuch die txt box zu leeren
        self.tb_suche_name.setText("")
        ############################
        try:
            self.dbClear()
            text = self.tb_suche_uid.text()
            spalte = self.appSetings.settingList["ExcelSettings"]['SpalteUID']
            self.indexListe = self.ex.sucheNachUID( text, spalte )
            self.index = self.indexListe[0]
            self.texteSetzen(self.indexListe[0])
        except:
            print("Fehler bei der Suche nach UID, überprüfen sie die Settings!")
##########################################################################
    # setze lable über die spalten
    def texteSetzen(self, index):
        self.dbClear()
        self.pruefungObSn(index)
        self.pruefenObHinweiss(index)
        self.quartalCheck(index)
        self.cb_modelauswahl.setCurrentText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["BestelltesModellSpalte"]}{index}'].value)
        self.lb_uid_ausgabe.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteUID"]}{index}'].value)
        self.lb_name_ausgabe.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteName"]}{index}'].value)
        self.lb_kostenstelle.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteKostenstelle"]}{index}'].value)
        self.lb_hinweis.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteAlterHinweis"]}{index}'].value)
        self.hostname = self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteHost"]}{index}'].value
        self.name = self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteName"]}{index}'].value
        self.cb_modelauswahl.setCurrentText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["BestelltesModellSpalte"]}{index}'].value)
        element = self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["BestelltesModellSpalte"]}{index}'].value
        if index > 1:
            if element != None:
                indexVomModell = self.listeModellAuswahl.index(element)
                self.cb_modelauswahl.setCurrentIndex(indexVomModell)
        self.quartalCheck(index)

        if self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteEntwickler"]}{index}'].value == "ja":
            self.comboBox.setCurrentIndex(0)
            self.lb_entwickler.setText("Ja")
        else:
            self.lb_entwickler.setText("Nein")
            self.comboBox.setCurrentIndex(1)

    def pruefenObHinweiss(self, index):

        if self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteHinweis"]}{index}'].value != None:
            self.notiz_eingabe.setHidden(True)
            self.lb_AushabeHinweis.setHidden(False)
            self.lb_AushabeHinweis.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteHinweis"]}{index}'].value)

    # funktion zum text clearen
    def textClear(self):
        self.notiz_eingabe.setText("")
    # funktion zum überprüfen ob splate  o, p oder q ein X hat  ( eintrag welches quartal )
    def quartalCheck(self, index):
        if self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Q4"]}{index}'].value == 'x':
            self.lb_quatal.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Q4"]}1'].value)
        elif self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Q1"]}{index}'].value == 'x':
            self.lb_quatal.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Q1"]}1'].value )
        elif self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Später"]}{index}'].value == 'x':
            self.lb_quatal.setText(self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Später"]}1'].value)
        else:
            self.lb_quatal.setText("-")

    ## funktion zum speicher der excel mit zeitstempel

    def exportToExcel(self):

        self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteNotiz"]}{self.index}'] = self.notiz_eingabe.text()
        self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteSN"]}{self.index}'] = self.tb_suche_sn.text()
        self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteAusModell"]}{self.index}'] = self.cb_modelauswahl.currentText()
        self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["Betriebssystem"]}{self.index}'] = self.comboBox.currentText()
        self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteDatum"]}{self.index}'] = datetime.today().strftime('%d.%m.%Y') # ganzes jahr anzeigen
    # adde ausgabe zu einer liste für backup
        if self.appSetings.settingList["ExcelSettings"]["Log_Erzeugen"] == True:
            self.ausgabeliste.append(str(self.ex.ws[f'A{self.index}'].value)) # 0
            self.ausgabeliste.append(datetime.today().strftime('%d.%m.%Y')) # 1
            self.ausgabeliste.append(self.tb_suche_name.text()) #2
            self.ausgabeliste.append(self.tb_suche_uid.text()) #3
            self.ausgabeliste.append(self.tb_suche_sn.text()) #4
            self.ausgabeliste.append(self.cb_modelauswahl.currentText()) #5
            self.ausgabeliste.append(self.comboBox.currentText()) #6
            self.ausgabeliste.append(self.notiz_eingabe.text()) #7
            self.backup.adding(self.ausgabeliste)
        else:
            print("Back-Up optionen wurden deaktiviert!")

        if self.appSetings.settingList["ExcelSettings"]["AutomatischesEintragenIn2Excel"] == "An":
            self.snE.check(inputDatum=self.ausgabeliste[1],inputName=self.ausgabeliste[2], inputUID=self.lb_uid_ausgabe.text(),
                    inputSn=self.ausgabeliste[4],inputKostenstelle=self.lb_kostenstelle.text(),inputImg=self.comboBox.currentText(),
                    inputHinweis=self.ausgabeliste[7], inputModel=self.ausgabeliste[5], inputHostname=self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["SpalteHost"]}{self.index}'].value)
        self.ausgabeliste.clear()
        # # überschreiben die ausgangedatei
        # leeren der text eingabe fehler damit man erkennt das er fertig ist        evtl Load screen?

        self.ex.saveExcel(self.appSetings.settingList["ExcelSettings"]["BackupOrt"], self.appSetings.settingList["ExcelSettings"]["BackupName"], self.appSetings.settingList["ExcelSettings"]["DateiEndung"])
        self.ex.excelExport(self.appSetings.settingList["ExcelSettings"]["ExportOrt"], self.appSetings.settingList["ExcelSettings"]["ExportName"], self.appSetings.settingList["ExcelSettings"]["DateiEndung"])
        self.indexListe = []
        self.notiz_eingabe.setText("")
        self.tb_suche_sn.setText("")
        self.tb_suche_name.setText("")
        self.ex.wb.close()

        self.ex.loadExcel()


    # einfach funktion zum füllen des dropdown menüs
    def dropdaownmenuAdd(self):
        for i in range(self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetA"], self.appSetings.settingList["ExcelSettings"]["BereichIm2SheetE"]):
            self.listeModellAuswahl.append(self.ex.ws2[f'{self.appSetings.settingList["ExcelSettings"]["Sheet2SpalteBereichsAuswahl"]}{i}'].value)
        self.listeModellAuswahl.append(" ")
    # funktion für die combobox mehrfachauswahl
    def dropdownMehrfach(self):
        self.dbClear()
        index = self.indexListe
        index = set(index)
        self.cb_mehr_eintrag.clear()
        try:
            if self.indexListe == None:
                self.cb_mehr_eintrag.setHidden(True)
                self.lb_mehr_eintrag.setHidden(True)
                self.cb_mehr_eintrag.clear()
            if len(self.indexListe) == 1:
                self.cb_mehr_eintrag.setHidden(True)
                self.lb_mehr_eintrag.setHidden(True)
                self.cb_mehr_eintrag.clear()
            if len(self.indexListe) > 1:
                self.cb_mehr_eintrag.setHidden(False)
                self.lb_mehr_eintrag.setHidden(False)
                self.cb_mehr_eintrag.clear()
                self.listeModelleDropBoxAnzeige = {}
                for element in index:
                    if self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["BestelltesModellSpalte"]}{element}'].value != None:
                        model = self.ex.ws[f'{self.appSetings.settingList["ExcelSettings"]["BestelltesModellSpalte"]}{element}'].value
                        self.listeDropBoxIndexWahl[model]=element
                        self.listeModelleDropBoxAnzeige[element] = model
                self.cb_mehr_eintrag.addItems(self.listeModelleDropBoxAnzeige.values())
        except:
            pass

    # funktion die das X in der App überschreibt und sichert
    def closeEvent(self, event):


        self.ex.exit()
        print("Programm wird beendet. Bye!")

        event.accept()


app = QApplication()
main_Frm = main_window()
main_Frm.show()
sWindow = setings_window()

sys.exit(app.exec())
