from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import mysql.connector
from tksheet import Sheet
import froms_and_query
    

def home_page():
    
    def widget_destroy():
        for widget in home.winfo_children():
            widget.destroy()
    
 # --------------------------------------------------------------------------------------------------------- #
        
    def insert():
        def back():
            root.destroy()
            home_page()
        
        def submit_insert():
            if(selected.get()=="Student"):
                root.destroy()
                froms_and_query.insert_student()

            elif(selected.get()=="Hostel Staff"):
                root.destroy()
                froms_and_query.insert_hostel_staff()
            
            elif(selected.get()=="Visitor"):
                root.destroy()
                froms_and_query.insert_visitor()
            
            elif(selected.get()=="Furniture"):
                root.destroy()
                froms_and_query.insert_furniture()
        
        widget_destroy()
        options=["Student","Hostel Staff","Visitor", "Furniture"]
        selected=StringVar()
        Label(home, text="where do you want to insert?: ", font=font.Font(size=15)).grid(row=0,column=0, pady=5)
        drop=OptionMenu(home, selected, *options)
        drop.grid(row=0,column=1, pady=5)

        submit= Button(home, text="Submit", font=font.Font(size=10), command=submit_insert)
        submit.grid(row=1,column=0, pady=5)

        back=Button(home, text="Back", font=font.Font(size=10), command=back)
        back.grid(row=1,column=1, pady=5)
# --------------------------------------------------------------------------------------------------------- #    
    def update():
        def back():
            root.destroy()
            home_page()
        
        def submit_update():
            if(selected.get()=="Student"):
                root.destroy()
                froms_and_query.update_student()

            elif(selected.get()=="Hostel Staff"):
                root.destroy()
                froms_and_query.update_hostel_staff()
            
            elif(selected.get()=="Fee"):
                root.destroy()
                froms_and_query.update_fee()

        
        widget_destroy()
        options=["Student","Hostel Staff","Fee"]
        selected=StringVar()
        Label(home, text="Where you want to update?: ", font=font.Font(size=15)).grid(row=0,column=0, pady=5)
        drop=OptionMenu(home, selected, *options)
        drop.grid(row=0,column=1, pady=5)

        submit= Button(home, text="Submit", font=font.Font(size=10), command=submit_update)
        submit.grid(row=1,column=0, pady=5)

        back=Button(home, text="Back", font=font.Font(size=10), command=back)
        back.grid(row=1,column=1, pady=5)

        

# --------------------------------------------------------------------------------------------------------- #    
    def search():
        def submit_select():
            display=Tk()
            a=selected.get()

            con = mysql.connector.connect(
                host="localhost", user="root", password="", database="hostel_management_system")
            cur = con.cursor()

            query1 = "select * from %s"%(a)
            cur.execute(query1)
            table = cur.fetchall()

            sheet=Sheet(display,show_x_scrollbar = True, show_y_scrollbar = True)
            sheet.set_sheet_data(data=table)
            sheet.pack()

            cur.close()
            con.close()

        
        def back():
            root.destroy()
            home_page()
        widget_destroy()
        Label(home, text="select the table you want to see: ", font=font.Font(size=15)).grid(row=0,column=0, pady=5)
        options=["students", "hostel_staff", "fee", "visitor", "room", "hostel", "furniture", "mess"]
        selected=StringVar()
        drop=OptionMenu(home, selected, *options)
        drop.grid(row=0, column=1, pady=5)

        submit= Button(home, text="Submit", font=font.Font(size=10), command=submit_select)
        submit.grid(row=1,column=0, pady=5)

        back=Button(home, text="Back", font=font.Font(size=10), command=back)
        back.grid(row=1,column=1, pady=5)

        
# --------------------------------------------------------------------------------------------------------- #
    def delete():
        def back():
            root.destroy()
            home_page()

        def submit_delete():
            if(selected.get()=="Student"):
                root.destroy()
                froms_and_query.delete_student()

            elif(selected.get()=="Hostel Staff"):
                root.destroy()
                froms_and_query.delete_hostel_staff()

        widget_destroy()
        options=["Student","Hostel Staff"]
        selected=StringVar()
        Label(home, text="select from where you want to delete: ", font=font.Font(size=15)).grid(row=0,column=0, pady=5)
        drop=OptionMenu(home, selected, *options)
        drop.grid(row=0,column=1, pady=5)

        submit= Button(home, text="Submit", font=font.Font(size=10), command=submit_delete)
        submit.grid(row=1,column=0, pady=5)

        back=Button(home, text="Back", font=font.Font(size=10), command=back)
        back.grid(row=1,column=1, pady=5)
            

# --------------------------------------------------------------------------------------------------------- #        

    def select():
        a=clicked.get()
        if(a=="Delete"):
            delete()

        elif(a=="Update"):
            update()
        
        elif(a=="Insert"):
            insert()
        
        elif(a=="Search"):
            search()


    root=Tk()
    root.title("HOME PAGE")
    root.geometry('1400x700')
    
    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    home=Frame(root)
    home.place(relx=.5,rely=.5, anchor=CENTER)
    option=["Insert", "Update", "Delete", "Search"]

    clicked=StringVar()
    Label(home, text="Enter the operation to perform: ", font=font.Font(size=15)).grid(row=0, column=0, pady=5)

    drop = OptionMenu(home, clicked, *option)
    drop.grid(row=0, column=1, pady=5)

    submit= Button(home, text="submit", font=font.Font(size=10), command=select)
    submit.grid(row=1,column=0,columnspan=2, pady=5)

    home.mainloop()
