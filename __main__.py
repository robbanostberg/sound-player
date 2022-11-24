from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtCore
import sys
from pygame import mixer
from pathlib import Path
import os
from time import sleep
from lib.ui_sound_player import *
#from .lib import *



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, None,  QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        mixer.init()
        self.channel = mixer.Channel(0)

        self.ui.StartSV.clicked.connect(self.startSV)
        self.ui.StartENG.clicked.connect(self.startENG)
        self.ui.BlueFlagSV.clicked.connect(self.blueFlagSV)
        self.ui.BlueFlagENG.clicked.connect(self.blueFlagENG)
        self.ui.BothSV.clicked.connect(self.bothSV)
        self.ui.BothENG.clicked.connect(self.bothENG)
        self.ui.Cancel.clicked.connect(self.stop)

        self.paths = ["startSV.wav", "startENG.wav", "blueFlagSV.wav", "blueFlagENG.wav"]
        self.playlist = []

        self.vscode = not True

        if not self.vscode:
            self.longpath = ''
        else:
            self.longpath = 'sound-player\\'
        
        for i in range(len(self.paths)):
            self.paths[i] = str(Path(self.longpath + 'lib\\' + self.paths[i]))

        if getattr(sys, 'frozen', False):
            for i in range(len(self.paths)): 
                self.paths[i] = os.path.join(sys._MEIPASS, self.paths[i])

        

        self.show()

    def stop(self):
        self.channel.stop()

    def queue(self, path):
        self.channel.queue(mixer.Sound(self.paths[path]))

    def play(self, path):
        self.playlist.append(mixer.Sound(self.paths[path]))
        if not self.channel.get_busy():
            self.channel.play(mixer.Sound(self.paths[path]))
        elif self.channel.get_queue() == None:
            self.queue(path)
        else:
            self.fullQueue() 

    def startSV(self):
        self.play(0)

    def startENG(self):
        self.play(1)

    def blueFlagSV(self):
        self.play(2)
        
    def blueFlagENG(self):
        self.play(3)
    
    def bothSV(self):
        self.play(0)
        self.queue(2)

    def bothENG(self):
        self.play(1)
        self.queue(3)  

    def fullQueue(self):
        icon = QMessageBox.warning
        title = "Kön är full"
        destruct = 5
        text = "Det går bara att lägga ett ljud i kö, vänta tills det första ljudet spelats klart"#.\n\n Jag försvinner automatiskt efter " + str(destruct) + " sekunder"
        buttons = QMessageBox.Ok
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec()
        

    def next(self):
        print('next!')

## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()

