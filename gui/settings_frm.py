# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_frm2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_Settings_frm(object):
    def setupUi(self, Settings_frm):
        if not Settings_frm.objectName():
            Settings_frm.setObjectName(u"Settings_frm")
        Settings_frm.resize(882, 621)
        self.frame = QFrame(Settings_frm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 866, 610))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 391, 521))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 91, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 60, 91, 20))
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 90, 91, 20))
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 120, 131, 20))
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 150, 151, 21))
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 180, 131, 20))
        self.le_UID_Suche = QLineEdit(self.frame_6)
        self.le_UID_Suche.setObjectName(u"le_UID_Suche")
        self.le_UID_Suche.setGeometry(QRect(160, 60, 81, 21))
        self.le_Name_Suche = QLineEdit(self.frame_6)
        self.le_Name_Suche.setObjectName(u"le_Name_Suche")
        self.le_Name_Suche.setGeometry(QRect(160, 90, 81, 21))
        self.le_Anzeige1 = QLineEdit(self.frame_6)
        self.le_Anzeige1.setObjectName(u"le_Anzeige1")
        self.le_Anzeige1.setGeometry(QRect(160, 120, 81, 21))
        self.le_q_nr1 = QLineEdit(self.frame_6)
        self.le_q_nr1.setObjectName(u"le_q_nr1")
        self.le_q_nr1.setGeometry(QRect(160, 150, 31, 21))
        self.le_q_nr2 = QLineEdit(self.frame_6)
        self.le_q_nr2.setObjectName(u"le_q_nr2")
        self.le_q_nr2.setGeometry(QRect(200, 150, 31, 21))
        self.le_q_nr3 = QLineEdit(self.frame_6)
        self.le_q_nr3.setObjectName(u"le_q_nr3")
        self.le_q_nr3.setGeometry(QRect(240, 150, 31, 20))
        self.le_Anzeige_nr2 = QLineEdit(self.frame_6)
        self.le_Anzeige_nr2.setObjectName(u"le_Anzeige_nr2")
        self.le_Anzeige_nr2.setGeometry(QRect(160, 180, 81, 21))
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 210, 141, 20))
        self.le_ersterSpaltenEintrag = QLineEdit(self.frame_6)
        self.le_ersterSpaltenEintrag.setObjectName(u"le_ersterSpaltenEintrag")
        self.le_ersterSpaltenEintrag.setGeometry(QRect(160, 210, 81, 21))
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 240, 151, 20))
        self.le_spalte_pf_JN = QLineEdit(self.frame_6)
        self.le_spalte_pf_JN.setObjectName(u"le_spalte_pf_JN")
        self.le_spalte_pf_JN.setGeometry(QRect(160, 240, 81, 21))
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 270, 161, 20))
        self.le_db_Eintrag1 = QLineEdit(self.frame_6)
        self.le_db_Eintrag1.setObjectName(u"le_db_Eintrag1")
        self.le_db_Eintrag1.setGeometry(QRect(160, 300, 81, 21))
        self.le_sh2_aBereich = QLineEdit(self.frame_6)
        self.le_sh2_aBereich.setObjectName(u"le_sh2_aBereich")
        self.le_sh2_aBereich.setGeometry(QRect(60, 460, 41, 21))
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 300, 151, 20))
        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 330, 151, 20))
        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 400, 231, 21))
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 460, 51, 20))
        self.le_db_Nr2 = QLineEdit(self.frame_6)
        self.le_db_Nr2.setObjectName(u"le_db_Nr2")
        self.le_db_Nr2.setGeometry(QRect(160, 330, 81, 21))
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 430, 131, 20))
        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(110, 460, 51, 20))
        self.le_sh2_eBereich = QLineEdit(self.frame_6)
        self.le_sh2_eBereich.setObjectName(u"le_sh2_eBereich")
        self.le_sh2_eBereich.setGeometry(QRect(160, 460, 41, 21))
        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 500, 141, 20))
        self.le_db_sh2_speicher_in = QLineEdit(self.frame_6)
        self.le_db_sh2_speicher_in.setObjectName(u"le_db_sh2_speicher_in")
        self.le_db_sh2_speicher_in.setGeometry(QRect(160, 500, 41, 21))
        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 360, 211, 20))
        self.le_db_schreiben_in = QLineEdit(self.frame_6)
        self.le_db_schreiben_in.setObjectName(u"le_db_schreiben_in")
        self.le_db_schreiben_in.setGeometry(QRect(250, 360, 31, 20))
        self.le_name_sh2 = QLineEdit(self.frame_6)
        self.le_name_sh2.setObjectName(u"le_name_sh2")
        self.le_name_sh2.setGeometry(QRect(250, 400, 71, 20))
        self.el_sh2_le_sh2_spalte_bereich = QLineEdit(self.frame_6)
        self.el_sh2_le_sh2_spalte_bereich.setObjectName(u"el_sh2_le_sh2_spalte_bereich")
        self.el_sh2_le_sh2_spalte_bereich.setGeometry(QRect(160, 430, 41, 21))
        self.frame_8 = QFrame(self.tab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(520, 0, 301, 481))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.buttonBox_4 = QDialogButtonBox(self.tab)
        self.buttonBox_4.setObjectName(u"buttonBox_4")
        self.buttonBox_4.setGeometry(QRect(350, 530, 156, 24))
        self.buttonBox_4.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.frame_7 = QFrame(self.tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(370, -10, 151, 531))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 10, 101, 41))
        self.label_28.setFont(font)
        self.lb_activ_UID = QLabel(self.frame_7)
        self.lb_activ_UID.setObjectName(u"lb_activ_UID")
        self.lb_activ_UID.setGeometry(QRect(0, 70, 91, 20))
        self.lb_activ_Name = QLabel(self.frame_7)
        self.lb_activ_Name.setObjectName(u"lb_activ_Name")
        self.lb_activ_Name.setGeometry(QRect(0, 100, 91, 20))
        self.lb_activ_Kostenstelle = QLabel(self.frame_7)
        self.lb_activ_Kostenstelle.setObjectName(u"lb_activ_Kostenstelle")
        self.lb_activ_Kostenstelle.setGeometry(QRect(0, 130, 91, 20))
        self.lb_aktiv_Qartale = QLabel(self.frame_7)
        self.lb_aktiv_Qartale.setObjectName(u"lb_aktiv_Qartale")
        self.lb_aktiv_Qartale.setGeometry(QRect(0, 160, 91, 20))
        self.lb_activ_Alter_Hinweis = QLabel(self.frame_7)
        self.lb_activ_Alter_Hinweis.setObjectName(u"lb_activ_Alter_Hinweis")
        self.lb_activ_Alter_Hinweis.setGeometry(QRect(0, 190, 91, 20))
        self.lb_activ_Notiz = QLabel(self.frame_7)
        self.lb_activ_Notiz.setObjectName(u"lb_activ_Notiz")
        self.lb_activ_Notiz.setGeometry(QRect(0, 220, 91, 20))
        self.lb_activ_Entwickler = QLabel(self.frame_7)
        self.lb_activ_Entwickler.setObjectName(u"lb_activ_Entwickler")
        self.lb_activ_Entwickler.setGeometry(QRect(0, 250, 91, 20))
        self.lb_activ_DD_auswahl1 = QLabel(self.frame_7)
        self.lb_activ_DD_auswahl1.setObjectName(u"lb_activ_DD_auswahl1")
        self.lb_activ_DD_auswahl1.setGeometry(QRect(0, 310, 91, 20))
        self.lb_activ_2SBereichAuswahl = QLabel(self.frame_7)
        self.lb_activ_2SBereichAuswahl.setObjectName(u"lb_activ_2SBereichAuswahl")
        self.lb_activ_2SBereichAuswahl.setGeometry(QRect(0, 440, 91, 20))
        self.lb_aktiv_aus_db_save_in = QLabel(self.frame_7)
        self.lb_aktiv_aus_db_save_in.setObjectName(u"lb_aktiv_aus_db_save_in")
        self.lb_aktiv_aus_db_save_in.setGeometry(QRect(0, 510, 91, 20))
        self.lb_activ_2Sheet = QLabel(self.frame_7)
        self.lb_activ_2Sheet.setObjectName(u"lb_activ_2Sheet")
        self.lb_activ_2Sheet.setGeometry(QRect(0, 410, 91, 20))
        self.lb_dmEA_save_in = QLabel(self.frame_7)
        self.lb_dmEA_save_in.setObjectName(u"lb_dmEA_save_in")
        self.lb_dmEA_save_in.setGeometry(QRect(0, 370, 91, 20))
        self.lb_activ_DD_auswahl2 = QLabel(self.frame_7)
        self.lb_activ_DD_auswahl2.setObjectName(u"lb_activ_DD_auswahl2")
        self.lb_activ_DD_auswahl2.setGeometry(QRect(0, 340, 91, 20))
        self.lb_aktiv_Sheet2SpalteBereichsAuswahl = QLabel(self.frame_7)
        self.lb_aktiv_Sheet2SpalteBereichsAuswahl.setObjectName(u"lb_aktiv_Sheet2SpalteBereichsAuswahl")
        self.lb_aktiv_Sheet2SpalteBereichsAuswahl.setGeometry(QRect(0, 470, 81, 20))
        self.tabWidget.addTab(self.tab, "")
        self.frame_8.raise_()
        self.buttonBox_4.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 311, 16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.frame_10 = QFrame(self.tab_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 30, 671, 431))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.cb_uebertragen = QCheckBox(self.frame_10)
        self.cb_uebertragen.setObjectName(u"cb_uebertragen")
        self.cb_uebertragen.setGeometry(QRect(10, 20, 181, 20))
        self.cb_uebertragen.setChecked(True)
        self.label_46 = QLabel(self.frame_10)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 140, 81, 16))
        self.el_wb2_suchspalte = QLineEdit(self.frame_10)
        self.el_wb2_suchspalte.setObjectName(u"el_wb2_suchspalte")
        self.el_wb2_suchspalte.setGeometry(QRect(150, 140, 41, 16))
        self.label_47 = QLabel(self.frame_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 170, 131, 16))
        self.label_48 = QLabel(self.frame_10)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 200, 131, 16))
        self.label_49 = QLabel(self.frame_10)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 230, 131, 16))
        self.label_50 = QLabel(self.frame_10)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 270, 131, 16))
        self.label_51 = QLabel(self.frame_10)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(10, 300, 131, 16))
        self.label_52 = QLabel(self.frame_10)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(10, 330, 131, 16))
        self.label_53 = QLabel(self.frame_10)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 360, 131, 16))
        self.label_54 = QLabel(self.frame_10)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(10, 390, 131, 16))
        self.el_wb2_Datum_in = QLineEdit(self.frame_10)
        self.el_wb2_Datum_in.setObjectName(u"el_wb2_Datum_in")
        self.el_wb2_Datum_in.setGeometry(QRect(150, 170, 41, 16))
        self.el_wb2_Name_in = QLineEdit(self.frame_10)
        self.el_wb2_Name_in.setObjectName(u"el_wb2_Name_in")
        self.el_wb2_Name_in.setGeometry(QRect(150, 200, 41, 16))
        self.el_wb2_uid_in = QLineEdit(self.frame_10)
        self.el_wb2_uid_in.setObjectName(u"el_wb2_uid_in")
        self.el_wb2_uid_in.setGeometry(QRect(150, 230, 41, 16))
        self.el_wb2_eintrag4_in = QLineEdit(self.frame_10)
        self.el_wb2_eintrag4_in.setObjectName(u"el_wb2_eintrag4_in")
        self.el_wb2_eintrag4_in.setGeometry(QRect(150, 270, 41, 16))
        self.el_wb2_eintrag5_in = QLineEdit(self.frame_10)
        self.el_wb2_eintrag5_in.setObjectName(u"el_wb2_eintrag5_in")
        self.el_wb2_eintrag5_in.setGeometry(QRect(150, 300, 41, 16))
        self.el_wb2_eintrag6_in = QLineEdit(self.frame_10)
        self.el_wb2_eintrag6_in.setObjectName(u"el_wb2_eintrag6_in")
        self.el_wb2_eintrag6_in.setGeometry(QRect(150, 330, 41, 16))
        self.el_wb2_eintrag7_in = QLineEdit(self.frame_10)
        self.el_wb2_eintrag7_in.setObjectName(u"el_wb2_eintrag7_in")
        self.el_wb2_eintrag7_in.setGeometry(QRect(150, 360, 41, 16))
        self.el_wb2_eintrag8_in = QLineEdit(self.frame_10)
        self.el_wb2_eintrag8_in.setObjectName(u"el_wb2_eintrag8_in")
        self.el_wb2_eintrag8_in.setGeometry(QRect(150, 390, 41, 16))
        self.label_55 = QLabel(self.frame_10)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(220, 100, 81, 16))
        self.lb_wb2_active_suchSpalte = QLabel(self.frame_10)
        self.lb_wb2_active_suchSpalte.setObjectName(u"lb_wb2_active_suchSpalte")
        self.lb_wb2_active_suchSpalte.setGeometry(QRect(220, 140, 81, 16))
        self.lb_wb2_activ_datum = QLabel(self.frame_10)
        self.lb_wb2_activ_datum.setObjectName(u"lb_wb2_activ_datum")
        self.lb_wb2_activ_datum.setGeometry(QRect(220, 170, 81, 16))
        self.lb_wb2_activ_name = QLabel(self.frame_10)
        self.lb_wb2_activ_name.setObjectName(u"lb_wb2_activ_name")
        self.lb_wb2_activ_name.setGeometry(QRect(220, 200, 81, 16))
        self.lb_wb2_activ_uid = QLabel(self.frame_10)
        self.lb_wb2_activ_uid.setObjectName(u"lb_wb2_activ_uid")
        self.lb_wb2_activ_uid.setGeometry(QRect(220, 230, 81, 16))
        self.lb_wb2_activ_Eintrag4 = QLabel(self.frame_10)
        self.lb_wb2_activ_Eintrag4.setObjectName(u"lb_wb2_activ_Eintrag4")
        self.lb_wb2_activ_Eintrag4.setGeometry(QRect(220, 270, 81, 16))
        self.lb_wb2_activ_Eintrag5 = QLabel(self.frame_10)
        self.lb_wb2_activ_Eintrag5.setObjectName(u"lb_wb2_activ_Eintrag5")
        self.lb_wb2_activ_Eintrag5.setGeometry(QRect(220, 300, 81, 16))
        self.lb_wb2_activ_Eintrag6 = QLabel(self.frame_10)
        self.lb_wb2_activ_Eintrag6.setObjectName(u"lb_wb2_activ_Eintrag6")
        self.lb_wb2_activ_Eintrag6.setGeometry(QRect(220, 330, 81, 16))
        self.lb_wb2_activ_Eintrag7 = QLabel(self.frame_10)
        self.lb_wb2_activ_Eintrag7.setObjectName(u"lb_wb2_activ_Eintrag7")
        self.lb_wb2_activ_Eintrag7.setGeometry(QRect(220, 360, 81, 16))
        self.lb_wb2_activ_Eintrag8 = QLabel(self.frame_10)
        self.lb_wb2_activ_Eintrag8.setObjectName(u"lb_wb2_activ_Eintrag8")
        self.lb_wb2_activ_Eintrag8.setGeometry(QRect(220, 390, 81, 16))
        self.buttonBox_3 = QDialogButtonBox(self.tab_2)
        self.buttonBox_3.setObjectName(u"buttonBox_3")
        self.buttonBox_3.setGeometry(QRect(350, 490, 156, 24))
        self.buttonBox_3.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 0, 771, 421))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 831, 131))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 80, 71, 16))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_4.setFont(font2)
        self.btn_importSave = QPushButton(self.frame_3)
        self.btn_importSave.setObjectName(u"btn_importSave")
        self.btn_importSave.setGeometry(QRect(90, 80, 90, 25))
        self.btn_importOpen = QPushButton(self.frame_3)
        self.btn_importOpen.setObjectName(u"btn_importOpen")
        self.btn_importOpen.setGeometry(QRect(90, 40, 90, 25))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 48, 22))
        self.label_3.setFont(font2)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 171, 16))
        self.lb_load_pfad = QLabel(self.frame_3)
        self.lb_load_pfad.setObjectName(u"lb_load_pfad")
        self.lb_load_pfad.setGeometry(QRect(200, 80, 351, 21))
        self.lb_aktiver_speicherOrt_Name = QLabel(self.frame_3)
        self.lb_aktiver_speicherOrt_Name.setObjectName(u"lb_aktiver_speicherOrt_Name")
        self.lb_aktiver_speicherOrt_Name.setGeometry(QRect(200, 40, 351, 21))
        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(-10, 260, 771, 171))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_65 = QLabel(self.frame_11)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(10, 40, 71, 16))
        self.label_65.setFont(font2)
        self.btn_log_save = QPushButton(self.frame_11)
        self.btn_log_save.setObjectName(u"btn_log_save")
        self.btn_log_save.setGeometry(QRect(100, 40, 90, 25))
        self.label_67 = QLabel(self.frame_11)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(10, 10, 171, 16))
        self.lb_activ_log_name = QLabel(self.frame_11)
        self.lb_activ_log_name.setObjectName(u"lb_activ_log_name")
        self.lb_activ_log_name.setGeometry(QRect(210, 40, 571, 21))
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 130, 771, 131))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 80, 71, 16))
        self.label_6.setFont(font2)
        self.btn_wb2_save = QPushButton(self.frame_4)
        self.btn_wb2_save.setObjectName(u"btn_wb2_save")
        self.btn_wb2_save.setGeometry(QRect(90, 80, 90, 25))
        self.btn_wb2_open = QPushButton(self.frame_4)
        self.btn_wb2_open.setObjectName(u"btn_wb2_open")
        self.btn_wb2_open.setGeometry(QRect(90, 40, 90, 25))
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 40, 48, 22))
        self.label_7.setFont(font2)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 171, 16))
        self.lb_activ_wb2_import = QLabel(self.frame_4)
        self.lb_activ_wb2_import.setObjectName(u"lb_activ_wb2_import")
        self.lb_activ_wb2_import.setGeometry(QRect(200, 40, 571, 21))
        self.lb_activ_wb2_save_2 = QLabel(self.frame_4)
        self.lb_activ_wb2_save_2.setObjectName(u"lb_activ_wb2_save_2")
        self.lb_activ_wb2_save_2.setGeometry(QRect(200, 80, 571, 21))
        self.buttonBox_2 = QDialogButtonBox(self.tab_3)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setGeometry(QRect(350, 490, 156, 24))
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.frame_9 = QFrame(self.tab_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 831, 521))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 0, 581, 451))
        self.frame_12.setFont(font1)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_69 = QLabel(self.frame_12)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(10, 0, 131, 31))
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 40, 571, 411))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.cb_logerzeugen = QCheckBox(self.frame_13)
        self.cb_logerzeugen.setObjectName(u"cb_logerzeugen")
        self.cb_logerzeugen.setGeometry(QRect(10, 10, 171, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.cb_logerzeugen.setFont(font3)
        self.cb_logerzeugen.setChecked(True)
        self.btn_backup_open = QPushButton(self.frame_13)
        self.btn_backup_open.setObjectName(u"btn_backup_open")
        self.btn_backup_open.setGeometry(QRect(10, 90, 90, 25))
        self.btn_backup_open.setFont(font3)
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 40, 291, 51))
        self.lb_activ_backupV = QLabel(self.frame_13)
        self.lb_activ_backupV.setObjectName(u"lb_activ_backupV")
        self.lb_activ_backupV.setGeometry(QRect(130, 90, 441, 21))
        self.lb_activ_backupV.setFont(font3)
        self.buttonBox = QDialogButtonBox(self.frame_9)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(350, 490, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Settings_frm)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Settings_frm)
    # setupUi

    def retranslateUi(self, Settings_frm):
        Settings_frm.setWindowTitle(QCoreApplication.translate("Settings_frm", u"Einstellungen", None))
        self.label_11.setText(QCoreApplication.translate("Settings_frm", u"Spalten Wahl:", None))
        self.label_12.setText(QCoreApplication.translate("Settings_frm", u"Suche UID in: ", None))
        self.label_13.setText(QCoreApplication.translate("Settings_frm", u"Suche Name in:", None))
        self.label_14.setText(QCoreApplication.translate("Settings_frm", u"Anzeige Nr1 in Spalte:", None))
        self.label_15.setText(QCoreApplication.translate("Settings_frm", u"Pr\u00fcfen auf X in den Spalten:", None))
        self.label_16.setText(QCoreApplication.translate("Settings_frm", u"Anzeige Nr3 in Spalte:", None))
        self.label_17.setText(QCoreApplication.translate("Settings_frm", u"Erster Spalten eintrag in:", None))
        self.label_18.setText(QCoreApplication.translate("Settings_frm", u"Pr\u00fcfen auf Ja oder Nein in:", None))
        self.label_19.setText(QCoreApplication.translate("Settings_frm", u"Dropdownmenu f\u00fcr Eintr\u00e4ge", None))
        self.label_20.setText(QCoreApplication.translate("Settings_frm", u"Eintrag A:", None))
        self.label_21.setText(QCoreApplication.translate("Settings_frm", u"Eintrag B:", None))
        self.label_22.setText(QCoreApplication.translate("Settings_frm", u"Dropdownmenu f\u00fcr Eintr\u00e4ge aus 2 Sheet:", None))
        self.label_23.setText(QCoreApplication.translate("Settings_frm", u"Von ", None))
        self.label_24.setText(QCoreApplication.translate("Settings_frm", u"Im 2 Sheet die Spalte:", None))
        self.label_25.setText(QCoreApplication.translate("Settings_frm", u"Bis", None))
        self.label_27.setText(QCoreApplication.translate("Settings_frm", u" Auswahl speichern in:", None))
        self.label_29.setText(QCoreApplication.translate("Settings_frm", u"Dropdownmenu Eintr\u00e4ge speichern in :", None))
        self.label_28.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_activ_UID.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_Name.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_Kostenstelle.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_aktiv_Qartale.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_Alter_Hinweis.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_Notiz.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_Entwickler.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_DD_auswahl1.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_2SBereichAuswahl.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_aktiv_aus_db_save_in.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_2Sheet.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_dmEA_save_in.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_DD_auswahl2.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_aktiv_Sheet2SpalteBereichsAuswahl.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Settings_frm", u"Prim\u00e4r Excel", None))
        self.label_2.setText(QCoreApplication.translate("Settings_frm", u"Einstellungen f\u00fcr die zweite Excel:", None))
        self.cb_uebertragen.setText(QCoreApplication.translate("Settings_frm", u"Automatisches \u00dcbertragen", None))
        self.label_46.setText(QCoreApplication.translate("Settings_frm", u"Suchspalte:", None))
        self.label_47.setText(QCoreApplication.translate("Settings_frm", u"Datum", None))
        self.label_48.setText(QCoreApplication.translate("Settings_frm", u"Name", None))
        self.label_49.setText(QCoreApplication.translate("Settings_frm", u"UID", None))
        self.label_50.setText(QCoreApplication.translate("Settings_frm", u"Eintrag Nr. 4 in Spalte:", None))
        self.label_51.setText(QCoreApplication.translate("Settings_frm", u"Eintrag Nr. 5 in Spalte:", None))
        self.label_52.setText(QCoreApplication.translate("Settings_frm", u"Eintrag Nr. 6 in Spalte:", None))
        self.label_53.setText(QCoreApplication.translate("Settings_frm", u"Eintrag Nr. 7 in Spalte:", None))
        self.label_54.setText(QCoreApplication.translate("Settings_frm", u"Eintrag Nr. 8 in Spalte:", None))
        self.label_55.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_active_suchSpalte.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_datum.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_name.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_uid.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_Eintrag4.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_Eintrag5.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_Eintrag6.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_Eintrag7.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.lb_wb2_activ_Eintrag8.setText(QCoreApplication.translate("Settings_frm", u"Eingestellt ist:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Settings_frm", u"Sekund\u00e4r Excel", None))
        self.label_4.setText(QCoreApplication.translate("Settings_frm", u"Speichern", None))
        self.btn_importSave.setText(QCoreApplication.translate("Settings_frm", u"in", None))
        self.btn_importOpen.setText(QCoreApplication.translate("Settings_frm", u"\u00d6ffnen", None))
        self.label_3.setText(QCoreApplication.translate("Settings_frm", u"Import", None))
        self.label_5.setText(QCoreApplication.translate("Settings_frm", u"Prim\u00e4re Excel Datei", None))
        self.lb_load_pfad.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_aktiver_speicherOrt_Name.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.label_65.setText(QCoreApplication.translate("Settings_frm", u"Speichern", None))
        self.btn_log_save.setText(QCoreApplication.translate("Settings_frm", u"als", None))
        self.label_67.setText(QCoreApplication.translate("Settings_frm", u"LogFile (.txt)", None))
        self.lb_activ_log_name.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Settings_frm", u"Speichern", None))
        self.btn_wb2_save.setText(QCoreApplication.translate("Settings_frm", u"in", None))
        self.btn_wb2_open.setText(QCoreApplication.translate("Settings_frm", u"\u00d6ffnen", None))
        self.label_7.setText(QCoreApplication.translate("Settings_frm", u"Import", None))
        self.label_8.setText(QCoreApplication.translate("Settings_frm", u"Sekund\u00e4re Excel Datei", None))
        self.lb_activ_wb2_import.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.lb_activ_wb2_save_2.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Settings_frm", u"Speicher Optionen", None))
        self.label_69.setText(QCoreApplication.translate("Settings_frm", u"Logfile Optionen:", None))
        self.cb_logerzeugen.setText(QCoreApplication.translate("Settings_frm", u"Logfile erzeugen", None))
        self.btn_backup_open.setText(QCoreApplication.translate("Settings_frm", u"\u00d6ffnen", None))
        self.label_9.setText(QCoreApplication.translate("Settings_frm", u"Verzeichnis f\u00fcr Backup Datein:", None))
        self.lb_activ_backupV.setText(QCoreApplication.translate("Settings_frm", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Settings_frm", u"Backup Optionen", None))
    # retranslateUi

