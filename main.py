employees = {}

def add_employee(): emp_id = input("Enter Employee ID: ") if emp_id in employees: print("Employee ID already exists!\n") return

name = input("Enter Name: ")
dept = input("Enter Department: ")
salary = float(input("Enter Salary: "))

employees[emp_id] = {
    "name": name,
    "department": dept,
    "salary": salary
}
print("Employee added successfully!\n")

def view_employees(): if not employees: print("No employees found.\n") return

print("\n--- Employee List ---")
for emp_id, details in employees.items():
    print(f"ID: {emp_id} | Name: {details['name']} | Dept: {details['department']} | Salary: {details['salary']}")
print()

def search_employee(): emp_id = input("Enter Employee ID to search: ") if emp_id in employees: e = employees[emp_id] print(f"Found -> Name: {e['name']}, Dept: {e['department']}, Salary: {e['salary']}\n") else: print("Employee not found!\n")

def update_employee(): emp_id = input("Enter Employee ID to update: ") if emp_id not in employees: print("Employee not found!\n") return

print("1. Update Name\n2. Update Department\n3. Update Salary")
choice = input("Choose field to update: ")

if choice == '1':
    employees[emp_id]['name'] = input("Enter new name: ")
elif choice == '2':
    employees[emp_id]['department'] = input("Enter new department: ")
elif choice == '3':
    employees[emp_id]['salary'] = float(input("Enter new salary: "))
else:
    print("Invalid choice!")
    return

print("Employee updated successfully!\n")

def delete_employee(): emp_id = input("Enter Employee ID to delete: ") if emp_id in employees: del employees[emp_id] print("Employee deleted successfully!\n") else: print("Employee not found!\n")

def main(): while True: print("--- Employee Management System ---") print("1. Add Employee") print("2. View Employees") print("3. Search Employee") print("4. Update Employee") print("5. Delete Employee") print("6. Exit")

choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_employee()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        print("Exiting program. Bye!")
        break
    else:
        print("Invalid choice! Try again.\n")

if name == "main": main()
