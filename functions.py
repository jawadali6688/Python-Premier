# Functions --> Reusable code --> Method
# Synta
# def test():
#     print("Hello Jawad")
#     print(10 + 10)
#     print("Function executed")
    
# Call the function
# test()
# test()
# def greet_to_Jawad():
#     print("Morning Jawad")
# greet_to_Jawad()

# returning function --> return keyword

# def sum():
#     return 2 + 5

# result_of_func = sum()

# print(result_of_func)


# Function with parameters

# def greet(name, roll):
#     print(f"Good Morning {name} and your Roll no is {roll}")
    
# greet("Jawad", 1003)


# def sum_of_two_numbers(first_num, second_num):
#     return first_num + second_num

# result = sum_of_two_numbers(24, 56)

# print(result)


# Default Parameters

# def greet(name = "Jawad", roll = "01003"):
#     print("Good Night", name, "And your roll no is", roll)
    
# greet("Khan", "01005")



# def sum_of_num(num):
#     print(num)

# sum_of_num(10, 5) 

# print("Jawad"*5)

# def sum_of_num(*args):
#     sum_of_numbers = 0
#     for num in args:
#         sum_of_numbers += num   
#     print(sum_of_numbers)
    
# sum_of_num(4, 5, 9, "Jawad", "Khan", False)
# sum_of_num(4, 10, name = "Jawad")
# sum_of_num(4, 5, 9, 10, 35)


# def printing_num(num):
#     for number in range(num):
#         yield number
    
# for i in printing_num(17):
#     print(i)


# def sum_of_num(*args, **kwargs):
#     print(args, kwargs)
    
# sum_of_num(5, num = 5, num2 = 10, jawad = 45,)

student_list = []
while True:
    def add_students(student_name):
        student_list.append(student_name)
        print(student_list)
    student_name = input("Enter student name: ") 
    student_roll = input("Enter roll no: ")
    add_students({"name":student_name, "roll":student_roll})