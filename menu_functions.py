### This file contains the features from the menu options.

from datetime import datetime  #in add_order


def add_customer(db):
    print(f'You chose add customer\n')

    company = input(f"Company name: ")
    last_name = input(f"Last name: ")
    first_name = input(f"Last name: ")
    email = input(f"Email address: ")
    job_title = input(f"Job title: ")
    business_phone = input(f"Business phone: ")

    try:
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO Customers (Company, `Last Name`, `First Name`, `Email Address`, `Job Title`, `Business Phone`)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (company, last_name, first_name, email, job_title, business_phone))
        
        db.commit()
        print("Customer added successfully!")

    except Exception as e:
        print("Error:" , e)

    finally:
        cursor.close()

def add_order(db):
    cursor = db.cursor()

    try: 
        #1. Customer ID and Validate
        customer_id = input(f'Enter Customer: ')
        cursor.execute("SELECT ID FROM Customers WHERE ID = %s", (customer_id,))  #SQL Query

        if not cursor.fetchone():  #Info validation
            print(f'Error: Customer ID does not exist.')
            return
        
        #2. Employee ID and validate
        employee_id = input(f"Enter Employee ID: ")
        cursor.execute("SELECT ID FROM Employees WHERE ID = %s", (employee_id,))  #SQL Query

        if not cursor.fetchone():  #Info validation
            print(f'Error: Employee ID N/a')


        #3. Shipper_ID and validate
        shipper_id = input(f"Enter Shipper ID: ")
        cursor.execute("SELECT ID FROM Shippers WHERE ID = %s", (shipper_id,))  #SQL Query

        if not cursor.fetchone():  #Info validation
            print(f"Error: Shipper ID does not exist.")


        #4. Get Shipping details 
        ship_name = input(f"Enter Ship Name: ")
        ship_address = input(f"Enter Ship Address: ")
        ship_city = input(f"Enter Ship City: ")
        ship_state = input(f"Enter Ship State: ")
        ship_zip = input(f"Enter Ship Zip/Postal Code: ")
        ship_country = input(f"Enter Ship Country: ")

        order_date = datetime.now().strftime('%Y-%m-%d')


        #5. Insert  into Orders Table
        cursor.execute("""
            INSERT INTO Orders (Customer_ID, Employee_ID, Order_Date, Ship_Name, Ship_Address,
                                Ship_City, Ship_State, Ship_ZIP, Ship_Country, Shipper_ID)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (customer_id, employee_id, order_date, ship_name, ship_address, ship_city,
                  ship_state, ship_zip, ship_country, shipper_id))   #SQL query
        

        #Get the generated Order ID
        order_id = cursor.lastrowid


        #6. Add multiple products to the order
        while True:
            product_id = input(f"Enter Product ID (or 'done' to finish)")
            if product_id.lower() == 'done':
                break

            #check if product is discontinued
            cursor.execute("SELECT Discontinued FROM Products WHERE ID = %s", (product_id,))
            product = cursor.fetchone()  #returns discontinued column
            
            if not product:
                print(f"Error: Product ID does not exist")
                continue


            if product[0] == 1: 
                print(f"Error: Product is discontinued, order denied")
                cursor.execute("DELETE FROM Orders WHERE Order_ID = %s",(order_id,))  #deletes your order
                db.commit()
                return
            

            #Get the price and quantity
            quantity = input(f"Enter the quantity of product {product_id}: ")
            price = input(f"Enter the price for product {product_id}: ")


            cursor.execute("""
                INSERT INTO Order_Details (Order_ID, Product_ID, Quantity, Unit_Price)
                VALUES (%s, %s, %s, %s)
            """, (order_id, product_id, quantity, price))  #SQL Query

            db.commit()  #finalizes your transaction
            print(f"Order added successfully!")

    except Exception as e:
        db.rollback()  #transaction control 
        print(f"Error: {e}")

    finally:
        cursor.close()  #closes connection 


def remove_order():
    None

def ship_order():
    None

def print_pending_orders():
    None

def more_options():
    None



