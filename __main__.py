from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtCore
import sys
from pygame import mixer
from pathlib import Path
import os
from time import sleep
from lib.ui_sound_player import *
from pydub import AudioSegment
#from .lib import *



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, None,  QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        mixer.init()
        self.channel = mixer.Channel(0)

#        self.ui.StartSV.clicked.connect(self.startSV)
#        self.ui.StartENG.clicked.connect(self.startENG)
#        self.ui.BlueFlagSV.clicked.connect(self.blueFlagSV)
#        self.ui.BlueFlagENG.clicked.connect(self.blueFlagENG)
#        self.ui.BothSV.clicked.connect(self.bothSV)
#        self.ui.BothENG.clicked.connect(self.bothENG)
        self.ui.Cancel.clicked.connect(self.stop)
#        self.ui.BothENG_2.clicked.connect(self.bothENG_2)
#        self.ui.BothSV_2.clicked.connect(self.bothSV_2)
#        self.ui.RevENG.clicked.connect(self.backaENG)
#        self.ui.RevSV.clicked.connect(self.backaSV)
#        self.ui.CrashENG.clicked.connect(self.krockaENG)
#        self.ui.CrashSV.clicked.connect(self.krockaSV)
        self.ui.start.clicked.connect(self.start)
        self.ui.eng.clicked.connect(self.language)
        self.ui.crash.clicked.connect(self.krocka)
        self.ui.dropin.clicked.connect(self.dropin)
        self.ui.blueflag.clicked.connect(self.blueFlag)
        self.ui.Final.clicked.connect(self.final)
        self.ui.practice.clicked.connect(self.practice)
        self.ui.prep.clicked.connect(self.prep)
        self.ui.qual.clicked.connect(self.quali)
        self.ui.rev.clicked.connect(self.backa)
        self.ui.sit.clicked.connect(self.sit)
        self.ui.start.clicked.connect(self.start)

        self.btns = [self.ui.blueflag, self.ui.crash, self.ui.prep, self.ui.practice, self.ui.start, self.ui.rev, self.ui.dropin, self.ui.qual, self.ui.Final, self.ui.sit]
        self.paths = ["startSV.wav", "startENG.wav", "blueFlagSV.wav", "blueFlagENG.wav", "backaSV.wav", "backaENG.wav", "krockaSV.wav", "krockaENG.wav",
                        "dropinSV.wav", "dropinENG.wav", "practiceSV.wav", "practiceENG.wav", "kvalSV.wav", "kvalENG.wav", "finalSV.wav", "finalENG.wav", 
                        "preppSV.wav", "preppENG.wav", "testSV.wav", "testENG.wav", "sittSV.wav", "sittENG.wav"]
        self.sv = ["Blåflagg", "Krocka", "Prepp", "Träning", "Start", "Backa", "Körpass", "Kval", "Final", "Sitt ner"]
        self.en = ["Blue flag", "Crash", "Prep", "Practice", "Start", "Reverse", "Drop-in", "Quali.", "Final", "Sit down"]
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

    def checkSounds(self, files):
        for file in files:
            if os.path.isfile(file):
                pass
            else:
                temp = file[0,-3] + "m4a"
                if os.path.isfile(temp):
                    track = AudioSegment.from_file(temp,  format= 'm4a')
                    file_handle = track.export(file, format='wav')



    def getLang(self):
        return self.ui.eng.isChecked()

    def language(self):
        for i in range(len(self.btns)):
            text = ""
            if self.getLang():
                text = self.en[i]
            else:
                text = self.sv[i]
            self.btns[i].setText(text)

    def stop(self):
        self.channel.stop()

    def queue(self, path):
        self.channel.queue(mixer.Sound(self.paths[path]))

    def play(self, path):
        try:
            self.playlist.append(mixer.Sound(self.paths[path]))
            if not self.channel.get_busy():
                self.channel.play(mixer.Sound(self.paths[path]))
            elif self.channel.get_queue() == None:
                self.queue(path)
            else:
                self.fullQueue()
        except:
            print("Shit went sideways ey!")
            try:
                self.play(18)
            except:
                print("Detta var ju inte så bra...")

    def start(self, sv):
        if sv:
            self.startSV()
        else:
            self.startENG()

    def startSV(self):
        self.play(0)

    def startENG(self):
        self.play(1)

    def blueFlag(self, sv):
        if sv:
            self.blueFlagSV()
        else:
            self.blueFlagENG()

    def blueFlagSV(self):
        self.play(2)
        
    def blueFlagENG(self):
        self.play(3)

    def backa(self, sv):
        if sv:
            self.backaSV()
        else:
            self.backaENG()

    def backaSV(self):
        self.play(4)

    def backaENG(self):
        self.play(5)

    def krocka(self, sv):
        if sv:
            self.krockaSV()
        else:
            self.krockaENG()

    def krockaSV(self):
        self.play(6)

    def krockaENG(self):
        self.play(7)

    def dropin(self, sv):
        if sv:
            self.play(8)
        else:
            self.play(9)

    def practice(self, sv):
        if sv:
            self.play(19)
        else:
            self.play(11)

    def quali(self, sv):
        if sv:
            self.play(12)
        else:
            self.play(13)

    def final(self, sv):
        if sv:
            self.play(14)
        else:
            self.play(15)
    
    def prep(self, sv):
        if sv:
            self.play(16)
        else:
            self.play(17)

    def sit(self, sv):
        if sv:
            self.play(20)
        else:
            self.play(21)

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

## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()

