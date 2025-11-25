#"os" is used to keep the code constant and make navigating within it much easier.
import os
import csv

Librery_list = []
IDs_books = set()
#Throughout this file I was responsible for bringing the information from stock.csv, ensuring that the information is always saved there and also that it is taken into account for any action requested by the operator.
file = "stock.csv"

if os.path.exists(file) and os.stat(file).st_size > 0:
    with open(file, "r", encoding="utf-8") as f: 
        reader = csv.DictReader(f)
        for row in reader:
            IDs_books.add(row["Book_ID"])


def book_record():
    
    while True:
        book = {} #here I'm looking for represent the dicctionary

        unique_ID = input ("Hi, enter the book ID or write 'End' to finish close: ")

        if unique_ID.lower() == "end":
            break

        if unique_ID in IDs_books:
            print("this book is already register in the system, please, enter a new boo ID")
            continue
        # here we are starting to request the book information to add it in our dicctionary.
        book ["Book_ID"]  =  unique_ID
        IDs_books.add(unique_ID)
        
        book["Title"] = input("Enter the book title: ")
        book["Autor"] = input("Enter the book's autor: ")
        book ["Category"] = input ("Enter the category: ")
        book["Price"] = input ("Enter the book price: ")
        book ["Amount in stock"] = input("Enter the quantity of these books that are in stock: ")

        Librery_list.append(book)

    fieldnames = ["Book_ID","Title","Autor","Category", "Price", "Amount in stock"]

    file_exist = os.path.exists
    
    with open(file, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter (f,fieldnames = fieldnames)

        if not file_exist  or os.stat(file).st_size == 0:
            w.writeheader()

        for books in Librery_list:
            w.writerow(books)
#Nested "IF" statements were used, in addition to the "While" and "for" loops, to improve code management.
def consult_librery():
    
    file = "stock.csv"

    search_ID = input("Enter the Book ID number: ")

    if not os.path.exists(file) or os.stat(file).st_size == 0:
        print("There are no books associated with this ID entered.")
        return
    
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Book_ID"] == search_ID:
                Book_tupla=tuple(row.values())

                print("ID found: ")
                print (Book_tupla)
                return
    print("ID not found")
            
def update_info_book():

    file = "stock.csv"
    
    if not os.path.exists(file) or os.stat(file).st_size == 0:
        print("There are no books associated with this ID entered.")
        return
    
    search_ID = input("Enter the Book ID number to update: ")

    Updated_books = []
    Found = False

    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
    
        for row in reader:
            if row["Book_ID"] == search_ID:
                Found=True
                change= input("""
                    What is the information that you need to change? 
                        1. Title
                        2. Autor
                        3. Category
                        4. Price
                        5. Amount in stock
                    """)
                
                if not change.isdigit():
                    print("Enter just numbers, it means 1, 2, 3, 4 or 5 option")
                    return
                if change == "1":
                    final_change=input("What is the change: ")
                    if row["Title"] != final_change:
                        row["Title"] = final_change
                    else:
                        row ["Title"] = row ["Title"]
                    
                    print(f"Nueva informacion: {row['Title']}")

                if change == "2":
                    final_change=input("What is the change: ")
                    if row["Autor"] != final_change:
                        row["Autor"] = final_change
                    else:
                        row ["Autor"] = row ["Autor"]
                    
                    print(f"Nueva informacion: {row['Autor']}")

                if change == "3":
                    final_change=input("What is the change: ")
                    if row["Category"] != final_change:
                        row["Category"] = final_change
                    else:
                        row ["Category"] = row ["Category"]
                    
                    print(f"Nueva informacion: {row['Category']}")

                if change == "4":
                    final_change=input("What is the change: ")
                    if row["Price"] != final_change:
                        row["Price"] = final_change
                    else:
                        row ["Price"] = row ["Price"]
                    
                    print(f"Nueva informacion: {row['Price']}")

                if change == "5":
                    final_change=input("What is the change: ")
                    if row["Amount in stock"] != final_change:
                        row["Amount in stock"] = final_change
                    else:
                        row ["Amount in stock"] = row ["Amount in stock"]
                    
                    print(f"Nueva informacion: {row['Amount in stock']}")

            Updated_books.append(row)

    if not Found:
        print("ID not found")
        return

    fieldnames = ["Book_ID","Title","Autor","Category", "Price", "Amount in stock"]

    with open(file, "w", encoding="utf-8", newline="")as f:
        writer =  csv.DictWriter (f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(Updated_books)
        print("Information updated")

def delete_book():

    file = "stock.csv"

    if not os.path.exists(file) or os.stat(file).st_size==0:
        print("There are no books associated with this ID entered.")
        return
    
    search_ID = input("Enter the Book ID number to delete: ")

    Deleted_books = []
    Found = False

    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
    
        for row in reader:
            if row["Book_ID"] == search_ID:
                Found=True
                print("This book has been deleted")
                continue
            Deleted_books.append(row)

    if not Found:
        print("Book ID not found ")
        return
    
    fieldnames = ["Book_ID","Title","Autor","Category", "Price", "Amount in stock"]

    with open(file, "w", encoding="utf-8", newline="")as f:
        writer =  csv.DictWriter (f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(Deleted_books)
    print("Information updated")

