#ch 4.2.3 main.py
import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout) 
from PyQt5.QtGui import QIcon # icon을 추가하기위한 라이브러리

class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()#텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)#텍스트에디트 위젯을 읽기만 가능하도록 수정

        self.btn1=QPushButton('Message', self)#버튼추가
        self.btn1.clicked.connect(self.activateMessage)#버튼 클릭시 핸들러 함수 연결

        self.btn2=QPushButton('Clear',self)#버튼 2 추가
        self.btn2.clicked.connect(self.clearMessage)#버튼2 핸들러 함수 연결

        hbox=QHBoxLayout()#수평박스 레이아웃을 추가하고 버튼1,2 추가
        hbox.addStretch(1)#공백
        hbox.addWidget(self.btn1)#버튼1배치
        hbox.addWidget(self.btn2)#버튼2배치

        vbox=QVBoxLayout()#수직레이아웃 위젯 생성
        vbox.addWidget(self.te1)#수직 레이아웃에 텍스트 에디트 위젯 추가
        #vbox.addWidget(self.btn1)
        vbox.addLayout(hbox)#btn1위치에 hbox를 배치
        vbox.addStretch(1)
        vbox.addStretch(1)#빈공간
        vbox.addWidget(self.btn1)#버튼위치
        vbox.addStretch(1)#빈공간

        self.setLayout(vbox)#빈공간-버튼-빈공간순으로 수직배치된 레이아웃 설저

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))#윈도 아이콘 추가
        self.resize(256,256)
        self.show()

    def activateMessage(self):#버튼을클릭할때 동작하는 함수: 메시지박스 출력
        #핸들러 함수 수정: 메시지가 텍스트에디트에 출력되도록
        #QMessageBox.information(self,"information","Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self): #버튼2 핸들러 함수 정의
        self.te1.clear()

if __name__=="__main__":
    app=QApplication(sys.argv)
    view=Calculator()
    sys.exit(app.exec_())