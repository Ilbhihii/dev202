from subprocess import call
from tkinter import ttk,Tk
from tkinter import *
from tkinter import messagebox

def Achat():
    root.destroy()
    call(["python", "Achat.py"], bufsize=0)

def Vente():
    root.destroy()
    call(["python", "Vente.py"], bufsize=0)

root=Tk()
root.title("Gestion")
root.geometry("400x200+450+200")
root.resizable(False,False)



Title=Label(root,text="Gestion de Stock",font=("algerian",30),bg="cyan")
Title.place(x=0,y=0,width=400,height=90)


btnAchat=Button(root,text="Entrée",command=Achat).place(x=100,y=130,width=100)
btnVente=Button(root,text="Sortie",command=Vente).place(x=200,y=130,width=100)



root.mainloop()