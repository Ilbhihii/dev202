from tkinter import ttk, Tk
from subprocess import call
from tkinter import*
from tkinter import messagebox
import mysql.connector as mysql

host = "localhost"
user = "root"
password = ""
dbname = "stock"

def Afficher():
    con = mysql.connect(host=host, user=user, password=password, database=dbname)
    cursor = con.cursor()
    cursor.execute("SELECT Quantité, QuantitéSotie FROM entrée JOIN sortie ON entrée.Quantité = sortie.QuantitéSortie WHERE entrée.Nomproduit = %s",(Prod))
    rows = cursor.fetchall()

    

root=Tk()
root.title("Gestion d'achat")
root.geometry("600x350")
root.resizable(False,False)
root.configure(background="grey")


Tittle=Label(root,text="Quantité restant dans le stock",font=("Times",20))
Tittle.place(x=-150,y=0,width=900,height=80)

LbProd=Label(root,text="Nom de produit",bg="grey")
LbProd.place(x=10,y=117)
Prod=Entry(root)
Prod.place(x=110,y=120)

LbCal=Label(root,text="Quantité restant",bg="grey")
LbCal.place(x=300,y=117)
Calcule=Entry(root,textvariable=Afficher)
Calcule.place(x=400,y=120,width=150)

root.mainloop()