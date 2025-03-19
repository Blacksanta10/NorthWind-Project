### This file contains the features from the menu options.

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
            INSERT INTO Customers (Company, 'Last Name', 'First Name', 'Email Address', 'Job Title', 'Business Phone')
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
        cursor.execute("SELECT ID FROM Customers WHERE ID = %s", (customer_id,))
        if not cursor.fetchone():  #Info validation
            print(f'Error: Customer ID does not exist.')
            return
        
        #2. Employee ID and validate
        employee_id = input(f"Enter Employee ID: ")
        cursor.execute("SELECT ID FROM Employees WHERE ID = %s", (employee_id,))

        if not cursor.fetchone():  #Info validation
            print(f'Error: Employee ID N/a')

        #3. Shipper_ID and validate
        shipper_id = input(f"Enter Shipper ID: ")
        cursor.execute("SELECT ID FROM Shippers WHERE ID = %s", (shipper_id,))

        if not cursor.fetchone():  #Info validation
            print(f"Error: Shipper ID does not exist.")

        #4. Get Shipping details 
        ship_name = input(f"Enter Ship Name: ")
        ship_address = input(f"Enter Ship Address: ")
        ship_city = input(f"Enter Ship City: ")
        ship_state = input(f"Enter Ship State: ")
        ship_zip = input(f"Enter Ship Zip/Postal Code: ")
        ship_country = input(f"Enter Ship Country: ")

    except Exception as e:
        db.rollback()  #transaction control 
        print(f"Error: {e}")

    finally:
        cursor.close()


def remove_order():
    None

def ship_order():
    None

def print_pending_orders():
    None

def more_options():
    None



