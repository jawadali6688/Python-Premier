# def test(*args):
#     print(args)
#     for item in args:
#         print(item)
    
# test("Jawad", "Ahmad", "Ali", 5)


# student_list = []
# def add_student(*args):
#     for std in args:
#         student_list.append(std)    
#     print(student_list)
#     for std in args:
#     #    index = student_list.index()
#        student_list.remove(std)  
#     print(student_list)
        
    
# add_student("Jawad", "Ahmad", "Ali")

# student_list = []
# while True:
#     def my_test(**kwargs):
#         student_list.append(kwargs)
    
#         print(student_list)

#     name = input("Enter Student Name: ")
#     roll = input("Enter Roll No: ")
#     my_test(name=name, roll=roll)
    

# my_name = "Jawad"
# my_roll = "01003"
# def test():
#     my_name = "Khan"
   
#     print(my_name)
#     print(my_roll)
    
#     def another_test():
#         print(my_roll)
        
#     another_test()

# test()
# print(my_roll)


# Lambda Function 


my_sum = lambda num1, num2: print(num1 + num2)

my_sum(10, 20)