from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from playsound import playsound
from pathlib import Path
import os
from time import sleep

here = str(os.path.abspath(__file__))[:-11]

from lib.ui_sound_player import *
from lib import *


class MainWindow(QMainWindow):
    """ Main Window

        This object is the main window and the center of everything. This is the thing it is run first.
    """

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if getattr(sys, 'frozen', False):
            self.sound_startSV = os.path.join(sys._MEIPASS, "lib\startSV.wav")
            self.sound_startENG = os.path.join(sys._MEIPASS, "lib\startENG.wav")
            self.sound_blueFlagSV = os.path.join(sys._MEIPASS, r"lib\blueFlagSV.wav")
            self.sound_blueFlagENG = os.path.join(sys._MEIPASS, r"lib\blueFlagENG.wav")
        else:
            self.sound_startSV = "lib\startSV.wav"
            self.sound_startENG = "lib\startSV.wav"
            self.sound_blueFlagSV = r"lib\startSV.wav"
            self.sound_blueFlagENG = r"lib\startENG.wav"

        self.sound_startSV = here + str(Path('lib\\startSV.wav'))
        self.sound_startENG = here + str(Path('lib\\startENG.wav'))
        self.sound_blueFlagSV = here + str(Path('lib\\blueFlagSV.wav'))
        self.sound_blueFlagENG = here + str(Path('lib\\blueFlagENG.wav'))

        self.ui.StartSV.clicked.connect(self.startSV)
        self.ui.StartENG.clicked.connect(self.startENG)
        self.ui.BlueFlagSV.clicked.connect(self.blueFlagSV)
        self.ui.BlueFlagENG.clicked.connect(self.blueFlagENG)

        self.show()

    def startSV(self):
        playsound(self.sound_startSV)

    def startENG(self):
        playsound(self.sound_startENG)

    def blueFlagSV(self):
        playsound(self.sound_blueFlagSV)
        
    def blueFlagENG(self):
        playsound(self.sound_blueFlagENG)

## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
    while 1:
        sleep(1)

