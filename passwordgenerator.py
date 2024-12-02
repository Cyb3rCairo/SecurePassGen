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
        pwlenght = int(entrada.get())  
        minhasenha = ''

        
        for _ in range(senhalength):
            minhasenha += chr(randint(33, 126))

        senha1.insert(0, minhasenha)  
    except ValueError:
        senha1.insert(0, "Digite um número válido!")


def copiar():
    pyperclip.copy(senha1.get()) 
    
def salvarsenha():
    salvarsenha = senha1.get()
    if salvarsenha:
        with open('senhas.txt', 'a') as file:
            file.write(" Senha: " + salvarsenha + '\n')  
        print("Senha salva com sucesso!")
        entrada.delete(0, 'end')
    else:
        print('error')
        
texto = CTkLabel(master=janela, text="BOTA OS NÚMERO")
texto.pack(padx=10, pady=10)

entrada = CTkEntry(master=janela)
entrada.pack(padx=20, pady=5)

senhalabel = CTkLabel(master=janela, text="SUA SENHA")
senhalabel.pack(padx=10, pady=10)

senha1 = CTkEntry(master=janela)
senha1.pack(padx=10, pady=5)

myframe = Frame(janela)
myframe.pack(pady=20)

botaoGerarSenha = Button(myframe, text="GERE SUA SENHA", command=password)
botaoGerarSenha.grid(row=0, column=0, padx=5, pady=10)

botaoCopiarSenha = Button(myframe, text="COPIE SUA SENHA", command=copiar)
botaoCopiarSenha.grid(row=0, column=1, padx=5)

botaosalvar = Button(janela, text='SALVE SUA SENHA', command=salvarsenha)
botaosalvar.pack(padx=10, pady=5)

janela.mainloop()
