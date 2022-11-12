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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 152)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 431, 91))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.BlueFlagSV = QPushButton(self.gridLayoutWidget)
        self.BlueFlagSV.setObjectName(u"BlueFlagSV")
        font = QFont()
        font.setPointSize(20)
        self.BlueFlagSV.setFont(font)

        self.gridLayout.addWidget(self.BlueFlagSV, 0, 0, 1, 1)

        self.BlueFlagENG = QPushButton(self.gridLayoutWidget)
        self.BlueFlagENG.setObjectName(u"BlueFlagENG")
        self.BlueFlagENG.setFont(font)

        self.gridLayout.addWidget(self.BlueFlagENG, 0, 1, 1, 1)

        self.StartSV = QPushButton(self.gridLayoutWidget)
        self.StartSV.setObjectName(u"StartSV")
        self.StartSV.setFont(font)

        self.gridLayout.addWidget(self.StartSV, 1, 0, 1, 1)

        self.StartENG = QPushButton(self.gridLayoutWidget)
        self.StartENG.setObjectName(u"StartENG")
        self.StartENG.setFont(font)

        self.gridLayout.addWidget(self.StartENG, 1, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(9, 99, 435, 41))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BlueFlagSV.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg", None))
        self.BlueFlagENG.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg ENG", None))
        self.StartSV.setText(QCoreApplication.translate("Form", u"Starta", None))
        self.StartENG.setText(QCoreApplication.translate("Form", u"Starta ENG", None))
        self.label.setText(QCoreApplication.translate("Form", u"V\u00e4nta tills f\u00f6reg\u00e5ende har spelats klart", None))
    # retranslateUi

