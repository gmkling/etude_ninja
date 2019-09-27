# add_composition.py
# Gather data for a composition
# its notation file
# and add to the database
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from db.sodb import Sodb, sodb_sf_data, sodb_recordings, sodb_notes, sodb_music, sodb_annotations
import datetime
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox

# Qt5 connection
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
from PyQt5.QtCore import pyqtSlot

today = datetime.date.today()

class CompositionWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title='Add Composition to Dataset'
        self.sodb_var = Sodb()

        # Text widgets
        self.titleEdit=QLineEdit()
        self.composerEdit=QLineEdit()
        self.opusEdit=QLineEdit()
        self.dateEdit=QLineEdit()
        self.notationEdit=QLineEdit()

        # the form
        self.formGroupBox = QGroupBox("Form layout")
        self.formLayout=QFormLayout()
        self.formLayout.addRow('Title: ', self.titleEdit)
        self.formLayout.addRow('Composer: ', self.composerEdit)
        self.formLayout.addRow('Opus Number: ', self.opusEdit)
        self.formLayout.addRow('Date: ', self.dateEdit)
        self.formLayout.addRow('Notation Filename: ', self.notationEdit)
        self.formGroupBox.setLayout(self.formLayout)

        # buttons for the form
        self.createButton=QPushButton('Create', self)
        self.resetButton=QPushButton('Reset', self)
        self.quitButton=QPushButton('Quit', self)

        self.buttonBox=QDialogButtonBox()
        self.buttonBox.addButton(self.createButton, QDialogButtonBox.ApplyRole)
        self.buttonBox.addButton(self.resetButton, QDialogButtonBox.ResetRole)
        self.buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)

        self.createButton.clicked.connect(self.accept)
        self.resetButton.clicked.connect(self.reset)
        self.quitButton.clicked.connect(self.reject)

        self.mainLayout=QVBoxLayout()
        self.mainLayout.addWidget(self.formGroupBox)
        self.mainLayout.addWidget(self.buttonBox)

        self.setWindowTitle(self.title)
        self.setLayout(self.mainLayout)
        self.show()

        self.comp_db = sodb_music(composer="Kopprasch",
                                title="Etude 10",
                                opus_num=16,
                                date=today,
                                notation_filename='honk_that_horn.txt ',
                                instrumentation=None)
    @pyqtSlot()
    def accept(self):
        # gather data and submit
        # add data type testing or you will dump core
        self.comp_db.composer=self.composerEdit.text()
        self.comp_db.title=self.titleEdit.text()
        self.comp_db.opus_num=self.opusEdit.text()
        self.comp_db.theDate=self.dateEdit.text()
        self.comp_db.notation_filename=self.notationEdit.text()

        # push it to DB
        self.sodb_var.add_object(self.comp_db)
        self.sodb_var.commit_changes()
        print('Accept action')

    @pyqtSlot()
    def reset(self):
        # clear fields and db objects
        self.titleEdit.clear()
        self.composerEdit.clear()
        self.opusEdit.clear()
        self.dateEdit.clear()
        self.notationEdit.clear()
        print('Reset action')

    @pyqtSlot()
    def reject(self):
        # cancel/close/quit
        # this version is rather rude

        # delete DB connection!
        QApplication.quit()
        print('Reject action')
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testWin = CompositionWindow()
    testWin.show()

    sys.exit(app.exec_())
