# Sys for opening windows
import sys

# Import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QCloseEvent

# Os for path
import os

# Re to check the special characters
import re

# Datetime for the date
from datetime import datetime
from datetime import date

# Path
filePath = os.path.dirname(os.path.realpath(__file__))
path1 = filePath.replace("\\","/")

# To be able to import .ui and define app
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

# Update window money values
def updateMoney():
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(openMoneyRead.read())
    openMoneyRead.close()
    yourAccontWindow.labelMoney.setText("Money: "+str(money)+" €")
    depositMoneyWindow.labelMoney.setText("Money: "+str(money)+" €")
    takeOutMoneyWindow.labelMoney.setText("Money: "+str(money)+" €")
    transferMoneyWindow2.labelMoney.setText("Money: "+str(money)+" €")

# Create an account
def createAccount():
    createUser = createAccountWindow.lineEditUser.text()
    
    # Check if the user alredy exists
    if os.path.isfile(path1+"/Data/Users/user_{}.txt".format(createUser)) == True:
        userError.show()
    else:
        pass

    # Checks if createUser contains special characters and password
    checkCharacters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (checkCharacters.search(createUser) == None):
        passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(createUser),"w")      
        createPassword = createAccountWindow.lineEditPassword.text()
        verifyPassword = createAccountWindow.lineEditVerifyPassword.text()
        if createPassword == "" and verifyPassword == "":
            passwordError3.show()
            passwordData.close()

        else:
            if createPassword == verifyPassword:
                passwordData.write(createPassword)
                usernameData = open(path1+"/Data/Users/user_{}.txt".format(createUser),"w")
                usernameData.write(createUser)   
                usernameData.close()
                money = open(path1+"/Data/user_money/money_{}.txt".format(createUser),"w")
                money.write("0")
                money.close()
                openHistory = open(path1+"/Data/History/history_{}.txt".format(createUser),"w")
                openHistory.close()
                createAccountWindow.close()
                passwordData.close()
                createAccountWindow.lineEditUser.setText("")
                createAccountWindow.lineEditPassword.setText("")
                createAccountWindow.lineEditVerifyPassword.setText("")
                correct.show()
            else:
                passwordError.show()
                passwordData.close()
               
    else:
        passwordError2.show()

# Log in 
def logIn():
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
        userError2.show()

    # Check password
    if correctAccount == True:
        askPassword = logInWindow.lineEditPassword.text()
        passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(username),"r")
        contraseña = passwordData.read()
        passwordData.close()

        if askPassword == contraseña:
            homeWindow.close()
            logInWindow.close()
            yourAccount()

        else:
            passwordError4.show()

    else:
        userError2.show()

# Your account window
def yourAccount():
    global money
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(openMoneyRead.read())
    openMoneyRead.close()
    updateMoney()
    yourAccontWindow.show()
    
    
# Deposit money
def depositMoney():
    updateMoney()
    depositMoneyWindow.show()

def depositMoneyScript(depositMoney):
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(openMoneyRead.read())
    openMoneyRead.close()
    money = money + int(depositMoney)
    history("Entered {} €".format(depositMoney))
    openMoneyWrite = open(path1+"/data/user_money/money_{}.txt".format(username),"w")
    openMoneyWrite.write(str(money))
    openMoneyWrite.close()
    updateMoney()
    correct.show()
    

def depositMoneyCustomScript():
    askDepositMoney = askDepositMoneyWindow.lineEdit.text()
    if askDepositMoney.isnumeric():
        if int(askDepositMoney) <= 1000000000:
            openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
            money = int(openMoneyRead.read())
            openMoneyRead.close()
            money = money + int(askDepositMoney)  
            askDepositMoneyWindow.lineEdit.setText("")
            openMoneyWrite = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
            openMoneyWrite.write(str(money))
            history("Entered {} €".format(money))
            openMoneyWrite.close()
            updateMoney()
            askDepositMoneyWindow.close()
            correct.show()
        else:
            moneyError.show()
    else:
        letterError.show()
    

# Take out money 
def takeOutMoney():
    updateMoney()
    takeOutMoneyWindow.show()

# Checks if there's enough money and more
def moneyChecker(checkMoney):
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(openMoneyRead.read())
    openMoneyRead.close()

    if checkMoney <= money:
        money = money - int(checkMoney)
        history("Withdrawn {} €".format(checkMoney))
        openTakeOutMoney = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
        openTakeOutMoney.write(str(money))
        openTakeOutMoney.close()
        updateMoney()
        correct.show()

    else:
        moneyError2.show()

def moneyCheckerCustom():
    askTakeOutMoneyWindow.show()
    askTakeOutMoney = askTakeOutMoneyWindow.lineEdit.text()
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(openMoneyRead.read())
    openMoneyRead.close()
    if askTakeOutMoney.isnumeric():
        openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
        money = int(openMoneyRead.read())
        openMoneyRead.close()
        if int(askTakeOutMoney) <= money:
            money = money - int(askTakeOutMoney)
            correct.show()
            history("Withdrawn {} €".format(askTakeOutMoney))
            openMoneyTakeOut = open(path1+"/Data/user_money/money_{}.txt".format(username),"w")
            openMoneyTakeOut.write(str(money))
            openMoneyTakeOut.close()
            updateMoney()
            askTakeOutMoneyWindow.close()
            askTakeOutMoneyWindow.lineEdit.setText("")
            correct.show()
        else:
            moneyError2.show()
    else:
        letterError.show()
    

# Show history window
def showHistory():
    openHistory = open(path1+"/Data/History/history_{}.txt".format(username),"r+")
    historyText = openHistory.read()
    openHistory.close
    historyWindow.textEdit.setText(historyText)
    historyWindow.show()

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
def changePassword():
    passwordChange = changePasswordWindow.lineEditActualPassword.text()
    passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(username),"r")
    password = passwordData.read()
    passwordData.close()
    if passwordChange == password:
        askChangePassword = changePasswordWindow.lineEditNewPassword.text()
        passwordData = open(path1+"/Data/Passwords/password_{}.txt".format(username),"w")
        passwordData.write(askChangePassword)
        passwordData.close()
        history("The password was changed")
        changePasswordWindow.close()
        correct.show()

    else:
        passwordError4.show()

# Transfer money
def transferMoneyScript(transferMoney):
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(openMoneyRead.read())
    openMoneyRead.close()
    openMoneyTransferGive = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    openMoneyTransferReceive = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"r")
    moneyGive = int(openMoneyTransferGive.read())
    moneyReceive = int(openMoneyTransferReceive.read())
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
        historyOpenYou.write(date1+" Has transferido "+str(transferMoney)+" € a "+askAccountTransfer+"\n")
        historyOpenOther.write(date1+" "+username+" te ha transferido "+str(transferMoney)+ "€"+"\n")
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

        openMoneyTransferGiveWrite.write(str(moneyGive))
        openMoneyTransferReceiveWrite.write(str(moneyReceive))
        openMoneyTransferGiveWrite.close()
        openMoneyTransferReceiveWrite.close()
        updateMoney()
        askTransferMoneyWindow.lineEdit.setText("")
        correct.show()
                                    
    else:
        moneyError2.show()

def transferMoneyCustomScript():
    openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
    money = int(openMoneyRead.read())
    openMoneyRead.close()
    askMoneyTransfer = askTransferMoneyWindow.lineEdit.text()
    if askMoneyTransfer.isnumeric():
        openMoneyTransferGive = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
        openMoneyTransferReceive = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"r")
        moneyGive = int(openMoneyTransferGive.read())
        moneyReceive = int(openMoneyTransferReceive.read())
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

            openMoneyTransferGiveWrite.write(str(moneyGive))
            openMoneyTransferReceiveWrite.write(str(moneyReceive))
            openMoneyTransferGiveWrite.close()
            openMoneyTransferReceiveWrite.close()
            updateMoney()
            askTransferMoneyWindow.lineEdit.setText("")
            correct.show()
            askTransferMoneyWindow.close()

        else:
            moneyError2.show()               
                                    
    else:
        letterError.show()

def transferMoney():
    correctAccount = False
    global askAccountTransfer
    askAccountTransfer = transferMoneyWindow.lineEdit.text()
    try:
        UserName = open(path1+"/Data/user_money/money_{}.txt".format(askAccountTransfer),"r")
        correctAccount = True
        UserName.close()

    except FileNotFoundError:
        userError2.show()
        correctAccount = False

    if askAccountTransfer == username:
        transferError.show()

    else:
        if correctAccount == True:
            transferMoneyWindow.close()
            transferMoneyWindow.lineEdit.setText("")
            openMoneyRead = open(path1+"/Data/user_money/money_{}.txt".format(username),"r")
            money = int(openMoneyRead.read())
            openMoneyRead.close()
            transferMoneyWindow2.show()
            transferMoneyWindow2.labelUser.setText(askAccountTransfer)
            openHistory2 = open(path1+"/Data/History/history_{}.txt".format(askAccountTransfer),"a")
            openHistory2.close()
            updateMoney()
            transferMoneyWindow2.show()
        

        else:
            userError2.show()

    
# Log out
def logOut():
    logInWindow.lineEditUser.setText("")
    logInWindow.lineEditPassword.setText("")
    homeWindow.show()
    yourAccontWindow.close()
    
# Import all windows
homeWindow = loader.load(path1+"/UIs/home.ui", None)
logInWindow = loader.load(path1+"/UIs/logIn.ui", None)
createAccountWindow = loader.load(path1+"/UIs/createAccount.ui", None)
yourAccontWindow = loader.load(path1+"/UIs/yourAccount.ui", None)
depositMoneyWindow = loader.load(path1+"/UIs/depositMoney.ui", None)
takeOutMoneyWindow = loader.load(path1+"/UIs/takeOutMoney.ui", None)
userError = loader.load(path1+"/UIs/userError.ui", None)
passwordError = loader.load(path1+"/UIs/passwordError.ui", None)
passwordError2 = loader.load(path1+"/UIs/passwordError2.ui", None)
passwordError3 = loader.load(path1+"/UIs/passwordError3.ui", None)
passwordError4 = loader.load(path1+"/UIs/passwordError4.ui", None)
userError2 = loader.load(path1+"/UIs/userError2.ui", None)
correct = loader.load(path1+"/UIs/correct.ui", None)
askDepositMoneyWindow = loader.load(path1+"/UIs/askMoney.ui", None)
askTakeOutMoneyWindow = loader.load(path1+"/UIs/askMoney.ui", None)
askTransferMoneyWindow = loader.load(path1+"/UIs/askMoney.ui", None)
moneyError = loader.load(path1+"/UIs/moneyError.ui", None)
letterError = loader.load(path1+"/UIs/letterError.ui", None)
moneyError2 = loader.load(path1+"/UIs/moneyError2.ui", None)
historyWindow = loader.load(path1+"/UIs/history.ui", None)
changePasswordWindow = loader.load(path1+"/UIs/changePassword.ui", None)
transferMoneyWindow = loader.load(path1+"/UIs/transferMoney.ui", None)
transferMoneyWindow2 = loader.load(path1+"/UIs/transferMoney2.ui", None)
transferError = loader.load(path1+"/UIs/transferError.ui", None)

# Open home window
homeWindow.show()

# Miscellaneous button actions
homeWindow.btnLogIn.clicked.connect(lambda: logInWindow.show())
homeWindow.btnCreateAccount.clicked.connect(lambda: createAccountWindow.show())
logInWindow.cancel.clicked.connect(lambda: logInWindow.close())
createAccountWindow.cancel.clicked.connect(lambda: createAccountWindow.close())
createAccountWindow.ok.clicked.connect(lambda: createAccount())
logInWindow.ok.clicked.connect(lambda: logIn())
changePasswordWindow.pushButtonOk.clicked.connect(lambda: changePassword())
changePasswordWindow.pushButtonCancel.clicked.connect(lambda: changePasswordWindow.close())
transferMoneyWindow.ok.clicked.connect(lambda: transferMoney())
transferMoneyWindow.cancel.clicked.connect(lambda: transferMoneyWindow.close())
yourAccontWindow.pushButtonDeposit.clicked.connect(lambda: depositMoney())
yourAccontWindow.pushButtonTakeOutMoney.clicked.connect(lambda: takeOutMoney())
yourAccontWindow.pushButtonHistory.clicked.connect(lambda: showHistory())
yourAccontWindow.pushButtonChangePassword.clicked.connect(lambda: changePasswordWindow.show())
yourAccontWindow.pushButtonTransfer.clicked.connect(lambda: transferMoneyWindow.show())
yourAccontWindow.pushButtonLogOut.clicked.connect(lambda: logOut())
depositMoneyWindow.pushButton10.clicked.connect(lambda: depositMoneyScript(10))
depositMoneyWindow.pushButton50.clicked.connect(lambda: depositMoneyScript(50))
depositMoneyWindow.pushButton100.clicked.connect(lambda: depositMoneyScript(100))
depositMoneyWindow.pushButton500.clicked.connect(lambda: depositMoneyScript(500))
depositMoneyWindow.pushButton1000.clicked.connect(lambda: depositMoneyScript(1000))
depositMoneyWindow.pushButtonChoose.clicked.connect(lambda: askDepositMoneyWindow.show())
askDepositMoneyWindow.ok.clicked.connect(lambda: depositMoneyCustomScript())
takeOutMoneyWindow.pushButton10.clicked.connect(lambda: moneyChecker(10))
takeOutMoneyWindow.pushButton50.clicked.connect(lambda: moneyChecker(50))
takeOutMoneyWindow.pushButton100.clicked.connect(lambda: moneyChecker(100))
takeOutMoneyWindow.pushButton500.clicked.connect(lambda: moneyChecker(500))
takeOutMoneyWindow.pushButton1000.clicked.connect(lambda: moneyChecker(1000))
takeOutMoneyWindow.pushButtonChoose.clicked.connect(lambda: askTakeOutMoneyWindow.show())
askTakeOutMoneyWindow.ok.clicked.connect(lambda: moneyCheckerCustom())
transferMoneyWindow2.pushButton10.clicked.connect(lambda: transferMoneyScript(10))
transferMoneyWindow2.pushButton50.clicked.connect(lambda: transferMoneyScript(50))
transferMoneyWindow2.pushButton100.clicked.connect(lambda: transferMoneyScript(100))
transferMoneyWindow2.pushButton500.clicked.connect(lambda: transferMoneyScript(500))
transferMoneyWindow2.pushButton1000.clicked.connect(lambda: transferMoneyScript(1000))
transferMoneyWindow2.pushButtonChoose.clicked.connect(lambda: askTransferMoneyWindow.show())
askTransferMoneyWindow.ok.clicked.connect(lambda: transferMoneyCustomScript())

# Execute app
app.exec()
