from tkinter import ttk, Tk
from subprocess import call
from tkinter import*
from tkcalendar import DateEntry
from tkinter.filedialog import *
import datetime as dt
from cProfile import label
from tkinter import messagebox
import mysql.connector as mysql

# base de donneé
host = "localhost"
user = "root" 
password = ""
dbname = "stock"

def Insert():
    Référence = txtRéff.get()
    Nomproduit = txtNomProd.get()
    Datesortie = txtDate.get_date()
    Fournisseur = txtForni.get()
    QuantitéSotie = txtQuantité.get()
    
    if Référence == "" or Nomproduit == "" or Datesortie == "" or Fournisseur == "" or QuantitéSotie == "":
        messagebox.showerror("Alert", "Veuillez saisir toutes les informations")
    else:
        con = mysql.connect(host=host, user=user, password=password, database=dbname)
        cursor = con.cursor()
        cursor.execute("insert into sortie values(%s,%s,%s,%s,%s)",(Référence, Nomproduit, Datesortie, Fournisseur, QuantitéSotie))
        con.commit()
        con.close()
        messagebox.showinfo("Status", "Enregistrement réussi")
        
root=Tk()
root.title("Gestion d'achat")
root.geometry("840x720")
root.resizable(False,False)

#Réference
LbRéff=Label(root,text="Référence",bg="grey")
LbRéff.place(x=45,y=150)
txtRéff=Entry(root)
txtRéff.place(x=125,y=150,width=220)

#Nom de Produit
LbNomProd=Label(root,text="Nom de Produit",bg="grey")
LbNomProd.place(x=30,y=200)
txtNomProd=Entry(root)
txtNomProd.place(x=125,y=200,width=220)

#Date de reçus
LbDate=Label(root,text="Date de Reçus",bg="grey")
LbDate.place(x=35,y=250)
txtDate=DateEntry(root, background='darkblue', foreground='white', borderwidth=2,date_pattern='yyyy-mm-dd')
txtDate.place(x=125,y=250, width=220)

#Nom de fournisseur
LbForni=Label(root,text="fournisseur",bg="grey")
LbForni.place(x=450,y=150)
txtForni=Entry(root)
txtForni.place(x=600,y=150,width=220)

#Quantité
LbQuantité=Label(root,text="Quantité",bg="grey")
LbQuantité.place(x=470,y=200)
txtQuantité=Entry(root)
txtQuantité.place(x=600,y=200,width=220)

BtnInsert=Button(root,text="Insert",command=Insert).place(x=200,y=300,width=100)

root.mainloop()