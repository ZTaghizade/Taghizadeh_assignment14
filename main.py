from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import math

class calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.arry=[]
        loader = QUiLoader()
        self.ui=loader.load("D:\Term 5\OS Lab_A\Code\A14_calculator\calcute.ui")
        self.ui.show()
        self.ui.lineEdit.setText("0")
        self.ui.pushButton_4.clicked.connect(self.Add)
        self.ui.pushButton_2.clicked.connect(self.Mul)
        self.ui.pushButton_3.clicked.connect(self.Sub)
        self.ui.pushButton.clicked.connect(self.Div)
        self.ui.pushButton_5.clicked.connect(self.Eql)
        self.ui.pushButton_20.clicked.connect(self.Sin)
        self.ui.pushButton_21.clicked.connect(self.Cos)
        self.ui.pushButton_22.clicked.connect(self.Tan)
        self.ui.pushButton_23.clicked.connect(self.Cot)
        self.ui.pushButton_17.clicked.connect(self.Sqr)
        self.ui.pushButton_18.clicked.connect(self.Log)
        self.ui.pushButton_19.clicked.connect(self.AC)
        self.ui.pushButton_15.clicked.connect(self.n0)
        self.ui.pushButton_14.clicked.connect(self.n1)
        self.ui.pushButton_11.clicked.connect(self.n2)
        self.ui.pushButton_8.clicked.connect(self.n3)
        self.ui.pushButton_13.clicked.connect(self.n4)
        self.ui.pushButton_10.clicked.connect(self.n5)
        self.ui.pushButton_7.clicked.connect(self.n6)
        self.ui.pushButton_12.clicked.connect(self.n7)
        self.ui.pushButton_9.clicked.connect(self.n8)
        self.ui.pushButton_6.clicked.connect(self.n9)
        self.ui.pushButton_24.clicked.connect(self.fe)
        self.ui.pushButton_16.clicked.connect(self.ndot)

    def fe(self):
            
        if(self.ui.lineEdit.text()>"0" or self.ui.lineEdit.text()==""):
            self.ui.lineEdit.setText("-"+self.ui.lineEdit.text())
        elif(self.ui.lineEdit.text()<"0"):
            self.ui.lineEdit.setText(str(math.fabs(float(self.ui.lineEdit.text()))))

    def ndot(self):
        self.ui.lineEdit.setText(self.ui.lineEdit.text()+".")

    def n0(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"0")
        
    def n1(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"1")
        else:
            self.ui.lineEdit.setText("1")

    def n2(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"2")
        else:
            self.ui.lineEdit.setText("2")

    def n3(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"3")
        else:
            self.ui.lineEdit.setText("3")

    def n4(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"4")
        else:
            self.ui.lineEdit.setText("4")

    def n5(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"5")
        else:
            self.ui.lineEdit.setText("5")

    def n6(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"6")
        else:
            self.ui.lineEdit.setText("6")

    def n7(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"7")
        else:
            self.ui.lineEdit.setText("7")

    def n8(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"8")
        else:
            self.ui.lineEdit.setText("8")

    def n9(self):
        if(self.ui.lineEdit.text()!="0"):
            self.ui.lineEdit.setText(self.ui.lineEdit.text()+"9")
        else:
            self.ui.lineEdit.setText("9")

    def AC(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.lineEdit.setText("0")
        self.arry.clear()

    def Add(self):
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 170, 0); background-color : rgb(255, 255, 255)")
        if(len(self.arry)!=0):
            if(self.arry[len(self.arry)-1]=="/" and self.ui.lineEdit.text()==0):
                self.ui.lineEdit.setText("ERROR!!!...Cannot divide by zero")
            else:
                self.arry.append(self.ui.lineEdit.text())
                self.arry.append("+")
                self.ui.lineEdit.setText("")
        else:
            self.arry.append(self.ui.lineEdit.text())
            self.arry.append("+")
            self.ui.lineEdit.setText("")
        
    def Mul(self):
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 170, 0); background-color : rgb(255, 255, 255)")
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")      
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        if(len(self.arry)!=0):
            if(self.arry[len(self.arry)-1]=="/" and self.ui.lineEdit.text()==0):
                self.ui.lineEdit.setText("ERROR!!!...Cannot divide by zero")
            else:
                self.arry.append(self.ui.lineEdit.text())
                self.arry.append("*")
                self.ui.lineEdit.setText("")
        else:
            self.arry.append(self.ui.lineEdit.text())
            self.arry.append("*")
            self.ui.lineEdit.setText("") 

    def Sub(self):
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 170, 0); background-color : rgb(255, 255, 255)")
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")      
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        if(len(self.arry)!=0):
            if(self.arry[len(self.arry)-1]=="/" and self.ui.lineEdit.text()==0):
                self.ui.lineEdit.setText("ERROR!!!...Cannot divide by zero")
            else:
                self.arry.append(self.ui.lineEdit.text())
                self.arry.append("-")
                self.ui.lineEdit.setText("")  
        else:
            self.arry.append(self.ui.lineEdit.text())
            self.arry.append("-")
            self.ui.lineEdit.setText("")  

    def Div(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 170, 0); background-color : rgb(255, 255, 255)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")      
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.arry.append(self.ui.lineEdit.text())
        self.arry.append("/")
        self.ui.lineEdit.setText("") 
    
    def Sin(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        ch=float(self.ui.lineEdit.text())
        res=math.sin(math.radians(ch))
        self.ui.lineEdit.setText(str(res))

    def Cos(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        ch=float(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(str(math.cos(math.radians(ch))))

    def Tan(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        ch=float(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(str(math.tan(math.radians(ch))))

    def Cot(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        ch=float(self.ui.lineEdit.text())
        res=1/math.tan(math.radians(ch))
        self.ui.lineEdit.setText(str(res))

    def Sqr(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        if(float(self.ui.lineEdit.text())>=0):
            self.ui.lineEdit.setText(str(math.sqrt(float(self.ui.lineEdit.text()))))
        else:
            self.ui.lineEdit.setText("ERROR!!!")

    def Log(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        if(float(self.ui.lineEdit.text())<=0):
            self.ui.lineEdit.setText("ERROR!!!")
        else:
            self.ui.lineEdit.setText(str(math.log10(float(self.ui.lineEdit.text()))))

    def Eql(self):
        self.ui.pushButton.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_2.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")            
        self.ui.pushButton_3.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")
        self.ui.pushButton_4.setStyleSheet("font: 20pt ""Arial"";border-radius: 15px; color: rgb(255, 255, 255); background-color : rgb(255, 170, 0)")    
        check=1
        self.arry.append(float(self.ui.lineEdit.text()))
        for i in range(len(self.arry)):
            if(self.arry[i]=="+"):
                self.arry[i+1]=float(self.arry[i-1])+float(self.arry[i+1])
            elif(self.arry[i]=="*"):
                self.arry[i+1]=float(self.arry[i-1])*float(self.arry[i+1])
            elif(self.arry[i]=="-"):
                self.arry[i+1]=float(self.arry[i-1])-float(self.arry[i+1])
            elif(self.arry[i]=="/"):
                if(float(self.arry[i+1])==0):
                    check=0
                    self.ui.lineEdit.setText("ERROR!!!...Cannot divide by zero")
                else:
                    self.arry[i+1]=float(self.arry[i-1])/float(self.arry[i+1])
        if(check==1):
            self.ui.lineEdit.setText(str(self.arry[len(self.arry)-1]))
        
        
app = QApplication()
cal_main = calculator()

app.exec()