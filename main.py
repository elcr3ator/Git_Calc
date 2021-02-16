import sys
from PyQt5.QtGui import QFont, QTextDocument
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QVBoxLayout, QApplication,QPushButton


class MyExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.form()
    def form(self):

        self.setGeometry(485,550,300,400)
        self.label=QLabel('')
        self.lbl=QLabel('')
        font = QFont('Times', 10, QFont.Bold)
        self.label.setFont(font)

        layout = QGridLayout(self)
        layout.addWidget(self.label)



        self.btns=   ['C','Clear','','',
                      '1','2','3','/',
                      '4','5','6','*',
                      '7','8','9','-',
                      '0','**','=','+']
        y=0
        pos= [(0,0),(0,1),(0,2),(0,3),
              (1,0),(1,1),(1,2),(1,3),
              (2,0),(2,1),(2,2),(2,3),
              (3,0),(3,1),(3,2),(3,3),
              (4,0),(4,1),(4,2),(4,3)]
        for b in self.btns:
            buttons=QPushButton(b)
            if y==2:
                layout.addWidget(self.label,0,2)
            elif y==3:
                layout.addWidget(self.lbl,0,3)
            else:
                layout.addWidget(buttons, pos[y][0], pos[y][1])
                if buttons.text().isdigit() or buttons.text()== '+' \
                   or buttons.text()== '-' or buttons.text()=='*' or buttons.text()=='/':
                    buttons.clicked.connect(self.buttonclicked)
                if buttons.text()== '=' :
                    buttons.clicked.connect(self.eval)
                if buttons.text()=='C':
                    buttons.clicked.connect(self.C)
                if buttons.text()=='Del':
                    buttons.clicked.connect(self.Del)
                if buttons.text() == '**':
                    buttons.clicked.connect(self.Square)

            y+=1
    def buttonclicked(self):
        sender =self.sender()
        res=self.label.text()
        self.label.setText(res+sender.text())
    def eval(self):
        s=eval(self.label.text())
        self.lbl.setText('')
        self.label.setText(str(s))
    def C(self):
        self.label.setText('')
        self.lbl.setText('')
    def Del(self):
        self.lbl.setText('')
        self.label.setText(self.label.text()[0:-1])
    def Square(self):
        self.lbl.setText('')
        a=eval(self.label.text()) ** 2
        self.label.setText(str(a))

if __name__=='__main__':
    app = QApplication(sys.argv)
    qb=MyExample()
    qb.show()
    sys.exit(app.exec())
