from tkinter import ttk, Tk
from tkinter import*
from subprocess import call
from tkinter.filedialog import *
import datetime as dt
from cProfile import label
from tkinter import messagebox

def Login():
    username = txUsnam.get()
    password = txPass.get()

    if not username or not password:
        messagebox.showwarning("Error", "Veuillez saisir le nom d'utilisateur et le mot de passe.")
        return
    if username == "admin" and password == "admin":
        root.destroy()
        call(["python","Acceuil.py"],bufsize=0)
    else:
        messagebox.showerror("Error", "Nom d'utilisateur ou mot de passe incorrect.")



root=Tk()
root.title("Gestion d'achat")
root.geometry("400x250")
root.resizable(False,False)
root.configure(background="#B2DFEE")

#Titre
Title=Label(root,text="Connexion",font=("Algerian",30),bg="#1C86EE")
Title.place(x=-50,y=0,width=500,height=90)

#Username
LbUsnam=Label(root,text="Username",font=("Algerian",15),bg="#B2DFEE")
LbUsnam.place(x=50,y=100)
txUsnam=Entry(root)
txUsnam.place(x=160,y=105,width=150)

#Password
LbPass=Label(root,text="Password",font=("Algerian",14),bg="#B2DFEE")
LbPass.place(x=50,y=140)
txPass=Entry(root,show="*")
txPass.place(x=160,y=144,width=150)

#Button connecter
btnVali=Button(root,text="Login",command=Login).place(x=150,y=200,width=100)
root.mainloop()