"""                                                                     

 ________  ________  ________   ___  __            ________  ________  ________        ___  _______   ________ _________   
|\   __  \|\   __  \|\   ___  \|\  \|\  \         |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\ 
\ \  \|\ /\ \  \|\  \ \  \\ \  \ \  \/  /|_       \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_| 
 \ \   __  \ \   __  \ \  \\ \  \ \   ___  \       \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \  
  \ \  \|\  \ \  \ \  \ \  \\ \  \ \  \\ \  \       \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \ 
   \ \_______\ \__\ \__\ \__\\ \__\ \__\\ \__\       \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\
    \|_______|\|__|\|__|\|__| \|__|\|__| \|__|        \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|
                                                                                                                           
By Rasphy: https://github.com/Rasphy2009/Bank-Project
V 4.2

""" 

# For encrypt/ decrypt  
import base64

def encrypt(variable):
    global encrypted
    encrypted = variable.encode("utf-8")
    return encrypted

# Sys for opening windows
import sys

# Import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QCloseEvent, QGuiApplication, QIcon, QPixmap

# Os for path
import os

# Re to check the special characters
import re

# Datetime for the date
from datetime import datetime
from datetime import date

# Time for time
import time

# Path
filePath = os.path.dirname(os.path.realpath(__file__))
path1 = filePath.replace("\\","/")

# To be able to import .ui and define app
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

# StyleSheet for buttons
btnStyleSheet = """QPushButton{\ntext-align: left;\npadding-left: 11px;\nbackground-color: fondo;\nborder-radius: 5px;\n}\nQPushButton::hover{\nbackground-color: rgb(199, 199, 205);\n}\nQPushButton::pressed{\nbackground-color: rgb(185, 185, 185);\n}"""

def clearLineEdits():
    # Log in
    logInWindow.lineEditUser.setText("")
    logInWindow.lineEditPassword.setText("")
    logInWindow.lineEditUser2.setText("")
    logInWindow.lineEditPassword2.setText("")
    logInWindow.lineEditVerifyPassword.setText("")
    # Deposit money
    mainWindow.lineEdit_2.setText("")
    # Take out money
    mainWindow.lineEdit_3.setText("")
    # Change password
    mainWindow.lineEditActualPassword.setText("")
    mainWindow.lineEditNewPassword.setText("")
    mainWindow.lineEditRepeatPassword.setText("")
    # Transfer
    mainWindow.lineEdit_6.setText("")
    mainWindow.lineEdit_7.setText("")
    # Change username
    mainWindow.lineEditUsername.setText("")

def clearErrors():
    # Log in
    logInWindow.labelUserError2.hide()
    logInWindow.labelPasswordError4.hide()
    logInWindow.labelUserError.hide()
    logInWindow.labelPasswordError2.hide()
    logInWindow.correct.hide()
    logInWindow.labelPasswordError2_2.hide()
    logInWindow.labelPasswordError.hide()
    # Deposit money
    mainWindow.moneyError.hide()
    mainWindow.lettersError.hide()
    # Take out money
    mainWindow.moneyError_2.hide()
    mainWindow.moneyError_3.hide()
    # Change password
    mainWindow.passwordError.hide()
    mainWindow.passwordError4.hide()
    # Trasnfer
    mainWindow.moneyError_5.hide()
    mainWindow.letterError_5.hide()
    mainWindow.nameError.hide()
    # Change username
    mainWindow.labelUserError.hide()

# Update window money values
def updateMoney():
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = bytes.decode(base64.b64decode(openMoneyRead.read()))
    openMoneyRead.close()
    mainWindow.labelMoney.setText(str(money)+" €")
    mainWindow.labelMoney_2.setText(str(money)+" €")
    mainWindow.labelMoney_3.setText(str(money)+" €")
    mainWindow.labelMoney_4.setText(str(money)+" €")
    mainWindow.labelMoney_5.setText(str(money)+" €")

# Splash screen
def splashScreen():
    # Remove title bar
    splashScreenWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    splashScreenWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Logo
    splashScreenWindow.label.setPixmap(QtGui.QPixmap(path1+"/UIs/Imgs/logo.png"))
    splashScreenWindow.label_2.setPixmap(QtGui.QPixmap(path1+"/UIs/Imgs/background.png"))
    splashScreenWindow.label.setScaledContents(True)

    # Open window
    splashScreenWindow.show()

    # Progress
    for percentage in range(1, 35):
        time.sleep(0.003)
        splashScreenWindow.labelLoading.setText("Starting components...")
        QGuiApplication.processEvents()
        if percentage == 99:
            splashScreenWindow.close()
            logIn()
            break

    for percentage in range(35, 75):
        time.sleep(0.005)
        splashScreenWindow.labelLoading.setText("Loading interfaces...")
        QGuiApplication.processEvents()
        if percentage == 99:
            splashScreenWindow.close()
            logIn()
            break

    for percentage in range(75, 100, 2):
        time.sleep(0.002)
        splashScreenWindow.labelLoading.setText("Starting...")
        QGuiApplication.processEvents()
        if percentage == 99:
            splashScreenWindow.close()
            logIn()
            break


# Log in and create account
def logIn():
    # Remove title bar, maximize and resizing
    logInWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
    logInWindow.logo.setPixmap(QPixmap(path1+"/UIs/Imgs/logo4.png"))
    logInWindow.setFixedSize(logInWindow.width(), logInWindow.height())
    logInWindow.show()
    clearErrors()

# Checks if checkBox is clicked
def checkBox1Checker():
    checkBoxValue = logInWindow.checkBox_password.checkState()
    
    if str(checkBoxValue) == "PySide6.QtCore.Qt.CheckState.Checked":
        logInWindow.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        logInWindow.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)

def checkBox2Checker():
    checkBoxValue = logInWindow.checkBox_Password2.checkState()
    
    if str(checkBoxValue) == "PySide6.QtCore.Qt.CheckState.Checked":
        logInWindow.lineEditPassword2.setEchoMode(QtWidgets.QLineEdit.Normal)
        logInWindow.lineEditVerifyPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        logInWindow.lineEditPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        logInWindow.lineEditVerifyPassword.setEchoMode(QtWidgets.QLineEdit.Password)

# Animation
def unfadeAnimation(window1, window2):
    window1.hide()
    window2.show()
    # Unfade
    logInWindow.effect = QtWidgets.QGraphicsOpacityEffect()
    window2.setGraphicsEffect(logInWindow.effect)

    logInWindow.animation = QtCore.QPropertyAnimation(logInWindow.effect, b"opacity")
    logInWindow.animation.setDuration(500)
    logInWindow.animation.setStartValue(0)
    logInWindow.animation.setEndValue(1)
    logInWindow.animation.start()

# Create an account
def createAccountScript():
    createUser = logInWindow.lineEditUser2.text()
    
    # Check if the user alredy exists
    if os.path.isfile(path1+"/Data/Users/user_{}.txt".format(createUser)) == True:
        logInWindow.labelUserError.show()
        error = 1
        return error
    else:
        pass

    # Checks if createUser contains special characters and password
    checkCharacters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (checkCharacters.search(createUser) == None):
        passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(createUser),"w")      
        createPassword = logInWindow.lineEditPassword2.text()
        verifyPassword = logInWindow.lineEditVerifyPassword.text()
        if createPassword == "" and verifyPassword == "":
            logInWindow.labelPasswordError2.show()
            passwordData.close()
            error = 1
            return error

        else:
            if createPassword == verifyPassword:
                passwordData.write(bytes.decode(base64.b64encode(encrypt(createPassword))))
                usernameData = open(path1+"/Data/Users/user_{}.txt".format(createUser),"w")
                usernameData.write(createUser)   
                usernameData.close()
                money = open(path1+"/Data/user_money/money_{}.txt".format(createUser),"w")
                money.write(bytes.decode(base64.b64encode(encrypt("0"))))
                money.close()
                openHistory = open(path1+"/Data/History/history_{}.txt".format(createUser),"w")
                openHistory.close()
                passwordData.close()
                logInWindow.lineEditUser2.setText("")
                logInWindow.lineEditPassword2.setText("")
                logInWindow.lineEditVerifyPassword.setText("")
                logInWindow.correct.show()
            else:
                logInWindow.labelPasswordError.show()
                passwordData.close()
                error = 1
                return error
               
    else:
        logInWindow.labelPasswordError2.show()
        error = 1
        return error

# Log in 
def logInScript():
    # Check if the user exists
    correctAccount = False
    askUser = logInWindow.lineEditUser.text()
    try:
        UserName = open(path1+"/Data/Users/user_{}.txt".format(askUser),"r")
        global username
        correctAccount = True
        username = UserName.read()
        UserName.close()

    except FileNotFoundError:
        logInWindow.labelUserError2.show()
        error = 1
        return error

    # Check password
    if correctAccount == True:
        askPassword = logInWindow.lineEditPassword.text()
        passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(username),"r")
        contraseña = bytes.decode(base64.b64decode(passwordData.read()))
        passwordData.close()

        if askPassword == contraseña:
            logInWindow.close()
            yourAccount()

        else:
            logInWindow.labelPasswordError4.show()
            error = 1
            return error

    else:
        logInWindow.labelUserError2.show()
        error = 1
        return error


# Main window
# Side bar animation
def clickButtonExpand(mainWindow):
    menuWidth = mainWindow.sidebar.width()

    # Check
    width = 50
    if menuWidth == 50:
        width = 190

    # Start animation
    mainWindow.animExp = QtCore.QPropertyAnimation(mainWindow.sidebar, b"minimumWidth")
    mainWindow.animExp.setDuration(300)
    mainWindow.animExp.setStartValue(menuWidth)
    mainWindow.animExp.setEndValue(width)
    mainWindow.animExp.setEasingCurve(QtCore.QEasingCurve.InOutCirc)
    mainWindow.animExp.start()


# Fade unfade animation
def fadeUnfadeAnimation(option):
    # Show
    mainWindow.stackedWidget.setCurrentWidget(option)

    # Unfade
    mainWindow.effect = QtWidgets.QGraphicsOpacityEffect()
    option.setGraphicsEffect(mainWindow.effect)
    mainWindow.animYourAccount = QtCore.QPropertyAnimation(mainWindow.effect, b"opacity")
    mainWindow.animYourAccount.setDuration(300)
    mainWindow.animYourAccount.setStartValue(0)
    mainWindow.animYourAccount.setEndValue(1)
    mainWindow.animYourAccount.start()

# Checks if checkBox is clicked in mainWindow
def checkBox3Checker():
    checkBoxValue = mainWindow.checkBox_Password.checkState()
    
    if str(checkBoxValue) == "PySide6.QtCore.Qt.CheckState.Checked":
        mainWindow.lineEditActualPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        mainWindow.lineEditNewPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        mainWindow.lineEditRepeatPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        mainWindow.lineEditActualPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        mainWindow.lineEditNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        mainWindow.lineEditRepeatPassword.setEchoMode(QtWidgets.QLineEdit.Password)


# Checks if checkBox is clicked in dark mode settings
def checkBox4Checker():
    checkBoxValue = mainWindow.checkBox_DarkMode.checkState()
    
    if str(checkBoxValue) == "PySide6.QtCore.Qt.CheckState.Checked":
        darkMode()
    else:
        lightMode()


# Your account window (mainWindow)
def yourAccount():
    global money
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = bytes.decode(base64.b64decode(openMoneyRead.read()))
    int(money)
    openMoneyRead.close()
    updateMoney()
    mainWindow.labelUsername.setText("<strong>"+username+"</strong>")
    mainWindow.show()
    fadeUnfadeAnimation(mainWindow.yourAccount)
    
    
# Deposit money
def depositMoney():
    updateMoney()
    fadeUnfadeAnimation(mainWindow.depositMoney)
    clearErrors()

def depositMoneyScript(depositMoney):
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(bytes.decode(base64.b64decode(openMoneyRead.read())))
    openMoneyRead.close()
    money = money + int(depositMoney)
    history("Entered {} €".format(depositMoney))
    openMoneyWrite = open(path1+"/data/user_money/money_{}.txt".format(username),"w")
    openMoneyWrite.write(bytes.decode(base64.b64encode(encrypt(str(money)))))
    openMoneyWrite.close()
    updateMoney()
    fadeUnfadeAnimation(mainWindow.correct)
    clearLineEdits()
    

def depositMoneyCustomScript():
    askDepositMoney = mainWindow.lineEdit_2.text()
    if askDepositMoney.isnumeric():
        if int(askDepositMoney) <= 1000000000:
            openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
            money = int(bytes.decode(base64.b64decode(openMoneyRead.read())))
            openMoneyRead.close()
            money = money + int(askDepositMoney)  
            mainWindow.lineEdit_2.setText("")
            openMoneyWrite = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
            openMoneyWrite.write(bytes.decode(base64.b64encode(encrypt(str(money)))))
            history("Entered {} €".format(money))
            openMoneyWrite.close()
            updateMoney()
            fadeUnfadeAnimation(mainWindow.correct)
            clearLineEdits()
        else:
            mainWindow.moneyError.show()
            error = 1
            return error
    else:
        mainWindow.lettersError.show()
        error = 1
        return error
    

# Take out money 
def takeOutMoney():
    updateMoney()
    fadeUnfadeAnimation(mainWindow.takeOut)
    clearErrors()

# Checks if there's enough money and more
def moneyChecker(checkMoney):
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(bytes.decode(base64.b64decode(openMoneyRead.read())))
    openMoneyRead.close()

    if checkMoney <= money:
        money = money - int(checkMoney)
        history("Withdrawn {} €".format(checkMoney))
        openTakeOutMoney = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
        openTakeOutMoney.write(bytes.decode(base64.b64encode(encrypt(str(money)))))
        openTakeOutMoney.close()
        updateMoney()
        fadeUnfadeAnimation(mainWindow.correct)
        clearLineEdits()

    else:
        fadeUnfadeAnimation(mainWindow.error)
        mainWindow.title.setText("There isn't enough money")
        mainWindow.filling.setText("There isn't enough money. Do you want to deposit some?")
        error = 1
        return error

def moneyCheckerCustom():
    askTakeOutMoney = mainWindow.lineEdit_3.text()
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(bytes.decode(base64.b64decode(openMoneyRead.read())))
    openMoneyRead.close()
    if askTakeOutMoney.isnumeric():
        openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
        money = int(bytes.decode(base64.b64decode(openMoneyRead.read())))
        openMoneyRead.close()
        if int(askTakeOutMoney) <= money:
            money = money - int(askTakeOutMoney)
            fadeUnfadeAnimation(mainWindow.correct)
            history("Withdrawn {} €".format(askTakeOutMoney))
            openMoneyTakeOut = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
            openMoneyTakeOut.write(bytes.decode(base64.b64encode(encrypt(str(money)))))
            openMoneyTakeOut.close()
            updateMoney()
            mainWindow.lineEdit_3.setText("")
            clearLineEdits()
        else:
            mainWindow.moneyError_2.show()
            error = 1
            return error
    else:
        mainWindow.moneyError_3.show()
        error = 1
        return error
    

# History
# Show history window
def showHistory():
    openHistory = open(path1+"/Data/History/history_{}.txt".format(username),"r+")
    historyText = openHistory.read()
    openHistory.close
    mainWindow.textEdit.setText(historyText)
    fadeUnfadeAnimation(mainWindow.history)

# Writes in the history file
def history(action):
    openHistory = open(path1+"/Data/History/history_{}.txt".format(username),"a")
    now = datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)
    date1 = str(date.today())+" "+hour+":"+minute
    openHistory.write(""+date1+" "+action+"\n") 
    openHistory.close() 

    openHistory = open(path1+"/Data/History/history_{}.txt".format(username),"r")
    lines = openHistory.readlines()
    openHistory.close()

    numberLines = len(lines)
    if numberLines > 100:
        with open(path1+"/Data/History/history_{}.txt".format(username),'r') as fin:
            data = fin.read().splitlines(True)
        with open(path1+"/Data/History/history_{}.txt".format(username),'w') as fout:
            fout.writelines(data[1:])
    else:
        pass


# Change password
def cambiarContraseña():
    fadeUnfadeAnimation(mainWindow.changePassword)
    clearErrors()

def changePasswordScript():
    actualPassword = mainWindow.lineEditActualPassword.text()
    passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(username),"r")
    password = bytes.decode(base64.b64decode(passwordData.read()))
    passwordData.close()
    verifyPassword = mainWindow.lineEditRepeatPassword.text()
    newPassword = mainWindow.lineEditNewPassword.text()
    if actualPassword == password:
        if verifyPassword == newPassword:
            askChangePassword = mainWindow.lineEditNewPassword.text()
            passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(username),"w")
            passwordData.write(bytes.decode(base64.b64encode(encrypt(askChangePassword))))
            passwordData.close()
            history("The password was changed")
            fadeUnfadeAnimation(mainWindow.correct)
        else:
            mainWindow.passwordError.show()
            error = 1
            return error
    else:
        mainWindow.passwordError4.show()
        error = 1
        return error


# Transfer money
def transferMoneyScript(transferMoney):
    correctAccount = False
    global askAccountTransfer
    askAccountTransfer = mainWindow.lineEdit_7.text()
    try:
        UserName = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"r")
        correctAccount = True
        UserName.close()

    except FileNotFoundError:
        mainWindow.nameError.setText("Can't find that account")
        correctAccount = False

    if askAccountTransfer == username:
        mainWindow.nameError.setText("Why do you want to transfer yourself?")

    else:
        if correctAccount == True:
            mainWindow.lineEdit_7.setText("")
            openHistory2 = open(path1+"/Data/History/history_{}.txt".format(askAccountTransfer),"a")
            openHistory2.close()
            updateMoney()
            openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
            money = int(bytes.decode(base64.b64decode(openMoneyRead.read())))
            openMoneyRead.close()
            openMoneyTransferGive = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
            openMoneyTransferReceive = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"r")
            moneyGive = int(bytes.decode(base64.b64decode(openMoneyTransferGive.read())))
            moneyReceive = int(bytes.decode(base64.b64decode(openMoneyTransferReceive.read())))
            openMoneyTransferGive.close()
            openMoneyTransferReceive.close()
            if transferMoney <= moneyGive:
                moneyGive = moneyGive - transferMoney
                moneyReceive = moneyReceive + transferMoney
                openMoneyTransferGiveWrite = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
                openMoneyTransferReceiveWrite = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"w")
                historyOpenYou = open(path1+"/Data/History/history_{}.txt".format(username),"a")
                historyOpenOther = open(path1+"/Data/History/history_{}.txt".format(askAccountTransfer),"a")
                now = datetime.now()
                hour = str(now.hour)
                minute = str(now.minute)
                date1 = str(date.today())+" "+hour+":"+minute
                historyOpenYou.write(date1+" You have transferred "+str(transferMoney)+" € to "+askAccountTransfer+"\n")
                historyOpenOther.write(date1+" "+username+" has transferred "+str(transferMoney)+ "€ to you."+"\n")
                historyOpenYou.close()
                historyOpenOther.close()

                openHistory = open(path1+"/Data/History/history_{}.txt".format(username),"r")
                lines = openHistory.readlines()

                openHistory.close()
                numberLines = len(lines)

                if numberLines > 100:
                    with open(path1+"/Data/History/history_{}.txt".format(username), 'r') as fin:
                        data = fin.read().splitlines(True)
                    with open(path1+"/Data/History/history_{}.txt".format(username), 'w') as fout:
                        fout.writelines(data[1:])
                else:
                    pass

                openMoneyTransferGiveWrite.write(bytes.decode(base64.b64encode(encrypt(str(moneyGive)))))
                openMoneyTransferReceiveWrite.write(bytes.decode(base64.b64encode(encrypt(str(moneyReceive)))))
                openMoneyTransferGiveWrite.close()
                openMoneyTransferReceiveWrite.close()
                updateMoney()
                mainWindow.lineEdit_6.setText("")
                fadeUnfadeAnimation(mainWindow.correct)
                clearLineEdits()
                                            
            else:
                mainWindow.nameError.setText("There isn't enough money :(")
                mainWindow.nameError.show()
                error = 1
                return error

        else:
            mainWindow.nameError.setText("Can't find that account")
            mainWindow.nameError.show()
            error = 1
            return error

def transferMoneyCustomScript():
    correctAccount = False
    global askAccountTransfer
    askAccountTransfer = mainWindow.lineEdit_7.text()
    try:
        UserName = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"r")
        correctAccount = True
        UserName.close()

    except FileNotFoundError:
        mainWindow.nameError.setText("Can't find that account")
        correctAccount = False

    if askAccountTransfer == username:
        mainWindow.nameError.setText("Why do you want to transfer yourself?")

    else:
        if correctAccount == True:
            mainWindow.lineEdit_7.setText("")
            openHistory2 = open(path1+"/Data/History/history_{}.txt".format(askAccountTransfer),"a")
            openHistory2.close()
            updateMoney()
        
        else:
            mainWindow.nameError.setText("Can't find that account")
            error = 1
            return error


        openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
        money = int(bytes.decode(base64.b64decode(openMoneyRead.read())))
        openMoneyRead.close()
        askMoneyTransfer = mainWindow.lineEdit_6.text()
        if askMoneyTransfer.isnumeric():
            openMoneyTransferGive = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
            openMoneyTransferReceive = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"r")
            moneyGive = int(bytes.decode(base64.b64decode(openMoneyTransferGive.read())))
            moneyReceive = int(bytes.decode(base64.b64decode(openMoneyTransferReceive.read())))
            openMoneyTransferGive.close()
            openMoneyTransferReceive.close()
            if int(askMoneyTransfer) <= moneyGive:
                moneyGive = moneyGive - int(askMoneyTransfer)
                moneyReceive = moneyReceive + int(askMoneyTransfer)
                openMoneyTransferGiveWrite = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
                openMoneyTransferReceiveWrite = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"w")                     
                    
                openHistoryYou = open(path1+"/Data/History/history_{}.txt".format(username),"a")
                openHistoryOther = open(path1+"/Data/History/history_{}.txt".format(askAccountTransfer),"a")
                now = datetime.now()
                hour = str(now.hour)
                minute = str(now.minute)
                date1 = str(date.today())+" "+hour+":"+minute
                openHistoryYou.write(date1+" You have transferred  "+str(askMoneyTransfer)+" € a "+askAccountTransfer+"\n")
                openHistoryOther.write(date1+" "+username+" has transferred you "+str(askMoneyTransfer)+ "€"+"\n")
                openHistoryYou.close()
                openHistoryOther.close()

                openHistory = open(path1+"/Data/History/history_{}.txt".format(username),"r")
                lines = openHistory.readlines()

                openHistory.close()
                numberLines = len(lines)

                if numberLines > 100:
                    with open(path1+"/Data/History/history_{}.txt".format(username), 'r') as fin:
                        data = fin.read().splitlines(True)
                    with open(path1+"/Data/History/history_{}.txt".format(username), 'w') as fout:
                        fout.writelines(data[1:])
                else:
                    pass

                openMoneyTransferGiveWrite.write(bytes.decode(base64.b64encode(encrypt(str(moneyGive)))))
                openMoneyTransferReceiveWrite.write(bytes.decode(base64.b64encode(encrypt(str(moneyReceive)))))
                openMoneyTransferGiveWrite.close()
                openMoneyTransferReceiveWrite.close()
                updateMoney()
                mainWindow.lineEdit_6.setText("")
                fadeUnfadeAnimation(mainWindow.correct)

            else:
                mainWindow.nameError.setText("Can't find that account")
                mainWindow.nameError.show()
                error = 1
                return error             
                                        
        else:
            mainWindow.nameError.setText("You can't transfer letters")
            mainWindow.nameError.show()
            error = 1
            return error

def transferMoney():
    mainWindow.nameError.setText("")
    clearErrors()
    fadeUnfadeAnimation(mainWindow.transfer)

# Log out
def logOut():
    mainWindow.close()
    logInWindow.show()


# Delete account
def deleteAccount():
    os.remove(path1+"/Data/Users/user_{}.txt".format(username))
    os.remove(path1+"/Data/Passwords/password_{}.txt".format(username))
    os.remove(path1+"/Data/user_money/money_{}.txt".format(username))
    os.remove(path1+"/Data/History/history_{}.txt".format(username))
    mainWindow.close()
    logInWindow.show()

# Change username
def changeUsername():
    newUsername = mainWindow.lineEditUsername.text()

    # User files
    # Check if user alredy exists
    if os.path.isfile(path1+"/Data/Users/user_{}.txt".format(newUsername)) == True:
        mainWindow.labelUserError.show()
        error = 1
        return error
    else:
        pass

    if newUsername == "":
        mainWindow.labelUserError.setText("Your username can not be empty")
        error = 1
        return error

    else:
        lastName = username

        usernameData = open(path1+"/Data/Users/user_{}.txt".format(newUsername),"w")
        usernameData.write(newUsername)   
        usernameData.close()

        # Money files
        openMoneyFile = open(path1+"/Data/user_money/money_{}.txt".format(lastName),"r")
        money = int(bytes.decode(base64.b64decode(openMoneyFile.read())))
        openMoneyFile.close()
        openMoneyFileNew = open(path1+"/Data/user_money/money_{}.txt".format(newUsername),"w")
        openMoneyFileNew.write(bytes.decode(base64.b64encode(encrypt(str(money)))))
        openMoneyFileNew.close()

        # History
        historyFile = open(path1+"/Data/History/history_{}.txt".format(lastName),"r+")
        historyText = historyFile.read()
        historyFile.close()
        historyFileNew = open(path1+"/Data/History/history_{}.txt".format(newUsername),"w+")
        historyFileNew.write(historyText)
        historyFileNew.close()

        # Password
        passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(lastName),"r+")
        actualPassword = bytes.decode(base64.b64decode(passwordData.read()))
        passwordData.close()
        newPassword = open(path1+"/Data/Passwords/password_{}.txt".format(newUsername),"w+")
        newPassword.write(bytes.decode(base64.b64encode(encrypt(actualPassword))))
        newPassword.close()

        os.remove(path1+"/Data/Users/user_{}.txt".format(lastName))
        os.remove(path1+"/Data/Passwords/password_{}.txt".format(lastName))
        os.remove(path1+"/Data/user_money/money_{}.txt".format(lastName))
        os.remove(path1+"/Data/History/history_{}.txt".format(lastName))
        fadeUnfadeAnimation(mainWindow.yourAccount)

        openMoneyFileRead = open(path1+"/Data/user_money/money_{}.txt".format(newUsername),"r")
        money = int(bytes.decode(base64.b64decode(openMoneyFileRead.read())))
        openMoneyFileRead.close()
        
        fadeUnfadeAnimation(mainWindow.ensureChangeUsername)


def darkMode():
    # Change settings
    openDarkMode = open(path1+"/Data/darkMode.txt","w")
    openDarkMode.write("1")
    openDarkMode.close()
    # Log in window
    logInWindow.frame.setStyleSheet("QFrame{\nbackground-color: rgb(36, 36, 36);\n}")
    logInWindow.logo.setPixmap(QPixmap(path1+"/UIs/Imgs/logo.png"))
    logInWindow.logo.setMaximumSize(5000000, 150)
    logInWindow.logo.setGeometry(20, 30, 361, 150)
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_CheckBox.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    logInWindow.checkBox_password.setStyleSheet(styleSheet)
    logInWindow.checkBox_Password2.setStyleSheet(styleSheet)
    mainWindow.checkBox_Password.setStyleSheet(styleSheet)# <---- Main window
    mainWindow.checkBox_DarkMode.setStyleSheet(styleSheet)# <---- Main window
    # Main window
    # History
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_History.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.textEdit.setStyleSheet(styleSheet)
    # Lateral buttons
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_LateralButtons.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.btnMinMax.setStyleSheet(styleSheet)
    mainWindow.btnYourAccount.setStyleSheet(styleSheet)
    mainWindow.btnLogOut.setStyleSheet(styleSheet)
    mainWindow.btnSettings.setStyleSheet(styleSheet)
    # Info frames
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_Frames.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.frameMoney.setStyleSheet(styleSheet)
    mainWindow.frameMoney_2.setStyleSheet(styleSheet)
    mainWindow.frameMoney_3.setStyleSheet(styleSheet)
    mainWindow.frameMoney_4.setStyleSheet(styleSheet)
    mainWindow.frameMoney_5.setStyleSheet(styleSheet)
    mainWindow.frameChoose.setStyleSheet(styleSheet)
    mainWindow.frameChoose_2.setStyleSheet(styleSheet)
    mainWindow.frameChoose_5.setStyleSheet(styleSheet)
    mainWindow.frameAccount.setStyleSheet(styleSheet)
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_MoneyLabels.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.labelYourMoney.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_2.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_3.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_4.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_5.setStyleSheet(styleSheet)
    mainWindow.labelChoose.setStyleSheet(styleSheet)
    mainWindow.labelChoose_2.setStyleSheet(styleSheet)
    mainWindow.labelChoose_5.setStyleSheet(styleSheet)
    mainWindow.labelChoose_6.setStyleSheet(styleSheet)
    # Side and top frames
    mainWindow.topBar.setStyleSheet("QFrame{\nbackground-color: rgb(65, 65, 65);\n}")
    mainWindow.sideBar.setStyleSheet("QFrame{\nbackground-color: rgb(65, 65, 65);\n}")
    # Content
    mainWindow.content.setStyleSheet("QFrame{\nbackground-color: rgb(36, 36, 36);\n}")
    # Settings
    mainWindow.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgb(36, 36, 36);\nborder: none;")
    # Labels
    mainWindow.labelYourAccount.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_3.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_4.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_8.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_10.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_12.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_13.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_19.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_17.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_16.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_18.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_15.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_25.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_23.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.labelWelcome.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.labelUsername.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.labelVersion.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.labelCorrect.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.filling.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.title.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.text.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.label_20.setStyleSheet("QFrame{\ncolor: rgb(255, 255, 255);\n}")
    mainWindow.labelMoney.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_2.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_3.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_4.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_5.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")
    mainWindow.label_31.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")
    mainWindow.label_7.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")
    mainWindow.label_6.setStyleSheet("QLabel{\ncolor: rgb(255, 255, 255);\nborder: none;\npadding: 1px;\n}")


def lightMode():
    # Change settings
    openDarkMode = open(path1+"/Data/darkMode.txt","w")
    openDarkMode.write("0")
    openDarkMode.close()
    # Log in window
    logInWindow.frame.setStyleSheet("QFrame{\nbackground-color: rgb(255, 255, 255);\n}")
    logInWindow.logo.setPixmap(QPixmap(path1+"/UIs/Imgs/logo4.png"))
    logInWindow.logo.setMaximumSize(5000000, 5000000)
    logInWindow.logo.setGeometry(20, 30, 361, 191)
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_CheckBox_Light.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    logInWindow.checkBox_password.setStyleSheet(styleSheet)
    logInWindow.checkBox_Password2.setStyleSheet(styleSheet)
    mainWindow.checkBox_Password.setStyleSheet(styleSheet)# <---- Main window
    mainWindow.checkBox_DarkMode.setStyleSheet(styleSheet)# <---- Main window
    # Main window
    # History
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_History_Light.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.textEdit.setStyleSheet(styleSheet)
    # Lateral buttons
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_LateralButtons_Light.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.btnMinMax.setStyleSheet(styleSheet)
    mainWindow.btnYourAccount.setStyleSheet(styleSheet)
    mainWindow.btnLogOut.setStyleSheet(styleSheet)
    mainWindow.btnSettings.setStyleSheet(styleSheet)
    # Info frames
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_Frames_Light.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.frameMoney.setStyleSheet(styleSheet)
    mainWindow.frameMoney_2.setStyleSheet(styleSheet)
    mainWindow.frameMoney_3.setStyleSheet(styleSheet)
    mainWindow.frameMoney_4.setStyleSheet(styleSheet)
    mainWindow.frameMoney_5.setStyleSheet(styleSheet)
    mainWindow.frameChoose.setStyleSheet(styleSheet)
    mainWindow.frameChoose_2.setStyleSheet(styleSheet)
    mainWindow.frameChoose_5.setStyleSheet(styleSheet)
    mainWindow.frameAccount.setStyleSheet(styleSheet)
    styleSheetData = open(path1+"/UIs/styleSheets/styleSheet_MoneyLabels_Light.txt", "r")
    styleSheet = styleSheetData.read()
    styleSheetData.close()
    mainWindow.labelYourMoney.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_2.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_3.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_4.setStyleSheet(styleSheet)
    mainWindow.labelYourMoney_5.setStyleSheet(styleSheet)
    mainWindow.labelChoose.setStyleSheet(styleSheet)
    mainWindow.labelChoose_2.setStyleSheet(styleSheet)
    mainWindow.labelChoose_5.setStyleSheet(styleSheet)
    mainWindow.labelChoose_6.setStyleSheet(styleSheet)
    # Side and top frames
    mainWindow.topBar.setStyleSheet("QFrame{\nbackground-color: rgb(239, 239, 239);\n}")
    mainWindow.sideBar.setStyleSheet("QFrame{\nbackground-color: rgb(239, 239, 239);\n}")
    # Content
    mainWindow.content.setStyleSheet("QFrame{\nbackground-color: rgb(255, 255, 255);\n}")
    # Settings
    mainWindow.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgb(255, 255, 255);\nborder: none;")
    # Labels
    mainWindow.labelYourAccount.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_3.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_4.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_8.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_10.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_12.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_13.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_19.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_17.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_16.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_18.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_15.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_25.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_23.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.labelWelcome.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.labelUsername.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.labelVersion.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.labelCorrect.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.filling.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.title.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.text.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.label_20.setStyleSheet("QFrame{\ncolor: rgb(0, 0, 0);\n}")
    mainWindow.labelMoney.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_2.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_3.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_4.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")
    mainWindow.labelMoney_5.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")
    mainWindow.label_31.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")
    mainWindow.label_7.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")
    mainWindow.label_6.setStyleSheet("QLabel{\ncolor: rgb(0, 0, 0);\nborder: none;\npadding: 1px;\n}")

    
# Define windows and other settings
splashScreenWindow = loader.load(path1+"/UIs/splashScreen.ui", None)
logInWindow = loader.load(path1+"/UIs/logIn.ui", None)
mainWindow = loader.load(path1+"/UIs/mainWindow.ui", None)
mainWindow.stackedWidget.setCurrentWidget(mainWindow.yourAccount)
mainWindow.btnGoBack.hide()
mainWindow.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) 
app.setWindowIcon(QIcon(path1+"/UIs/Imgs/icon.ico"))

# Icons and images
mainWindow.btnMinMax.setIcon(QtGui.QIcon(path1+"/UIs/Imgs/minMaxIcon.png"))
mainWindow.btnYourAccount.setIcon(QtGui.QIcon(path1+"/UIs/Imgs/homeIconClicked.png"))
mainWindow.btnSettings.setIcon(QtGui.QIcon(path1+"/UIs/Imgs/settingsIcon.png")) 
mainWindow.btnGoBack.setIcon(QtGui.QIcon(path1+"/UIs/Imgs/goBackIcon.png"))
mainWindow.btnLogOut.setIcon(QtGui.QIcon(path1+"/UIs/Imgs/logOutIon.png"))
mainWindow.tick.setPixmap(QPixmap(path1+"/UIs/Imgs/correctIcon.png"))
mainWindow.interrogationIcon.setPixmap(QPixmap(path1+"/UIs/Imgs/interrogationIcon.png"))
mainWindow.interrogationIcon_2.setPixmap(QPixmap(path1+"/UIs/Imgs/interrogationIcon.png"))
mainWindow.iconError.setPixmap(QPixmap(path1+"/UIs/Imgs/errorIcon.png"))
mainWindow.btnYourAccount.setStyleSheet(btnStyleSheet.replace("fondo","qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 203, 203, 255), stop:1 rgba(229, 229, 229, 255))"))

# Miscellaneous buttons
# Log in and create account icons
logInWindow.btnLogIn_2.clicked.connect(lambda: logInScript())
logInWindow.btnCreateAccount_2.clicked.connect(lambda: createAccountScript())
# Checks if checkBox is clicked and changes echoMode
logInWindow.checkBox_password.clicked.connect(lambda: checkBox1Checker())
logInWindow.checkBox_Password2.clicked.connect(lambda: checkBox2Checker())
# logInWindow actions
# Clear errors
logInWindow.lineEditUser.textChanged.connect(lambda: clearErrors())
logInWindow.lineEditPassword.textChanged.connect(lambda: clearErrors())
logInWindow.lineEditUser2.textChanged.connect(lambda: clearErrors())
logInWindow.lineEditPassword2.textChanged.connect(lambda: clearErrors())
logInWindow.lineEditVerifyPassword.textChanged.connect(lambda: clearErrors())
# Hide and show panels in logInWindow
logInWindow.btnLogIn.clicked.connect(lambda: unfadeAnimation(logInWindow.frameCreateAccount, logInWindow.frameLogIn))
logInWindow.btnLogIn.clicked.connect(lambda: clearErrors())
logInWindow.btnLogIn.clicked.connect(lambda: clearLineEdits())
logInWindow.btnCreateAccount.clicked.connect(lambda: unfadeAnimation(logInWindow.frameLogIn, logInWindow.frameCreateAccount))
logInWindow.btnCreateAccount.clicked.connect(lambda: clearErrors())
logInWindow.btnCreateAccount.clicked.connect(lambda: clearLineEdits())
# Hide button clicked
mainWindow.btnMinMax.clicked.connect(lambda: clickButtonExpand(mainWindow))
# Your account button clicked
mainWindow.btnYourAccount.clicked.connect(lambda: mainWindow.btnYourAccount.setIcon(QIcon(path1+"/UIs/Imgs/homeIconClicked.png")))
mainWindow.btnYourAccount.clicked.connect(lambda: mainWindow.btnSettings.setIcon(QIcon(path1+"/UIs/Imgs/settingsIcon.png")))
mainWindow.btnYourAccount.clicked.connect(lambda: mainWindow.btnYourAccount.setStyleSheet(btnStyleSheet.replace("fondo","qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 203, 203, 255), stop:1 rgba(229, 229, 229, 255))")))
mainWindow.btnYourAccount.clicked.connect(lambda: mainWindow.btnSettings.setStyleSheet(btnStyleSheet.replace("fondo","rgb(255, 255, 255)")))
mainWindow.btnYourAccount.clicked.connect(lambda: fadeUnfadeAnimation(mainWindow.yourAccount))
mainWindow.btnYourAccount.clicked.connect(lambda: mainWindow.btnGoBack.hide())
# Settings button clicked
mainWindow.btnSettings.clicked.connect(lambda: mainWindow.btnSettings.setIcon(QIcon(path1+"/UIs/Imgs/settingsIconClicked.png")))
mainWindow.btnSettings.clicked.connect(lambda: mainWindow.btnYourAccount.setIcon(QIcon(path1+"/UIs/Imgs/homeIcon.png")))
mainWindow.btnSettings.clicked.connect(lambda: mainWindow.btnSettings.setStyleSheet(btnStyleSheet.replace("fondo","qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 203, 203, 255), stop:1 rgba(229, 229, 229, 255))")))
mainWindow.btnSettings.clicked.connect(lambda: mainWindow.btnYourAccount.setStyleSheet(btnStyleSheet.replace("fondo","rgb(255, 255, 255)")))
mainWindow.btnSettings.clicked.connect(lambda: fadeUnfadeAnimation(mainWindow.settings))
mainWindow.btnSettings.clicked.connect(lambda: mainWindow.btnGoBack.hide())
# Go bak button clicked
mainWindow.btnGoBack.clicked.connect(lambda: fadeUnfadeAnimation(mainWindow.yourAccount))
mainWindow.btnGoBack.clicked.connect(lambda: mainWindow.btnGoBack.hide())
# Boton ingresar dinero pulsado
mainWindow.pushButtonDeposit.clicked.connect(lambda: depositMoney())
mainWindow.pushButtonDeposit.clicked.connect(lambda: clearErrors())
mainWindow.pushButtonDeposit.clicked.connect(lambda: mainWindow.btnGoBack.show())
mainWindow.pushButtonDeposit.clicked.connect(lambda: clearErrors())
mainWindow.pushButtonDeposit.clicked.connect(lambda: clearLineEdits())
mainWindow.btnDepositMoney.clicked.connect(lambda: depositMoney())
mainWindow.btnDepositMoney.clicked.connect(lambda: clearErrors())
mainWindow.btnDepositMoney.clicked.connect(lambda: clearLineEdits())
mainWindow.btnDepositMoney.clicked.connect(lambda: mainWindow.btnGoBack.show())
mainWindow.lineEdit_2.textChanged.connect(lambda: clearErrors())
# Transfer actions
mainWindow.pushButton10_5.clicked.connect(lambda: transferMoneyScript(10))
mainWindow.pushButton50_5.clicked.connect(lambda: transferMoneyScript(50))
mainWindow.pushButton100_5.clicked.connect(lambda: transferMoneyScript(100))
mainWindow.pushButton500_5.clicked.connect(lambda: transferMoneyScript(500))
mainWindow.pushButton1000_5.clicked.connect(lambda: transferMoneyScript(1000))
mainWindow.pushButton10000_5.clicked.connect(lambda: transferMoneyScript(10000))
mainWindow.pushButtonTransfer_3.clicked.connect(lambda: transferMoneyCustomScript())
mainWindow.lineEdit_6.textChanged.connect(lambda: clearErrors())
mainWindow.lineEdit_7.textChanged.connect(lambda: clearErrors())
# Take out money button clicked
mainWindow.pushButtonTakeOut.clicked.connect(lambda: takeOutMoney())
mainWindow.pushButtonTakeOut.clicked.connect(lambda: clearLineEdits())
mainWindow.pushButtonTakeOut.clicked.connect(lambda: clearErrors())
mainWindow.pushButtonTakeOut.clicked.connect(lambda: mainWindow.btnGoBack.show())
# History button clicked
mainWindow.pushButtonHistory.clicked.connect(lambda: showHistory())
mainWindow.pushButtonHistory.clicked.connect(lambda: mainWindow.btnGoBack.show())
# Change password button clicked
mainWindow.pushButtonChangePassword.clicked.connect(lambda: cambiarContraseña())
mainWindow.pushButtonChangePassword.clicked.connect(lambda: clearErrors())
mainWindow.pushButtonChangePassword.clicked.connect(lambda: clearLineEdits())
mainWindow.pushButtonChangePassword.clicked.connect(lambda: mainWindow.btnGoBack.show())
mainWindow.btnChangePassword.clicked.connect(lambda: changePasswordScript())
mainWindow.lineEditActualPassword.textChanged.connect(lambda: clearErrors())
mainWindow.lineEditNewPassword.textChanged.connect(lambda: clearErrors())
mainWindow.lineEditRepeatPassword.textChanged.connect(lambda: clearErrors())
# Transfer button clicked
mainWindow.pushButtonTransfer.clicked.connect(lambda: transferMoney())
mainWindow.pushButtonTransfer.clicked.connect(lambda: clearLineEdits())
mainWindow.pushButtonTransfer.clicked.connect(lambda: mainWindow.btnGoBack.show())
# Log out button clicked
mainWindow.btnLogOut.clicked.connect(lambda: logOut())
mainWindow.pushButtonLogOut.clicked.connect(lambda: logOut())
mainWindow.btnLogOut_2.clicked.connect(lambda: logOut())

# Change username button clicked
mainWindow.pushButtonChangeUsername.clicked.connect(lambda: fadeUnfadeAnimation(mainWindow.changeUsername))
mainWindow.pushButtonChangeUsername.clicked.connect(lambda: clearLineEdits())
mainWindow.pushButtonChangeUsername.clicked.connect(lambda: mainWindow.labelUserError.hide())
mainWindow.pushButtonChangeUsername.clicked.connect(lambda: mainWindow.btnGoBack.show())
mainWindow.btnChangeUsername.clicked.connect(lambda: changeUsername())
mainWindow.lineEditUsername.textChanged.connect(lambda: clearErrors())
# Delete account button clicked
mainWindow.pushButtonDeleteAccount.clicked.connect(lambda: fadeUnfadeAnimation(mainWindow.ensureAccountDelete))
mainWindow.pushButtonDeleteAccount.clicked.connect(lambda: mainWindow.btnGoBack.show())
# CheckBox clicked
mainWindow.checkBox_Password.clicked.connect(lambda: checkBox3Checker())
# Aceptar pulsado
mainWindow.btnOk.clicked.connect(lambda: fadeUnfadeAnimation(mainWindow.yourAccount))
# Delete account button clicked
mainWindow.btnDelete.clicked.connect(lambda: deleteAccount())
# Deposit money actions
mainWindow.pushButton10.clicked.connect(lambda: depositMoneyScript(10))
mainWindow.pushButton50.clicked.connect(lambda: depositMoneyScript(50))
mainWindow.pushButton100.clicked.connect(lambda: depositMoneyScript(100))
mainWindow.pushButton500.clicked.connect(lambda: depositMoneyScript(500))
mainWindow.pushButton1000.clicked.connect(lambda: depositMoneyScript(1000))
mainWindow.pushButton10000.clicked.connect(lambda: depositMoneyScript(10000))
mainWindow.pushButtonDeposit_2.clicked.connect(lambda: depositMoneyCustomScript())
# Take out actions
mainWindow.pushButton10_2.clicked.connect(lambda: moneyChecker(10))
mainWindow.pushButton50_2.clicked.connect(lambda: moneyChecker(50))
mainWindow.pushButton100_2.clicked.connect(lambda: moneyChecker(100))
mainWindow.pushButton500_2.clicked.connect(lambda: moneyChecker(500))
mainWindow.pushButton1000_2.clicked.connect(lambda: moneyChecker(1000))
mainWindow.pushButton10000_2.clicked.connect(lambda: moneyChecker(10000))
mainWindow.pushButtonTakeOut_2.clicked.connect(lambda: moneyCheckerCustom())
mainWindow.lineEdit_3.textChanged.connect(lambda: clearErrors())
# Dark mode checkBox
mainWindow.checkBox_DarkMode.clicked.connect(lambda: checkBox4Checker())

# Execute app
splashScreen()

# Check dark mode
openDarkMode = open(path1+"/Data/darkMode.txt","r")
darkModeState = openDarkMode.read()
openDarkMode.close()
if darkModeState == "1":
    darkMode()
    mainWindow.checkBox_DarkMode.click()
else:
   pass

app.exec()
