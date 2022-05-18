
import tkinter as tk

janela = tk.Tk() #inicio
janela.title('Bem vindo ao Tkinter')
botao = tk.Button(janela, text='Sair', height=1, width=35, command=janela.destroy)
botao.pack()

janela.mainloop()  #fim