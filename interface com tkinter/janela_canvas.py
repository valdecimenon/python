

import tkinter as tk

janela = tk.Tk()

#cria o canas (tela de desenho)
canvas = tk.Canvas(janela, width=100, height=80)

#a janela terá as dimensões do canvas
canvas.pack()

#desenha uma linha no canvas: create_line(p1, p2, cor)
canvas.create_line(0,20, 100,20, fill='green', )
canvas.create_line(0,40, 100,40, fill='yellow', )
canvas.create_line(0,60, 100,60, fill='blue', )


#exibe a janela com o canvas
janela.mainloop()