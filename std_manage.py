

std_list = [
    {
        "name": "Jawad",
        "roll": "01003",
        "depart": "ai"
    },
    
    
    
]


# Show Student list

def show_list():

    for index, std in enumerate(std_list):
        print(f"{index + 1} - {std["name"]} - {std["roll"]} - {std["depart"]}")


# Add Student 

def add_student(data):

    std_list.append(data)
    print("Student Added Successfully")

# Edit Student

def edit_std(roll):

    for std in std_list:
        if std["roll"] == roll:

            new_name = input("Enter student new name:  ")

            new_roll = input("Enter student new roll number: ")

            new_depart = input("Enter student new department: ")

            std["name"] = new_name

            std["roll"] = new_roll

            std["depart"] = new_depart

            print("Student Updated Successfully!")
            break

    else:
        print("Oops, student with roll number not exist!")


# Deleting a Student

def delete_std(roll):

    for std in std_list:
        if std["roll"] == roll:

            std_list.remove(std)
            print("Student deleted Successfully!")
            break

    else:
        print("Oops, student with roll number not exist!")


while True:

    print("___Student Management Portal___")
    print("1. Show Student List")
    print("2. Add a Student")
    print("3. Edit a Student")
    print("4. Delete a Student")
    print("5. Exit from Portal")


    choice = int(input("Enter your choice: "))

    if choice == 5:

        break


    match choice:

        case 1:

            show_list()

        case 2:

            std_name = input("Enter student name: ")

            std_roll = input("Enter student roll number: ")

            std_depart = input("Enter student department: ")

            data = {
                "name": std_name,
                "roll": std_roll,
                "depart": std_depart
            }

            add_student(data)

        case 3:
            
            std_roll = input("Enter student roll number for edit: ")

            edit_std(std_roll)


        case 4:

             std_roll = input("Enter student roll number for delete: ")

             delete_std(std_roll)

# 