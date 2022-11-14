# takes some message to print, then a startin and end
def input_validation(msg, start=0, end=None):
    # keep iterating till the given input is valid
    # hidden assumption both stat and end value or none #both are optional
    while True:
        inp = input(msg)
        if not inp.isdecimal():  # validates that the inout is not a word
            print("Invalid input. Try again!")
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):  # validates the range of 1 to 5
                print("Invalid range. Try again")
            else:
                return int(inp)
        else:
            return int(inp)


class Employee():
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age. salary

    def __str__(self):  # string function
        return f"Employee: {self.name} has age {self.age} and salary {self.salary}"

    def __repr__(self):  # presentation function
        return f"Employee (name='{self.name}', age= {self.age}, salary= {self.salary})"


class EmployeeManager():  # hold the functionaly of the menu's option
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age):
        self.employees.append(Employee(name, age, salary))

    def list_employee(self):
        if len(self.employees) == 0:
            print("\nNo employees at the moment!")
            return
        print("\n**Employees list**")
        for emp in self.employees:
            print(emp)

    def delete_employee_by_age(self, age_from, age_to):
        # remove from the back
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print("\nDeleting", emp.name)
                self.employees.pop(idx)

    def find_employee_by_name(self, name):  # utility needed from the next class
        for emp in sel.employee:
            if emp.name == name:
                return emp
        return None

    def update_salary_of_employee_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print("Error: No employee wiith such name")
        else:
            emp.salary = salary


class FrontendManager():
    def __init__(self):
        self.employees_manager = EmployeeManager()

    def print_menu(self):
        print("\nChose one option")
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete employee by age',
            '4) Update salary by name',
            '5) Exit'
        ]
        print("\n".join(messages))
        msg = f"Enter your choice (from 1 to {len(messages)}): "
        return input(input_validation(msg, 1, len(messages)))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manager.add_employee()
                print("\nEnter employee data")
                name = input("Enter the name: ")
                age = input_validation("Enter the age: ")
                salary = input_validation("Enter the salary: ")
            elif choice == 2:
                self.employees_manager.list_employee
            elif choice == 3:
                age_from = input_validation("Enter age from")
                age_to = input_validation("Enter age to: ")
                self.employees_manager.delete_employee_by_age(age_from, age_to)
            elif choice == 4:
                name = input("Enter name: ")
                salary = input_validation("Enter a new salary: ")
                self.employees_manager.update_salary_of_employee_name(
                    name, salary)
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()
