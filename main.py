import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QLabel, QPushButton
from start import Ui_MainWindow as Ui_Start
from open import Ui_MainWindow as Ui_Open
from create import Ui_MainWindow as Ui_Create
import sqlite3
import pygame
from time import sleep


class Start(QMainWindow, Ui_Start):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createButton.clicked.connect(self.create)
        self.openButton.clicked.connect(self.open)

    def open(self):
        self.ex = Open()
        self.ex.show()

    def create(self):
        self.ex = Create()
        self.ex.show()


class Open(QMainWindow, Ui_Open):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox
        con = sqlite3.connect('records.db')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM recs""").fetchall()
        self.playButton
        self.closeButton
        for elem in result:
            elem = str(elem)
            self.comboBox.addItem(elem)


class Create(QMainWindow, Ui_Create):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modeBox.addItem("Loop")
        self.modeBox.addItem("Usual")
        tunes = ["С", "Cm", "C#", "C#m", "D", "Dm", "D#", "D#m", "E", "Em", "F", "Fm", "F#", "F#m", "G", "Gm", "G#",
                 "G#m", "A", "Am", "A#", "A#m", "B", "Bm", "Random", "Minor", "Major"]
        for elem in tunes:
            self.tuneBox.addItem(elem)
        lenght = self.lenght.text()
        instr = ["Piano", "Guitar", "Brass", "Bass"]
        for elem in instr:
            self.instrBox.addItem(elem)
        self.modeBox.currentIndexChanged.connect(self.click_item)
        self.tuneBox.currentIndexChanged.connect(self.click_item)
        self.instrBox.currentIndexChanged.connect(self.click_item)
        self.nextButton(self.nl)


    def play(self, instr, elem):
        sound = pygame.mixer.Sound(f'sounds/{instr}/{instr}{elem}.wav')
        pygame.mixer.Sound.play(sound)
        if instr == 'Piano':
            sleep(0.3)
        if instr == 'Guitar':
            sleep(0.2)
        if instr == 'Brass':
            sleep(0.25)
        if instr == 'Bass':
            sleep(0.5)

    def nl(self):
        def note_list(tune):
            if tune == 'C':
                notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

            if tune == 'Cm':
                notes = ['C', 'D', 'D#', 'F', 'G', 'G#', 'B']  # Correct

            if tune == 'C#':
                notes = ['C', 'C#', 'D#', 'F', 'F#', 'G#', 'A#']  # Correct

            if tune == 'C#m':
                notes = ['C', 'C#', 'D#', 'E', 'F#', 'G#', 'A']

            if tune == 'D':
                notes = ['C#', 'D', 'E', 'F#', 'G', 'A', 'B']

            if tune == 'Dm':
                notes = ['C#', 'D', 'E', 'F', 'G', 'A', 'A#']

            if tune == 'D#':
                notes = ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']

            if tune == 'D#m':
                notes = ['D', 'D#', 'F', 'F#', 'G#', 'A#', 'B']

            if tune == 'E':
                notes = ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']

            if tune == 'Em':
                notes = ['C', 'D#', 'E', 'F#', 'G', 'A', 'B']

            if tune == 'F':
                notes = ['C', 'D', 'E', 'F', 'G', 'A', 'A#']

            if tune == 'Fm':
                notes = ['C', 'C#', 'E', 'F', 'G', 'G#', 'A#']

            if tune == 'F#':
                notes = ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'B']  # Correct

            if tune == 'F#m':
                notes = ['C#', 'D', 'F', 'F#', 'G#', 'A', 'B']

            if tune == 'G':
                notes = ['C', 'D', 'E', 'F#', 'G', 'A', 'B']

            if tune == 'Gm':
                notes = ['C', 'D', 'D#', 'F#', 'G', 'A', 'A#']

            if tune == 'G#':
                notes = ['C', 'C#', 'D#', 'F', 'G', 'G#', 'A#']

            if tune == 'G#m':
                notes = ['C#', 'D#', 'E', 'G', 'G#', 'A#', 'B']

            if tune == 'A':
                notes = ['C#', 'D', 'E', 'F#', 'G#', 'A', 'B']

            if tune == 'Am':
                notes = ['C', 'D', 'E', 'F', 'G#', 'A', 'B']

            if tune == 'A#':
                notes = ['C', 'D', 'D#', 'F', 'G', 'A', 'A#']

            if tune == 'A#m':
                notes = ['C', 'C#', 'D#', 'F', 'F#', 'A', 'A#']

            if tune == 'B':
                notes = ['C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']

            if tune == 'Bm':
                notes = ['C', 'C#', 'E', 'F', 'G', 'G#', 'A#']  # Correct

            for elem in notes:
                self.play(elem)

    def click_item(self, index):
        tune = self.tuneBox.itemData(index)
        instr = self.instrBox.itemData(index)
        mode = self.modeBox.itemData(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start()
    ex.show()
    sys.exit(app.exec_())
