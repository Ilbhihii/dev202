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

def Search():
    if txtRéff.get()=="":
        messagebox.showerror("Alert","aucun référence ")
    else:
        con=mysql.connect(host=host,user=user,password=password,database=dbname)
        cursor=con.cursor()
        cursor.execute("SELECT * FROM entrée WHERE Référence=%s", (txtRéff.get(),))
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                call(["python", "test2.py", str(row[0]), str(row[1]), str(row[2]), str(row[3])], bufsize=0)
        else:
            messagebox.showinfo("Information", "Aucun enregistrement trouvé pour cette référence")
    con.close()    
    
root=Tk()
root.title("Gestion d'achat")
root.geometry("500x200")
root.resizable(False,False)
root.configure(background="grey")


Tittle=Label(root,text="Recherche",font=("algerian",20))
Tittle.place(x=0,y=0,width=500,height=50)
#Réference
LbRéff=Label(root,text="Référence",bg="grey",font=("Times New Roman",15))
LbRéff.place(x=30,y=70)
txtRéff=Entry(root)
txtRéff.place(x=130,y=75,width=220)

BtnAffiche=Button(root,text="Search",command=Search).place(x=200,y=140,width=100)

root.mainloop()