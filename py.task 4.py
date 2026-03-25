# task 4.py

#miniproject 1

employees = []

# Function to add employee
def add_employee():
    name = input("siranjeevi: ")
    age = int(input("28: "))
    role = input("aws: ")
    salary = float(input("250000: "))
    
    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }
    
    employees.append(emp)
    print("✅ Employee added successfully!\n")


# Function to display employees
def display_employees():
    if not employees:
        print(" No employees found.\n")
        return
    
    print("\n----- Employee List -----")
    for i, emp in enumerate(employees):
        print(f"\nEmployee ID: {i}")
        print(f"Name   : {emp['name']}")
        print(f"Age    : {emp['age']}")
        print(f"Role   : {emp['role']}")
        print(f"Salary : {emp['salary']}")
    print("--------------------------\n")


# Function to update employee
def update_employee():
    display_employees()
    
    if not employees:
        return
    
    emp_id = int(input("Enter Employee ID to update: "))
    
    if emp_id < len(employees):
        employees[emp_id]['name'] = input("sirak: ")
        employees[emp_id]['age'] = int(input("29: "))
        employees[emp_id]['role'] = input("deovps: ")
        employees[emp_id]['salary'] = float(input("300000: "))
        
        print("✅ Employee updated successfully!\n")
    else:
        print("❌ Invalid Employee ID\n")


# Function to delete employee
def delete_employee():
    display_employees()
    
    if not employees:
        return
    
    emp_id = int(input("Enter Employee ID to delete: "))
    
    if emp_id < len(employees):
        removed = employees.pop(emp_id)
        print(f"✅ Employee {removed['siranjeevi']} deleted successfully!\n")
    else:
        print("❌ Invalid Employee ID\n")


# Main menu
def main():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice, try again!\n")


# Run program
main()


#minpeoject 2

# Function to calculate total and average
def calculate(marks):
    total = sum(marks.values())
    avg = total / len(marks)
    return total, avg


# Function to assign grade
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


# Function to print report card
def print_report(student):
    print("\n====== REPORT CARD ======")
    print(f"Name : {student['name']}")
    
    print("\nMarks:")
    for sub, mark in student['marks'].items():
        print(f"{sub} : {mark}")
    
    total, avg = calculate(student['marks'])
    
    print("\n--------------------------")
    print(f"Total   : {total}")
    print(f"Average : {avg:.2f}")
    print(f"Grade   : {grade(avg)}")
    print("==========================\n")


# Main program
def main():
    name = input("siranjeevi: ")
    
    marks = {}
    subjects = ["Maths", "Science", "English"]
    
    for sub in subjects:
        marks[sub] = int(input(f"Enter marks for {sub}: "))
    
    student = {
        "name": name,
        "marks": marks
    }
    
    print_report(student)


# Run program
main()



#miniprojet 3

cart = []

def add_item():
    name = input("milk: ")
    price = float(input("28: "))
    qty = int(input("4: "))
    
    cart.append({"name": name, "price": price, "qty": qty})
    print("✅ Item added\n")

def view_cart():
    total = 0
    print("\n--- Cart Items ---")
    for i, item in enumerate(cart):
        item_total = item["price"] * item["qty"]
        total += item_total
        print(f"{i}. {item['name']} - {item['qty']} x {item['price']} = {item_total}")
    print(f"Total Bill: {total}\n")

def remove_item():
    view_cart()
    i = int(input("Enter item index to remove: "))
    if 0 <= i < len(cart):
        cart.pop(i)
        print("✅ Item removed\n")

#miniproject 4

users = {"admin": "1234", "user": "pass"}

username = input("sirak: ")
password = input("1234: ")

if username in users and users[username] == password:
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")

    #miniproject 5

    visitors = set()

while True:
    name = input("siranjeevi (or 'exit'): ")
    if name == "exit":
        break
    visitors.add(name)

print("Unique Visitors:", len(visitors))
print(visitors)

#miniproject 6

name = input("Enter your name: ")
product = input("Enter product: ")

print(f"\n{name} purchased {product}")

# Padding
print(name.ljust(20, "-"))
print(name.rjust(20, "-"))
print(name.center(20, "-"))

#miniproject 7

account = {"name": "", "balance": 0}

def create_account():
    account["name"] = input("Enter name: ")
    account["balance"] = float(input("Enter initial balance: "))

def deposit():
    amt = float(input("Enter amount: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Enter amount: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("❌ Insufficient balance")

def check_balance():
    print("Balance:", account["balance"])

    #miniproject 8

    votes = {"A": 0, "B": 0, "C": 0}

while True:
    v = input("Vote (A/B/C) or exit: ")
    if v == "exit":
        break
    #if v in votes:
        votes[v] += 1

#winner = max(votes, key=votes.get)
#winner)
#print(votes)

#miniproject 9

students = {}

def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")
    students[name] = courses

def update_courses():
    name = input("Enter student name: ")
    if name in students:
        students[name] = input("Enter new courses: ").split(",")

def display():
    for name, courses in students.items():
        print(name, ":", courses)


#miniproject 10

num = int(input("Enter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))

# Formatting
print("With commas:", f"{num:,}")
print("Scientific:", f"{num:.2e}")