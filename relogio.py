import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title("Lain Clock")
root.geometry("900x620")
root.maxsize(900, 620)
root.minsize(900, 620)
root.configure(background = '#141413')

def getOi():
    nomeUser = os.getlogin()
    oi.config(text = "Olá " + nomeUser)
def getData():
    dataHoje = strftime(" %A, %d %b %Y ")
    data.config(text = dataHoje)
def getHora():
    horario = strftime("%H:%M:%S")
    hora.config(text = horario)
    hora.after(1000, getHora)
def getLocal():
    localAtual = strftime("%Z")
    local.config(text = localAtual)


margem = tk.Canvas(root, width = 900, height = 120, bg='#141413', bd = 0, highlightthickness = 0, relief = "ridge")
margem.pack()
oi = Label(root, bg='#141413', fg = "#4c00a8", font = ("Jersey 15 Regular", 28))
oi.pack()
data = Label(root, bg='#141413', fg = "#4c00a8", font = ("Jersey 15 Regular", 28, "underline"))
data.pack(pady = 2)
hora = Label(root, bg='#141413', fg = "#4c00a8", font = ("Jersey 15 Regular", 125))
hora.pack(pady = 2)
local = Label(root, bg='#141413', fg = "#4c00a8", font = ("Jersey 15 Regular", 20))
local.pack(pady = 2)
img = PhotoImage(file = "img/lain.png")
lain = Label(root, image = img, bg='#141413', fg = "#4c00a8", height = 145).pack()


getOi()
getData()
getHora()
getLocal()

root.mainloop()