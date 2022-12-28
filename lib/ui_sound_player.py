# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sound_player.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(478, 176)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);")
        self.gridLayoutWidget_3 = QWidget(Form)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 3, 461, 131))
        self.someOtherLayout = QGridLayout(self.gridLayoutWidget_3)
        self.someOtherLayout.setObjectName(u"someOtherLayout")
        self.someOtherLayout.setContentsMargins(0, 0, 0, 0)
        self.btnLayout = QGridLayout()
        self.btnLayout.setObjectName(u"btnLayout")
        self.rev = QPushButton(self.gridLayoutWidget_3)
        self.rev.setObjectName(u"rev")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.rev.setFont(font)

        self.btnLayout.addWidget(self.rev, 1, 1, 1, 1)

        self.crash = QPushButton(self.gridLayoutWidget_3)
        self.crash.setObjectName(u"crash")
        self.crash.setFont(font)

        self.btnLayout.addWidget(self.crash, 0, 1, 1, 1)

        self.aa = QPushButton(self.gridLayoutWidget_3)
        self.aa.setObjectName(u"aa")
        self.aa.setEnabled(False)
        self.aa.setFont(font)

        self.btnLayout.addWidget(self.aa, 2, 1, 1, 1)

        self.start = QPushButton(self.gridLayoutWidget_3)
        self.start.setObjectName(u"start")
        self.start.setFont(font)

        self.btnLayout.addWidget(self.start, 1, 0, 1, 1)

        self.dropin = QPushButton(self.gridLayoutWidget_3)
        self.dropin.setObjectName(u"dropin")
        self.dropin.setMinimumSize(QSize(0, 33))
        self.dropin.setFont(font)

        self.btnLayout.addWidget(self.dropin, 1, 2, 1, 1)

        self.eng = QPushButton(self.gridLayoutWidget_3)
        self.eng.setObjectName(u"eng")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.eng.setFont(font1)
        self.eng.setCheckable(True)

        self.btnLayout.addWidget(self.eng, 2, 0, 1, 1)

        self.blueflag = QPushButton(self.gridLayoutWidget_3)
        self.blueflag.setObjectName(u"blueflag")
        self.blueflag.setFont(font)

        self.btnLayout.addWidget(self.blueflag, 0, 0, 1, 1)

        self.prep = QPushButton(self.gridLayoutWidget_3)
        self.prep.setObjectName(u"prep")
        self.prep.setFont(font)

        self.btnLayout.addWidget(self.prep, 0, 2, 1, 1)

        self.sit = QPushButton(self.gridLayoutWidget_3)
        self.sit.setObjectName(u"sit")
        self.sit.setEnabled(True)
        self.sit.setFont(font)

        self.btnLayout.addWidget(self.sit, 2, 2, 1, 1)

        self.Final = QPushButton(self.gridLayoutWidget_3)
        self.Final.setObjectName(u"Final")
        self.Final.setFont(font)

        self.btnLayout.addWidget(self.Final, 2, 3, 1, 1)

        self.qual = QPushButton(self.gridLayoutWidget_3)
        self.qual.setObjectName(u"qual")
        self.qual.setFont(font)

        self.btnLayout.addWidget(self.qual, 1, 3, 1, 1)

        self.practice = QPushButton(self.gridLayoutWidget_3)
        self.practice.setObjectName(u"practice")
        self.practice.setFont(font)

        self.btnLayout.addWidget(self.practice, 0, 3, 1, 1)


        self.someOtherLayout.addLayout(self.btnLayout, 0, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 130, 461, 51))
        self.StopLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.StopLayout.setObjectName(u"StopLayout")
        self.StopLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StopLayout.addItem(self.horizontalSpacer)

        self.Cancel = QPushButton(self.horizontalLayoutWidget)
        self.Cancel.setObjectName(u"Cancel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Cancel.sizePolicy().hasHeightForWidth())
        self.Cancel.setSizePolicy(sizePolicy1)
        self.Cancel.setFont(font)

        self.StopLayout.addWidget(self.Cancel)

        self.horizontalSpacer_2 = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StopLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Sound Player", None))
        self.rev.setText(QCoreApplication.translate("Form", u"Backa", None))
        self.crash.setText(QCoreApplication.translate("Form", u"Krocka", None))
        self.aa.setText(QCoreApplication.translate("Form", u"?", None))
        self.start.setText(QCoreApplication.translate("Form", u"Starta", None))
        self.dropin.setText(QCoreApplication.translate("Form", u"K\u00f6rpass", None))
        self.eng.setText(QCoreApplication.translate("Form", u"Engelska", None))
        self.blueflag.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg", None))
        self.prep.setText(QCoreApplication.translate("Form", u"Prepp", None))
        self.sit.setText(QCoreApplication.translate("Form", u"Sitt ner", None))
        self.Final.setText(QCoreApplication.translate("Form", u"Final", None))
        self.qual.setText(QCoreApplication.translate("Form", u"Kval", None))
        self.practice.setText(QCoreApplication.translate("Form", u"Tr\u00e4ning", None))
        self.Cancel.setText(QCoreApplication.translate("Form", u"Stopp", None))
    # retranslateUi

