class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display employee details."""
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        """Update the employee's salary."""
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def total_salary_expenditure(self):
        """Calculate and display the total salary expenditure for the department."""
        total = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total}")
        return total

    def display_all_employees(self):
        """Display details of all employees in the department."""
        print(f"Employees in {self.department_name} department:")
        if self.employees:
            for employee in self.employees:
                employee.display_details()
        else:
            print("No employees in this department.")


# Interactive code for managing employees and departments

# Create a department
department_name = input("Enter department name: ")
department = Department(department_name)

while True:
    print("\nDepartment Management System")
    print("1. Add an employee")
    print("2. Update an employee's salary")
    print("3. Display all employees")
    print("4. Display total salary expenditure")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee's name: ")
        employee_id = input("Enter employee's ID: ")
        try:
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)
        except ValueError:
            print("Invalid input for salary. Please enter a numeric value.")

    elif choice == "2":
        employee_id = input("Enter employee ID to update salary: ")
        employee = next((emp for emp in department.employees if emp.employee_id == employee_id), None)
        if employee:
            try:
                new_salary = float(input(f"Enter new salary for {employee.name}: "))
                employee.update_salary(new_salary)
            except ValueError:
                print("Invalid input for salary. Please enter a numeric value.")
        else:
            print("Employee not found.")

    elif choice == "3":
        department.display_all_employees()

    elif choice == "4":
        department.total_salary_expenditure()

    elif choice == "5":
        print("Exiting the department management system.")
        break

    else:
        print("Invalid choice, please try again.")
