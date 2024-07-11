# Match Statement --> Data Type --> list , tuple , dictionary 
# Python 3.10
day = "Wednesday"

match day:    
    case "Saturday":
        print("Java Lecture")
        print("It's Saturday")

    case "Friday":
        print("Python Lecture")

    case "Monday":
        print("No Lecture")
        
    case "Wednesday":
        print("Golang Lecture")
        
    case _:
        print("Invalid Input")


# Loops --> For Loop, While Loop

# For Loop --> List, tuple , string

for i in range(0, 11):
    print("Hello World", i)


name = "Jawad"
for j in name:
    print(j)
for i in range(0, 11, 3):
    print(i)

user_input = int(input("Enter a number "))   
for i in range(0, user_input, 3):
    print(i)


# While Loop --> conditon
num = 1
while num <= 10:
    print("Hello World", num)
    num += 1


# Control Statements in LOOP
# Break Statement --> Terminate

for i in range(5, 11):
    if i == 8:
        break
    print(i)
# Continue statement --> step exit
for i in range(1, 9):
    if i == 5:
        continue
    print(i)

table_num = 5
i = 1
while i in range(1, 11):
    print(f"{i} X {table_num} = {i * table_num}")
    i += 1



# Project 


while True:
    print("A Calculator")
    print("Choose a method for calculation, Choose in option like --> 1,2,3,4,5")
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")
    user_input = int(input("Enter Choice: "))
    # if user_input not in 1 or 2 or 3:
    #     break
    num1 = int(input("Enter number one: "))
    num2 = int(input("Enter number two: "))
    match user_input: 
        case 1:
            print(f"You choosed addition")
            print(f"The sum of {num1} and {num2} is {num1 + num2}")   
        case 2:
            print(f"You choosed Subtraction")
            print(f"The subtraction of {num1} and {num2} is {num1 - num2}")    
        case 3:
            print(f"You choosed Multiplication")
            print(f"The multiplication of {num1} and {num2} is {num1 * num2}") 
        case 4:
            break     
        case _:
            print("Invalid Input")










    