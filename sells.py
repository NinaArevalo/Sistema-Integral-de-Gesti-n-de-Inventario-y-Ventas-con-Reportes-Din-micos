import os
import csv
import datetime


Sales_list = []
IDs_sales = set()

file = "sells.csv"

if os.path.exists(file) and os.stat(file).st_size > 0:
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            IDs_sales.add(row["Sales_ID"])

def New_sales():

    while True:
        Sale = {} #here I'm looking for represent the dicctionary

        unique_ID = input ("Hi, enter the sale ID or write 'End' to finish close: ")

        if unique_ID.lower() == "end":
            break

        if unique_ID in IDs_sales:
            print("this sale is already register in the system, please, enter a new sell ID")
            continue
        # here we are starting to request the book information to add it in our dicctionary.
        Sale ["Sales_ID"]  =  unique_ID
        IDs_sales.add(unique_ID)
        
        Sale ["Client"] = input("Enter the cLient's name: ")
        Sale ["Product"] = input("Enter the Book ID for the product selected: ")
        Sale ["Amount"] = input ("Enter the Amount: ")
        Sale ["Date"] = datetime.datetime.now()
        Sale ["Discount amount"] = input("Enter the discount amount for this sale: ")
        Sales_list.append(Sale)

    fieldnames = ["Sales_ID","Client","Product","Amount", "Date", "Discount amount"]

    file_exist = os.path.exists
    
    with open(file, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter (f,fieldnames = fieldnames)

        if not file_exist  or os.stat(file).st_size == 0:
            w.writeheader()

        for sells in Sales_list:
            w.writerow(sells)
