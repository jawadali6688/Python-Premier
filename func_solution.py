
# Lambda function
# def my_sum(num1, num2):

#     print(num1 + num2)

# print(my_sum(5, 10))


# new_sum = lambda num1, num2: print(num1 + num2)

# print(new_sum(10, 20))


# greet = lambda name: f"Good morning {name}"


# print(greet("Jawad"))


# square = lambda value: value ** 2

# print(square(10))


# def my_sum(num1, num2):

#     return num1 + num2

# print(my_sum(5, 10))


# new_sum = lambda num1, num2: num1 + num2

# print(new_sum(10, 20))

# fahrenheit = 10

# celcius = 5 / 9 * (fahrenheit - 32)

# print(celcius)


# def temp_con(fahrenheit):

#     celcius = 5 / 9 * (fahrenheit - 32)

#     return f"Temprature in celcius is {celcius}"

# print(temp_con(70))


# temp_con = lambda fahrenheit: f"Temprature in celcius is {5 / 9 * (fahrenheit - 32)}" 

# print(temp_con(70))


# def num_check(num):

#     if num % 2 == 0:

#         return f"{num} is even"
    
#     return f"{num} is odd"

# print(num_check(5))

# print(num_check(4))

# print(num_check(10))

# print(num_check(7))


# student_list = []


# def adding_student(*args):


#     for std in args:

#         if type(std) == str:

#             student_list.append(std)

#     return student_list


# result = adding_student("Jawad", 234234, "Ali", "Khan", "Ahmad", True, 12, 234.234, False)

# result2 = adding_student("Jawad", 234234, "Ali", "Khan", "Ahmad", True, 12, 234.234, False)


# adding_student("Jawad", "Ali")

# adding_student("Ahmad", "Ali2", True)

# print(student_list)



# student_list = [
    
# ]


# def adding_std(**kwargs):

#     student_list.append(kwargs)

#     return f"Student Added Successfully", student_list

# adding_std(name="Jawad", roll="01003", depart="ai")

# adding_std(name="Ahmad", roll="01004", depart="ai")

# print(student_list)


# def fact(num):

#     if num == 0:
#         return 1
    
#     return num * fact(num - 1)

#             # 5 * 4 * 3 * 2 * 1 * 1
# print(fact(3))

# my_list = ["Jawad", "Khan", 234, 2342, True]


# def my_yield():

#     for item in my_list:

#        yield item

# result = my_yield()


# for i in result:

#     print(i)

# 