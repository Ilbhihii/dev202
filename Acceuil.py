from subprocess import call
from tkinter import ttk,Tk
from tkinter import *
from tkinter import messagebox

def Achat():
    call(["python", "Achat.py"], bufsize=0)

def Vente():
    call(["python", "Vente.py"], bufsize=0)
    
def Search():
    call(["python","search.py"],bufsize=0)
    
def Afficher():
    call(["python","Afficher.py"],bufsize=0)
    
def Logout():
    root.destroy()
    call(["python","Login.py"],bufsize=0)

root=Tk()
root.title("Gestion")
root.geometry("400x300")
root.resizable(False,False)



Title=Label(root,text="Gestion de Stock",font=("algerian",30),bg="cyan")
Title.place(x=0,y=0,width=400,height=90)


btnAchat=Button(root,text="Entrée",command=Achat).place(x=100,y=130,width=200)
btnVente=Button(root,text="Sortie",command=Vente).place(x=100,y=165,width=200)
btnSearch=Button(root,text="Recherche",command=Search).place(x=100,y=200,width=200)
btnAfficher=Button(root,text="Afficher au tableau",command=Afficher).place(x=100,y=230,width=200)
btnLogout=Button(root,text="Logout",command=Logout,bg="#B22222").place(x=355,y=90)



root.mainloop()