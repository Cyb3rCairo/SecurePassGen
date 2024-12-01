from tkinter import *
from random import randint
from customtkinter import *
import pyperclip  

janela = Tk()
janela.title("Password Generator")
janela.geometry("500x300")


def password():
    senha1.delete(0, END)
    try:
        senhalength = int(entrada.get())  
        minhasenha = ''

        
        for _ in range(senhalength):
            minhasenha += chr(randint(33, 126))

        senha1.insert(0, minhasenha)  
    except ValueError:
        senha1.insert(0, "Digite um número válido!")


def copiar():
    pyperclip.copy(senha1.get())  


texto = CTkLabel(master=janela, text="BOTA OS NÚMERO")
texto.pack(padx=10, pady=10)

entrada = CTkEntry(master=janela)
entrada.pack(padx=20, pady=5)

sla = CTkLabel(master=janela, text="SUA SENHA")
sla.pack(padx=10, pady=10)

senha1 = CTkEntry(master=janela)
senha1.pack(padx=10, pady=5)

myframe = Frame(janela)
myframe.pack(pady=20)

botao = Button(myframe, text="GERE SUA SENHA", command=password)
botao.grid(row=0, column=0, padx=5, pady=10)

botao2 = Button(myframe, text="COPIE SUA SENHA", command=copiar)
botao2.grid(row=0, column=1, padx=5)

janela.mainloop()
