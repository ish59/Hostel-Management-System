from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
import mysql.connector
import home1

root=Tk()
root.title("LOGIN PAGE")
root.geometry('1400x700')

img = Image.open("2.png")
test= ImageTk.PhotoImage(img)

lbl=Label(image=test, borderwidth=0, highlightthickness=0)
lbl.place(relx=.5, rely=.5, anchor=CENTER)

def login_page():
    main=Frame(root, padx=10, pady=10)
    main.place(relx=.5, rely=.5, anchor=CENTER)

    def clear_():
        username.delete(0, END)
        password.delete(0, END)

    def checkin():
        user_input = username.get()
        pass_input = password.get()

        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="login_info")
        cur = con.cursor()
        query1 = "select * from users_info"
        cur.execute(query1)
        table = cur.fetchall()


        for i in table:
            if(user_input == i[0] and pass_input == i[1]):
                a=0
                break
            else:
                a=1

        if(a==0):
            root.destroy()
            home1.home_page()
            
        else:
            messagebox.showerror("error","Wrong username or Password")

        cur.close()
        con.close()

    Label(main, text="LOGIN PAGE", font=font.Font(size=20)).grid(row=0, column=0,pady=5, columnspan=2)

    Label(main, text="Username: ", font=font.Font(size=15)).grid(row=1, column=0, pady=5)
    username = Entry(main, width=30)
    username.grid(row=1, column=1, pady=5)

    Label(main, text="Password: ", font=font.Font(size=15)).grid(row=2, column=0, pady=5)
    password = Entry(main,  width=30, show="*")
    password.grid(row=2, column=1, pady=5)

    sign_in = Button(main, padx=10, text="Sign in", font=font.Font(size=10), command=checkin)
    sign_in.grid(row=3, column=0, pady=5)
    clear = Button(main, padx=10, text="Clear", font=font.Font(size=10), command=clear_)
    clear.grid(row=3, column=1, pady=5)

    main.mainloop()
login_page()