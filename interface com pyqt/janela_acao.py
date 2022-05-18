#janela_acao.py

from PyQt5.QtWidgets import *

def acao_botao():
    alerta = QMessageBox()
    alerta.setText('Você clicou!')
    alerta.exec()


app = QApplication([])

botao = QPushButton('Clicar')
botao.clicked.connect(acao_botao)
botao.show()

app.exec()
