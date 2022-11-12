# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sound-player.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 381, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.BlueFlagSV = QPushButton(self.gridLayoutWidget)
        self.BlueFlagSV.setObjectName(u"BlueFlagSV")

        self.gridLayout.addWidget(self.BlueFlagSV, 0, 0, 1, 1)

        self.BlueFlagENG = QPushButton(self.gridLayoutWidget)
        self.BlueFlagENG.setObjectName(u"BlueFlagENG")

        self.gridLayout.addWidget(self.BlueFlagENG, 0, 1, 1, 1)

        self.StartSV = QPushButton(self.gridLayoutWidget)
        self.StartSV.setObjectName(u"StartSV")

        self.gridLayout.addWidget(self.StartSV, 1, 0, 1, 1)

        self.StartENG = QPushButton(self.gridLayoutWidget)
        self.StartENG.setObjectName(u"StartENG")

        self.gridLayout.addWidget(self.StartENG, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BlueFlagSV.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg", None))
        self.BlueFlagENG.setText(QCoreApplication.translate("Form", u"Bl\u00e5flagg ENG", None))
        self.StartSV.setText(QCoreApplication.translate("Form", u"Starta", None))
        self.StartENG.setText(QCoreApplication.translate("Form", u"Starta ENG", None))
    # retranslateUi

