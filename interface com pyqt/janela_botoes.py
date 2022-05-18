#janela_botoes.py


#pip install pyqt5
from PyQt5.QtWidgets import *

app = QApplication([])

#cria um layout vertical
layout = QVBoxLayout()
#adiciona 2 botões ao layout
layout.addWidget(QPushButton('Acima'))
layout.addWidget(QPushButton('Abaixo'))

#cria uma janela para o app
#aqui widget significa componente gráfico
janela = QWidget()
#define o layout da janela
janela.setLayout(layout)
janela.show()

app.exec()
