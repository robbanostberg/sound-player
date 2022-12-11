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
        Form.resize(668, 176)
        self.gridLayoutWidget_3 = QWidget(Form)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 3, 651, 131))
        self.someOtherLayout = QGridLayout(self.gridLayoutWidget_3)
        self.someOtherLayout.setObjectName(u"someOtherLayout")
        self.someOtherLayout.setContentsMargins(0, 0, 0, 0)
        self.btnLayout = QGridLayout()
        self.btnLayout.setObjectName(u"btnLayout")
        self.RevSV = QPushButton(self.gridLayoutWidget_3)
        self.RevSV.setObjectName(u"RevSV")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.RevSV.setFont(font)

        self.btnLayout.addWidget(self.RevSV, 1, 1, 1, 1)

        self.CrashSV = QPushButton(self.gridLayoutWidget_3)
        self.CrashSV.setObjectName(u"CrashSV")
        self.CrashSV.setFont(font)

        self.btnLayout.addWidget(self.CrashSV, 0, 1, 1, 1)

        self.BothSV_2 = QPushButton(self.gridLayoutWidget_3)
        self.BothSV_2.setObjectName(u"BothSV_2")
        self.BothSV_2.setFont(font)

        self.btnLayout.addWidget(self.BothSV_2, 2, 1, 1, 1)

        self.StartSV = QPushButton(self.gridLayoutWidget_3)
        self.StartSV.setObjectName(u"StartSV")
        self.StartSV.setFont(font)

        self.btnLayout.addWidget(self.StartSV, 1, 0, 1, 1)

        self.StartENG = QPushButton(self.gridLayoutWidget_3)
        self.StartENG.setObjectName(u"StartENG")
        self.StartENG.setFont(font)

        self.btnLayout.addWidget(self.StartENG, 1, 2, 1, 1)

        self.BothSV = QPushButton(self.gridLayoutWidget_3)
        self.BothSV.setObjectName(u"BothSV")
        self.BothSV.setFont(font)

        self.btnLayout.addWidget(self.BothSV, 2, 0, 1, 1)

        self.BlueFlagSV = QPushButton(self.gridLayoutWidget_3)
        self.BlueFlagSV.setObjectName(u"BlueFlagSV")
        self.BlueFlagSV.setFont(font)

        self.btnLayout.addWidget(self.BlueFlagSV, 0, 0, 1, 1)

        self.BlueFlagENG = QPushButton(self.gridLayoutWidget_3)
        self.BlueFlagENG.setObjectName(u"BlueFlagENG")
        self.BlueFlagENG.setFont(font)

        self.btnLayout.addWidget(self.BlueFlagENG, 0, 2, 1, 1)

        self.BothENG = QPushButton(self.gridLayoutWidget_3)
        self.BothENG.setObjectName(u"BothENG")
        self.BothENG.setFont(font)

        self.btnLayout.addWidget(self.BothENG, 2, 2, 1, 1)

        self.BothENG_2 = QPushButton(self.gridLayoutWidget_3)
        self.BothENG_2.setObjectName(u"BothENG_2")
        self.BothENG_2.setFont(font)

        self.btnLayout.addWidget(self.BothENG_2, 2, 3, 1, 1)

        self.RevENG = QPushButton(self.gridLayoutWidget_3)
        self.RevENG.setObjectName(u"RevENG")
        self.RevENG.setFont(font)

        self.btnLayout.addWidget(self.RevENG, 1, 3, 1, 1)

        self.CrashENG = QPushButton(self.gridLayoutWidget_3)
        self.CrashENG.setObjectName(u"CrashENG")
        self.CrashENG.setFont(font)

        self.btnLayout.addWidget(self.CrashENG, 0, 3, 1, 1)


        self.someOtherLayout.addLayout(self.btnLayout, 0, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 130, 651, 51))
        self.StopLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.StopLayout.setObjectName(u"StopLayout")
        self.StopLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StopLayout.addItem(self.horizontalSpacer)

        self.Cancel = QPushButton(self.horizontalLayoutWidget)
        self.Cancel.setObjectName(u"Cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel.sizePolicy().hasHeightForWidth())
        self.Cancel.setSizePolicy(sizePolicy)
        self.Cancel.setFont(font)

        self.StopLayout.addWidget(self.Cancel)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StopLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Sound Player", None))
        self.RevSV.setText(QCoreApplication.translate("Form", u"Backa", None))
        self.CrashSV.setText(QCoreApplication.translate("Form", u"Krocka", None))
        self.BothSV_2.setText(QCoreApplication.translate("Form", u"B\u00e5da", None))
        self.StartSV.setText(QCoreApplication.translate("Form", u"Starta", None))
        self.StartENG.setText(QCoreApplication.translate("Form", u"Starta ENG", None))
        self.BothSV.setText(QCoreApplication.translate("Form", u"B\u00e5da", None))
        self.BlueFlagSV.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg", None))
        self.BlueFlagENG.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg ENG", None))
        self.BothENG.setText(QCoreApplication.translate("Form", u"B\u00e5da ENG", None))
        self.BothENG_2.setText(QCoreApplication.translate("Form", u"B\u00e5da ENG", None))
        self.RevENG.setText(QCoreApplication.translate("Form", u"Backa ENG", None))
        self.CrashENG.setText(QCoreApplication.translate("Form", u"Krocka ENG", None))
        self.Cancel.setText(QCoreApplication.translate("Form", u"Stopp", None))
    # retranslateUi

