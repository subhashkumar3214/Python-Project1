import os
import json

print("***STUDENT RECORD MANAGEMENT***")
FILE="Student.json"
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        students=json.load(f)

else:
    students={}

def save_data():
    with open(FILE,"w") as f:
        json.dump(students, f, indent=4)

while True:
    print('''Enter below details
            1.)  Add Students
            2.)  Display Students
            3.)  Search Students
            4.)  Update Students
            5.)  Delete Students 
            6.)  Highest Marks
            7.)  Lowest Marks
            8.)  Average Marks
            9.)  Exit''')

    choice = int(input("Enter The Choice: "))
    if choice == 1:
        name = input("Enter The Name: ")
        age = int(input("Enter The Age: "))
        marks = int(input("Enter The Marks: "))
        course = input("Enter The Course: ")

        students[name] = {
            "Age": age,
            "Marks": marks,
            "Course": course
        }
        print("Student Addded Successfully")

    elif choice == 2:
        if len(students) == 0:
            print("No Record To Find")
        else:
            for name, detail in students.items():
                print("-"*30)
                print(name)
                print("Age :", detail["Age"])
                print("Marks  :", detail["Marks"])
                print("Course  :", detail["Course"])

    elif choice == 3:
        name = input("Enter The name: ")
        if name in students:
            print(students[name])
        else:
            print("Name not Available")

    elif choice == 4:
        name = input("Enter The Name: ")
        if name in students:
            students[name]["Marks"] = int(input("Enter The Marks: "))
            students[name]["Age"]=int(input("Enter The Age: "))
            students[name]["Course"]=input("Enter The Course: ")
            save_data()
            print("Data Save Successfully")
        else:
            print("Name Not Available")

    elif choice == 5:
        name = input("Enter The Name: ")
        if name in students:
            del students[name]
            save_data()
            print("Name Deleted Successfully")
        else:
            print("Name Not Available")

    elif choice == 6:
        Topper = max(students, key=lambda x:students[x]["Marks"])
        print("Topper  :", Topper)
        print("Highest Marks  :", students[Topper]["Marks"])

    elif choice == 7:
        Lowest = min(students, key=lambda x:students[x]["Marks"])
        print("Lowest  :", Lowest)
        print("Lowest Marks  :", students[Lowest]["Marks"])

    elif choice == 8:
        if len(students) == 0:
            print("No Record To Find Average")

        else:
            total = 0
            for i in students.values():
                total += i["Marks"]

            print("Average Marks  ", total/len(students))
    elif choice == 9:
        print("Thank You....")
        break