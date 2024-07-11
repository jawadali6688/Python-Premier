data_table_of_students = [
    {
        "name": "Jawad",
        "roll": "01003",
        "depart": "AI"
    },
    {
        "name": "Ahmad",
        "roll": "01004",
        "depart": "CS"
    }
]

while True:
    print("---- Welcome To Student Portal ----")
    print("---- Which action to perform ----")
    print("1. Show Students List")
    print("2. Add a Student")
    print("3. Update a Student")
    print("4. Remove a Student")
    print("5. Exit from Portal")
    choice = int(input("Enter a choice for action: "))
    if choice == 5:
        break
    match choice:
        case 1:
            print("---------- Student List ---------")
            for index, items in enumerate(data_table_of_students, start=1):
                print(f"{index}. {items["name"]} | {items["roll"]}")   
            print("________________________________________")
        case 2:
            name = input("Enter Student Name: ")
            roll = input("Enter Student Roll No: ")
            data_table_of_students.append({"name": name, "roll": roll})
            print("Student is added succcessfully")
        case 3:
            index = int(input("Enter index of Student: "))
            new_name = input("Enter new name of Student: ")
            new_roll = input("Enter new roll no of Student")
            data_table_of_students[index-1]["name"] = new_name
            data_table_of_students[index-1]["roll"] = new_roll
            print("Student Updated Successfully")    
        case _:
            print("Invalid Input")