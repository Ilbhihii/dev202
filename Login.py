from subprocess import call
from tkinter import ttk,Tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def Seconnecter(event=None):
    Usernam=txtUsern.get()
    Password=txtPassword.get()
    if (Usernam=="" and Password==""):
        messagebox.showerror("","saisir les données")
        txtPassword.delete("0","end")
        txtUsern.delete("0","end")
    elif (Usernam=="admin" and Password=="admin"):
        txtUsern.delete("0","end")
        txtPassword.delete("0","end")
        root.destroy()
        call(["python", "Acceuil.py"], bufsize=0)
    else :
        messagebox.showwarning("","erreur de connexion")
        txtPassword.delete("0","end")
        txtUsern.delete("0","end")
        
        
root=Tk()
root.title("Connection")
root.geometry("400x300+450+200")
root.resizable(False,False)


image =Image.open("NeoLogo.jpg")
image = image.resize((400, 400))
photo = ImageTk.PhotoImage(image)

label_image = Label(root, image=photo)
label_image.place(x=5,y=60,width=400,height=200)

Title=Label(root,text="Connexion",font=("algerian",30),bg="cyan")
Title.place(x=0,y=0,width=400,height=70)

lbUsern=Label(root,text="Username")
lbUsern.place(x=40,y=100)
txtUsern=Entry(root)
txtUsern.place(x=100,y=100,width=200)

lbPassword=Label(root,text="Password")
lbPassword.place(x=40,y=150)
txtPassword=Entry(root,show="*")
txtPassword.place(x=100,y=150,width=200)

btnConnect=Button(root,text="Connecter",command=Seconnecter).place(x=160,y=220)
root.bind("<Return>", Seconnecter)


root.mainloop()