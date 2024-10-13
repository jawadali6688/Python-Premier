# For Loop

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")


# Loop through String
# my_name = "Jawad"

# for character in my_name:

#     print(character)
#     # print("Hello World")


# Loop through a List

# my_list = ["Jawad", "Khan", True, False, 242, 3.343]


# for item in my_list:

#     print(item)


# user = {
#     "name": "Jawad",
#     "roll": "01003",
#     "depart": "ai"
# }

# for key in user.keys():

#     print(key)

# for value in user.values():

#     print(value)


# for key, value in user.items():

#     print(key, value)


# Hello World 50 times


# for number in range(0, 11, 5):

#     print("Hello World", number)


# Table of 5

# table = 10

# for count in range(1, 11):

#     print(f"{count} X {table} = {count * table}")


# Reverse A String using for loop

# my_name = "Jawad"

# reversed_str = ""

# for char in my_name:

#     reversed_str = char + reversed_str

                
# print(reversed_str)


# my_list = [2, 5, 7, 9, 11]

# for num in my_list:

#     if num % 2 == 0:
#         print(f"{num} is even")

#     else:
#          print(f"{num} is odd")


# While Loop

# age = 15

# while age < 20:

#     print("Your age is less than 20", age)

#     age = age + 1


# i = 1

# while i <= 10:

#     print("Hello World", i)

#     i += 1


# table = 5

# i = 1

# while i <= 10:

#     print(f"{i} X {table} = {table * i}")

#     i += 1


# my_name = "Jawad"

# reversed_str = ""

# i = 0

# while i < len(my_name):

#     reversed_str = my_name[i] + reversed_str

#     i = i + 1

# print(reversed_str)


my_list = [1, 5, 7, 6, 8, 2, 4, 9]

i = 0

while i < len(my_list):

    if my_list[i] % 2 == 0:
        print("Yes even")

    else:

        print("Odd")

    i = i + 1
