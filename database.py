import pprint
import pandas as pd
import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
import time

root = Tk()
root.title("Database Project")
root.geometry("800x600")

# dark bg color
dark_bg = "#262B33"

# Window sizing to center on screen
window_height = 600
window_width = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_val = int((screen_width / 2) - (window_width / 2))
y_val = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_val, y_val - 100))

# Inner-frame styling (Dark BG Color)
frame = tkinter.Frame(root, bg=dark_bg)
frame.place(relwidth=1, relheight=1)

# font styling
font_mono = "Consolas"
font_label = ("Arial", 14)
font_ital = ("Arial", 10, "italic")
font_bold = ("Arial", 10, "bold")

# Connect to the database
conn = sqlite3.connect('BikeStores.db')

# Create cursor
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Stores (
            StoreID INTEGER PRIMARY KEY NOT NULL,
            StoreName text,
            StoreEmail text,
            StorePhone text,
            StoreAddress text,
            StoreZipcode text
    )""")


# delete all rows from store table
# c.execute("DELETE FROM Stores")

def submit():
    # Connect to the database
    conn = sqlite3.connect('BikeStores.db')

    # Create cursor
    c = conn.cursor()

   # Get data from Input boxes and pass to sql_query
    sql_query = "INSERT INTO Stores VALUES ('" + str(store_id.get()) + "', '" + str(store_name.get()) + "', '" + str(store_email.get()) + "', '" + str(store_phone.get()) + "', '" + str(store_address.get()) + "', '" + str(store_zipcode.get()) + "')"

    c.execute(sql_query)
    conn.commit()

    c.close()
    conn.close()

    # clear the text boxes
    store_id.delete(0, END)
    store_name.delete(0, END)
    store_email.delete(0, END)
    store_phone.delete(0, END)
    store_address.delete(0, END)
    store_zipcode.delete(0, END)


# Text boxes
store_id = Entry(root, width=30)
store_id.grid(row=0, column=1, padx=20)
store_name = Entry(root, width=30)
store_name.grid(row=1, column=1)
store_email = Entry(root, width=30)
store_email.grid(row=2, column=1)
store_phone = Entry(root, width=30)
store_phone.grid(row=3, column=1)
store_address = Entry(root, width=30)
store_address.grid(row=4, column=1)
store_zipcode = Entry(root, width=30)
store_zipcode.grid(row=5, column=1)

# Labels
store_id_label = Label(root, text="Store ID")
store_id_label.grid(row=0, column=0, pady=10)
store_name_label = Label(root, text="Store Name")
store_name_label.grid(row=1, column=0, pady=10)
store_email_label = Label(root, text="Store Email")
store_email_label.grid(row=2, column=0, pady=10)
store_phone_label = Label(root, text="Store Phone")
store_phone_label.grid(row=3, column=0, pady=10)
store_address_label = Label(root, text="Store Address")
store_address_label.grid(row=4, column=0, pady=10)
store_zipcode_label = Label(root, text="Store Zipcode")
store_zipcode_label.grid(row=5, column=0, pady=10)

# Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=100)

# Get data from database
def query_to_console():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("SELECT * FROM Stores")
    pprint.pprint(c.fetchall())
    c.close()
    conn.close()
# Print the data from the datbase to the GUI



def query_to_gui():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Stores")
    output = c.fetchall()

    # check if there is data in output
    if len(output) > 0:
        print_records = ''
        for record in output:
            print_records += str(record) + "\n"

        global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=9, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    c.close()
    conn.close()





# Query button
query_button = Button(root, text="Show records", command=query_to_gui)
query_button.grid(row=7, column=1, columnspan=2, pady=10, padx=10, ipadx=100)


def delete_rows(tableName):
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()
    c.execute("DELETE FROM " + tableName)

    # remove query_label
    query_to_gui()

    conn.commit()
    c.close()
    conn.close()

# Delete button
delete_button = Button(root, text="Delete all rows", command=lambda: delete_rows("Stores"))
delete_button.grid(row=8, column=1, columnspan=2, pady=10, padx=10, ipadx=100)

conn.commit()
conn.close()

if __name__ == '__main__':
    root.mainloop()
