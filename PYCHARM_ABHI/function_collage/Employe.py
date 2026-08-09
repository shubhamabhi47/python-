#define a class Employee with private attributes name , salary , write a method to set and get the values of their attributes
# then create an instance of employee and use methods to set and display its details
class Employee:
    def __init__(self, name='', salary=0.0):
        # Private attributes
        self.__name = name
        self.__salary = salary

    # Method to set name
    def set_name(self, name):
        self.__name = name

    # Method to get name
    def get_name(self):
        return self.__name

    # Method to set salary
    def set_salary(self, salary):
        self.__salary = salary

    # Method to get salary
    def get_salary(self):
        return self.__salary

# Create an instance of Employee
e1 = Employee()

# Set details for the employee
e1.set_name("Abhimanyu")
e1.set_salary(50000)

# Display the employee's details
print("Employee Name:", e1.get_name())
print("Employee Salary:", e1.get_salary())
