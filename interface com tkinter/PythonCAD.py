
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import math

janela = Tk()
janela.title('Python CAD 1.0')


p1 = None
p2 = None
lista_objs = []

var_objeto = IntVar()
var_objeto.set(1)

var_cor = IntVar()
var_cor.set(1) #1 = 'white'
cores = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

var_espessura = IntVar()
var_espessura.set(1)

mensagens_p1  = ['Clique o ponto inicial da linha',
                 'Clique o centro do círculo',
                 'Clique o primeiro canto da área da elipse',
                 'Clique o primeiro canto do retângulo',
                 'Clique o primeiro canto do sólido']

mensagens_p2  = ['Clique o ponto final da linha',
                 'Clique para definir o raio do círculo',
                 'Clique o canto oposto para definir a área da elipse',
                 'Clique o canto oposto do retângulo',
                 'Clique o canto oposto do sólido']

var_mensagem = StringVar()
var_mensagem.set(mensagens_p1[0])



def acao_clique(evento):
    global p1, p2
    obj = var_objeto.get()
    indice = var_objeto.get() - 1
    if indice < 0:
        messagebox.showwarning('Alerta', 'Nenhum comando foi selecionado em Desenhar!')
        return
    
    if p1 is None:
        p1 = (evento.x, evento.y)
        msg = mensagens_p2[indice]
        var_mensagem.set(msg)
    else:
        p2 = (evento.x, evento.y)
        if obj == 1:
            desenhar_linha(p1, p2)
        elif obj == 2:
            desenhar_circulo(p1, p2)
        elif obj == 3:
            desenhar_elipse(p1, p2)
        elif obj == 4:
            desenhar_retangulo(p1, p2)
        elif obj == 5:
            desenhar_solido(p1, p2)
        p1 = None
        msg = mensagens_p1[indice]
        var_mensagem.set(msg)

def desenhar_linha(p1, p2):
    cor = cores[var_cor.get() - 1]
    espessura = var_espessura.get()
    ultimo_obj = canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=cor, width=espessura)
    lista_objs.append(ultimo_obj)

def calcular_raio(p1, p2):
    #raio = raiz(quadrado(Xp2 - Xp1) + quadrado(Yp2 - Yp1))
    return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

def desenhar_circulo(p1, p2):
    cor = cores[var_cor.get() - 1]
    espessura = var_espessura.get()
    raio = calcular_raio(p1, p2)
    x = p1[0]
    y = p1[1]
    x0 = x - raio
    y0 = y - raio
    x1 = x + raio
    y1 = y + raio
    ultimo_obj = canvas.create_oval(x0, y0, x1, y1, outline=cor, width=espessura)
    lista_objs.append(ultimo_obj)

def desenhar_elipse(p1, p2):
    cor = cores[var_cor.get() - 1]
    espessura = var_espessura.get()
    ultimo_obj = canvas.create_oval(p1[0], p1[1], p2[0], p2[1], outline=cor, width=espessura)
    lista_objs.append(ultimo_obj)

def desenhar_retangulo(p1, p2):
    cor = cores[var_cor.get() - 1]
    espessura = var_espessura.get()
    ultimo_obj = canvas.create_rectangle(p1[0], p1[1], p2[0], p2[1], outline=cor, width=espessura)
    lista_objs.append(ultimo_obj)

def desenhar_solido(p1, p2):
    cor = cores[var_cor.get() - 1]
    espessura = var_espessura.get()
    ultimo_obj = canvas.create_rectangle(p1[0], p1[1], p2[0], p2[1], outline=cor, fill=cor, width=0)
    lista_objs.append(ultimo_obj)

def apagar_tudo():
    global lista_objs
    if len(lista_objs) > 0:
        canvas.delete("all")
        lista_objs = []
    else:
        messagebox.showwarning('Alerta', 'Nenhum objeto para apagar')

def apagar_ultimo():
    if len(lista_objs) > 0:
        canvas.delete(lista_objs[-1])
        del(lista_objs[-1])
    else:
        messagebox.showwarning('Alerta', 'Nenhum objeto para apagar')

def muda_mensagem():
    indice = var_objeto.get() - 1
    msg = mensagens_p1[indice]
    var_mensagem.set(msg)

def cor_canvas():
    cor = askcolor(title="Escolha a cor do canvas") #Cancelar = (None, None)
    canvas.configure(bg=cor[1])

def cor_janela():
    cor = askcolor(title="Escolha a cor da janela")  #Cancelar = (None, None)
    janela.configure(bg=cor[1])

def sobre():
     messagebox.showinfo('Sobre', 'Python CAD 1.0\nDesenvolvido por Valdeci Menon')

def donothing():
    pass


menubar = Menu(janela)

menu_arquivo = Menu(menubar, tearoff=0)
menu_arquivo.add_command(label="Novo", command=donothing)
menu_arquivo.add_command(label="Abrir", command=donothing)
menu_arquivo.add_command(label="Salvar", command=donothing)
menu_arquivo.add_command(label="Salvar como...", command=donothing)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=exit)

menu_desenhar = Menu(menubar, tearoff=0)
menu_desenhar.add_checkbutton(label="Linha", variable=var_objeto, onvalue=1, offvalue=0, command=muda_mensagem)
menu_desenhar.add_checkbutton(label="Circulo", variable=var_objeto, onvalue=2, offvalue=0, command=muda_mensagem)
menu_desenhar.add_checkbutton(label="Elipse", variable=var_objeto, onvalue=3, offvalue=0, command=muda_mensagem)
menu_desenhar.add_checkbutton(label="Retângulo", variable=var_objeto, onvalue=4, offvalue=0, command=muda_mensagem)
menu_desenhar.add_checkbutton(label="Sólido", variable=var_objeto, onvalue=5, offvalue=0, command=muda_mensagem)

menu_modificar = Menu(menubar, tearoff=0)
menu_modificar.add_command(label="Apagar último", command=apagar_ultimo)
menu_modificar.add_command(label="Apagar tudo", command=apagar_tudo)

menu_cor = Menu(menubar, tearoff=0)
menu_cor.add_checkbutton(label="Branco", variable=var_cor, onvalue=1, offvalue=0)
menu_cor.add_checkbutton(label="Preto", variable=var_cor, onvalue=2, offvalue=0)
menu_cor.add_checkbutton(label="Vermelho", variable=var_cor, onvalue=3, offvalue=0)
menu_cor.add_checkbutton(label="Verde", variable=var_cor, onvalue=4, offvalue=0)
menu_cor.add_checkbutton(label="Azul",  variable=var_cor, onvalue=5, offvalue=0)
menu_cor.add_checkbutton(label="Ciano", variable=var_cor, onvalue=6, offvalue=0)
menu_cor.add_checkbutton(label="Amarelo", variable=var_cor, onvalue=7, offvalue=0)
menu_cor.add_checkbutton(label="Magenta", variable=var_cor, onvalue=8, offvalue=0)

menu_espessura = Menu(menubar, tearoff=0)
menu_espessura.add_checkbutton(label="1", variable=var_espessura, onvalue=1, offvalue=0)
menu_espessura.add_checkbutton(label="2", variable=var_espessura, onvalue=2, offvalue=0)
menu_espessura.add_checkbutton(label="3", variable=var_espessura, onvalue=3, offvalue=0)
menu_espessura.add_checkbutton(label="4", variable=var_espessura, onvalue=4, offvalue=0)
menu_espessura.add_checkbutton(label="5",  variable=var_espessura, onvalue=5, offvalue=0)
menu_espessura.add_checkbutton(label="6", variable=var_espessura, onvalue=6, offvalue=0)
menu_espessura.add_checkbutton(label="7", variable=var_espessura, onvalue=7, offvalue=0)
menu_espessura.add_checkbutton(label="8", variable=var_espessura, onvalue=8, offvalue=0)

menu_opcoes = Menu(menubar, tearoff=0)
menu_opcoes.add_command(label="Cor do canvas", command=cor_canvas)
menu_opcoes.add_command(label="Cor da janela", command=cor_janela)
menu_opcoes.add_command(label="Sobre", command=sobre)

menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
menubar.add_cascade(label="Desenhar", menu=menu_desenhar)
menubar.add_cascade(label="Modificar", menu=menu_modificar)
menubar.add_cascade(label="Cor", menu=menu_cor)
menubar.add_cascade(label="Espessura", menu=menu_espessura)
menubar.add_cascade(label="Opções", menu=menu_opcoes)

canvas = Canvas(janela, width=1024, height=768, bg='lightgray', cursor='cross')
canvas.bind("<Button-1>", acao_clique)
canvas.pack()

#desenha uma linha no canvas: create_line (p1, p2, cor)
#canvas.create_line(0, 20, 100, 20, fill="green")
#canvas.grid(column=0, row=0)


mensagem = Label(janela, textvariable = var_mensagem).place(x = 0, y = 0)

janela.config(menu=menubar)
janela.mainloop()
