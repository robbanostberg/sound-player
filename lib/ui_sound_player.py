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
        Form.resize(550, 222)
        self.gridLayoutWidget_3 = QWidget(Form)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 9, 531, 145))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BlueFlagSV = QPushButton(self.gridLayoutWidget_3)
        self.BlueFlagSV.setObjectName(u"BlueFlagSV")
        font = QFont()
        font.setPointSize(20)
        self.BlueFlagSV.setFont(font)

        self.gridLayout.addWidget(self.BlueFlagSV, 0, 0, 1, 1)

        self.BlueFlagENG = QPushButton(self.gridLayoutWidget_3)
        self.BlueFlagENG.setObjectName(u"BlueFlagENG")
        self.BlueFlagENG.setFont(font)

        self.gridLayout.addWidget(self.BlueFlagENG, 0, 1, 1, 1)

        self.StartENG = QPushButton(self.gridLayoutWidget_3)
        self.StartENG.setObjectName(u"StartENG")
        self.StartENG.setFont(font)

        self.gridLayout.addWidget(self.StartENG, 1, 1, 1, 1)

        self.StartSV = QPushButton(self.gridLayoutWidget_3)
        self.StartSV.setObjectName(u"StartSV")
        self.StartSV.setFont(font)

        self.gridLayout.addWidget(self.StartSV, 1, 0, 1, 1)

        self.BothSV = QPushButton(self.gridLayoutWidget_3)
        self.BothSV.setObjectName(u"BothSV")
        self.BothSV.setFont(font)

        self.gridLayout.addWidget(self.BothSV, 2, 0, 1, 1)

        self.BothENG = QPushButton(self.gridLayoutWidget_3)
        self.BothENG.setObjectName(u"BothENG")
        self.BothENG.setFont(font)

        self.gridLayout.addWidget(self.BothENG, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 170, 531, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Cancel = QPushButton(self.horizontalLayoutWidget)
        self.Cancel.setObjectName(u"Cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel.sizePolicy().hasHeightForWidth())
        self.Cancel.setSizePolicy(sizePolicy)
        self.Cancel.setFont(font)

        self.horizontalLayout.addWidget(self.Cancel)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Sound Player", None))
        self.BlueFlagSV.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg", None))
        self.BlueFlagENG.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg ENG", None))
        self.StartENG.setText(QCoreApplication.translate("Form", u"Starta ENG", None))
        self.StartSV.setText(QCoreApplication.translate("Form", u"Starta", None))
        self.BothSV.setText(QCoreApplication.translate("Form", u"B\u00e5da", None))
        self.BothENG.setText(QCoreApplication.translate("Form", u"B\u00e5da ENG", None))
        self.Cancel.setText(QCoreApplication.translate("Form", u"Stopp", None))
    # retranslateUi

