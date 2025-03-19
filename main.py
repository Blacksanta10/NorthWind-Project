

#importing function file
import menu_functions as func

##Next few steps are making and testing connect to Database.
import mysql.connector as dbconn

print ("MySql connector is installed and working")

#Create connection
def connect_to_db():
    try:
        db = dbconn.connect(
            host="localhost", \
            user="cs4430", 
            password="cs4430", 
            db="northwind"
        )
        print(f'Connnected to: {db.database} database')
        return db
    
    except dbconn.Error as e:
        print(f'Database connection error: ', e)
        return None
        


#Displays the main menu options

def main():

    #Establish connection
    db = connect_to_db()
    if not db:
        return
    

    #Main menu display
    while True:
        print(f'\n Main Menu:')
        print(f'1. Add a customer')
        print(f'2. Add an order')
        print(f'3. Remove an order')
        print(f'4. Ship an order')
        print(f'5. Print pending order')
        print(f'6. More Options')
        print(f'7. Exit')

        choice = input("Enter a menu item: ")

        if choice == "1":
            func.add_customer(db)

        elif choice == "2":
            func.add_order(db)
        
        elif choice == "3":
            func.remove_order(db)

        elif choice == "4":
            func.ship_order(db)

        elif choice == "5":
            func.print_pending_orders(db)
        
        elif choice == "6":
            func.more_options(db)
        
        elif choice == "7":
            print("Exiting program")
            break

        else: 
            print(f'\nInvalid choice. Try again')
    
    #Close connection
    db.close()
    
if __name__ == "__main__":
    main()
