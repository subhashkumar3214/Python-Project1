student = {}

while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. ADD Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exist")

    choice = input("Your choice: ")


    # Add Students
    if choice == "1":
        name = input("Enter Student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} successfull Added!")

    # View Students
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # Check Result 
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")

        else:
            print("Student Not Found!")

    # Exit
    elif choice == "4":
        print("Exiting.....")
        break
    else:
        print("In-valid input")


