#github.com/professorCruz/TheRuffierText
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
#from second_win import *
from inst import *

#txt_title = 'Health'
#win_x, win_y = 200, 100
#win_width, win_height = 1000, 600

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # define a aparência da janela
        self.initUI() # criar e configurar elementos gráficos
        self.connects() # estabelece conexões entre elementos
        self.show() # exibe a janela
        
    def set_appear(self):
        #pass
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
            
    def initUI(self):
        self.hello_text = QLabel(txt_hello)  #Cria uma etiqueta
        self.instruction = QLabel (txt_instruction)  #Cria uma etiqueta
        self.button = QPushButton (txt_next)  #Cria um botão
        self.layout = QVBoxLayout()  #Cria um layout
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout) # faz o layout aparecer

    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    
app = QApplication([])
mw = MainWin()
app.exec()
