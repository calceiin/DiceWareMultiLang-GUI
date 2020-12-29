# -*- coding: utf-8 -*-
"""
Patta 2021
"""

from PyQt5 import QtWidgets, QtGui, uic, QtCore
import sys
import ctypes
import secrets

import numpy as np

from DiceWareMainWindow_py_v01 import Ui_MainWindow
from DiceWareProg_Functions import *


# -----------------------------------------------------------------------------
# INITIALISE GUI WITH FOLLOWING CLASS
# -----------------------------------------------------------------------------
class GUIForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GUIForm, self).__init__()
        self.setupUi(self)
        
        # QtGui.QWidget.__init__(self)
        # self.setupUi(self)
        
        self.pushButton_LoadAdditionalWordList.clicked.connect(self.BrowseWordLists)
        self.pushButton_MakeNewPassPhrase.clicked.connect(self.MakePassPhrase)
        
        self.WordLists = [u'.\WordLists\English_WordList.txt',
                          u'.\WordLists\French_WordList.txt',
                          u'.\WordLists\German_WordList.txt']
        self.WordListsNames = ['english', 'french', 'german']
        self.WordListsCheckBoxes = [self.checkBox_english,
                                    self.checkBox_french,
                                    self.checkBox_german]
        
 # setup parameters       
        self.checkBox_english.setChecked(True)
        self.checkBox_french.setChecked(True)
        self.checkBox_german.setChecked(True)
        self.lineEdit_Separator.setText(QtCore.QCoreApplication.translate("MainWindow", '_'))
        self.spinBox_WordCount.setValue(7)
        self.spinBox_SpecialCharsToAdd.setValue(6)
        self.spinBox_NumbersToAdd.setValue(5)
        # add whereever
        # caps?
        

    def BrowseWordLists(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Select Word Lists to Include')
        dialog.setNameFilter('Word Lists (*.txt *.csv)')
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            tFnames = str(dialog.selectedFiles()[0])
            self.WordLists.append(tFnames)   #make this play nice
            tname = tFnames.split('/')           
            tLname = tname[-1].split('.')[-2]
            self.WordListsNames.append(tLname)
            tcheckBox = QtWidgets.QCheckBox(self.centralwidget)
            tcheckBox.setObjectName("checkBox_" + tLname)
            self.WordListsCheckBoxes.append(tcheckBox)
            self.verticalLayout_LanguagesCheckBoxes.addWidget(tcheckBox) 
            self.WordListsCheckBoxes[-1].setText(QtCore.QCoreApplication.translate("MainWindow", tLname))
        else:
            return None     

    def MakePassPhrase(self):
        tListCount = 0
        tListsToUse = []
        i = 0
        for tlist in self.WordListsCheckBoxes:
            if tlist.isChecked():
                tListCount += 1
                tListsToUse.append(self.WordLists[i])
            i += 1
        
        tWordCount = self.spinBox_WordCount.value()
        tSeparator = self.lineEdit_Separator.text()
        
        tPassPhrase = ''
        
        for j in range(tWordCount):
            tRandWordIndex = secrets.SystemRandom().randint(0,7775)
            tWordList = ''
            if tListCount > 1:
                tRandListIndex = secrets.SystemRandom().randint(0,tListCount-1)
                tWordList = tListsToUse[tRandListIndex]
            else:
                tWordList = tListsToUse[0]
            with open(tWordList, 'r') as rWordList:
                tlines = rWordList.readlines()
                tWord = tlines[tRandWordIndex]
                _, tWord = tWord.split()
                tPassPhrase += tSeparator + tWord
        
        
# add other options, like chars and numbers, maybe also add Caps Option
        
        

        tCutLen = len(tSeparator)
        tPassPhrase = tPassPhrase[tCutLen:]
        self.textEdit_PassPhrase.setText(QtCore.QCoreApplication.translate("MainWindow", tPassPhrase))


    
    
def main():
    app = QtWidgets.QApplication(sys.argv)  
    
    myappid = u'DiceWare MultiLanguage 0.1' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)    
    
    myapp = GUIForm()
    myapp.show()


    a = app.exec_() 
    tmp_str = 'System exit: ' + str(a)
    print(tmp_str)
    
    
# -----------------------------------------------------------------------------
# CODE FOR MAIN
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()