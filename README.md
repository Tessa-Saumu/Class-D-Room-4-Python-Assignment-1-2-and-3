# Room 4 Python Assignments

A comprehensive collection of Python programming assignments covering fundamental concepts and Object-Oriented Programming (OOP). This repository contains two complete assignments designed to build strong Python programming skills from basics to advanced OOP concepts.

## 📋 Repository Overview

This repository contains:
- **Assignment 1**: Python Basics (30 exercises)
- **Assignment 2**: Object-Oriented Programming (30 exercises)

## 🎯 Learning Objectives

### Assignment 1: Python Basics
- Understand Python variables and data types
- Handle user input and output
- Implement conditional logic and operators
- Work with control flow (if/else statements)
- Master loop structures (for and while loops)
- Manipulate data structures (lists, tuples, sets, dictionaries)
- Create and use functions

### Assignment 2: Object-Oriented Programming
- Understand classes and objects
- Work with constructors (`__init__` method)
- Use instance attributes and the `self` parameter
- Create and call instance methods
- Design real-world class models
- Implement encapsulation and data management
- Build interactive object behaviors

## 📚 Assignment 1: Python Basics

### Sections Covered

**Section A: Basics & Variables (Questions 1-5)**
- Variable creation and assignment
- Basic arithmetic operations
- Print statements

**Section B: User Input (Questions 6-8)**
- Collecting user input
- Type conversion and string manipulation

**Section C: Operators & Logic (Questions 9-12)**
- Comparison and logical operators
- Boolean expressions

**Section D: If/Else Statements (Questions 13-16)**
- Conditional logic and validation

**Section E: Loops (Questions 17-20)**
- For and while loops
- Loop iteration and filtering

**Section F: Data Structures (Questions 21-28)**
- Lists, tuples, sets, and dictionaries

**Section G: Functions (Questions 29-30)**
- Function definition and parameters
- Return values

## 📚 Assignment 2: Object-Oriented Programming

### Classes Implemented

**Student Class (Exercises 1-14, 28)**
- Attributes: name, age, grade
- Methods: introduce, is_adult, increase_age
- Demonstrates: basic class structure, instance methods, object lists

**Car Class (Exercises 15-18, 29)**
- Attributes: brand, speed
- Methods: drive, increase_speed
- Demonstrates: object creation, method invocation

**BankAccount Class (Exercises 19-23)**
- Attributes: balance
- Methods: deposit, withdraw
- Demonstrates: state management, data manipulation

**Transaction Class (Exercise 30)**
- Attributes: customer_name, item, amount, quantity
- Methods: total_amount
- Demonstrates: custom class design, calculations

### Key OOP Concepts Covered
- **Classes**: Blueprint for creating objects
- **Objects**: Instances of classes with specific data
- **`__init__` Method**: Constructor for initializing objects
- **`self` Parameter**: Reference to the current instance
- **Instance Attributes**: Data stored in each object
- **Instance Methods**: Functions that operate on object data
- **Encapsulation**: Bundling data and methods together

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- A code editor (VS Code, PyCharm, or any text editor)
- Basic command line knowledge

### Running the Code

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Run Assignment 1 (Python Basics):
```bash
python "Room 4 Python Assignment 1.py"
```

3. Run Assignment 2 (OOP):
```bash
python "Room 4 Python OOP Assignment.py"
```

## 💡 Code Examples

### Assignment 1: Basic Function
```python
def sum_numbers(first_number, second_number):
    sum = first_number + second_number
    return sum
```

### Assignment 2: Student Class
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade
        
    def introduce(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

student1 = Student('Grace', 27, 'A')
student1.introduce()
```

### Assignment 2: BankAccount Class
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        print(f'Deposit {amount}, New balance is {self.balance}')

account1 = BankAccount(250)
account1.deposit(40)
```

## 📂 Repository Structure

```
Room-4-Python-Assignments/
│
├── Room 4 Python Assignment 1.py    # Python basics exercises
├── Room 4 Python OOP Assignment.py  # Object-oriented programming exercises
└── README.md                         # This file
```

## 🤝 Contributing

This is a group project. To contribute:

1. Create a new branch for your work
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and test thoroughly

3. Commit your changes
```bash
git add .
git commit -m "Description of changes"
```

4. Push to the branch
```bash
git push origin feature/your-feature-name
```

5. Submit a pull request with a clear description of changes

## 👥 Contributors

- **Group**: Room 4
- Add your name here when contributing to the project

## 📖 Resources

### Python Basics
- [Python Official Documentation](https://docs.python.org/3/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

### Object-Oriented Programming
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools Python Classes](https://www.w3schools.com/python/python_classes.asp)

## 📝 Notes

- **Assignment 1**: Some exercises require user input. When running the complete file, you'll be prompted to enter values.
- **Assignment 2**: All exercises run automatically and demonstrate OOP concepts through practical examples.
- Each assignment can be run independently
- Code includes comments explaining each exercise
