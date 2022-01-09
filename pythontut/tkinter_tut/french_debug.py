#coding:utf-8

from tkinter import *
import sqlite3


with sqlite3.connect('base_le_chat.db') as db:
    curs = db.cursor()

creat_table = """CREATE TABLE IF NOT EXISTS client_le_chat (
    ID_EMP INTEGER NULL PRIMARY KEY,
    nom TEXT NOT NULL ,
    prenom TEXT NOT NULL,
    tel TEXT NULL,
    mail TEXT NOT NULL,
    adresse TEXT NULL,
    code_postal INTEGER NULL,
    commentaires TEXT NULL,
    sexe INTEGER NOT NULL);"""

curs.execute(creat_table)

db.commit()
curs.close()
db.close()


class deb:


    def __init__(self,fenetre):


        self.nom=StringVar()
        self.prenom=StringVar()
        self.tel=StringVar()
        self.mail=StringVar()
        self.adresse=StringVar()
        self.code_postal=IntVar()
        self.commentaires=StringVar()
        self.sex=IntVar()
        self.fen()








    def fen(self):

        self.Nom = Label(fenetre, text = 'Nom : ')
        self.Champ_nom = Entry(fenetre, textvariable= self.nom, width=31)

        self.Prenom = Label(fenetre, text = 'Prénom : ',)
        self.Champ_prenom = Entry(fenetre, textvariable= self.prenom, width=31)

        self.Tel = Label(fenetre, text = 'Tel : ')
        self.Champ_tel = Entry(fenetre, textvariable= self.tel,width=31)

        self.Mail = Label(fenetre, text = 'Adresse mail : ')
        self.Champ_mail = Entry(fenetre, textvariable= self.mail,width=31)

        self.Adresse = Label(fenetre, text = 'adresse : ')
        self.Champ_adresse = Entry(fenetre, textvariable= self.adresse,width=31)

        self.Code_postal = Label(fenetre, text = 'code_postal : ')
        self.Champ_code_postal = Entry(fenetre, textvariable= self.code_postal,width=31)

        self.Commentaires = Label(fenetre, text = 'Commentaires : ')
        self.Champ_commentair = Entry(fenetre, textvariable= self.commentaires,width=31)

        self.Sexe = Label(fenetre, text = 'Sexe : ')


        self.homme= Radiobutton (fenetre, text="homme", variable=self.sex, value=1)
        self.femme= Radiobutton (fenetre, text="femme", variable=self.sex, value=2)

        self.envoyer= Button (fenetre, text="Envoyer",command=self.Envoyer, pady=2)
        self.effacer= Button (fenetre, text="Réeinitialiser", command=self.Effacer, pady=2)


        self.Nom.grid(column=0, row=0, sticky='w')
        self.Champ_nom.grid(column=1, row=0, sticky='sw', columnspan=2, padx=10)
        self.Prenom.grid(column=0, row=1,sticky='w',pady=2)
        self.Champ_prenom.grid(column=1, row=1,columnspan=2)
        self.Tel.grid(column=0, row=2, sticky='w',pady=2)
        self.Champ_tel.grid(column=1, row=2,columnspan=2)
        self.Mail.grid(column=0, row=3,sticky='w',pady=2)
        self.Champ_mail.grid(column=1, row=3,columnspan=2)
        self.Adresse.grid(column=0, row=4,sticky='w',pady=2)
        self.Champ_adresse.grid(column=1, row=4,columnspan=2)
        self.Code_postal.grid(column=0, row=5,sticky='w',pady=2)
        self.Champ_code_postal.grid(column=1, row=5,columnspan=2)
        self.Commentaires.grid(column=0,row=6, sticky='w',pady=2)
        self.Champ_commentair.grid(column=1, row=6, ipady=25,columnspan=2)
        self.Sexe.grid(column=0,row=7, sticky='w',pady=2)
        self.homme.grid(column=1, row=7,sticky='sw')
        self.femme.grid(column=2, row=7,sticky='sw')
        self.envoyer.grid(column=1, row=8,sticky='sw', pady=20)
        self.effacer.grid(column=2, row=8,sticky='sw',pady=20)

    def Envoyer(self):
        no = self.nom
        pr = self.prenom
        te = self.tel
        ma = self.mail
        ad = self.adresse
        cod = self.code_postal
        com = self.commentaires
        se = self.sex

        print("Bonjour {} {} {} tel numero {} mail : {} commentaires :{} ".format(self.sex.get(),self.nom.get(),self.prenom.get(),self.tel.get(),self.mail.get(),self.commentaires.get()))



        with sqlite3.connect('base_le_chat.db') as db:
            curs = db.cursor()
            curs.execute("INSERT INTO client_le_chat(nom,prenom,tel,mail,adresse,code_postal,commentaires,sexe) VALUES (?,?,?,?,?,?,?,?)",[(self.nom.get()),(self.prenom.get()),(self.tel.get()),(self.mail.get()),(self.adresse.get()),(self.code_postal.get()),(self.commentaires.get()),(self.sex.get())])

            #nv = [no,pr,te,ma,ad,cod,com,se]
            #insert = 'INSERT INTO client_le_chat(nom,prenom,tel,mail,adresse,code_postal,commentaires,sexe) VALUES (?,?,?,?,?,?,?,?)',(no,pr,te,ma,ad,cod,com,se)


            #insert = 'INSERT INTO client_le_chat(nom,prenom,tel,mail,adresse,code_postal,commentaires,sexe) VALUES (?,?,?,?,?,?,?,?)'
            #curs.execute(insert,[(self.nom.get()),(self.prenom.get()),(self.tel.get()),(self.mail.get()),(self.adresse.get()),(self.code_postal.get()),(self.commentaires.get()),(self.sex.get())])


        db.commit()
        curs.close()
        db.close()

    def Effacer(self):
        self.Champ_nom.delete(0,END)
        self.Champ_prenom.delete(0,END)
        self.Champ_tel.delete(0,END)
        self.Champ_mail.delete(0,END)
        self.Champ_adresse.delete(0,END)
        self.Champ_code_postal.delete(0,END)
        self.Champ_commentair.delete(0,END)

fenetre = Tk()
fenetre.title("Le Chat")
fenetre.geometry("1400x900")
r1 = deb(fenetre)
fenetre.mainloop()
