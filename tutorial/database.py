from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('Dropdown Meny')
root.iconbitmap('images/dibalo.ico')
root.geometry("300x400")



# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table 
'''
c.execute("""CREATE TABLE adresses (
        firstName text, 
        lastName text,
        adress text,
        city text,
        zipcode integer
)""")
'''

# Create a function to update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    record_ID = select_box.get()
    c.execute("""UPDATE adresses SET
        firstName = :firstName,
        lastName = :lastName,
        adress = :adress,
        city = :city,
        zipcode = :zipcode

        WHERE oid = :oid""",{
            'firstName': firstName_editor.get(),
            'lastName': lastName_editor.get(),
            'adress': adress_editor.get(),
            'city': city_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid': record_ID
        })

    # Commit changes
    conn.commit()
    # close connection
    conn.close()
    editor.destroy()


# Create a function to edit a record
def edit():
    global editor
    editor = Tk()
    editor.title('Update Record')
    editor.iconbitmap('images/dibalo.ico')
    editor.geometry("300x200")


    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_ID = select_box.get()

    # query the database
    c.execute('SELECT * FROM adresses WHERE oid = '+ record_ID)
    records = c.fetchall()

    # Create Global variables
    global firstName_editor
    global lastName_editor
    global adress_editor
    global city_editor
    global zipcode_editor

    # Create Text Boxes
    firstName_editor = Entry(editor, width=30)
    firstName_editor.grid(row=0,column=1, padx=20, pady=(10, 0))
    lastName_editor = Entry(editor, width=30)
    lastName_editor.grid(row=1,column=1)
    adress_editor = Entry(editor, width=30)
    adress_editor.grid(row=2,column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3,column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=4,column=1)

    # Create text box labels
    firstNameLbl_editor = Label(editor, text='First Name')
    firstNameLbl_editor.grid(row=0, column=0, pady=(10,0))
    lastNameLbl_editor = Label(editor, text='Last Name')
    lastNameLbl_editor.grid(row=1, column=0)
    adreeLbl_editor = Label(editor, text='Adress')
    adreeLbl_editor.grid(row=2, column=0)
    citylbl_editor = Label(editor, text='City')
    citylbl_editor.grid(row=3, column=0)
    zipcodelbl_editor = Label(editor, text='Zipcode')
    zipcodelbl_editor.grid(row=4, column=0)

    # Loop thru results
    for record in records:
        firstName_editor.insert(0, record[0])
        lastName_editor.insert(0, record[1])
        adress_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        zipcode_editor.insert(0, record[4])

    # Create submit button
    sub_btn_editor = Button(editor, text='Re-submit', command=update)
    sub_btn_editor.grid(row=6, column=0, columnspan=2, pady=(10,0), padx=10, ipadx=100)
    
    # Commit changes
    conn.commit()
    # close connection
    conn.close()

    


# Create a function to delete a record
def delete():
    response = messagebox.askokcancel('Deleting','Permanent delete, are you sure?')
    # Create a database or connect to one
    if response:
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        c = conn.cursor()

        c.execute("DELETE from adresses WHERE oid= " + select_box.get())
        select_box.delete(0,END)
        # Commit changes
        conn.commit()
        # close connection
        conn.close()

# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO adresses VALUES (:firstName, :lastName, :adress, :city, :zipcode)",
            {
                'firstName': firstName.get(),
                'lastName': lastName.get(),
                'adress': adress.get(),
                'city': city.get(),
                'zipcode': zipcode.get()
            })


    # Commit changes
    conn.commit()
    # close connection
    conn.close()

    # Clear the Text Boxes
    firstName.delete(0,END)
    lastName.delete(0,END)
    adress.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

# Create query funciton
def query():
      # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # query the database
    c.execute('SELECT *, oid FROM adresses')
    records = c.fetchall()
    #print(records)
    
    # loopå thru results
    print_name = ''
    print_ID = ''
    for record in records:
        print_name += str(record[0]) + ' ' + str(record[1]) + "\n"
        print_ID += str(record[-1]) + "\n"
    #prints out the result
    name_lbl = Label(root, text=print_name)
    name_lbl.grid(row=12, column=0)
    ID_lbl = Label(root, text=print_ID)
    ID_lbl.grid(row=12, column=1)

    # Commit changes
    conn.commit()
    # close connection
    conn.close()



# Create Text Boxes
firstName = Entry(root, width=30)
firstName.grid(row=0,column=1, padx=20, pady=(10, 0))
lastName = Entry(root, width=30)
lastName.grid(row=1,column=1)
adress = Entry(root, width=30)
adress.grid(row=2,column=1)
city = Entry(root, width=30)
city.grid(row=3,column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=4,column=1)

select_box = Entry(root,width=30)
select_box.grid(row=8,column=1, pady=(20,0))


# Create text box labels
firstNameLbl = Label(root, text='First Name')
firstNameLbl.grid(row=0, column=0, pady=(10,0))
lastNameLbl = Label(root, text='Last Name')
lastNameLbl.grid(row=1, column=0)
adreeLbl = Label(root, text='Adress')
adreeLbl.grid(row=2, column=0)
citylbl = Label(root, text='City')
citylbl.grid(row=3, column=0)
zipcodelbl = Label(root, text='Zipcode')
zipcodelbl.grid(row=4, column=0)

select_lbl = Label(root, text='Select ID')
select_lbl.grid(row=8, column=0, pady=(20,0))

# Create submit button
sub_btn = Button(root, text='Submit', command=submit)
sub_btn.grid(row=6, column=0, columnspan=2, pady=(10,0), padx=10, ipadx=120)

# Create a Quert Button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, ipadx=100)

# Create a delete button
delete_btn = Button(root, text='Delete Record', command=delete)
delete_btn.grid(row=9, column=0, columnspan=2,  padx=10, ipadx=100)

# Create a delete button
edit_btn = Button(root, text='Update Record', command=edit)
edit_btn.grid(row=10, column=0, columnspan=2,  padx=10, ipadx=100)

# Create column for name and ID
name_lbl = Label(root, text='Name:')
name_lbl.grid(row=11, column=0)
ID_lbl = Label(root, text='ID:')
ID_lbl.grid(row=11, column=1)


# Commit changes
conn.commit()

# close connection
conn.close()
#Button(root, text='Exit', command=root.quit, width=30).grid(row=6, column= 1)
root.mainloop()


