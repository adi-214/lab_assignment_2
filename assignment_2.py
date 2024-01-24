class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.employee_id} {self.name} {self.age} {self.salary}"


class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_id, name, age, salary):
        self.employees.append(Employee(employee_id, name, age, salary))

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def display(self):
        for employee in self.employees:
            print(employee)


# Creating the database and adding employees
database = EmployeeDatabase()
database.add_employee("161E90", "Ramu", 35, 59000)
database.add_employee("171E22", "Tejas", 30, 82100)
database.add_employee("171G55", "Abhi", 25, 100000)
database.add_employee("152K46", "Jaya", 32, 85000)

# User input for sorting choice
print("Choose the sorting parameter:")
print("1. Age\n2. Name\n3. Salary")
choice = input("Enter your choice (1, 2, or 3): ")

if choice == '1':
    database.sort_by_age()
elif choice == '2':
    database.sort_by_name()
elif choice == '3':
    database.sort_by_salary()
else:
    print("Invalid choice")

# Displaying sorted data
database.display()
