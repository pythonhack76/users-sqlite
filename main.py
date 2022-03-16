from tkinter import *

import sqlite3
with sqlite3.connect("details.db") as db:
    cursor=db.cursor()


cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username text NOT NULL, password text NOT NULL); """)

def add_new_user():
    
    newUsername = username.get()
    newPassword = password.get()

    cursor.execute("SELECT COUNT(*) from users WHERE username = '"+ newUsername + "' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Errore: Username già presente"
    elif newUsername  == '' or newPassword == '':
        error["text"] ="Errore: Tutti i campi devono essere compilati!"
    else:
        error["text"] = "Added New USers"
        cursor.execute("INSERT INTO users(username,password) VALUES(?,?)",(newUsername, newPassword))
        db.commit()

def delete_user():
    pass


def update_user():
    pass 



window = Tk()
window.geometry("500x200")
#errori 
error = Message(text="", width=160)
error.place(x = 30, y = 10)
error.config(padx=0)

label1 = Label(text = "inserisci usenrame:")
label1.place(x = 30, y = 40)
label1.config(bg='lightgreen', padx=10)

username = Entry(text = "")
username.place(x=150, y=40, width=200, height=25)

label2 = Label(text = "Inserisci password:")
label2.place(x = 30, y = 80) 
label2.config(bg='lightgreen', padx=0)

password = Entry(text = "")
password.place(x=150, y=80, width=200, height=25)

button = Button(text = "aggiungi", command = add_new_user)
button.place(x=150, y=120, width=75, height=35)




window.mainloop()
