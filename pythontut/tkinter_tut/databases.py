from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Databases')
root.iconbitmap('quakechamps.ico')
root.geometry("350x550")

# Databases
# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create a cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )
    """)
'''
# Create a search function
def search():
    # Create a database or connect to one inside the function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor inside the function
    c = conn.cursor()
    s_string=erase_Box.get()
    # Search the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    # Loop thru results
    print_records = ''
    for record in records:
        for i in range(6):
            if record[i] == s_string:
                print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    s_query_label = Label(root, text=print_records)
    s_query_label.grid(row=13, column=0, columnspan=2)
    # Commit Changes inside the function
    conn.commit()
    # Close connection to database inside the function
    conn.close()

# Create function to save modifications
def update():
    # Create a database or connect to one inside the function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor inside the function
    c = conn.cursor()
    record_id = erase_Box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              }
              )

    # Commit Changes inside the function
    conn.commit()
    # Close connection to database inside the function
    conn.close()
    editor.destroy() # Close editor window after saving modifications

# Create edit function to update records
def edit():
    global editor
    editor = Tk()
    editor.title('Update record')
    editor.iconbitmap('quakechamps.ico')
    editor.geometry("350x250")

    # Create a database or connect to one inside the function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor inside the function
    c = conn.cursor()

    record_id = erase_Box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = c.fetchall()
    # Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    # Create text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create textbox labels
    f_name_label_editor = Label(editor, text="First name")
    f_name_label_editor.grid(row=0, column=0, pady=(10,0))
    l_name_label_editor = Label(editor, text="Last name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State/County")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a save edited entry button
    save_button = Button(editor, text="Save Record", command=update)
    save_button.grid(row=6, columnspan=2, column=0, padx=10, pady=10, ipadx=128)
    # Commit Changes inside the function
    conn.commit()
    # Close connection to database inside the function
    conn.close()
# Create function to delete a record
def delete():
    # Create a database or connect to one inside the function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor inside the function
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid=" + erase_Box.get())

    erase_Box.delete(0, END)

    # Commit Changes inside the function
    conn.commit()
    # Close connection to database inside the function
    conn.close()


# Create submit function for database
def submit():
    # Create a database or connect to one inside the function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor inside the function
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }

    )
    # Commit Changes inside the function
    conn.commit()
    # Close connection to database inside the function
    conn.close()
    # Clear texboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    # Create a database or connect to one inside the function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor inside the function
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)
    # Commit Changes inside the function
    conn.commit()
    # Close connection to database inside the function
    conn.close()

# Create text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
erase_Box = Entry(root, width=30)
erase_Box.grid(row=9, column=1)

# Create textbox labels
f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0, pady=(10,0))
l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State/County")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box = Label(root, text="Select record or search")
delete_box.grid(row=9, column=0)

# Create a Submit button
submit_button = Button(root, text="Add record to database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_button = Button(root, text="Show records", command=query)
query_button.grid(row=7, columnspan=2, column=0, padx=10, pady=10, ipadx=126)

# Create a delete button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, columnspan=2, column=0, padx=10, pady=10, ipadx=126)

# Create an Update Button
update_button = Button(root, text="Update Record", command=edit)
update_button.grid(row=11, columnspan=2, column=0, padx=10, pady=10, ipadx=122)

# Create Search button
search_button = Button(root, text="Search Record", command=search)
search_button.grid(row=12, columnspan=2, column=0, padx=10, pady=10, ipadx=122)

# Commit Changes
conn.commit()

#Close connection to database
conn.close()


root.mainloop()
