students = []


def add_student():
    student_id = int(input("Enter the ID: "))

    for student in students:
        if student["id"] == student_id:
            print("This ID already exists!")
            return

    student = {
        "id": student_id,
        "name": input("Enter Name: "),
        "age": int(input("Enter age: ")),
        "course": input("Enter The Course name: "),
        "Marks": int(input("Enter Marks: "))
    }

    students.append(student)
    print("Student added Successfully.")

def view_students():
    if not students: 
       print("No students registered yet.")
    else:
        for student in students:
                print("-----------------------")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["Marks"])

def update_student():
    search_id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == search_id:

            while True:
                print("\n===== UPDATE STUDENT =====")
                print("Current Information:")
                print(student)

                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Course")
                print("4. Update Marks")
                print("5. Update All Information")
                print("6. Finish Updating")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("Current Name:", student["name"])
                    student["name"] = input("Enter New Name: ")

                elif choice == 2:
                    print("Current Age:", student["age"])
                    student["age"] = int(input("Enter New Age: "))

                elif choice == 3:
                    print("Current Course:", student["course"])
                    student["course"] = input("Enter New Course: ")

                elif choice == 4:
                    print("Current Marks:", student["Marks"])
                    student["Marks"] = int(input("Enter New Marks: "))

                elif choice == 5:
                    student["name"] = input("Enter New Name: ")
                    student["age"] = int(input("Enter New Age: "))
                    student["course"] = input("Enter New Course: ")
                    student["Marks"] = int(input("Enter New Marks: "))

                elif choice == 6:
                    print("Information Updated Successfully!")
                    print("Exit!")
                    return

                else:
                    print("Invalid Choice!")

    print("Student Not Found!")

def delete_student():
    search_id = int(input("Enter the ID: "))

    for student in students:
        if student["id"] == search_id:
            print(student["name"]," Deleted Successfully!")
            students.remove(student)
            return
    print("student Not Found!")   
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Students")
    print("4. Delete Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")