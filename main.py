from tkinter import *
import math
from PIL import Image, ImageTk

janela = Tk()
janela.configure(bg="gray")



janela.title("Calculadora Simples")
janela.geometry("320x300")

entrada = Entry(janela, bg="#DBE6F0", fg="#000000", font=("Arial", 14), relief="flat", justify="right", insertbackground="black")

entrada.grid(row=0, column=0, columnspan=8, padx=10, pady=10, sticky="we")


#Imagens operadores:
imagem_mais = PhotoImage(file="imagens/mais.png")
imagem_menos = PhotoImage(file="imagens/menos.png")
imagem_vezes = PhotoImage(file="imagens/vezes.png")
imagem_por = PhotoImage(file="imagens/por.png")
imagem_raizquadrada = PhotoImage(file="imagens/raizquadrada.png")
imagem_porcentagem = PhotoImage(file="imagens/porcentagem.png")
imagem_igual = PhotoImage(file="imagens/igual.png")

#Imagens números:
imagem_um = PhotoImage(file="imagens/um.png")
imagem_dois = PhotoImage(file="imagens/dois.png")
imagem_tres = PhotoImage(file="imagens/tres.png")
imagem_quatro = PhotoImage(file="imagens/quatro.png")
imagem_cinco = PhotoImage(file="imagens/cinco.png")
imagem_seis = PhotoImage(file="imagens/seis.png")
imagem_sete = PhotoImage(file="imagens/sete.png")
imagem_oito = PhotoImage(file="imagens/oito.png")
imagem_nove = PhotoImage(file="imagens/nove.png")
imagem_zero = PhotoImage(file="imagens/zero.png")

#Imagens extra
imagem_ponto = PhotoImage(file="imagens/ponto.png")
imagem_limpar = PhotoImage(file="imagens/limpar.png")
icone = PhotoImage(file="imagens/icone.png")
janela.iconphoto(False, icone)


#Definir funções para os botões:

def clicar_numero(numero):
    atual = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, str(atual) + str(numero))

def limpar():
    entrada.delete(0, END)

def somar():
    try:
        primeiro_numero = entrada.get()
        global n1
        global operacao 
        operacao = "soma"
        n1 = float(primeiro_numero)
        entrada.delete(0, END)
    except ValueError:
        entrada.delete(0, END)

def subtrair():
    try:
        primeiro_numero = entrada.get()
        global n1
        global operacao 
        operacao = "subtracao"
        n1 = float(primeiro_numero)
        entrada.delete(0, END)
    except ValueError:
        entrada.delete(0, END)

def multiplicar():
    try:
        primeiro_numero = entrada.get()
        global n1
        global operacao 
        operacao = "multiplicacao"
        n1 = float(primeiro_numero)
        entrada.delete(0, END)    
    except ValueError:
        entrada.delete(0, END)

def dividir():
    try:
        primeiro_numero = entrada.get()
        global n1
        global operacao 
        operacao = "divisao"
        n1 = float(primeiro_numero)
        entrada.delete(0, END)
    except ValueError:
        entrada.delete(0, END)    
     
       

def raiz_quadrada():
    try:
        numero = float(entrada.get())
        resultado = math.sqrt(numero)
        entrada.delete(0, END)
        entrada.insert(0, str(resultado))
    except ValueError:
        entrada.delete(0, END)
        

def porcentagem():
    try:
        numero = float(entrada.get())
        resultado = numero / 100
        entrada.delete(0, END)
        entrada.insert(0, str(resultado))
    except ValueError:
        entrada.delete(0, END)
                   

def igual():
    segundo_numero = entrada.get()
    entrada.delete(0, END)
    try:
        if operacao == "soma":
            entrada.insert(0, n1 + float(segundo_numero))
        elif operacao == "subtracao":
            entrada.insert(0, n1 - float(segundo_numero))
        elif operacao == "multiplicacao":
            entrada.insert(0, n1 * float(segundo_numero))
        elif operacao == "divisao":
            entrada.insert(0, n1 / float(segundo_numero))
        elif (operacao == ZeroDivisionError):
             entrada.insert(0, "Valor indefinido")
    except ZeroDivisionError:
        entrada.insert(0, "Valor indefinido")  
    except ValueError:
        entrada.insert(0, "Erro")
    except:            
        entrada.delete(0, END)
#Usar teclas:
def pressionar_tecla(event):
    tecla = event.char

    if tecla in "0123456789":
        clicar_numero(tecla)
    elif tecla == ".":
        clicar_numero(".")
    elif tecla == "+":
        somar()
    elif tecla == "-":
        subtrair()
    elif tecla == "*" or tecla == "x":
        multiplicar()
    elif tecla == "/":
        dividir()
    elif tecla == "r":
        raiz_quadrada()    
    elif tecla == "%":
        raiz_quadrada()    
    elif tecla == "\r":  # Enter
        igual()
    elif tecla == "\x08":  # Backspace
        apagar_ultimo_caractere() 
    elif tecla == "c":
        limpar()    

janela.bind("<Key>", pressionar_tecla)     

def apagar_ultimo_caractere():
    atual = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, atual[:-1])               

# Botões numéricos
botao_1 = Button(janela, text="1", padx=40, pady=20, image= imagem_um  ,command=lambda: clicar_numero(1), bd=0, highlightthickness=0, relief="flat")
botao_2 = Button(janela, text="2", padx=40, pady=20, image= imagem_dois ,command=lambda: clicar_numero(2),  bd=0, highlightthickness=0, relief="flat")
botao_3 = Button(janela, text="3", padx=40, pady=20, image= imagem_tres ,command=lambda: clicar_numero(3),  bd=0, highlightthickness=0, relief="flat")
botao_4 = Button(janela, text="4", padx=40, pady=20, image= imagem_quatro ,command=lambda: clicar_numero(4),  bd=0, highlightthickness=0, relief="flat")
botao_5 = Button(janela, text="5", padx=40, pady=20, image= imagem_cinco ,command=lambda: clicar_numero(5),  bd=0, highlightthickness=0, relief="flat")
botao_6 = Button(janela, text="6", padx=40, pady=20, image= imagem_seis ,command=lambda: clicar_numero(6),  bd=0, highlightthickness=0, relief="flat")
botao_7 = Button(janela, text="7", padx=40, pady=20, image= imagem_sete ,command=lambda: clicar_numero(7),  bd=0, highlightthickness=0, relief="flat")
botao_8 = Button(janela, text="8", padx=40, pady=20, image= imagem_oito ,command=lambda: clicar_numero(8),  bd=0, highlightthickness=0, relief="flat")
botao_9 = Button(janela, text="9", padx=40, pady=20, image= imagem_nove ,command=lambda: clicar_numero(9),  bd=0, highlightthickness=0, relief="flat")
botao_0 = Button(janela, text="0", padx=40, pady=20, image= imagem_zero ,command=lambda: clicar_numero(0),  bd=0, highlightthickness=0, relief="flat")
botao_ponto = Button(janela, text=".", padx=41, pady=20, image= imagem_ponto ,command=lambda: clicar_numero("."),  bd=0, highlightthickness=0, relief="flat")


# Botões de operação
botao_somar = Button(janela, text="+", padx=39, pady=20, image= imagem_mais, command=somar,  bd=0, highlightthickness=0, relief="flat")
botao_subtrair = Button(janela, text="-", padx=40.5, pady=20, image= imagem_menos, command=subtrair,  bd=0, highlightthickness=0, relief="flat")
botao_multiplicar = Button(janela, text="x", padx=40.5, pady=20, image= imagem_vezes, command=multiplicar,  bd=0, highlightthickness=0, relief="flat")
botao_dividir = Button(janela, text="÷", padx=40.5, pady=20, image= imagem_por, command=dividir,  bd=0, highlightthickness=0, relief="flat")
botao_raiz = Button(janela, text="√", padx=40, pady=20, image= imagem_raizquadrada, command=raiz_quadrada,  bd=0, highlightthickness=0, relief="flat")
botao_porcento = Button(janela, text="%", padx=40, pady=20, image= imagem_porcentagem, command=porcentagem,  bd=0, highlightthickness=0, relief="flat")
botao_igual = Button(janela, text="=", padx=88, pady=20, image= imagem_igual, command=igual,  bd=0, highlightthickness=0, relief="flat")
botao_limpar = Button(janela, text="Limpar", padx=76, pady=20, image= imagem_limpar, command=limpar,  bd=0, highlightthickness=0, relief="flat")



# Posicionamento dos botões
botao_1.grid(row=3, column=2)
botao_2.grid(row=3, column=3)
botao_3.grid(row=3, column=4)

botao_4.grid(row=2, column=2)
botao_5.grid(row=2, column=3)
botao_6.grid(row=2, column=4)

botao_7.grid(row=1, column=2)
botao_8.grid(row=1, column=3)
botao_9.grid(row=1, column=4)

botao_0.grid(row=4, column=2)
botao_limpar.grid(row=1, column=7)

botao_somar.grid(row=3, column=6, rowspan=2)
botao_igual.grid(row=4, column=7)
botao_subtrair.grid(row=3, column=7)
botao_multiplicar.grid(row=2, column=6)
botao_dividir.grid(row=2, column=7)

botao_raiz.grid(row=4, column=4)
botao_porcento.grid(row=1, column=6)
botao_ponto.grid(row=4, column=3)


janela.mainloop()
