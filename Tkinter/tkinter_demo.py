# Program of tkinter demo, 1.create window, 2.Label,place 3.Entry, 4.Button, 5.def button clicked command at button

from tkinter import *

# create window
root=Tk()
root.title("Tkinter Demo")
root.geometry("500x500")
root.resizable(width=False,height=False)

# def button clicked
def insert_data():
    print("Insert Button Clicked")
def search_data():
    print("Search Button Clicked")
def update_data():
    print("Update Button Clicked")
def delete_data():
    print("Delete Button Clicked")



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
search.place(x=140,y=350)

update=Button(root,text="Update",font=(15),fg="white",bg="black",command=update_data)
update.place(x=222,y=350)

delete=Button(root,text="Delete",font=(15),fg="white",bg="black",command=delete_data)
delete.place(x=305,y=350)

root.mainloop()