from tkinter import *
import os 
import keyboard
import random


def desliga():
    os.system("shutdown /s /t 1")

def disable():
    pass

def abrir_janela1():
    #Gerar janelas
    janela1 = Tk()
    janela1.title("Janela")
    janela1.geometry('350x350')
    
    #Gerar textos
    texto = Label(janela1,text='Quer fechar essa janela?')
    texto.grid(column=0, row=0, padx=10,pady=50)
    
    #Gerar botões
    b_sim = Button(janela1, text='SIM', command=abrir_janela2)
    b_nao = Button(janela1, text='NÃO', command=abrir_janela2)
    b_sim.grid(column=2,row=1, padx=10,pady=10)
    b_nao.grid(column=1,row=1, padx=10,pady=10)
    
    #Comandos bloqueados
    janela1.protocol("WM_DELETE_WINDOW", disable)
    if keyboard.is_pressed("alt") and keyboard.is_pressed("F4"):
        pass
    if keyboard.is_pressed("Ctrl") and keyboard.is_pressed("alt"):
        pass
    janela1.mainloop()

def abrir_janela2():
    #Gerar janelas
    janela2=Toplevel()
    janela2.title('Janela')
    janela2.geometry('350x350')
    
    #Gerar textos
    texto = Label(janela2,text='Deseja Realmente fechar?')
    texto.grid(column=0, row=0, padx=10,pady=50)
    
    #Gerar botoes
    b_sim = Button(janela2, text='SIM', command=desliga)
    b_nao = Button(janela2, text='NÃO', command=abrir_janela1)
    b_sim.grid(column=2,row=1, padx=10,pady=10)
    b_nao.grid(column=1,row=1, padx=10,pady=10)
    
    #Comandos bloqueados
    janela2.protocol("WM_DELETE_WINDOW", disable)
    if keyboard.is_pressed("alt") and keyboard.is_pressed("F4"):
        pass
    if keyboard.is_pressed("Ctrl") and keyboard.is_pressed("alt"):
        pass


while True:
    abrir_janela1()