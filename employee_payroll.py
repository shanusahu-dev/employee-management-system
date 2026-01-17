import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shanu123",
        database="company_db"
    )

def add_employee():
    conn = get_connection()
    cursor = conn.cursor()

    emp_id = int(input("Enter ID: "))
    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    tax = salary * 0.1
    net_salary = salary - tax
    print(f"Calculated Tax(10%): {tax}")
    print(f"Net Salary: {net_salary}")

    query = """
    INSERT INTO employees (emp_id, name, salary, tax, net_salary)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (emp_id, name, salary, tax, net_salary))
    conn.commit()

    print("Employee added successfully")

    conn.close()

def main():
    while True:
        print("\n1. Add Employee")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            break
        else:
            print("Invalid choice")

main()
