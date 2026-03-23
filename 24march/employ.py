employees = {}

def add_employee():
    """Add a new employee to the system"""
    
    # Get employee ID from user
    emp_id = input("\nEnter Employee ID (e.g., E001): ")
    
    # Check if employee already exists
    if emp_id in employees:
        print("This employee already exists!")
        return
    

    name = input("Enter Employee Name: ")
    
    department = input("Enter Department (IT/HR/Sales): ")
     
    employees[emp_id] = {
        "name": name,
        "department": department,
        "present": 0,      # Count of present days
        "absent": 0,       # Count of absent days
        "leave": 0         # Count of leave days
    }
    
    print(f"✅ {name} added successfully!\n")
 
def remove_employee():
    emp_id = input("\nEnter Employee ID to remove: ")

    if emp_id in employees:
        name = employees[emp_id]["name"]
        del employees[emp_id]
        print(f" {name} removed from system!\n")
    else:
        print(" Employee not found!\n")

def display_all():
    """Show all employees in the system"""
    if len(employees) == 0:
        print("\n❌ No employees in the system!\n")
        return
    
 
    print("\n" + "=" * 70)
    print("ALL EMPLOYEES")
    print("=" * 70)
     
    for emp_id in employees:
        employee = employees[emp_id]
        
        print(f"\nID: {emp_id}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Present: {employee['present']} | Absent: {employee['absent']} | Leave: {employee['leave']}")
    
    print("\n" + "=" * 70 + "\n")

 
def mark_attendance():
    """Mark attendance for an employee"""
    
    # Check if there are employees
    if len(employees) == 0:
        print("\n No employees in system! Add employees first.\n")
        return
    
 
    emp_id = input("\nEnter Employee ID: ")
    
  
    if emp_id not in employees:
        print("❌ Employee not found!\n")
        return
 
    status = input("Mark attendance (P/A/L):\n  P = Present\n  A = Absent\n  L = Leave\nEnter (P/A/L): ").upper()
 
    if status == "P":
        employees[emp_id]["present"] += 1
        print(f"✅ {employees[emp_id]['name']} marked Present!\n")
    
    elif status == "A":
        employees[emp_id]["absent"] += 1
        print(f"✅ {employees[emp_id]['name']} marked Absent!\n")
    
    elif status == "L":
        employees[emp_id]["leave"] += 1
        print(f"✅ {employees[emp_id]['name']} marked Leave!\n")
    
    else:
        print("❌ Invalid input! Enter P, A, or L\n")

def sort_by_name():
 
    
    if len(employees) == 0:
        print("\n❌ No employees in the system!\n")
        return
 
    employee_list = []
    
    for emp_id in employees:
        name = employees[emp_id]["name"]
        employee_list.append((emp_id, name))
 
    employee_list.sort(key=lambda x: x[1])
 
    print("\n" + "=" * 70)
    print("EMPLOYEES SORTED BY NAME")
    print("=" * 70)
    
    for emp_id, name in employee_list:
        employee = employees[emp_id]
        print(f"\n{name} ({emp_id})")
        print(f"  Department: {employee['department']}")
        print(f"  P: {employee['present']} | A: {employee['absent']} | L: {employee['leave']}")
    
    print("\n" + "=" * 70 + "\n")
 
def sort_by_id():
    """Sort employees by ID"""
    
    if len(employees) == 0:
        print("\n❌ No employees in the system!\n")
        return
    
 
    emp_ids = sorted(employees.keys())
 
    print("\n" + "=" * 70)
    print("EMPLOYEES SORTED BY ID")
    print("=" * 70)
    
    for emp_id in emp_ids:
        employee = employees[emp_id]
        print(f"\n{emp_id}: {employee['name']}")
        print(f"  Department: {employee['department']}")
        print(f"  P: {employee['present']} | A: {employee['absent']} | L: {employee['leave']}")
    
    print("\n" + "=" * 70 + "\n")

 
def sort_by_attendance():
    """Sort employees by total attendance (Present days)"""
    
    if len(employees) == 0:
        print("\n❌ No employees in the system!\n")
        return

    employee_list = []
    
    for emp_id in employees:
        name = employees[emp_id]["name"]
        present = employees[emp_id]["present"]
        employee_list.append((emp_id, name, present))
    
    
    employee_list.sort(key=lambda x: x[2], reverse=True)
    

    print("\n" + "=" * 70)
    print("EMPLOYEES SORTED BY ATTENDANCE (MOST PRESENT)")
    print("=" * 70)
    
    for emp_id, name, present in employee_list:
        employee = employees[emp_id]
        total = employee['present'] + employee['absent'] + employee['leave']
        
        if total == 0:
            percentage = 0
        else:
            percentage = (present / total) * 100
        
        print(f"\n{name} ({emp_id})")
        print(f"  Present: {present} | Absent: {employee['absent']} | Leave: {employee['leave']}")
        print(f"  Attendance %: {percentage:.1f}%")
    
    print("\n" + "=" * 70 + "\n")

def search_employee():
    """Search for a specific employee"""
    emp_id = input("\nEnter Employee ID to search: ")
    
    # Check if employee exists
    if emp_id in employees:
        employee = employees[emp_id]
        
        print("\n" + "=" * 50)
        print("EMPLOYEE DETAILS")
        print("=" * 50)
        print(f"ID: {emp_id}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Present Days: {employee['present']}")
        print(f"Absent Days: {employee['absent']}")
        print(f"Leave Days: {employee['leave']}")
        
        total = employee['present'] + employee['absent'] + employee['leave']
        if total > 0:
            percentage = (employee['present'] / total) * 100
            print(f"Attendance %: {percentage:.1f}%")
        
        print("=" * 50 + "\n")
    else:
        print(" Employee not found!\n")



def load_sample_data():

    
    employees["E001"] = {
        "name": "Arjun",
        "department": "IT",
        "present": 15,
        "absent": 2,
        "leave": 1
    }
    
    employees["E002"] = {
        "name": "Zara",
        "department": "HR",
        "present": 17,
        "absent": 0,
        "leave": 2
    }
    
    employees["E003"] = {
        "name": "Mukesh",
        "department": "Sales",
        "present": 16,
        "absent": 1,
        "leave": 1
    }
    
    employees["E004"] = {
        "name": "Sneha",
        "department": "IT",
        "present": 14,
        "absent": 3,
        "leave": 1
    }
    
    print("Sample employees loaded!\n")

def main_menu():
    """Main menu - loop until user exits"""
    
    print("\n" + "=" * 50)
    print("WELCOME TO EMPLOYEE ATTENDANCE SYSTEM")
    print("=" * 50)
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Mark Attendance")
        print("4. Display All Employees")
        print("5. Sort by Name")
        print("6. Sort by ID")
        print("7. Sort by Attendance")
        print("8. Search Employee")
        print("9. Exit")
    
        choice = input("\nEnter choice (1-9): ")

        if choice == "1":
            add_employee()
        
        elif choice == "2":
            remove_employee()
        
        elif choice == "3":
            mark_attendance()
        
        elif choice == "4":
            display_all()
        
        elif choice == "5":
            sort_by_name()
        
        elif choice == "6":
            sort_by_id()
        
        elif choice == "7":
            sort_by_attendance()
        
        elif choice == "8":
            search_employee()
        
        elif choice == "9":
            print("\nThank you for using Employee Attendance System!")
            print("Goodbye! \n")
            break
        
        else:
            print("\n Invalid choice! Please enter 1-9\n")

if __name__ == "__main__":
    # Load sample data first
    load_sample_data()
    
    # Start the menu
    main_menu()