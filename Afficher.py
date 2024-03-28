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
    rows = cursor.fetchall()
    
    for row in rows:
        if len(row) >= 10:
            print("Row does not have enough elements:", row)# Check if row has at least 10 elements
            
        else:
            if row not in displayed:
                Table.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                displayed.add(row[0])  # Print row for debugging purposes

    cursor.execute("UPDATE entrée, sortie SET sortie.QuantitéReste = entrée.Quantité - sortie.QuantitéSotie WHERE entrée.Référence = %s", (row[0],))
    con.commit()
    cursor.close()
    con.close()

           

            

root=Tk()
root.title("Affichage")
root.geometry("1300x720")
root.resizable(False,False)
root.configure(background="#53868B")

Title=Label(root,text="Affichage de stock entrée",font=("Times",20,"italic bold"))
Title.place(x=-100,y=0,width=1400,height=100)



Table=ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8,9,10),height=5,show="headings")
Table.place(x=0,y=100,width=1300,height=500)

Table.heading(1,text="Référence")
Table.heading(2,text="Nom de produit")
Table.heading(3,text="Date de reçus")
Table.heading(4,text="fournisseur d'entrée")
Table.heading(5,text="Quantité d'entrée")
Table.heading(6,text="Référence Sortie")
Table.heading(7,text="Date de sortie")
Table.heading(8,text="Fournisseur de sortie")
Table.heading(9,text="Quantité de sortie")
Table.heading(10,text="Quantité Reste")



Table.column(1,width=60)
Table.column(2,width=80)
Table.column(3,width=80)
Table.column(4,width=80)
Table.column(5,width=60)
Table.column(6,width=90)
Table.column(7,width=80)
Table.column(8,width=70)
Table.column(9,width=100)
Table.column(10,width=20)


brnaf=Button(root,text="view",command=Afficher).place(x=20,y=600)



root.mainloop()
