# Program of tkinter demo, 1.create window, 2.Label,place 3.Entry, 4.Button, 5.def button clicked command at button

from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

# create window
root=Tk()
root.title("Tkinter Demo")
root.geometry("500x500")
root.resizable(width=False,height=False)

# def functions
def create_conn():
    return mysql.connector.connect(
            host="localhost",
            database='python10',
            user='root',
            password=""
        )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()       
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo('Insert Status','Data Inserted Successfully')

def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("Search Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()                    # if changes thato hoi toj commit use thai  search ma koi change nathi karvano elte commit use thase nai    
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
            msg.showinfo("Search Status","Id Not Found")
        conn.close()
            
def update_data():
    if e_id.get()=="" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status",'Data Deleted Successfully')

# Label :
l_id=Label(root,text="Id : ",font=(15))            # label nam na object ne apde root ni andar store karishu
l_id.place(x=70,y=70)

l_fname=Label(root,text="First Name : ",font=(15))
l_fname.place(x=70,y=120)

l_lname=Label(root,text="Last Name : ",font=(15))
l_lname.place(x=70,y=170)

l_email=Label(root,text="Email : ",font=(15))
l_email.place(x=70,y=220)

l_mobile=Label(root,text="Mobile : ",font=(15))
l_mobile.place(x=70,y=270)

# Entry :
e_id=Entry(root)
e_id.place(x=240,y=70)

e_fname=Entry(root)
e_fname.place(x=240,y=120)

e_lname=Entry(root)
e_lname.place(x=240,y=170)

e_email=Entry(root)
e_email.place(x=240,y=220)

e_mobile=Entry(root)
e_mobile.place(x=240,y=270)

# Button : CRUD
insert=Button(root,text="Insert",font=(15),fg="white",bg="black",command=insert_data)
insert.place(x=70,y=350)

search=Button(root,text="Search",font=(15),fg="white",bg="black",command=search_data)
search.place(x=143,y=350)

update=Button(root,text="Update",font=(15),fg="white",bg="black",command=update_data)
update.place(x=230,y=350)

delete=Button(root,text="Delete",font=(15),fg="white",bg="black",command=delete_data)
delete.place(x=316,y=350)


root.mainloop()