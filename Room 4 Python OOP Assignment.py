# Exercise 1 Create a class called Student.
class Student:
    # Exercise 2 Add an __init__ method that takes name and age.
    def __init__(self, name, age, grade):
        # Exercise 3 Inside the __init__ method, store name and age using self.
        self.name = name 
        self.age = age
        # Exercise 6 Add an attribute called grade to the Student class. 
        self.grade = grade
        
    # Exercise 9 Add a method called introduce that prints: “Hello, my name is ___ and I am ___ years old.”
    def introduce(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')
        
    # Exercise 11 Create a method called is_adult that prints "Adult" if age is 18 or above, otherwise prints "Minor".
    def is_adult(self):
        if self.age >= 18:
            print('Adult')
        else:
            print('Minor')
            
    # Exercise 28 Add a method to Student that increases age by 1.
    def increase_age(self):
        self.age = self.age + 1
        print(self.age)

# Exercise 4 Create two Student objects with different names and ages.
student1 = Student('Grace',27, 'A')
student2 = Student('Chidinma',29, 'B')

# Exercise 5 Print the name of the first student.
print(student1.name)

# Exercise 7 Create a student with a grade and print the grade.
student3 = Student('Ellen', 22, 'C')
print(student3.grade)

# Exercise 8 Change the grade of a student and print the new grade.
student2.grade = 'D'
print(student2.grade)

# Exercise 10 Call the introduce method for one student.
student1.introduce()

# Exercise 12 Create three Student objects and store them in a list.
student4 = Student('Anita', 24, 'A')
student5 = Student('Theresia', 52, 'B')
student6 = Student('Hurumnanya', 17, 'C')

student_list = [student4, student5, student6]

# Exercise 13 Use a loop to print the name of each student in the list.
for student in student_list:
    print(student.name)
    
# Exercise 14 Use a loop to call the introduce method for each student.
for student in student_list:
    student.introduce()

# Exercise 15 Create a class called Car with attributes brand and speed.
class Car:
    def __init__(self, brand, speed):
        self.brand = brand 
        self.speed = speed
        
    # Exercise 17 Add a method called drive that prints: “The car is driving at ___ km/h.”
    def drive(self):
        print(f'The car is driving at {self.speed} km/h')
        
    # Exercise 29 Add a method to Car that increases speed.
    def increase_speed(self, km):
        self.speed = self.speed + km
        print(f'Increase by {km}, New speed {self.speed}')

# Exercise 16 Create two Car objects with different brands and speeds.        
car1 = Car('Benz', 140)
car2 = Car('BMW', 120)

# Exercise 18 Call the drive method for each car.
car1.drive()
car2.drive()

# Exercise 19 Create a class called Bank Account.

class BankAccount:
    def __init__(self, balance):
    # Exercise 20 Add an attribute called balance.
        self.balance = balance

# Exercise 21 Create a method called deposit that adds money to balance.
    def deposit(self, amount):
        self.balance += amount 
        print(f'Deposit {amount}, New balance is {self.balance}')
    
    #method 2  
    # def deposit(self, amount):
    #     self.balance = self.balance + amount
    #     print(f'Deposit {amount}, New balance is {self.balance}')

    # Exercise 22 Create a method called withdraw that subtracts money from balance.
    def withdraw (self, amount):
        self.balance = self.balance - amount
        print(f'Withdraw {amount}, New balance is {self.balance}')

# Exercise 23 Create an object and test deposit and withdraw.
account1 = BankAccount(250)
account1.deposit(40)
account1.withdraw(600)

# Exercise 24 In your own words, explain what a class is.
'''A class is the blueprint/design that describes what an object should have (data) and what it can do (methods). It is not the real thing yet until you create an actual object based on the class. It is a structured data container with attributes and methods. '''

# Exercise 25 In your own words, explain what an object is.
'''An object is a concrete instance in memory that holds data (state) and can perform operations (methods) on that data. It is defined by a class which has the attributes (data) and methods (operations) of the object. For example a House class with attributes for number of rooms and size will define it and the object will be specific instance with number of rooms being 3 and size being 100m2'''

# Exercise 26 What is the purpose of the __init__ method?
'''__init__ is a constructor that initializes or runs automatically when you create an object from a class.
Its purpose is to set up the object by giving it initial data.
'''

# Exercise 27 What does self represent?
'''Self is a parameter. It is a reference to current/particular object that is using the class. For example if you have car1 (an object of the Car class) then self would be car1 and if you have car2 then self would be car2.'''

# Exercise 30 Create your own class (any idea) with: 
# • At least 2 attributes
# • At least 1 method

class Transaction:
    def __init__(self, customer_name, item, amount, quantity):
        self.customer_name = customer_name
        self.item = item
        self.amount = amount
        self.quantity = quantity
    
    def total_amount(self):
        total = self.quantity * self.amount
        return total
        
transaction1 = Transaction('Enuwa', 'shoe', 35000, 1)
transaction2 = Transaction('Maryrose', 'bag', 15000, 2)

print(transaction1.customer_name, transaction1.amount)
print(transaction2.customer_name, transaction2.item)

print(transaction2.total_amount())