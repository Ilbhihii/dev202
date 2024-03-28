from tkinter import ttk, Tk
from subprocess import call
from tkinter import*
from tkinter import messagebox
import mysql.connector as mysql


# base de donneé
host = "localhost"
user = "root" 
password = ""
dbname = "stock"



def Afficher():
    displayed = set()
    con = mysql.connect(host=host, user=user, password=password, database=dbname)
    cursor = con.cursor()
    cursor.execute("(SELECT entrée.*, sortie.DateSortie AS DS, sortie.Fournisseur AS FS, sortie.QuantitéSotie AS QS, entrée.Quantité - sortie.QuantitéSotie AS QR FROM entrée JOIN sortie ON entrée.Référence = sortie.Référencesortie) UNION ALL (SELECT entrée.*, NULL, NULL, NULL, NULL FROM entrée JOIN sortie ON entrée.Référence = sortie.Référencesortie WHERE entrée.Nomproduit = %s)", ('Nomproduit',))
    
    for row in cursor.fetchall(): 
        if row[0] not in displayed:
            Table.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            displayed.add(row[0])
            con.close()
        
def Switch():
    root.destroy()
    call(["python","Acceuil.py"],bufsize=0)

            

root=Tk()
root.title("Affichage")
root.geometry("1300x720")
root.resizable(False,False)
root.configure(background="#53868B")

Title=Label(root,text="Affichage de stock entrée",font=("Times",20,"italic bold"))
Title.place(x=-100,y=0,width=1400,height=100)



Table=ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8,9),height=5,show="headings")
Table.place(x=0,y=100,width=1300,height=500)

Table.heading(1,text="Référence")
Table.heading(2,text="Nom de produit")
Table.heading(3,text="Date de reçus")
Table.heading(4,text="fournisseur d'entrée")
Table.heading(5,text="Quantité d'entrée")
Table.heading(6,text="Date de sortie")
Table.heading(7,text="Fournisseur de sortie")
Table.heading(8,text="Quantité de sortie")
Table.heading(9,text="Quantité Reste")



Table.column(1,width=60)
Table.column(2,width=80)
Table.column(3,width=80)
Table.column(4,width=80)
Table.column(5,width=60)
Table.column(6,width=80)
Table.column(7,width=70)
Table.column(8,width=90)
Table.column(9,width=20)

Afficher()


btnReturn=Button(root,text="<-",command=Switch).place(x=0,y=600)

root.mainloop()