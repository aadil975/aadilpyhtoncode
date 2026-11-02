
students = []

def create_student()
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student = {
        "id": student_id,
        "name": name,
        "age": age
    }

    students.append(student)
    print("Student added successfully!")


def read_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)


def update_student():
    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n--- Student CRUD Operations ---")
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        read_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")
