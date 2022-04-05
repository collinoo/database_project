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
window_height = 800
window_width = 1600
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

# create a scroll bar
# scrollbar = Scrollbar(frame)
# scrollbar.pack(side=RIGHT, fill=Y)
# # create a scroll bar for the other direction
# scrollbar2 = Scrollbar(frame, orient=HORIZONTAL)
# scrollbar2.pack(side=BOTTOM, fill=X)

# Connect to the database
conn = sqlite3.connect('BikeStores.db')

# Create cursor
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Stores (
            StoreID INTEGER,
            StoreName nvarchar(50),
            StoreEmail nvarchar(50),
            StorePhone nvarchar(50),
            StoreAddress nvarchar(50),
            StoreZipcode nvarchar(50)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS BikeCategory (
            BikeCatID INTEGER,
            BikeCat nvarchar(50)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS BikeBrand (
            BikeBrandID INTEGER,
            BikeCategory nvarchar(50)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS BikeProducts (
            BikeProdID INTEGER,
            BikeProdName nvarchar(50),
            ModelYear nvarchar(50),
            BikePrice nvarchar(50),
            BikeBrandID nvarchar(50) references BikeBrand(BikeBrandID),
            BikeCatID nvarchar(50) references BikeCategory(BikeCatID)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS Customers (
            CustID INTEGER,
            CustFirstName nvarchar(50),
            CustLastName nvarchar(50),
            CustEmail nvarchar(50),
            CustPhone nvarchar(50),
            CustAddress nvarchar(50)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS Orders (
            OrderID INTEGER,
            OrderDate nvarchar(50),
            CustID INTEGER references Customers(CustID),
            StoreStaffID INTEGER references StoreStaff(StoreStaffID),
            Discount nvarchar(50),
            TotalPrice nvarchar(50)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS Stock (
            StockID INTEGER,
            StoreID INTEGER references Stores(StoreID),
            BikeProdID INTEGER references BikeProducts(BikeProdID),
            StockQuantity INTEGER
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS Staff (
            StaffID INTEGER,
            StaffFirstName nvarchar(50),
            StaffLastName nvarchar(50),
            StaffEmail nvarchar(50),
            StaffPhone nvarchar(50),
            StaffAddress nvarchar(50)
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS StoreStaff (
            StoreStaffID INTEGER,
            StaffID INTEGER references Staff(StaffID),
            StoreID INTEGER references Stores(StoreID)
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS Managers (
            ManagerID INTEGER,
            StoreID INTEGER references Stores(StoreID),
            StaffID INTEGER references Staff(StaffID)
    )""")


def submit():
    # Connect to the database
    conn = sqlite3.connect('BikeStores.db')

    # Create cursor
    c = conn.cursor()

    # Get data from Input boxes and pass to sql_query
    # sql_query = "INSERT INTO Stores VALUES ('" + str(store_id.get()) + "', '" + str(store_name.get()) + "', '" + str(store_email.get()) + "', '" + str(store_phone.get()) + "', '" + str(store_address.get()) + "', '" + str(store_zipcode.get()) + "', '" + "INSERT INTO BikeCategory VALUES ('" + str(bike_cat_id.get()) + "', '" + str(bike_cat.get()) + "')" + "')"
    # sql_query2 = "INSERT INTO BikeCategory VALUES ('" + str(bike_cat_id.get()) + "', '" + str(bike_cat.get()) + "')"

    # Inserting data into the database
    # Store
    c.execute("INSERT INTO Stores VALUES ('" + str(store_id.get()) + "', '" + str(store_name.get()) + "', '" + str(store_email.get()) + "', '" + str(store_phone.get()) + "', '" + str(store_address.get()) + "', '" + str(store_zipcode.get()) + "')")
    # BikeCategory
    c.execute("INSERT INTO BikeCategory VALUES ('" + str(bike_cat_id.get()) + "', '" + str(bike_cat.get()) + "')")
    # BikeBrand
    c.execute("INSERT INTO BikeBrand VALUES ('" + str(bike_brand_id.get()) + "', '" + str(bike_brand.get()) + "')")
    # c.execute("INSERT INTO BikeProducts VALUES ('" + str(bike_prod_id.get()) + "', '" + str(bike_prod_name.get()) + "', '" + str(bike_prod_year.get()) + "', '" + str(bike_prod_price.get()) + "')")
    # BikeProducts
    c.execute("INSERT INTO BikeProducts VALUES ('" + str(bike_prod_id.get()) + "', '" + str(bike_prod_name.get()) + "', '" + str(bike_prod_year.get()) + "', '" + str(bike_prod_price.get()) + "', '" + str(bike_brand_id.get()) + "', '" + str(bike_cat_id.get()) + "')")
    # Customers
    c.execute("INSERT INTO Customers VALUES ('" + str(cust_id.get()) + "', '" + str(cust_first_name.get()) + "', '" + str(cust_last_name.get()) + "', '" + str(cust_email.get()) + "', '" + str(cust_phone.get()) + "', '" + str(cust_address.get()) + "')")
    # Orders
    c.execute("INSERT INTO Orders VALUES ('" + str(order_id.get()) + "', '" + str(order_date.get()) + "', '" + str(cust_id.get()) + "', '" + str(store_staff_id.get()) + "', '" + str(discount.get()) + "', '" + str(total_price.get()) + "')")
    # Stock
    c.execute("INSERT INTO Stock VALUES ('" + str(stock_id.get()) + "', '" + str(store_id.get()) + "', '" + str(bike_prod_id.get()) + "', '" + str(stock_quantity.get()) + "')")
    # Staff
    c.execute("INSERT INTO Staff VALUES ('" + str(staff_id.get()) + "', '" + str(staff_first_name.get()) + "', '" + str(staff_last_name.get()) + "', '" + str(staff_email.get()) + "', '" + str(staff_phone.get()) + "', '" + str(staff_address.get()) + "')")
    # StoreStaff
    c.execute("INSERT INTO StoreStaff VALUES ('" + str(store_staff_id.get()) + "', '" + str(staff_id.get()) + "', '" + str(store_id.get()) + "')")
    # Managers
    c.execute("INSERT INTO Managers VALUES ('" + str(manager_id.get()) + "', '" + str(store_id.get()) + "', '" + str(staff_id.get()) + "')")


    # c.execute(sql_query)
    # c.execute(sql_query2)
    conn.commit()

    c.close()
    conn.close()


    # Clear the text boxes once data is submitted
    # Stores
    store_id.delete(0, END)
    store_name.delete(0, END)
    store_email.delete(0, END)
    store_phone.delete(0, END)
    store_address.delete(0, END)
    store_zipcode.delete(0, END)
    # Bike Category
    bike_cat_id.delete(0, END)
    bike_cat.delete(0, END)
    # Bike Brand
    bike_brand_id.delete(0, END)
    bike_brand.delete(0, END)
    # Bike Product
    bike_prod_id.delete(0, END)
    bike_prod_name.delete(0, END)
    bike_prod_year.delete(0, END)
    bike_prod_price.delete(0, END)
    # Customers
    cust_id.delete(0, END)
    cust_first_name.delete(0, END)
    cust_last_name.delete(0, END)
    cust_email.delete(0, END)
    cust_phone.delete(0, END)
    cust_address.delete(0, END)
    # Orders
    order_id.delete(0, END)
    order_date.delete(0, END)
    # cust_id.delete(0, END)
    # store_staff_id.delete(0, END)
    discount.delete(0, END)
    total_price.delete(0, END)
    # Stock
    stock_id.delete(0, END)
    # store_id.delete(0, END)
    # bike_prod_id.delete(0, END)
    stock_quantity.delete(0, END)
    # Staff
    staff_id.delete(0, END)
    staff_first_name.delete(0, END)
    staff_last_name.delete(0, END)
    staff_email.delete(0, END)
    staff_phone.delete(0, END)
    staff_address.delete(0, END)
    # StoreStaff
    store_staff_id.delete(0, END)
    # store_id.delete(0, END)
    # staff_id.delete(0, END)
    # Managers
    manager_id.delete(0, END)


# Text boxes (used to enter and identify data)
# Stores
store_id = Entry(root, width=15)
store_id.grid(row=0, column=1, padx=20)
store_name = Entry(root, width=15)
store_name.grid(row=1, column=1)
store_email = Entry(root, width=15)
store_email.grid(row=2, column=1)
store_phone = Entry(root, width=15)
store_phone.grid(row=3, column=1)
store_address = Entry(root, width=15)
store_address.grid(row=4, column=1)
store_zipcode = Entry(root, width=15)
store_zipcode.grid(row=5, column=1)
# Bike Category
bike_cat_id = Entry(root, width=15)
bike_cat_id.grid(row=0, column=3, padx=20)
bike_cat = Entry(root, width=15)
bike_cat.grid(row=1, column=3)
# Bike Brand
bike_brand_id = Entry(root, width=15)
bike_brand_id.grid(row=0, column=5, padx=20)
bike_brand = Entry(root, width=15)
bike_brand.grid(row=1, column=5)
# Bike Product
bike_prod_id = Entry(root, width=15)
bike_prod_id.grid(row=0, column=7, padx=20)
bike_prod_name = Entry(root, width=15)
bike_prod_name.grid(row=1, column=7)
bike_prod_year = Entry(root, width=15)
bike_prod_year.grid(row=2, column=7)
bike_prod_price = Entry(root, width=15)
bike_prod_price.grid(row=3, column=7)
# Customers
cust_id = Entry(root, width=15)
cust_id.grid(row=0, column=9, padx=20)
cust_first_name = Entry(root, width=15)
cust_first_name.grid(row=1, column=9)
cust_last_name = Entry(root, width=15)
cust_last_name.grid(row=2, column=9)
cust_email = Entry(root, width=15)
cust_email.grid(row=3, column=9)
cust_phone = Entry(root, width=15)
cust_phone.grid(row=4, column=9)
cust_address = Entry(root, width=15)
cust_address.grid(row=5, column=9)
# Orders
order_id = Entry(root, width=15)
order_id.grid(row=0, column=11, padx=20)
order_date = Entry(root, width=15)
order_date.grid(row=1, column=11)
# store_staff_id = Entry(root, width=15)
# store_staff_id.grid(row=2, column=11)
discount = Entry(root, width=15)
discount.grid(row=2, column=11)
total_price = Entry(root, width=15)
total_price.grid(row=3, column=11)
# Stock
stock_id = Entry(root, width=15)
stock_id.grid(row=0, column=13, padx=20)
stock_quantity = Entry(root, width=15)
stock_quantity.grid(row=1, column=13)
# Staff
staff_id = Entry(root, width=15)
staff_id.grid(row=13, column=1, padx=20)
staff_first_name = Entry(root, width=15)
staff_first_name.grid(row=14, column=1)
staff_last_name = Entry(root, width=15)
staff_last_name.grid(row=15, column=1)
staff_email = Entry(root, width=15)
staff_email.grid(row=16, column=1)
staff_phone = Entry(root, width=15)
staff_phone.grid(row=17, column=1)
staff_address = Entry(root, width=15)
staff_address.grid(row=18, column=1)
# StoreStaff
store_staff_id = Entry(root, width=15)
store_staff_id.grid(row=13, column=3, padx=20)
# store_id = Entry(root, width=15)
# store_id.grid(row=14, column=3)
# staff_id = Entry(root, width=15)
# staff_id.grid(row=15, column=3)
# Managers
manager_id = Entry(root, width=15)
manager_id.grid(row=13, column=5, padx=20)


# Labels
# Stores
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
# Bike Category
bike_cat_id_label = Label(root, text="Bike Category ID")
bike_cat_id_label.grid(row=0, column=2, pady=10)
bike_cat_label = Label(root, text="Bike Category")
bike_cat_label.grid(row=1, column=2, pady=10)
# Bike Brand
bike_brand_id_label = Label(root, text="Bike Brand ID")
bike_brand_id_label.grid(row=0, column=4, pady=10)
bike_brand_label = Label(root, text="Bike Brand")
bike_brand_label.grid(row=1, column=4, pady=10)
# Bike Product
bike_prod_id_label = Label(root, text="Bike Product ID")
bike_prod_id_label.grid(row=0, column=6, pady=10)
bike_prod_name_label = Label(root, text="Bike Product Name")
bike_prod_name_label.grid(row=1, column=6, pady=10)
bike_prod_year_label = Label(root, text="Bike Product Year")
bike_prod_year_label.grid(row=2, column=6, pady=10)
bike_prod_price_label = Label(root, text="Bike Product Price")
bike_prod_price_label.grid(row=3, column=6, pady=10)
# Customers
cust_id_label = Label(root, text="Customer ID")
cust_id_label.grid(row=0, column=8, pady=10)
cust_first_name_label = Label(root, text="Customer First Name")
cust_first_name_label.grid(row=1, column=8, pady=10)
cust_last_name_label = Label(root, text="Customer Last Name")
cust_last_name_label.grid(row=2, column=8, pady=10)
cust_email_label = Label(root, text="Customer Email")
cust_email_label.grid(row=3, column=8, pady=10)
cust_phone_label = Label(root, text="Customer Phone")
cust_phone_label.grid(row=4, column=8, pady=10)
cust_address_label = Label(root, text="Customer Address")
cust_address_label.grid(row=5, column=8, pady=10)
# Orders
order_id_label = Label(root, text="Order ID")
order_id_label.grid(row=0, column=10, pady=10)
order_date_label = Label(root, text="Order Date")
order_date_label.grid(row=1, column=10, pady=10)
# store_staff_id_label = Label(root, text="Store Staff ID")
# store_staff_id_label.grid(row=2, column=10, pady=10)
discount_label = Label(root, text="Discount")
discount_label.grid(row=2, column=10, pady=10)
total_price_label = Label(root, text="Total Price")
total_price_label.grid(row=3, column=10, pady=10)
# Stock
stock_id_label = Label(root, text="Stock ID")
stock_id_label.grid(row=0, column=12, pady=10)
stock_quantity_label = Label(root, text="Stock Quantity")
stock_quantity_label.grid(row=1, column=12, pady=10)
# Staff
staff_id_label = Label(root, text="Staff ID")
staff_id_label.grid(row=13, column=0, pady=10)
staff_first_name_label = Label(root, text="Staff First Name")
staff_first_name_label.grid(row=14, column=0, pady=10)
staff_last_name_label = Label(root, text="Staff Last Name")
staff_last_name_label.grid(row=15, column=0, pady=10)
staff_email_label = Label(root, text="Staff Email")
staff_email_label.grid(row=16, column=0, pady=10)
staff_phone_label = Label(root, text="Staff Phone")
staff_phone_label.grid(row=17, column=0, pady=10)
staff_address_label = Label(root, text="Staff Address")
staff_address_label.grid(row=18, column=0, pady=10)
# StoreStaff
store_staff_id_label = Label(root, text="Store Staff ID")
store_staff_id_label.grid(row=13, column=2, pady=10)
# store_staff_store_id_label = Label(root, text="Store ID")
# store_staff_store_id_label.grid(row=14, column=2, pady=10)
# store_staff_staff_id_label = Label(root, text="Staff ID")
# store_staff_staff_id_label.grid(row=15, column=2, pady=10)
# Managers
manager_id_label = Label(root, text="Manager ID")
manager_id_label.grid(row=13, column=4, pady=10)


# Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=12, column=6, columnspan=2, pady=10, padx=10, ipadx=30)


# Get data from database
# def query_to_console():
#     conn = sqlite3.connect('BikeStores.db')
#     c = conn.cursor()
#
#     c.execute("SELECT * FROM Stores, BikeCategory")
#     pprint.pprint(c.fetchall())
#     c.close()
#     conn.close()


# Print the data from the datbase to the GUI
def query_to_gui():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()
    b = conn.cursor()
    d = conn.cursor()
    e = conn.cursor()
    f = conn.cursor()
    g = conn.cursor()
    h = conn.cursor()
    i = conn.cursor()
    j = conn.cursor()
    k = conn.cursor()

    c.execute("Select * FROM Stores")
    b.execute("Select * FROM BikeCategory")
    d.execute("Select * FROM BikeBrand")
    e.execute("Select * FROM BikeProducts")
    f.execute("Select * FROM Customers")
    g.execute("Select * FROM Orders")
    h.execute("Select * FROM Stock")
    i.execute("Select * FROM Staff")
    j.execute("Select * FROM StoreStaff")
    k.execute("Select * FROM Managers")

    output = c.fetchall()
    bike_output = b.fetchall()
    brand_output = d.fetchall()
    prod_output = e.fetchall()
    cust_output = f.fetchall()
    order_output = g.fetchall()
    stock_output = h.fetchall()
    staff_output = i.fetchall()
    store_staff_output = j.fetchall()
    manager_output = k.fetchall()

    # check if there is data in output
    # Stores
    if len(output) > 0:
        print_records = 'Stores'
        for record in output:
            print_records += str(record) + "\n"

        global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=9, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Bike Category
    if len(bike_output) > 0:
        print_records = 'Bike Category'
        for record in bike_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=12, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Bike Brand
    if len(brand_output) > 0:
        print_records = 'Bike Brand'
        for record in brand_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=13, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Bike Product
    if len(prod_output) > 0:
        print_records = 'Bike Product'
        for record in prod_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=14, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Customers
    if len(cust_output) > 0:
        print_records = 'Customers'
        for record in cust_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=15, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Orders
    if len(order_output) > 0:
        print_records = 'Orders'
        for record in order_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=16, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Stock
    if len(stock_output) > 0:
        print_records = 'Stock'
        for record in stock_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=17, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Staff
    if len(staff_output) > 0:
        print_records = 'Staff'
        for record in staff_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=18, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Store Staff
    if len(store_staff_output) > 0:
        print_records = 'Store Staff'
        for record in store_staff_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=19, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Managers
    if len(manager_output) > 0:
        print_records = 'Managers'
        for record in manager_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(root, text=print_records)
        query_label.grid(row=20, column=9, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()


    c.close()
    conn.close()


# Query button
query_button = Button(root, text="Show records", command=query_to_gui)
query_button.grid(row=13, column=6, columnspan=2, pady=10, padx=10, ipadx=30)


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
# Delete Stores
delete_button = Button(root, text="Delete Stores", command=lambda: delete_rows("Stores"))
delete_button.grid(row=14, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete BikeCategory
delete_button2 = Button(root, text="Delete BikeCategory", command=lambda: delete_rows("BikeCategory"))
delete_button2.grid(row=15, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete BikeBrand
delete_button3 = Button(root, text="Delete BikeBrand", command=lambda: delete_rows("BikeBrand"))
delete_button3.grid(row=16, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete BikeProduct
delete_button4 = Button(root, text="Delete BikeProducts", command=lambda: delete_rows("BikeProducts"))
delete_button4.grid(row=17, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete Customers
delete_button5 = Button(root, text="Delete Customers", command=lambda: delete_rows("Customers"))
delete_button5.grid(row=18, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete Orders
delete_button6 = Button(root, text="Delete Orders", command=lambda: delete_rows("Orders"))
delete_button6.grid(row=19, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete Stock
delete_button7 = Button(root, text="Delete Stock", command=lambda: delete_rows("Stock"))
delete_button7.grid(row=20, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete Staff
delete_button8 = Button(root, text="Delete Staff", command=lambda: delete_rows("Staff"))
delete_button8.grid(row=21, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete StoreStaff
delete_button9 = Button(root, text="Delete StoreStaff", command=lambda: delete_rows("StoreStaff"))
delete_button9.grid(row=22, column=6, columnspan=2, pady=10, padx=10, ipadx=20)
# Delete Managers
delete_button10 = Button(root, text="Delete Managers", command=lambda: delete_rows("Managers"))
delete_button10.grid(row=23, column=6, columnspan=2, pady=10, padx=10, ipadx=20)


conn.commit()
conn.close()

if __name__ == '__main__':
    root.mainloop()
