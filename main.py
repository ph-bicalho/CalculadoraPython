from cgitb import text
import string
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import color, right
from wsgiref.validate import validator

#   cores
cor1 = "#363636"
cor2 = "#1c1c1c"
cor3 = "#ffffff"
cor4 = "#bdbdbd"

# criando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.config(bg=cor2)

# criando frames

frame_tela = Frame(janela, width=300, height=60, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=340, bg=cor2)
frame_corpo.grid(row=1, column=0)


#DEFININDO VALORES

todos_valores = ''

# mostrando os valores na tela

def inserir_valores(event):
    global todos_valores

    todos_valores= todos_valores + str(event)

    # passando valor pra tela

    valor_texto.set(todos_valores)

# função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

# função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=17, height=2, padx=11, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 20'), fg=cor3, bg=cor1)
app_label.place(x=0,y=0)


# criando botões
b_1=Button(frame_corpo, command=limpar_tela, text="C", width=20, height=4, bg=cor2, fg=cor4)
b_1.place(x=0, y=0)
b_2=Button(frame_corpo, command= lambda: inserir_valores('%'), text="%", width=10, height=4, bg=cor2, fg=cor4)
b_2.place(x=73*2, y=0)
b_3=Button(frame_corpo, command= lambda: inserir_valores('/'), text="/", width=10, height=4, bg=cor2, fg=cor4)
b_3.place(x=73*3, y=0)

b_4=Button(frame_corpo, command= lambda: inserir_valores('7'), text="7", width=10, height=4, bg=cor2, fg=cor4)
b_4.place(x=0, y=70)
b_5=Button(frame_corpo, command= lambda: inserir_valores('8'),text="8", width=10, height=4, bg=cor2, fg=cor4)
b_5.place(x=73, y=70)
b_6=Button(frame_corpo, command= lambda: inserir_valores('9'), text="9", width=10, height=4, bg=cor2, fg=cor4)
b_6.place(x=73*2, y=70)
b_7=Button(frame_corpo, command= lambda: inserir_valores('*'), text="x", width=10, height=4, bg=cor2, fg=cor4)
b_7.place(x=73*3, y=70)

b_8=Button(frame_corpo, command= lambda: inserir_valores('4'), text="4", width=10, height=4, bg=cor2, fg=cor4)
b_8.place(x=0, y=70*2)
b_9=Button(frame_corpo, command= lambda: inserir_valores('5'), text="5", width=10, height=4, bg=cor2, fg=cor4)
b_9.place(x=73, y=70*2)
b_10=Button(frame_corpo, command= lambda: inserir_valores('6'), text="6", width=10, height=4, bg=cor2, fg=cor4)
b_10.place(x=73*2, y=70*2)
b_11=Button(frame_corpo, command= lambda: inserir_valores('-'), text="-", width=10, height=4, bg=cor2, fg=cor4)
b_11.place(x=73*3, y=70*2)

b_8=Button(frame_corpo, command= lambda: inserir_valores('1'), text="1", width=10, height=4, bg=cor2, fg=cor4)
b_8.place(x=0, y=70*3)
b_9=Button(frame_corpo, command= lambda: inserir_valores('2'), text="2", width=10, height=4, bg=cor2, fg=cor4)
b_9.place(x=73, y=70*3)
b_10=Button(frame_corpo, command= lambda: inserir_valores('3'), text="3", width=10, height=4, bg=cor2, fg=cor4)
b_10.place(x=73*2, y=70*3)
b_11=Button(frame_corpo, command= lambda: inserir_valores('+'), text="+", width=10, height=4, bg=cor2, fg=cor4)
b_11.place(x=73*3, y=70*3)

b_12=Button(frame_corpo, command= lambda: inserir_valores('0'), text="0", width=20, height=4, bg=cor2, fg=cor4)
b_12.place(x=0, y=70*4)
b_13=Button(frame_corpo, command= lambda: inserir_valores('.'), text=".", width=10, height=4, bg=cor2, fg=cor4)
b_13.place(x=73*2, y=70*4)
b_14=Button(frame_corpo, command= calcular , text="=", width=10, height=4, bg=cor2, fg=cor4)
b_14.place(x=73*3, y=70*4)

janela.mainloop()
