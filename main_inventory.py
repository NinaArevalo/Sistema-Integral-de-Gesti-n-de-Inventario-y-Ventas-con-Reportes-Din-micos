
from librery import book_record 
from librery import consult_librery 
from librery import update_info_book 
from librery import delete_book 

#This second menu was created to redirect to specific product information, not sales data. This provides better control over decisions and a clearer visual experience when using the console.
def show_main():
    print("""
             Menu
        >1. Book's record
        >2. Consult librery 
        >3. Update book's information
        >4. Delete book
        >5. Salir
          """)

      
def main_1():
    show_main()
  
    try:
        while True:

            option= input("Choose one of the menu options to continue: ")

            if not option.isdigit():
                print("Choose a valid option: Remember that you just can choose a number like 1, 2, 3, 4 or 5")
                continue

            elif option =="1":
                book_record()
            elif option == "2":
                consult_librery()
            elif option == "3":
                update_info_book()
            elif option == "4":
                delete_book()
            elif option == "5":
                print("\n Returning to the main manu...")
                break
            else:
                
                print("\n Wrong option chose. Please, slect a valid option from 1 to 5.")

    except KeyboardInterrupt:
        print("\n Interrupt menu")
       