from PySide6.QtWidgets import QApplication, QMainWindow
from .sound_player import *
import sys
from playsound import playsound
from pathlib import Path


class MainWindow(QMainWindow):
    """ Main Window

        This object is the main window and the center of everything. This is the thing it is run first.
    """

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.sound_startSV = str(Path('sound-player\\sounds\\startSV.wav'))

        self.ui.StartSV.clicked.connect(self.startSV)

        self.show()

    def startSV(self):
        #print(self.sound_startSV)
        playsound(self.sound_startSV)

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

## EXECUTE APP
if __name__ == "__main__":
    main()

