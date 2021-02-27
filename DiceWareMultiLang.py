# -*- coding: utf-8 -*-
"""
Patta 2021
"""

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import ctypes
import secrets
import os
import pathlib
import webbrowser
# import numpy as np

from DiceWareMainWindow import Ui_MainWindow


# -----------------------------------------------------------------------------
# INITIALISE GUI WITH FOLLOWING CLASS
# -----------------------------------------------------------------------------
class GUIForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GUIForm, self).__init__()
        self.setupUi(self)

        self.pushButton_LoadAdditionalWordList.clicked.connect(self.BrowseWordLists)
        self.pushButton_MakeNewPassPhrase.clicked.connect(self.MakePassPhrase)
        self.pushButton_GoToWebsite.clicked.connect(self.callWebsite)
        
        curFilePath = pathlib.Path().absolute()
        self.WordLists = [os.path.join(curFilePath, "WordLists", "English_WordList.txt"),
                          os.path.join(curFilePath, "WordLists", "French_WordList.txt"),
                          os.path.join(curFilePath, "WordLists", "German_WordList.txt")]

        self.WordListsNames = ['english', 'french', 'german']
        self.WordListsCheckBoxes = [self.checkBox_english,
                                    self.checkBox_french,
                                    self.checkBox_german]
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        
 # setup parameters       
        self.checkBox_english.setChecked(True)
        self.checkBox_french.setChecked(True)
        self.checkBox_german.setChecked(True)
        self.lineEdit_Separator.setText(QtCore.QCoreApplication.translate("DiceWareMultiLang", '_'))
        self.spinBox_WordCount.setValue(7)
        self.spinBox_SpecialCharsToAdd.setValue(6)
        self.spinBox_NumbersToAdd.setValue(5)
        self.spinBox_NumbersToAdd.setValue(2)
        self.checkBox_NumbersToAdd_randomPosition.setChecked(True)
        self.spinBox_SpecialCharsToAdd.setValue(2)
        self.checkBox_SpecialCharsToAdd_randomPosition.setChecked(True)
        
        # to add:
        # 	caps
        #	position scramble
        #	passphrase brute force time to solve estimation
        # 	optimize executables
        
    def randSpecialChar(self):
        specialCharsArr = ['~', '!', '#', '$', '%', '^', '&', '*', '(', ')',
                           '-', '=', '+', '[', ']', '\\', '{', '}', ':', ';',
                           '\"', '\'', '<', '>', '?', '/']
        trandnum = secrets.SystemRandom().randint(0,len(specialCharsArr))
        return specialCharsArr[trandnum]

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
                
        for i in range(self.spinBox_NumbersToAdd.value()):
            trandnum = str(secrets.SystemRandom().randint(0,9))
            if self.checkBox_NumbersToAdd_randomPosition.checkState():
                trandpos = secrets.SystemRandom().randint(0,len(tPassPhrase))
                tPassPhrase = tPassPhrase[:trandpos] + trandnum + tPassPhrase[trandpos:]
            else:
                tPassPhrase = tPassPhrase + trandnum
        
        for i in range(self.spinBox_SpecialCharsToAdd.value()):
            trandChar = self.randSpecialChar()
            if self.checkBox_SpecialCharsToAdd_randomPosition.checkState():
                trandpos = secrets.SystemRandom().randint(0,len(tPassPhrase))
                tPassPhrase = tPassPhrase[:trandpos] + trandChar + tPassPhrase[trandpos:]
            else:
                tPassPhrase = tPassPhrase + trandChar

        tCutLen = len(tSeparator)
        tPassPhrase = tPassPhrase[tCutLen:]
        self.textEdit_PassPhrase.setText(QtCore.QCoreApplication.translate("MainWindow", tPassPhrase))

    def callWebsite(self):
        webbrowser.open('https://theworld.com/~reinhold/diceware.html', new=2)
        

def main():
    app = QtWidgets.QApplication(sys.argv)  
    
    myappid = u'DiceWare MultiLanguage 0.1' # arbitrary string
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)    
    
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
