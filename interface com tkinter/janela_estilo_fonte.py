
import tkinter as tk

janela = tk.Tk()
janela.title('Bem vindo ao python')
label = tk.Label(janela, text='Hello World', font=('Arial Bold', 70))
label.grid(column=0, row=0)
janela.mainloop()