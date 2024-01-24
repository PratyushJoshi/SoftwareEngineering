#Lab 2: Sorting Employee Data
#Pratyush Joshi 
#Roll no: 2110110781
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employees(employees, sort_key):
    if sort_key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return employees

def print_employee_data(employees):
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    # Creating employee instances
    emp1 = Employee("161E90", "Ramu", 35, 59000)
    emp2 = Employee("171E22", "Tejas", 30, 82100)
    emp3 = Employee("171G55", "Abhi", 25, 100000)
    emp4 = Employee("152K46", "Jaya", 32, 85000)

    employees_list = [emp1, emp2, emp3, emp4]

    # Getting user input for sorting parameter
    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    sort_parameter = int(input("Enter your choice (1/2/3): "))

    # Sorting and printing based on user input
    sorted_employees = sort_employees(employees_list, sort_parameter)
    print("\nSorted Employee Data:")
    print_employee_data(sorted_employees)
