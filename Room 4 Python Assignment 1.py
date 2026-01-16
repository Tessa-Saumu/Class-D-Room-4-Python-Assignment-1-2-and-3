#SECTION A — BASICS & VARIABLES (1–5)
#Create a variable called age and store your age. Print it.
age = 34
print(age)

#Create two variables a and b with values 10 and 5. Print their sum.
a,b = 10,5
print(a+b)

#Multiply two numbers and print the result.
multiply = 4 * 4
print(multiply)

#Divide 20 by 4 and print the result.
divide = 20 / 4
print(divide)

#Write a program that prints “Python is fun”.
fun = 'Python is fun'
print(fun)

# SECTION B — USER INPUT (6–8)
# 6. Ask the user for their name and print “Hello” followed by their name.
name = input('what is your name') 
print('hello', name)

# 7. Ask the user for two numbers and print their sum.
first_number = int(input('enter your first number'))
second_number =int(input('enter your second number'))
sum_value = first_number + second_number
print(sum_value)

# 8. Ask the user for their age and print how old they will be next year.
age = int(input('enter your age'))
print('next year you would be ' + str(age + 1))

# SECTION C — OPERATORS & LOGIC (9–12)
# 9. Write a program that checks if a number is greater than 10.
check_number = int(input('enter a number '))
if check_number > 10:
    print('greater than 10')
elif check_number < 10:
    print('less than 10')
else:
    print('equal to 10')

# 10. Write a program that checks if a number is even or odd.
number = int(input('enter a number: '))
if number % 2 == 0:
    print('number is even')
else:
    print('number is odd')

# 11. Compare two numbers and print True if they are equal.
num_one = int(input('write your first number'))
num_two = int(input('write your second number'))
if num_one == num_two:
    print('True')
else:
    print('false')

# METHOD 2
num_one = int(input('write your first number'))
num_two = int(input('write your second number'))
print(num_one == num_two)

# 12. Write a program that checks if a number is between 1 and 100.
number = int(input('enter a number '))
print((number >= 1) and (number <= 100))

# SECTION D — IF / ELSE (13–16)
# # 13. Write a program that prints “Pass” if a score is 50 or above, otherwise print “Fail”.
score = int(input('enter a number'))
if score > 50:
    print('pass')
else:
    print('fail')  

# 14. Ask the user for their age and print “Adult” or “Minor”.
age = int(input('enter your age '))
if age >= 18:
    print('Adult')
else:
    print('Minor')

# 15. Write a program that checks if a number is positive or negative.
check_number = int(input('enter a number '))
if check_number < 0 :
    print('negative')
else:
    print('postive or zero')

# 16. Write a program that checks if a password equals "python123".
password = input('enter your password ')
if password == 'python123':
    print('yes password is correct')
else:
    print('no password is not correct')

# SECTION E — LOOPS (17–20)
# 17. Use a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print(i)

# 18. Use a for loop to print your name 5 times.
for i in range(5):
    print('maryrose')

# 19. Use a while loop to print numbers from 1 to 5.
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# 20. Use a loop to print all even numbers between 1 and 20.
for i in range(1,21):
    if i % 2== 0:
        print(i)

# SECTION F — LISTS (21–24)
# 21. Create a list of 5 fruits and print the list.
fruits_list = ['banana','apple','mango','pineapple','cucumber']
for fruit in fruits_list:
    print(fruit)

# 22. Print the first and last item in a list.
cities_countries_list = ['Tokyo','Havana','Las Vegas','Nairobi','Cuba','Qatar']
print(cities_countries_list[0])
print(cities_countries_list[-1])


# 23. Add a new item to a list and print the updated list.
cities_countries_list.append('Nigeria')
print(cities_countries_list)

# 24. Use a loop to print each item in a list.
for city_country in cities_countries_list:
    print(city_country)

# 25. Create a tuple of 3 colors and print it.
colors_tuple = ('red','blue','green')
print(colors_tuple)

# 26. Create a set with duplicate numbers and print the result.
numbers_set = {1,2,3,1,2,3,1,2,3}
print(numbers_set)

# 27. Create a dictionary with your name, age, and course. Print it.
bio_dictionary = {
    'name': 'Theresia',
    'age': 25,
    'course': 'data science and engineering'
}
print(bio_dictionary)

# 28. Print only the name from the dictionary.
print(bio_dictionary['name'])

#29. Write a function that prints “Welcome to Python”
def print_welcome():
    print('Welcome to Python')
    
print_welcome()

# 30. Write a function that takes two numbers and returns their sum.
def sum_numbers(first_number, second_number):
    sum = first_number + second_number
    return sum
    
sum = sum_numbers(1,2)
print(sum)