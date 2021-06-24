import os, sys, sqlite3, tkinter
def ende():
    main.destroy()

#-----function to show column in a Text
def datenzeigen():
    label=tkinter.Label(fr1, text=listbox.get("active"))
    
    string=listbox.get("active")
    SplitListe=string.split()

    eName.delete(0, 'end')
    eVorname.delete(0, 'end')
    ePersonalnummer.delete(0, 'end')
    eGehalt.delete(0, 'end')
    eGeburtstag.delete(0, 'end')

    eName.insert(0,SplitListe[0])
    eVorname.insert(0,SplitListe[1])
    ePersonalnummer.insert(0,SplitListe[2])
    eGehalt.insert(0,SplitListe[3])
    eGeburtstag.insert(0,SplitListe[4])                  

#-----function to display dataset
def DatenLaden():
    connection=sqlite3.connect("firma.db")
    cursor=connection.cursor()

    sql="SELECT *FROM personen"
    cursor.execute(sql)

    for dsatz in cursor:
        listbox.insert("end", f"{dsatz[0]:<15}{dsatz[1]:<12}{dsatz[2]:<10}{dsatz[3]:<10}{dsatz[4]:<12}")
        listbox.pack(side="top")
        
    connection.close()

#-----function to enter new values to DB
def DatenEingabe():
    Name=eName.get()

    Vorname=eVorname.get()

    Personalnummer=ePersonalnummer.get()

    Gehalt=eGehalt.get()

    Geburtstag=eGeburtstag.get()

    connection=sqlite3.connect("firma.db")
    cursor=connection.cursor()

    sql=("INSERT INTO personen VALUES(?,?,?,?,?);")
    cursor.execute(sql, (Name,Vorname,Personalnummer,Gehalt,Geburtstag)) 
    connection.commit()
    connection.close()

    eName.delete(0, 'end')
    eVorname.delete(0, 'end')
    ePersonalnummer.delete(0, 'end')
    eGehalt.delete(0, 'end')
    eGeburtstag.delete(0, 'end')

    listbox.delete(0, tkinter.END)
    DatenLaden()
#---------------Aufgabe 4 a)-------------------------------------------------------------#
def DatenÄndern():
    Name=eName.get()

    Vorname=eVorname.get()

    Personalnummer=ePersonalnummer.get()

    Gehalt=eGehalt.get()

    Geburtstag=eGeburtstag.get()

    connection=sqlite3.connect("firma.db")
    cursor=connection.cursor()

    sql="UPDATE personen SET name=?, vorname=?, personalnummer=?," \
         "gehalt=?, geburtstag=? WHERE personalnummer=?"

    cursor.execute(sql,(Name,Vorname,Personalnummer,Gehalt,Geburtstag,Personalnummer))
    connection.commit()
    connection.close()

    eName.delete(0, 'end')
    eVorname.delete(0, 'end')
    ePersonalnummer.delete(0, 'end')
    eGehalt.delete(0, 'end')
    eGeburtstag.delete(0, 'end')

    listbox.delete(0, tkinter.END)
    DatenLaden()
    
#--------zum Leeren der Textfelder-------
def Leeren():
    Name=eName.get()

    Vorname=eVorname.get()

    Personalnummer=ePersonalnummer.get()

    Gehalt=eGehalt.get()

    Geburtstag=eGeburtstag.get()
    
    eName.delete(0, 'end')
    eVorname.delete(0, 'end')
    ePersonalnummer.delete(0, 'end')
    eGehalt.delete(0, 'end')
    eGeburtstag.delete(0, 'end')

#-----------Aufgabe 4 b)

def DatenLöschen():

    Personalnummer=ePersonalnummer.get()

    connection=sqlite3.connect("firma.db")
    cursor=connection.cursor()

    sql="DELETE FROM personen WHERE personalnummer=?"
    cursor.execute(sql,([Personalnummer]))
    connection.commit()
    connection.close()

    eName.delete(0, 'end')
    eVorname.delete(0, 'end')
    ePersonalnummer.delete(0, 'end')
    eGehalt.delete(0, 'end')
    eGeburtstag.delete(0, 'end')

    listbox.delete(0, tkinter.END)
    DatenLaden()
    
    
#--------------------------------------------------------------------------------#  

if os.path.exists("firma.db"):
    #main interface with buttons, listbox and label
    main=tkinter.Tk()
    fr1=tkinter.Frame(main, width=1000, height=500, relief="sunken", bd=1)
    fr1.pack(side="top")

    fr2=tkinter.Frame(main, width=500, height=250)
    fr2.pack(side="bottom")

    listbox=tkinter.Listbox(fr1, height=0, width=70, relief="sunken", bd=1)
    DatenLaden()
    
    name=tkinter.Label(fr2,text="Name")
    eName=tkinter.Entry(fr2)

    vorname=tkinter.Label(fr2,text="Vorname")
    eVorname=tkinter.Entry(fr2)

    personalnummer=tkinter.Label(fr2,text="Personalnummer")
    ePersonalnummer=tkinter.Entry(fr2)

    gehalt=tkinter.Label(fr2,text="Gehalt")
    eGehalt=tkinter.Entry(fr2)

    geburtstag=tkinter.Label(fr2,text="Geburtstag")
    eGeburtstag=tkinter.Entry(fr2)

    name.pack()
    eName.pack()

    vorname.pack()
    eVorname.pack()

    personalnummer.pack()
    ePersonalnummer.pack()

    gehalt.pack()
    eGehalt.pack()

    geburtstag.pack()
    eGeburtstag.pack()
    
    bEnde=tkinter.Button(fr1, text ="Ende", command=ende)
    bEnde.pack(side="right", padx=5, pady=5)

    bLeeren=tkinter.Button(fr1, text="Leeren", command=Leeren)
    bLeeren.pack(side="right", padx=5, pady=5)
    
    bDatenZeigen=tkinter.Button(fr1, text="Daten Zeigen",command=datenzeigen)
    bDatenZeigen.pack(side="left", padx=5, pady=5)

    bDatenNeu=tkinter.Button(fr1, text="Neu", command=DatenEingabe)
    bDatenNeu.pack(side="left", padx=5, pady=5)

    bDatenÄndern=tkinter.Button(fr1, text="Ändern", command=DatenÄndern)
    bDatenÄndern.pack(side="left", padx=5, pady=5)
    
    bDatenLöschen=tkinter.Button(fr1, text="Löschen", command=DatenLöschen)
    bDatenLöschen.pack(side="left", padx=5, pady=5)

    main.mainloop()

else:
    
    main=tkinter.Tk()
    bEnde=tkinter.Button(main, text ="Ende", command=ende)
    lb1=tkinter.Label(main, text="DatenBank nicht vorhanden")
    lb1.pack()
    bEnde.pack()

    main.mainloop()

