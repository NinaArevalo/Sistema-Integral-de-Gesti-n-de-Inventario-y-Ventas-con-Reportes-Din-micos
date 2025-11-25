#The import function was used to retrieve specific information from the files.

import librery
import main_inventory
import sells
from sells import New_sales
from main_inventory import main_1

#mostramos el menu al operador, este solo es visual. 

def show_main():
    print("""
             Menu
        >1. Inventory management
        >2. Sales registration and inquiry
        >3. Reporting module
        >4. Salir
          """)

 #Here, we generate the process that tells the program what actions to take, because it is an interactive console and the information is located in different files within the same folder.
      
def main():
    show_main()

    option= input("Choose one of the menu options to continue: ")

    if not option.isdigit():
        print("Choose a valid option: Remember that you just can choose a number like 1, 2, 3 or 4")
        
    elif option =="1":
        main_1()
    elif option == "2":
        New_sales()
    elif option == "3":
        print("pending")
    elif option == "4":
        print("Have nice day!")
    else:
        print("Wrong information enter, please, just choose between 1,2,3 or 4 numbers.")
main()