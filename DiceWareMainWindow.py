# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiceWareMainWindow_v02.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(281, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_LanguagesCheckBoxes = QtWidgets.QVBoxLayout()
        self.verticalLayout_LanguagesCheckBoxes.setObjectName("verticalLayout_LanguagesCheckBoxes")
        self.checkBox_english = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_english.setObjectName("checkBox_english")
        self.verticalLayout_LanguagesCheckBoxes.addWidget(self.checkBox_english)
        self.checkBox_french = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_french.setObjectName("checkBox_french")
        self.verticalLayout_LanguagesCheckBoxes.addWidget(self.checkBox_french)
        self.checkBox_german = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_german.setObjectName("checkBox_german")
        self.verticalLayout_LanguagesCheckBoxes.addWidget(self.checkBox_german)
        self.verticalLayout.addLayout(self.verticalLayout_LanguagesCheckBoxes)
        self.pushButton_LoadAdditionalWordList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LoadAdditionalWordList.setObjectName("pushButton_LoadAdditionalWordList")
        self.verticalLayout.addWidget(self.pushButton_LoadAdditionalWordList)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_WordCount = QtWidgets.QLabel(self.centralwidget)
        self.label_WordCount.setObjectName("label_WordCount")
        self.horizontalLayout_2.addWidget(self.label_WordCount)
        self.spinBox_WordCount = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_WordCount.setObjectName("spinBox_WordCount")
        self.horizontalLayout_2.addWidget(self.spinBox_WordCount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Separator = QtWidgets.QLabel(self.centralwidget)
        self.label_Separator.setObjectName("label_Separator")
        self.horizontalLayout.addWidget(self.label_Separator)
        self.lineEdit_Separator = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Separator.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_Separator.setObjectName("lineEdit_Separator")
        self.horizontalLayout.addWidget(self.lineEdit_Separator)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_NumbersToAdd = QtWidgets.QLabel(self.centralwidget)
        self.label_NumbersToAdd.setObjectName("label_NumbersToAdd")
        self.horizontalLayout_3.addWidget(self.label_NumbersToAdd)
        self.spinBox_NumbersToAdd = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_NumbersToAdd.setObjectName("spinBox_NumbersToAdd")
        self.horizontalLayout_3.addWidget(self.spinBox_NumbersToAdd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.checkBox_NumbersToAdd_randomPosition = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_NumbersToAdd_randomPosition.setObjectName("checkBox_NumbersToAdd_randomPosition")
        self.horizontalLayout_5.addWidget(self.checkBox_NumbersToAdd_randomPosition)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_SpecialCharsToAdd = QtWidgets.QLabel(self.centralwidget)
        self.label_SpecialCharsToAdd.setObjectName("label_SpecialCharsToAdd")
        self.horizontalLayout_4.addWidget(self.label_SpecialCharsToAdd)
        self.spinBox_SpecialCharsToAdd = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_SpecialCharsToAdd.setObjectName("spinBox_SpecialCharsToAdd")
        self.horizontalLayout_4.addWidget(self.spinBox_SpecialCharsToAdd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.checkBox_SpecialCharsToAdd_randomPosition = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_SpecialCharsToAdd_randomPosition.setObjectName("checkBox_SpecialCharsToAdd_randomPosition")
        self.horizontalLayout_6.addWidget(self.checkBox_SpecialCharsToAdd_randomPosition)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_MakeNewPassPhrase = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_MakeNewPassPhrase.setObjectName("pushButton_MakeNewPassPhrase")
        self.verticalLayout_4.addWidget(self.pushButton_MakeNewPassPhrase)
        self.textEdit_PassPhrase = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_PassPhrase.setObjectName("textEdit_PassPhrase")
        self.verticalLayout_4.addWidget(self.textEdit_PassPhrase)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_GoToWebsite = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GoToWebsite.setObjectName("pushButton_GoToWebsite")
        self.verticalLayout.addWidget(self.pushButton_GoToWebsite)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>This tools lets you select multiple word lists to generate you password.</p><p>During the calculation, all lists are equally likely to be selected. The choice of words grows with each list by a factor of 7776.</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Select Word Lists to include in Pass Phrase:"))
        self.checkBox_english.setText(_translate("MainWindow", "english"))
        self.checkBox_french.setText(_translate("MainWindow", "french"))
        self.checkBox_german.setText(_translate("MainWindow", "german"))
        self.pushButton_LoadAdditionalWordList.setToolTip(_translate("MainWindow", "<html><head/><body><p>Load additional word lists in you own language. The files must be .txt files, with the dice numbers (ID) as the first column and the words as the second column, seperated by tabs, spaces, or commas. </p></body></html>"))
        self.pushButton_LoadAdditionalWordList.setText(_translate("MainWindow", "Load additional Word List"))
        self.label_WordCount.setToolTip(_translate("MainWindow", "<html><head/><body><p>A minimum of six (6) words is suggested for security reasons.<br/>Selecting a longer pass phrase improves the security of you new pass phrase exponentially!</p></body></html>"))
        self.label_WordCount.setText(_translate("MainWindow", "Word count for Pass Phrase"))
        self.spinBox_WordCount.setToolTip(_translate("MainWindow", "<html><head/><body><p>A minimum of six (6) words is suggested for security reasons.<br/>Selecting a longer pass phrase improves the security of you new pass phrase exponentially!</p></body></html>"))
        self.label_Separator.setText(_translate("MainWindow", "Seperator between single words:"))
        self.label_NumbersToAdd.setToolTip(_translate("MainWindow", "<html><head/><body><p>Some website or login services require a password that includes at least one number or special character.</p></body></html>"))
        self.label_NumbersToAdd.setText(_translate("MainWindow", "Amount of Numbers to add"))
        self.spinBox_NumbersToAdd.setToolTip(_translate("MainWindow", "<html><head/><body><p>Some website or login services require a password that includes at least one number or special character.</p></body></html>"))
        self.checkBox_NumbersToAdd_randomPosition.setToolTip(_translate("MainWindow", "<html><head/><body><p>Checking this box puts the numbers at random positions of you pass phrase.</p></body></html>"))
        self.checkBox_NumbersToAdd_randomPosition.setText(_translate("MainWindow", "at random position"))
        self.label_SpecialCharsToAdd.setToolTip(_translate("MainWindow", "<html><head/><body><p>Some website or login services require a password that includes at least one number or special character.</p></body></html>"))
        self.label_SpecialCharsToAdd.setText(_translate("MainWindow", "Amount of Special Characters to add"))
        self.spinBox_SpecialCharsToAdd.setToolTip(_translate("MainWindow", "<html><head/><body><p>Some website or login services require a password that includes at least one number or special character.</p></body></html>"))
        self.checkBox_SpecialCharsToAdd_randomPosition.setToolTip(_translate("MainWindow", "<html><head/><body><p>Checking this box puts the special characters at random positions of you pass phrase.</p></body></html>"))
        self.checkBox_SpecialCharsToAdd_randomPosition.setText(_translate("MainWindow", "at random position"))
        self.pushButton_MakeNewPassPhrase.setToolTip(_translate("MainWindow", "<html><head/><body><p>All pass phrases are unique. Clicking this button will generate a new truely random pass phrase.</p></body></html>"))
        self.pushButton_MakeNewPassPhrase.setText(_translate("MainWindow", "Make new Pass Phrase"))
        self.label_3.setText(_translate("MainWindow", "Estimated time to crack\n"
"with a super computer:"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>This estimate follows maths of the the online java-based Diceware pass phrase calculator, https://www.rempe.us/diceware/#eff</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "x years"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Learn more about DiceWare:"))
        self.pushButton_GoToWebsite.setToolTip(_translate("MainWindow", "<html><head/><body><p>This button opens a new tab on your webbrowser and goes to the original Diceware page, created by Arnold G. Reinhold: https://theworld.com/~reinhold/diceware.html</p></body></html>"))
        self.pushButton_GoToWebsite.setText(_translate("MainWindow", "Go to Website"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
