from tkinter import ttk, Tk
from subprocess import call
from tkinter import*
from tkcalendar import DateEntry
from cProfile import label
from tkinter import messagebox
import mysql.connector as mysql


host = "localhost"
user = "root"
password = ""
dbname = "stock"

def Insert():
    Référence=txtRéff.get()
    NomProduit=txtNomProd.get()
    Datereçus=txtDate.get_date()
    Fournisseur=txtForni.get()
    Quantité=txtQuantité.get()
    
    if(Référence=="" or NomProduit=="" or Datereçus=="" or Fournisseur=="" or Quantité==""):
        messagebox.showerror("Alert","s'il-te-plait entrer tous les information")
    else:
        con=mysql.connect(host=host,user=user,password=password,database=dbname)
        cursor=con.cursor()
        cursor.execute("INSERT INTO entrée (Référence, NomProduit, Datereçus, Fournisseur, Quantité) VALUES (%s, %s, %s, %s, %s)", (Référence, NomProduit, Datereçus, Fournisseur, Quantité))

        cursor.execute("commit")
        
        messagebox.showinfo("Status","Successfully")
        con.close()
        
def Update():
    Référence = txtRéff.get()
    NomProduit = txtNomProd.get()
    Datereçus = txtDate.get_date()
    Fournisseur = txtForni.get()
    Quantité = txtQuantité.get()
    
    if Référence == "":
        messagebox.showerror("Alert", "Veuillez saisir les informations que vous souhaitez modifier")
    else:
        con = mysql.connect(host=host, user=user, password=password, database=dbname)
        cursor = con.cursor()
        cursor.execute("UPDATE entrée SET NomProduit = %s, Datereçus = %s, Fournisseur = %s, Quantité = %s WHERE Référence = %s", (NomProduit, Datereçus, Fournisseur, Quantité, Référence))
        con.commit()
        for item in Table.get_children():
            if Table.item(item, "values")[0] == Référence:
                Table.item(item, values=(Référence,NomProduit, Datereçus, Fournisseur, Quantité, Référence))
        con.commit()
        for item in Table.get_children():
                break
        con.close()
        messagebox.showinfo("Status", "Mise à jour effectuée avec succès")
        
        
def Delete():
    
    if(txtRéff.get()==""):
        messagebox.showerror("Alert","s'il-te-plait entrer le nom de produit")
        
    else:
        con=mysql.connect(host=host,user=user,password=password,database=dbname)
        cursor=con.cursor()
        cursor.execute("delete from entrée where Référence='"+txtRéff.get()+"'")
        cursor.execute("commit")
        for item in Table.get_children():
            if Table.item(item, "values")[0] == txtRéff.get():
                Table.delete(item)
                break
        
    messagebox.showinfo("Status","Successfully deleted")
    con.close()
    
def Clear():
    txtRéff.delete(0,"end")
    txtNomProd.delete(0,"end")
    txtDate.set_date(None)
    txtForni.delete(0,"end")
    txtQuantité.delete(0,"end")
    
def Select():
    if txtRéff.get()=="" :
        messagebox.showerror("Alert","Donner ID pour afficher")
        
    else:
        con = mysql.connect(host = host, user = user, password = password, database = dbname)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM entrée WHERE Référence=%s", (txtRéff.get(),))
        rows=cursor.fetchall()
        
        for row in rows:
            txtNomProd.insert("0",row[1])
            txtDate.delete(0, "end")
            txtDate.set_date(row[2])
            txtForni.insert("0",row[3])
            txtQuantité.insert("0",row[4])
        
    con.close();
    
def Affichage(): 
                
   displayed = set()
   con = mysql.connect(host=host, user=user, password=password, database=dbname)
   cursor = con.cursor()
   cursor.execute("SELECT * FROM entrée")
   for row in cursor.fetchall():
       if row[0] not in displayed:
           Table.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))
           displayed.add(row[0])
           con.close()

root=Tk()
root.title("Gestion d'achat")
root.geometry("750x350")
root.resizable(False,False)
root.configure(background="grey")

Titre=Label(root,text="Gestion d'entrée",font=("Algerian",40),bg="#3D59AB")
Titre.place(x=-150,y=0,width=1100,height=100)

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
LbForni.place(x=380,y=150)
txtForni=Entry(root)
txtForni.place(x=460,y=150,width=220)

#Quantité
LbQuantité=Label(root,text="Quantité",bg="grey")
LbQuantité.place(x=380,y=200)
txtQuantité=Entry(root)
txtQuantité.place(x=460,y=200,width=220)

BtnInsert=Button(root,text="Insert",command=Insert).place(x=70,y=300,width=100)
BtnDelet=Button(root,text="Delete",command=Delete).place(x=230,y=300,width=100)
BtnUpdate=Button(root,text="Update",command=Update).place(x=390,y=300,width=100)
BtnSelect=Button(root,text="Select",command=Select).place(x=570,y=300,width=100)
BtnAffiche=Button(root,text="Afficher",command=Affichage).place(x=250,y=350,width=100)
BtnAffiche=Button(root,text="clear",command=Clear).place(x=400,y=350,width=100)

Table=ttk.Treeview(root,columns=(1,2,3,4,5),height=5,show="headings")
Table.place(x=20,y=400,width=800,height=300)

Table.heading(1,text="Référence")
Table.heading(2,text="Nom de produit")
Table.heading(3,text="Date de reçus")
Table.heading(4,text="fournisseur")
Table.heading(5,text="Quantité")

Table.column(1,width=20)
Table.column(2,width=100)
Table.column(3,width=100)
Table.column(4,width=80)
Table.column(5,width=80)


root.mainloop()