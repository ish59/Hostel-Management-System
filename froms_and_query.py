from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tktimepicker import SpinTimePickerModern, constants
from PIL import ImageTk, Image
import home1
import mysql.connector

# --------------------------------------------------------------------------------------------------------- #

def delete_student():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    def submit_query():
        
        rollno_input=rollno.get()
        print(rollno_input)
        print(type(rollno_input))
        # entering data
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()

        query1 = "delete from students where roll_number=  '%s' ;" % (rollno_input)
        print(query1)
        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data removed succussfully.')


    def back():
        root.destroy()
        home1.home_page()


    Label(form, text="Enter the rollno you want to delete: ").grid(row=0, column=0)
    rollno = Entry(form, width=20)
    rollno.grid(row=0, column=1)

    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=7, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=7, column=1)

    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def delete_hostel_staff():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    def submit_query():
        staffId_input=staffId.get()

        # entering data
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()

        query1 = "delete from hostel_staff where emp_id=%s;"%(staffId_input)

        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data added succussfully.')


    def back():
        root.destroy()
        home1.home_page()


    Label(form, text="Enter the StaffID you want to delete: ").grid(row=0, column=0)
    staffId = Entry(form, width=20)
    staffId.grid(row=0, column=1)

    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=1, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=1, column=1)

    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def insert_student():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    # interface code
    def submit_query():
        name_input = name.get()
        f_name_input = f_name.get()
        rollno_input = rollno.get()
        dob_input = dob.get_date()
        hostel_input = hostel_id.get()
        roomid_input = selected.get()
        branch_input = branch.get()
        
        

        # entering data

        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()
        query1 = "INSERT INTO `students` (`roll_number`, `student_name`, `student_father_name`, `branch`, `room_id`, `hostel_id`, `DOB`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (rollno_input,name_input, f_name_input,branch_input, roomid_input, hostel_input, dob_input)

        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data entered successfully.')




    def back():
        root.destroy()
        home1.home_page()

    Label(form, text="Enter name of the student: ").grid(row=0, column=0)
    name = Entry(form, width=20)
    name.grid(row=0, column=1)

    Label(form, text="Enter father's name: ").grid(row=1, column=0)
    f_name = Entry(form, width=20)
    f_name.grid(row=1, column=1)

    Label(form, text="Enter rollno. of the student: ").grid(row=2, column=0)
    rollno = Entry(form, width=20)
    rollno.grid(row=2, column=1)

    Label(form, text="Enter branch of the student: ").grid(row=3, column=0)
    branch = Entry(form, width=20)
    branch.grid(row=3, column=1)

    Label(form, text="Enter room id of the student: ").grid(row=4, column=0)
     ############################################
    con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
    cur = con.cursor()
    query1 = "select room_id from room where number_of_students_living < capacity;"

    cur.execute(query1)

    table = cur.fetchall()
    a=list()
    for i in table:
        a.append(i[0])
    print(a)
    con.commit()
    cur.close()
    con.close()
    ##############################################
    options=a
    selected=StringVar()
    roomid = OptionMenu(form, selected, *options)
    roomid.grid(row=4, column=1)

    Label(form, text="Enter hostel id of the student: ").grid(row=5, column=0)
    hostel_id = Entry(form, width=20)
    hostel_id.grid(row=5, column=1)

    Label(form, text="Enter date of birth of the student: ").grid(row=6, column=0)
    dob = DateEntry(form, selectmode="day")
    dob.grid(row=6, column=1)

    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=7, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=7, column=1)

    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def insert_hostel_staff():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    def submit_query():
        empid_input = empid.get()
        name_input = emp_name.get()
        emp_job_input = emp_job.get()
        hostelId_input = hostelId.get()
        phone_input = phone.get()

        # entering data
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()

        query1 = "INSERT INTO `hostel_staff` (`emp_id`, `emp_name`, `hostel_id`, `emp_job`, `phone_number`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (empid_input, name_input, hostelId_input, emp_job_input, phone_input)

        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data added succussfully.')


    def back():
        root.destroy()
        home1.home_page()

    Label(form, text="enter the empID: ").grid(row=0, column=0)
    empid = Entry(form, width=20)
    empid.grid(row=0, column=1)

    Label(form, text="enter the emp_job: ").grid(row=1, column=0)
    emp_job = Entry(form, width=20)
    emp_job.grid(row=1, column=1)

    Label(form, text="enter the emp_name: ").grid(row=2, column=0)
    emp_name = Entry(form, width=20)
    emp_name.grid(row=2, column=1)

    Label(form, text="enter the hostelId: ").grid(row=3, column=0)
    hostelId = Entry(form, width=20)
    hostelId.grid(row=3, column=1)

    Label(form, text="enter the phone: ").grid(row=4, column=0)
    phone = Entry(form, width=20)
    phone.grid(row=4, column=1)

    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=5, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=5, column=1)
    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def insert_visitor():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    def submit_query():
        vid_input = v_id.get()
        rollno_input = rollno.get()
        name_input = v_name.get()
        in_time_input = in_time.time()
        in_str = str(in_time_input[0])+":"+str(in_time_input[1])+":00"
        out_time_input = out_time.time()
        out_str = str(out_time_input[0])+":"+str(out_time_input[1])+":00"
        date_input = date.get_date()
        date_str=str(date_input)

        # entering data

        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()

        query1 = "INSERT INTO `visitor` (`visitor_id`, `visitor_name`, `roll_number`, `in_time`, `out_time`, `date`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (vid_input, name_input, rollno_input, in_str, out_str, date_str)

        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data added succussfully.')


    def back():
        root.destroy()
        home1.home_page()

    Label(form, text="enter the visitorID: ").grid(row=0, column=0)
    v_id = Entry(form, width=20)
    v_id.grid(row=0, column=1)

    Label(form, text="enter the rollno of the student: ").grid(row=1, column=0)
    rollno = Entry(form, width=20)
    rollno.grid(row=1, column=1)

    Label(form, text="enter the visitor_name: ").grid(row=2, column=0)
    v_name = Entry(form, width=20)
    v_name.grid(row=2, column=1)

    Label(form, text="enter the in time: ").grid(row=3, column=0)
    in_time = SpinTimePickerModern(form)
    in_time.addAll(constants.HOURS24)
    in_time.grid(row=3, column=1)

    Label(form, text="enter the out time: ").grid(row=4, column=0)
    out_time = SpinTimePickerModern(form)
    out_time.addAll(constants.HOURS24)
    out_time.grid(row=4, column=1)

    Label(form, text="enter the date: ").grid(row=5, column=0)
    date = DateEntry(form, selectmode="day")
    date.grid(row=5, column=1)

    submit=Button(form, text="Submit", command=submit_query)
    submit.grid(row=6, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=6, column=1)
    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def insert_furniture():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    def submit_query():
        furid_input = fur_id.get()
        roomid_input = roomid.get()
        

        # entering data
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()
        query1 = "INSERT INTO `furniture` (`furniture_id`, `room_id`) VALUES ('%s', '%s');" %(furid_input,roomid_input)
        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data added succussfully.')



    def back():
        root.destroy()
        home1.home_page()

    Label(form, text="enter the furnitureID: ").grid(row=0, column=0)
    fur_id = Entry(form, width=20)
    fur_id.grid(row=0, column=1)

    Label(form, text="enter the roomid: ").grid(row=1, column=0)
    roomid = Entry(form, width=20)
    roomid.grid(row=1, column=1)


    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=3, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=3, column=1)
    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def update_student():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    def submit_query():
        rollno_input = rollno.get()
        roomid_input = selected.get()

        #code for checking the presence of the rollno in the database




        # entering data
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()
        query1 = "update students set room_id=%s where students.roll_number='%s';"%(roomid_input, rollno_input)
        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data updated succussfully.')

    def back():
        root.destroy()
        home1.home_page()

    Label(form, text="enter the student rollno: ").grid(row=0, column=0)
    rollno = Entry(form, width=20)
    rollno.grid(row=0, column=1)

    Label(form, text="enter the roomid: ").grid(row=1, column=0)
    ############################################
    con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
    cur = con.cursor()
    query1 = "select room_id from room where number_of_students_living < capacity;"

    cur.execute(query1)

    table = cur.fetchall()
    a=list()
    for i in table:
        a.append(i[0])
    print(a)
    con.commit()
    cur.close()
    con.close()
    ##############################################
    options=a
    selected=StringVar()
    roomid = OptionMenu(form, selected, *options)
    roomid.grid(row=1, column=1)

    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=2, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=2, column=1)
    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def update_hostel_staff():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)

    def submit_query():
        empid_input = empid.get()
        phone_no_input = phone_no.get()

        #code for checking the presence of empid in the database




        # entering data
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()
        query1 = "update hostel_staff set phone_number=%s where hostel_staff.emp_id='%s';"%(phone_no_input,empid_input)
        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data added succussfully.')

    def back():
        root.destroy()
        home1.home_page()

    Label(form, text="enter the empid: ").grid(row=0, column=0)
    empid = Entry(form, width=20)
    empid.grid(row=0, column=1)

    Label(form, text="enter the phone no: ").grid(row=1, column=0)
    phone_no = Entry(form, width=20)
    phone_no.grid(row=1, column=1)

    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=2, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=2, column=1)
    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #

def update_fee():
    root = Tk()
    root.geometry('1400x700')

    img = Image.open("2.png")
    test= ImageTk.PhotoImage(img)

    lbl=Label(image=test, borderwidth=0, highlightthickness=0)
    lbl.place(relx=.5, rely=.5, anchor=CENTER)

    form = Frame(root)
    form.place(relx=.5,rely=.5, anchor=CENTER)
# ---------------------INCOMPLETE--------------------- #
    def submit_query():

        rollno_input = roll_no.get()
        status_input = selected.get()
        date_input = date.get_date()
        date_str=str(date_input)
        print(date_str)
        print(type(date_str))
        if(status_input=="Paid"):
            status_input='1'
        else:
            status_input='0'
         #entering data
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="hostel_management_system")
        cur = con.cursor()
        query1 = "update fee set fee_status=%s, date_of_submission='%s' where roll_number='%s'"%(status_input,date_str,rollno_input)
        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()

        messagebox.showinfo('info','Data updated succussfully.')
        



    def back():
        root.destroy()
        home1.home_page()

    Label(form, text="enter the roll no: ").grid(row=1, column=0)
    roll_no = Entry(form, width=20)
    roll_no.grid(row=1, column=1)

    options = ["Paid", "Not Paid"]
    selected = StringVar()
    Label(form, text="Fee Status: ").grid(row=2, column=0)
    drop = OptionMenu(form, selected, *options)
    drop.grid(row=2, column=1)

    Label(form, text="Date of fee payment: ").grid(row=3, column=0)
    date = DateEntry(form, selectmode="day")
    date.grid(row=3, column=1)

    submit = Button(form, text="Submit", command=submit_query)
    submit.grid(row=4, column=0)

    back = Button(form, text="Back", command=back)
    back.grid(row=4, column=1)
    form.mainloop()

# --------------------------------------------------------------------------------------------------------- #
#insert_student()
#update_fee()