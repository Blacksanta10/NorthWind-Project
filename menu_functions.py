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

def add_order():
    None

def remove_order():
    None

def ship_order():
    None

def print_pending_orders():
    None

def more_options():
    None



