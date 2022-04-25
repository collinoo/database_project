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

# create a scrollbar


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
c.execute(""" CREATE TABLE IF NOT EXISTS Items (
            ItemToOrderID INTEGER,
            OrderID INTEGER references Orders(OrderID),
            BikeProdID INTEGER references BikeProducts(BikeProdID),
            BikeProdName nvarchar(50),
            ItemQuantity INTEGER
    )""")

# SUBMITTING TOGETHER, FOREIGN KEYS WORK
def submit():
    # Connect to the database
    conn = sqlite3.connect('BikeStores.db')

    # Create cursor
    c = conn.cursor()

    # Inserting data into the database
    # Store
    c.execute("INSERT INTO Stores VALUES ('" + str(store_id.get()) + "', '" + str(store_name.get()) + "', '" + str(
        store_email.get()) + "', '" + str(store_phone.get()) + "', '" + str(store_address.get()) + "', '" + str(
        store_zipcode.get()) + "')")
    # BikeCategory
    c.execute("INSERT INTO BikeCategory VALUES ('" + str(bike_cat_id.get()) + "', '" + str(bike_cat.get()) + "')")
    # BikeBrand
    c.execute("INSERT INTO BikeBrand VALUES ('" + str(bike_brand_id.get()) + "', '" + str(bike_brand.get()) + "')")
    # BikeProducts
    c.execute("INSERT INTO BikeProducts VALUES ('" + str(bike_prod_id.get()) + "', '" + str(
        bike_prod_name.get()) + "', '" + str(bike_prod_year.get()) + "', '" + str(bike_prod_price.get()) + "', '" + str(
        bike_brand_id.get()) + "', '" + str(bike_cat_id.get()) + "')")
    # Customers
    c.execute("INSERT INTO Customers VALUES ('" + str(cust_id.get()) + "', '" + str(cust_first_name.get()) + "', '" + str(
            cust_last_name.get()) + "', '" + str(cust_email.get()) + "', '" + str(cust_phone.get()) + "', '" + str(
            cust_address.get()) + "')")
    # Orders
    c.execute("INSERT INTO Orders VALUES ('" + str(order_id.get()) + "', '" + str(order_date.get()) + "', '" + str(
        cust_id.get()) + "', '" + str(store_staff_id.get()) + "', '" + str(discount.get()) + "', '" + str(
        total_price.get()) + "')")
    # Stock
    c.execute("INSERT INTO Stock VALUES ('" + str(stock_id.get()) + "', '" + str(store_id.get()) + "', '" + str(
        bike_prod_id.get()) + "', '" + str(stock_quantity.get()) + "')")
    # Staff
    c.execute("INSERT INTO Staff VALUES ('" + str(staff_id.get()) + "', '" + str(staff_first_name.get()) + "', '" + str(
        staff_last_name.get()) + "', '" + str(staff_email.get()) + "', '" + str(staff_phone.get()) + "', '" + str(
        staff_address.get()) + "')")
    # StoreStaff
    c.execute("INSERT INTO StoreStaff VALUES ('" + str(store_staff_id.get()) + "', '" + str(staff_id.get()) + "', '" + str(
            store_id.get()) + "')")
    # Managers
    c.execute("INSERT INTO Managers VALUES ('" + str(manager_id.get()) + "', '" + str(store_id.get()) + "', '" + str(
        staff_id.get()) + "')")

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

# SUBMITTING INDIVIDUALLY (FOREIGN KEYS DONT WORK)
def submit_stores():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO Stores VALUES ('" + str(store_id.get()) + "', '" + str(store_name.get()) + "', '" + str(
        store_email.get()) + "', '" + str(store_phone.get()) + "', '" + str(store_address.get()) + "', '" + str(
        store_zipcode.get()) + "')")

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

# submit_stores buttons
submit_stores_btn = Button(root, text="Submit Stores", fg="black", width=10, height=1, command=submit_stores)
# place under the stores label's
submit_stores_btn.grid(row=7, column=0, padx=10, pady=10)


def submit_bike_category():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO BikeCategory VALUES ('" + str(bike_cat_id.get()) + "', '" + str(bike_cat.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Bike Category
    bike_cat_id.delete(0, END)
    bike_cat.delete(0, END)

# submit_bike_category buttons
submit_bike_category_btn = Button(root, text="Submit Bike Cat", fg="black", width=12, height=1, command=submit_bike_category)
# place under the bike category label's
submit_bike_category_btn.grid(row=3, column=2, padx=10, pady=10)

def submit_bike_brand():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO BikeBrand VALUES ('" + str(bike_brand_id.get()) + "', '" + str(bike_brand.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Bike Brand
    bike_brand_id.delete(0, END)
    bike_brand.delete(0, END)

# submit_bike_brand buttons
submit_bike_brand_btn = Button(root, text="Submit \nBike Brand", fg="black", width=8, height=2, command=submit_bike_brand)
# place under the bike brand label's
submit_bike_brand_btn.grid(row=3, column=4, padx=10, pady=10)

def submit_bike_product():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO BikeProducts VALUES ('" + str(bike_prod_id.get()) + "', '" + str(
        bike_prod_name.get()) + "', '" + str(bike_prod_year.get()) + "', '" + str(bike_prod_price.get()) + "', '" + str(
        bike_brand_id.get()) + "', '" + str(bike_cat_id.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Bike Product
    bike_prod_id.delete(0, END)
    bike_prod_name.delete(0, END)
    bike_prod_year.delete(0, END)
    bike_prod_price.delete(0, END)

# submit_bike_product buttons
submit_bike_product_btn = Button(root, text="Submit Bike Prod", fg="black", width=13, height=1, command=submit_bike_product)
# place under the bike product label's
submit_bike_product_btn.grid(row=4, column=6, padx=10, pady=10)

def submit_customer():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO Customers VALUES ('" + str(cust_id.get()) + "', '" + str(cust_first_name.get()) + "', '" + str(
        cust_last_name.get()) + "', '" + str(cust_email.get()) + "', '" + str(cust_phone.get()) + "', '" + str(
        cust_address.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Customer
    cust_id.delete(0, END)
    cust_first_name.delete(0, END)
    cust_last_name.delete(0, END)
    cust_email.delete(0, END)
    cust_phone.delete(0, END)
    cust_address.delete(0, END)

# submit_customer buttons
submit_customer_btn = Button(root, text="Submit Customer", fg="black", width=13, height=1, command=submit_customer)
# place under the customer label's
submit_customer_btn.grid(row=7, column=8, padx=10, pady=10)

def submit_order():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO Orders VALUES ('" + str(order_id.get()) + "', '" + str(order_date.get()) + "', '" + str(
        cust_id.get()) + "', '" + str(store_staff_id.get()) + "', '" + str(discount.get()) + "', '" + str(
        total_price.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Order
    order_id.delete(0, END)
    order_date.delete(0, END)
    discount.delete(0, END)
    total_price.delete(0, END)

# submit_orders buttons
submit_order_btn = Button(root, text="Submit Orders", fg="black", width=10, height=1, command=submit_order)
# place under the order label's
submit_order_btn.grid(row=4, column=10)

def submit_stock():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO Stock VALUES ('" + str(stock_id.get()) + "', '" + str(store_id.get()) + "', '" + str(
        bike_prod_id.get()) + "', '" + str(stock_quantity.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Stock
    stock_id.delete(0, END)
    stock_quantity.delete(0, END)

# submit_stock buttons
submit_stock_btn = Button(root, text="Submit Stock", fg="black", width=10, height=1, command=submit_stock)
# place under the stock label's
submit_stock_btn.grid(row=15, column=0, padx=10, pady=10)

def submit_staff():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO Staff VALUES ('" + str(staff_id.get()) + "', '" + str(staff_first_name.get()) + "', '" + str(
        staff_last_name.get()) + "', '" + str(staff_email.get()) + "', '" + str(staff_phone.get()) + "', '" + str(
        staff_address.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Staff
    staff_id.delete(0, END)
    staff_first_name.delete(0, END)
    staff_last_name.delete(0, END)
    staff_email.delete(0, END)
    staff_phone.delete(0, END)
    staff_address.delete(0, END)

# submit_staff buttons
submit_staff_btn = Button(root, text="Submit Staff", fg="black", width=9, height=1, command=submit_staff)
# place under the staff label's
submit_staff_btn.grid(row=19, column=2, padx=10, pady=10)

def submit_storestaff():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO StoreStaff VALUES ('" + str(store_staff_id.get()) + "', '" + str(staff_id.get()) + "', '" + str(
            store_id.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # StoreStaff
    store_staff_id.delete(0, END)

# submit_storestaff buttons
submit_storestaff_btn = Button(root, text="Submit StoreStaff", fg="black", width=13, height=1, command=submit_storestaff)
# place under the store staff label's
submit_storestaff_btn.grid(row=14, column=4, padx=10, pady=10)

def submit_manager():
    conn = sqlite3.connect('BikeStores.db')
    c = conn.cursor()

    c.execute("INSERT INTO Managers VALUES ('" + str(manager_id.get()) + "', '" + str(store_id.get()) + "', '" + str(
        staff_id.get()) + "')")

    conn.commit()

    c.close()
    conn.close()

    # Clear the text boxes once data is submitted
    # Manager
    manager_id.delete(0, END)

# submit_manager buttons
submit_manager_btn = Button(root, text="Submit Manager", fg="black", width=12, height=1, command=submit_manager)
# place under the manager label's
submit_manager_btn.grid(row=14, column=6, padx=10, pady=10)

# SUBMITTING ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Text boxes (used to enter and identify data)
# Stores
store_id = Entry(root, width=15)
store_id.grid(row=0, column=1)
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
bike_cat_id.grid(row=0, column=3)
bike_cat = Entry(root, width=15)
bike_cat.grid(row=1, column=3)
# Bike Brand
bike_brand_id = Entry(root, width=15)
bike_brand_id.grid(row=0, column=5)
bike_brand = Entry(root, width=15)
bike_brand.grid(row=1, column=5)
# Bike Product
bike_prod_id = Entry(root, width=15)
bike_prod_id.grid(row=0, column=7)
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
order_id.grid(row=0, column=11)
order_date = Entry(root, width=15)
order_date.grid(row=1, column=11)
discount = Entry(root, width=15)
discount.grid(row=2, column=11)
total_price = Entry(root, width=15)
total_price.grid(row=3, column=11)
# Stock
stock_id = Entry(root, width=15)
stock_id.grid(row=13, column=1)
stock_quantity = Entry(root, width=15)
stock_quantity.grid(row=14, column=1)
# Staff
staff_id = Entry(root, width=15)
staff_id.grid(row=13, column=3)
staff_first_name = Entry(root, width=15)
staff_first_name.grid(row=14, column=3)
staff_last_name = Entry(root, width=15)
staff_last_name.grid(row=15, column=3)
staff_email = Entry(root, width=15)
staff_email.grid(row=16, column=3)
staff_phone = Entry(root, width=15)
staff_phone.grid(row=17, column=3)
staff_address = Entry(root, width=15)
staff_address.grid(row=18, column=3)
# StoreStaff
store_staff_id = Entry(root, width=15)
store_staff_id.grid(row=13, column=5)
# Managers
manager_id = Entry(root, width=15)
manager_id.grid(row=13, column=7)

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
discount_label = Label(root, text="Discount")
discount_label.grid(row=2, column=10, pady=10)
total_price_label = Label(root, text="Total Price")
total_price_label.grid(row=3, column=10, pady=10)
# Stock
stock_id_label = Label(root, text="Stock ID")
stock_id_label.grid(row=13, column=0, pady=10)
stock_quantity_label = Label(root, text="Stock Quantity")
stock_quantity_label.grid(row=14, column=0, pady=10)
# Staff
staff_id_label = Label(root, text="Staff ID")
staff_id_label.grid(row=13, column=2, pady=10)
staff_first_name_label = Label(root, text="Staff First Name")
staff_first_name_label.grid(row=14, column=2, pady=10)
staff_last_name_label = Label(root, text="Staff Last Name")
staff_last_name_label.grid(row=15, column=2, pady=10)
staff_email_label = Label(root, text="Staff Email")
staff_email_label.grid(row=16, column=2, pady=10)
staff_phone_label = Label(root, text="Staff Phone")
staff_phone_label.grid(row=17, column=2, pady=10)
staff_address_label = Label(root, text="Staff Address")
staff_address_label.grid(row=18, column=2, pady=10)
# StoreStaff
store_staff_id_label = Label(root, text="Store Staff ID")
store_staff_id_label.grid(row=13, column=4, pady=10)
# Managers
manager_id_label = Label(root, text="Manager ID")
manager_id_label.grid(row=13, column=6, pady=10)

# Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=12, column=8, columnspan=2, pady=10, padx=10, ipadx=10)


# Print the data from the datbase to the GUI
def query_to_gui():
    gui_print = Tk()
    gui_print.title("Printed Data")
    gui_print.geometry("1200x800")
    gui_print.configure(background='#919191')
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
    l = conn.cursor()

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
    l.execute("Select * FROM Items")

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
    item_output = l.fetchall()

    # check if there is data in output
    # Stores
    if len(output) > 0:
        print_records = 'Stores'
        for record in output:
            print_records += str(record) + "\n"

        global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Bike Category
    if len(bike_output) > 0:
        print_records = 'Bike Category'
        for record in bike_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Bike Brand
    if len(brand_output) > 0:
        print_records = 'Bike Brand'
        for record in brand_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=2, column=0, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Bike Product
    if len(prod_output) > 0:
        print_records = 'Bike Product'
        for record in prod_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=3, column=0, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Customers
    if len(cust_output) > 0:
        print_records = 'Customers'
        for record in cust_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=4, column=0, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Orders
    if len(order_output) > 0:
        print_records = 'Orders'
        for record in order_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=5, column=0, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Stock
    if len(stock_output) > 0:
        print_records = 'Stock'
        for record in stock_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=0, column=6, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Staff
    if len(staff_output) > 0:
        print_records = 'Staff'
        for record in staff_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=1, column=6, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Store Staff
    if len(store_staff_output) > 0:
        print_records = 'Store Staff'
        for record in store_staff_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=2, column=6, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Managers
    if len(manager_output) > 0:
        print_records = 'Managers'
        for record in manager_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=3, column=6, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    # Items
    if len(item_output) > 0:
        print_records = 'Items'
        for record in item_output:
            print_records += str(record) + "\n"

        # global query_label
        query_label = Label(gui_print, text=print_records)
        query_label.grid(row=4, column=6, columnspan=3, pady=10, padx=10)
    else:
        time.sleep(1)
        query_label.destroy()

    c.close()
    conn.close()


conn = sqlite3.connect('BikeStores.db')
c = conn.cursor()
# Buttons
# Defining the buttons
def search_stores():
    search_stores = Tk()
    search_stores.title("Sales/Staff")
    search_stores.geometry("1200x800")
    search_stores.configure(background='#d9d9d9')

    # Entry box to search for stores (Pick a store from the pulldown)
    # Working within the search_stores window

    stores = ['Store 1', 'Store 2', 'Store 3']

    store_one = [(c.execute("Select * FROM Stock WHERE StoreID = 1")).fetchall(), c.execute("Select * from Stores WHERE StoreID = 1").fetchall()]
    store_two = [(c.execute("Select * FROM Stock WHERE StoreID = 2")).fetchall(), c.execute("Select * from Stores WHERE StoreID = 2").fetchall()]
    store_three = [(c.execute("Select * FROM Stock WHERE StoreID = 3")).fetchall(), c.execute("Select * from Stores WHERE StoreID = 3").fetchall()]

    def dropdown_stores(e):
        listbox3.delete(0, END)
        if store_label.get() == "Store 1":
            for item in store_one:
                listbox3.insert(END, item)
        if store_label.get() == "Store 2":
            for item in store_two:
                listbox3.insert(END, item)
        if store_label.get() == "Store 3":
            for item in store_three:
                listbox3.insert(END, item)

    store_search_label = Label(search_stores, text="Search for a store:")
    store_search_label.grid(row=0, column=0, columnspan=3)
    # Buttons in the search store window
    # Drop down box to select the store
    store_label = ttk.Combobox(search_stores, values=stores)
    store_label.current(0)
    store_label.grid(row=1, column=0, pady=2, padx=2, ipadx=5)
    # Listbox to print store results
    listbox3 = Listbox(search_stores, height=5, width=15)
    listbox3.grid(row=2, column=0, pady=5, padx=5, ipadx=50)
    # Bind
    store_label.bind("<<ComboboxSelected>>", dropdown_stores)

    # Searching for what stores have what bikes (within the search_stores window)
    bikes = ['Pegasus', 'Burley', 'Canyon']

    # select the first value in the Stock table from column BikeProdID
    small_colors = [(c.execute("Select Stock.BikeProdID FROM Stock WHERE StoreID = 1")).fetchall(), c.execute("Select * FROM BikeProducts WHERE BikeProdID = 31").fetchall()]
    medium_colors = [(c.execute("Select Stock.BikeProdID FROM Stock WHERE StoreID = 2")).fetchall(), c.execute("Select * FROM BikeProducts WHERE BikeProdID = 32").fetchall()]
    large_colors = [(c.execute("Select Stock.BikeProdID FROM Stock WHERE StoreID = 3")).fetchall(), c.execute("Select * FROM BikeProducts WHERE BikeProdID = 33").fetchall()]

    # When a store is picked, the bikes will show up
    def pick_color(e):
        listbox2.delete(0, END)
        if my_combo.get() == "Pegasus":
            for item in small_colors:
                listbox2.insert(END, item)
        instock_label = Label(search_stores, text="Bike is in stock")
        instock_label.grid(row=13, column=0, pady=10)
        if my_combo.get() == "Burley":
            for item in medium_colors:
                listbox2.insert(END, item)
        instock_label = Label(search_stores, text="Bike is in stock")
        instock_label.grid(row=13, column=0, pady=10)
        if my_combo.get() == "Canyon":
            for item in large_colors:
                listbox2.insert(END, item)
        instock_label = Label(search_stores, text="Bike is in stock")
        instock_label.grid(row=13, column=0, pady=10)

    # Create a drop down box to select the store
    my_combo = ttk.Combobox(search_stores, values=bikes)
    my_combo.current(0)
    my_combo.grid(row=8, column=0, pady=2, padx=2, ipadx=5)
    # Listbox where input from dropbox will show up
    listbox2 = Listbox(search_stores, height=5, width=15)
    listbox2.grid(row=9, column=0, pady=5, padx=5, ipadx=50)
    # Bind
    my_combo.bind("<<ComboboxSelected>>", pick_color)

    # Staff functionality
    staff_search_label = Label(search_stores, text="Search for a\n staff member")
    staff_search_label.grid(row=0, column=1)

    staff = ['Bob Bill', 'Randy Rall', 'Sally Smith', 'Joe Johnson']

    staff_one = [(c.execute("Select * FROM Staff WHERE StaffFirstName = 'Bob'")).fetchall()]
    staff_two = [(c.execute("Select * FROM Staff WHERE StaffFirstName = 'Randy'")).fetchall()]
    staff_three = [(c.execute("Select * FROM Staff WHERE StaffFirstName = 'Sally'")).fetchall()]
    staff_four = [(c.execute("Select * FROM Staff WHERE StaffFirstName = 'Joe'")).fetchall()]

    # Pick a staff member from drop down box
    def pick_staff(e):
        listbox4.delete(0, END)
        if staff_label.get() == "Bob Bill":
            for item in staff_one:
                listbox4.insert(END, item)
        if staff_label.get() == "Randy Rall":
            for item in staff_two:
                listbox4.insert(END, item)
        if staff_label.get() == "Sally Smith":
            for item in staff_three:
                listbox4.insert(END, item)
        if staff_label.get() == "Joe Johnson":
            for item in staff_four:
                listbox4.insert(END, item)

    # Staff drop down box
    staff_label = ttk.Combobox(search_stores, values=staff)
    staff_label.current(0)
    staff_label.grid(row=1, column=1, pady=2, padx=2, ipadx=5)
    # Listbox to show staff results
    listbox4 = Listbox(search_stores, height=5, width=15)
    listbox4.grid(row=2, column=1, pady=5, padx=5, ipadx=50)
    # Bind
    staff_label.bind("<<ComboboxSelected>>", pick_staff)

    # Customer functionality
    # def submit_customers():
    #     # Customers
    #     c.execute(
    #         "INSERT INTO Customers VALUES ('" + str(cust_id.get()) + "', '" + str(cust_first_name.get()) + "', '" + str(
    #             cust_last_name.get()) + "', '" + str(cust_email.get()) + "', '" + str(cust_phone.get()) + "', '" + str(
    #             cust_address.get()) + "')")
    #     # Delete after entry
    #     conn.commit()
    #     cust_id.delete(0, END)
    #     cust_first_name.delete(0, END)
    #     cust_last_name.delete(0, END)
    #     cust_email.delete(0, END)
    #     cust_phone.delete(0, END)
    #     cust_address.delete(0, END)
    #
    # # Entry boxes for customers
    # cust_id = Entry(search_stores, width=10)
    # cust_id.grid(row=0, column=9)
    # cust_first_name = Entry(search_stores, width=10)
    # cust_first_name.grid(row=1, column=9)
    # cust_last_name = Entry(search_stores, width=10)
    # cust_last_name.grid(row=2, column=9)
    # cust_email = Entry(search_stores, width=10)
    # cust_email.grid(row=3, column=9)
    # cust_phone = Entry(search_stores, width=10)
    # cust_phone.grid(row=4, column=9)
    # cust_address = Entry(search_stores, width=10)
    # cust_address.grid(row=5, column=9)
    # # Labels for customers
    # cust_id_label = Label(search_stores, text="Customer ID")
    # cust_id_label.grid(row=0, column=8)
    # cust_first_name_label = Label(search_stores, text="Customer First Name")
    # cust_first_name_label.grid(row=1, column=8)
    # cust_last_name_label = Label(search_stores, text="Customer Last Name")
    # cust_last_name_label.grid(row=2, column=8)
    # cust_email_label = Label(search_stores, text="Customer Email")
    # cust_email_label.grid(row=3, column=8)
    # cust_phone_label = Label(search_stores, text="Customer Phone")
    # cust_phone_label.grid(row=4, column=8)
    # cust_address_label = Label(search_stores, text="Customer Address")
    # cust_address_label.grid(row=5, column=8)
    # # Submit button
    # submit_button = Button(search_stores, text="Submit Customers", command=submit_customers)
    # submit_button.grid(row=8, column=8)

    # Order & Items functionality
    def submit_orders():
        # Orders
        c.execute("INSERT INTO Orders VALUES ('" + str(order_id.get()) + "', '" + str(order_date.get()) + "', '" + str(
            cust_id.get()) + "', '" + str(store_staff_id.get()) + "', '" + str(discount.get()) + "', '" + str(
            total_price.get()) + "')")
        # Delete after entry
        conn.commit()
        order_id.delete(0, END)
        order_date.delete(0, END)
        cust_id.delete(0, END)
        store_staff_id.delete(0, END)
        discount.delete(0, END)
        total_price.delete(0, END)

        # Items
        c.execute("INSERT INTO Items VALUES ('" + str(item_id.get()) + "', '" + str(order_id.get()) + "', '" + str(
            bike_prod_id.get()) + "', '" + str(bike_prod_name.get()) + "', '" + str(quantity.get()) + "')")
        # Delete after entry
        conn.commit()
        item_id.delete(0, END)
        order_id.delete(0, END)
        bike_prod_id.delete(0, END)
        quantity.delete(0, END)


    # Entry boxes for orders
    order_id = Entry(search_stores, width=10)
    order_id.grid(row=0, column=11, padx=20)
    order_date = Entry(search_stores, width=10)
    order_date.grid(row=1, column=11)
    cust_id = Entry(search_stores, width=10)
    cust_id.grid(row=2, column=11)
    # store_staff_id = Entry(search_stores, width=10)
    # store_staff_id.grid(row=3, column=11)
    discount = Entry(search_stores, width=10)
    discount.grid(row=4, column=11)
    total_price = Entry(search_stores, width=10)
    total_price.grid(row=5, column=11)
    # Labels for orders
    order_id_label = Label(search_stores, text="Order ID")
    order_id_label.grid(row=0, column=10, pady=10)
    order_date_label = Label(search_stores, text="Order Date")
    order_date_label.grid(row=1, column=10, pady=10)
    cust_id_label = Label(search_stores, text="Customer ID")
    cust_id_label.grid(row=2, column=10, pady=10)

    store_staff_id_label = Label(search_stores, text="Staff Sellling")
    store_staff_id_label.grid(row=3, column=10, pady=10)
    staff_names = ['Bob Bill', 'Randy Rall', 'Sally Smith']

    def pick_staff(e):
        if store_staff_id_list.get() == 'Bob Bill':
            store_staff_id.set('Bob Bill')
        elif store_staff_id_list.get() == 'Randy Rall':
            store_staff_id.set('Randy Rall')
        elif store_staff_id_list.get() == 'Sally Smith':
            store_staff_id.set('Sally Smith')

    store_staff_id_list = ttk.Combobox(search_stores, values=staff_names, width=10)
    store_staff_id_list.grid(row=3, column=11)

    discount_label = Label(search_stores, text="Discount")
    discount_label.grid(row=4, column=10, pady=10)
    total_price_label = Label(search_stores, text="Total Price")
    total_price_label.grid(row=5, column=10, pady=10)
    # Submit button FOR ORDERS AND ITEMS
    submit_button = Button(search_stores, text="Submit Orders & Items", command=submit_orders)
    submit_button.grid(row=8, column=12)
    # Submit button for just orders
    submit_button = Button(search_stores, text="Submit Orders", command=submit_orders)
    submit_button.grid(row=8, column=11)
    # # Entry boxes for items
    item_id = Entry(search_stores, width=10)
    item_id.grid(row=0, column=13, padx=20)

    choose_bike_label = Label(search_stores, text="What bike is being purchased?")
    choose_bike_label.grid(row=5, column=0, pady=10)

    products = ['Pegasus', 'Burley', 'Canyon']

    def pick_bike_product(e):
        bike_prod_id.delete(0, END)
        if bike_prod_name.get() == 'Pegasus':
            bike_prod_id.set('Pegasus')
        elif bike_prod_name.get() == 'Burley':
            bike_prod_id.set('Burley')
        elif bike_prod_name.get() == 'Canyon':
            bike_prod_id.set('Canyon')


    # Entry boxes
    bike_prod_name = ttk.Combobox(search_stores, values=products, width=10)
    bike_prod_name.grid(row=2, column=13)
    # bike_prod_id = Entry(search_stores, width=10)
    # bike_prod_id.grid(row=1, column=13)
    bike_ids = ['31', '32', '33']

    def pick_bike_ids(e):
        bike_prod_id.delete(0, END)
        if bike_prod_id_list.get() == '31':
            bike_prod_id.set('31')
        elif bike_prod_id_list.get() == '32':
            bike_prod_id.set('32')
        elif bike_prod_id_list.get() == '33':
            bike_prod_id.set('33')

    bike_prod_id_list = ttk.Combobox(search_stores, values=bike_ids, width=10)
    bike_prod_id_list.grid(row=1, column=13)

    quantity = Entry(search_stores, width=10)
    quantity.grid(row=3, column=13)
    # Labels for items
    item_id_label = Label(search_stores, text="Item Order ID")
    item_id_label.grid(row=0, column=12)
    bike_prod_id_label = Label(search_stores, text="Bike Product ID")
    bike_prod_id_label.grid(row=1, column=12)
    bike_prod_name_label = Label(search_stores, text="Bike Product Name")
    bike_prod_name_label.grid(row=2, column=12)
    quantity_label = Label(search_stores, text="Quantity")
    quantity_label.grid(row=3, column=12)
    # Submit button for just items
    submit_button = Button(search_stores, text="Submit Items", command=submit_orders)
    submit_button.grid(row=8, column=13)

    # Subtract 1 value from quantity
    def subtract_quantity():
        if store_label.get() == "Store 1":
            # subtract quantity from stock table where store id is 1
            c.execute("UPDATE Stock SET StockQuantity = StockQuantity - 1 WHERE StoreID = '1'")
        elif store_label.get() == "Store 2":
            # subtract quantity from stock table where store id is 2
            c.execute("UPDATE Stock SET StockQuantity = StockQuantity - 1 WHERE StoreID = '2'")
        elif store_label.get() == "Store 3":
            # subtract quantity from stock table where store id is 3
            c.execute("UPDATE Stock SET StockQuantity = StockQuantity - 1 WHERE StoreID = '3'")
        conn.commit()


    # Create a button to subtract 1 from quantity
    subtract_button = Button(search_stores, text="Item Sold! -1 quantity", command=subtract_quantity)
    subtract_button.grid(row=3, column=14)





# Buttons on the main window to open the new window
# Sales/Staff
search_store_button = Button(root, text="Sales/Staff", command=search_stores)
search_store_button.grid(row=17, column=5, columnspan=3, pady=10, padx=10)

# Closeing the connection
# conn.commit()
# c.close()
# conn.close()

# Query button
query_button = Button(root, text="Show records", command=query_to_gui)
query_button.grid(row=13, column=8, columnspan=2, pady=10, padx=10, ipadx=10)


# ---------------------------------------------------------------------------------------------------------


# Create a function to delete any empty table
def delete_empty_tables():
    c.execute("DELETE FROM Stores WHERE StoreID = ''")
    c.execute("DELETE FROM BikeCategory WHERE BikeCatID = ''")
    c.execute("DELETE FROM BikeBrand WHERE BikeBrandID = ''")
    c.execute("DELETE FROM BikeProducts WHERE BikeProdID = ''")
    c.execute("DELETE FROM Customers WHERE CustID = ''")
    c.execute("DELETE FROM Orders WHERE OrderID = ''")
    c.execute("DELETE FROM Stock WHERE StockID = ''")
    c.execute("DELETE FROM Staff WHERE StaffID = ''")
    c.execute("DELETE FROM StoreStaff WHERE StoreStaffID = ''")
    c.execute("DELETE FROM Managers WHERE ManagerID = ''")
    c.execute("DELETE FROM Items WHERE ItemToOrderID = ''")
    conn.commit()

# Create a button for delete_empty_tables
delete_empty_button = Button(root, text="Delete Empty Tables", command=delete_empty_tables)
delete_empty_button.grid(row=13, column=10, columnspan=2, pady=10, padx=10, ipadx=10)


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
delete_button.grid(row=14, column=8, columnspan=2, pady=10, padx=10)
# Delete BikeCategory
delete_button2 = Button(root, text="Delete BikeCategory", command=lambda: delete_rows("BikeCategory"))
delete_button2.grid(row=15, column=8, columnspan=2, pady=10, padx=10)
# Delete BikeBrand
delete_button3 = Button(root, text="Delete BikeBrand", command=lambda: delete_rows("BikeBrand"))
delete_button3.grid(row=16, column=8, columnspan=2, pady=10, padx=10)
# Delete BikeProduct
delete_button4 = Button(root, text="Delete BikeProducts", command=lambda: delete_rows("BikeProducts"))
delete_button4.grid(row=17, column=8, columnspan=2, pady=10, padx=10)
# Delete Customers
delete_button5 = Button(root, text="Delete Customers", command=lambda: delete_rows("Customers"))
delete_button5.grid(row=18, column=8, columnspan=2, pady=10, padx=10)
# Delete Orders
delete_button6 = Button(root, text="Delete Orders", command=lambda: delete_rows("Orders"))
delete_button6.grid(row=19, column=8, columnspan=2, pady=10, padx=10)
# Delete Stock
delete_button7 = Button(root, text="Delete Stock", command=lambda: delete_rows("Stock"))
delete_button7.grid(row=20, column=8, columnspan=2, pady=10, padx=10)
# Delete Staff
delete_button8 = Button(root, text="Delete Staff", command=lambda: delete_rows("Staff"))
delete_button8.grid(row=21, column=8, columnspan=2, pady=10, padx=10)
# Delete StoreStaff
delete_button9 = Button(root, text="Delete StoreStaff", command=lambda: delete_rows("StoreStaff"))
delete_button9.grid(row=22, column=8, columnspan=2, pady=10, padx=10)
# Delete Managers
delete_button10 = Button(root, text="Delete Managers", command=lambda: delete_rows("Managers"))
delete_button10.grid(row=23, column=8, columnspan=2, pady=10, padx=10)

# conn.commit()
# conn.close()

# Connection for dropdown menu
# conn = sqlite3.connect('BikeStores.db')
# c = conn.cursor()

if __name__ == '__main__':
    root.mainloop()
