"""
Create our new data type --> Class
Define the class
call the class
access the attributes.

Obejct refers to two variables

You can define a function to read the class
ex:
    define the attributes in the class
    then call the attributes with methods as inputs


    class Employee():
    name = None
    salary = None
    address = None

    def print(self):
        print("Employee Name:", self.name)

    def read(self):
        self.name = input("Enter name:")

mosta = Employee()
mosta.read() --> this method does not take parameters since it is passed automatically to the interpreter in the definition of the class
mosta.print()

Encapsulation grouping variables an functions of a specific concept in as single component, named class
Classes represent something


CONSTRUCTORS --> initializes the data members of the class when an object of class is created
    CALL THE CLASS
    DEF __INIT__ --> a reserved method, called when the object is created
    It passes their parameters as soon as thei are called

THE INIT METHOD

class Employee:
    def __init__(self, name, address):
        self.name = input("Whats your name ")
        self.middle_name = None
        self.address = input("And your address? ")

    def print(self):
        print(f"Employee name:{self.name}\nEmployee address: {self.address} ")


mosta = Employee("hola", "chau")

mosta.print()

class Rectangle():
    def __init__(self):
        # attributes
        self.width = int(input("Whats the height? "))
        self.height = int(input("What's the width? "))
    # methods

    def get_area(self):
        self.area = self.width*self.height
        print(f"The area of the rectangle is: {self.area}")

    def get_perimeter(self):
        self.perimeter = (self.width*2)+(self.height*2)
        print(f"The perimeter of the rectangle is: {self.perimeter}")


class Circle():
    def __init__(self):
        self.radius = int(input("Whats is the radius of the circle? "))

    def get_area(self):
        self.area = 3.14*self.radius**2
        print(f"The area of the circle is {self.area}")


class Editor():
    def __init__(self):
        self.circulo = Circle()
        self.rectangulo = Rectangle()

    def change(self):
        self.factor = int(input("Which number do you want to increase"))
        self.height_factor = self.rectangulo.height + self.factor
        self.width_factor = self.rectangulo.width + self.factor

    def print(self):
        print(f"The new measures are {self.width_factor, self.height_factor}")


editor = Editor()
editor.change()
editor.print()

THE __STR__ ()AND __REPR__ (default representation) METHOD

    if __STR__ is not provided -- intended for users, provide something readable
    HOw to call it --> name_object.__str__()
    then the __REPR__ is used -- intended mainly for developers for debugging or logging
    it will print the memory addres if the str was not provided

Every variable in python is an object

__init__" is a reserved method in python classes 
representing constructor. This method called when an 
object is created from the class and it allows the class 
to initialize the attributes of a class.

"""


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.gpa = 0
        self.grades_sum = 0
        self.total_subjects = 0

    def get_avg(self):
        if self.total_subjects == 0:
            return 0
        return self.grades_sum / self.total_subjects

    def add_course_grade(self, grade):
        self.grades_sum += grade
        self.total_subjects += 1

    def print(self):
        avg = self.get_avg()
        print(self.name, 'grades average is', avg)


mostafa = Student('Mostafa', 10010123)
mostafa.add_course_grade(float(input("What's the first mark? ")))
mostafa.add_course_grade((float(input("What's the second mark? "))))
mostafa.add_course_grade((float(input("What's the third mark? "))))
mostafa.print()
