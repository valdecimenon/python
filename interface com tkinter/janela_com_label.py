import tkinter as tk

janela = tk.Tk()
janela.title('Bem vindo ao Tkinter')

label = tk.Label(janela, text='Isto é um label')
label.grid(column=0, row=0)
janela.mainloop()
