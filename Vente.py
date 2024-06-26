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
    Référencesortie = txtRéff.get()
    Datesortie = txtDate.get_date()
    Fournisseur = txtForni.get()
    QuantitéSotie = txtQuantité.get()
    
    if Référencesortie == "" or Datesortie == "" or Fournisseur == "" or QuantitéSotie == "":
        messagebox.showerror("Alert", "Veuillez saisir toutes les informations.")
    else:
        try:
            con = mysql.connect(host=host, user=user, password=password, database=dbname)
            cursor = con.cursor()
            # Explicitly specify the column names in the INSERT statement
            cursor.execute("INSERT INTO sortie (Référencesortie, Datesortie, Fournisseur, QuantitéSotie) VALUES (%s, %s, %s, %s)", (Référencesortie, Datesortie, Fournisseur, QuantitéSotie))
            con.commit()
            messagebox.showinfo("Status", "Enregistrement réussi.")
        except mysql.Error as e:
            messagebox.showerror("Error", f"Impossible d'ajouter l'enregistrement: {e}")
        finally:
            cursor.close()
            con.close()
            
def Update():
    Référencesortie = txtRéff.get()
    Datesortie = txtDate.get_date()
    Fournisseur = txtForni.get()
    QuantitéSotie = txtQuantité.get()
    
    if Référencesortie == "":
        messagebox.showerror("Alert", "Veuillez saisir les informations que vous souhaitez modifier")
    else:
        con = mysql.connect(host=host, user=user, password=password, database=dbname)
        cursor = con.cursor()
        cursor.execute("UPDATE sortie SET  Datesortie = %s, Fournisseur = %s, QuantitéSotie = %s WHERE Référencesortie = %s", (Datesortie, Fournisseur, QuantitéSotie, Référencesortie))
        con.commit()

    
def Archiver():
    
    if(txtRéff.get()==""):
        messagebox.showerror("Alert","s'il-te-plait entrer le nom de produit")
        
    else:
        con=mysql.connect(host=host,user=user,password=password,database=dbname)
        cursor=con.cursor()
        cursor.execute("UPDATE sortie SET Archivé = 1 WHERE Référencesortie = %s", (txtRéff.get(),))
        con.commit()
        cursor.execute("SELECT * FROM entrée WHERE Archivé = 0")
        
    messagebox.showinfo("Status","Successfully Archivé")
    con.close()
    
def Select():
    if txtRéff.get()=="" :
        messagebox.showerror("Alert","Donner ID pour afficher")
        
    else:
        con = mysql.connect(host = host, user = user, password = password, database = dbname)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM sortie WHERE 	Référencesortie=%s", (txtRéff.get(),))
        rows=cursor.fetchall()
        
        for row in rows:
            txtDate.delete(0, "end")
            txtDate.set_date(row[1])
            txtForni.insert("0",row[2])
            txtQuantité.insert("0",row[3])
        
    con.close();

def Switch():
    
    call(["python","Acceuil.py"], bufsize=0)
        
root=Tk()
root.title("Gestion d'achat")
root.geometry("800x400")
root.resizable(False,False)
root.configure(background="#C1FFC1")

#Titre
Title=Label(root,text="Gestion de Sortie",bg="#8A360F",fg="white",font=("Times New Roman",35))
Title.place(x=-50,y=0,width=900,height=100)

#Réference
LbRéff=Label(root,text="Référence",bg="#C1FFC1",font=("Berlin Sans FB Demi",15))
LbRéff.place(x=10,y=126)
txtRéff=Entry(root)
txtRéff.place(x=115,y=135,width=220)

#Date de reçus
LbDate=Label(root,text="Date de Sortie",bg="#C1FFC1",font=("Berlin Sans FB Demi",12))
LbDate.place(x=7,y=197)
txtDate=DateEntry(root, background='darkblue', foreground='white', borderwidth=2,date_pattern='yyyy-mm-dd')
txtDate.place(x=115,y=200, width=220)

#Nom de fournisseur
LbForni=Label(root,text="Fournisseur",bg="#C1FFC1",font=("Berlin Sans FB Demi",15))
LbForni.place(x=380,y=126)
txtForni=Entry(root)
txtForni.place(x=500,y=135,width=220)

#Quantité
LbQuantité=Label(root,text="Quantité",bg="#C1FFC1",font=("Berlin Sans FB Demi",15))
LbQuantité.place(x=380,y=195)
txtQuantité=Entry(root)
txtQuantité.place(x=500,y=200,width=220)

BtnInsert=Button(root,text="Insert",command=Insert).place(x=150,y=300,width=100)
BtnUpdat=Button(root,text="Update",command=Update).place(x=300,y=300,width=100)
BtnDelete=Button(root,text="Archiver",command=Archiver).place(x=450,y=300,width=100)
BtnSelect=Button(root,text="Select",command=Select).place(x=600,y=300,width=100)
Btnreturn=Button(root,text="Return à la page d'acceuil",command=Switch).place(x=300,y=350,width=220)


root.mainloop()