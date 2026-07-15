from student import Student

students = []

def find_stu(roll_no):
    for student in students:
        if student.roll_no == roll_no:
            return student
    return None


def add_stu():
    roll_no = int(input("Enter Roll Number: "))

    if find_stu(roll_no):
        print("Roll Number already exists!")
        return

    name = input("Enter Name: ")

    marks = float(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100.")
        return

    student = Student(roll_no, name, marks)
    students.append(student)

    print("Student Added Successfully!")


def view_stu():
    if not students:
        print("No Students Found.")
        return

    for student in students:
        student.display()


def search():
    roll_no = int(input("Enter Roll Number: "))

    student = find_stu(roll_no)

    if student:
        student.display()
    else:
        print("Student Not Found")


def update():
    roll_no = int(input("Enter Roll Number: "))

    student = find_stu(roll_no)

    if student:
        marks = float(input("Enter New Marks: "))

        if marks < 0 or marks > 100:
            print("Invalid Marks")
            return

        student.update_marks(marks)
        print("Marks Updated Successfully")

    else:
        print("Student Not Found")


def delete():
    roll_no = int(input("Enter Roll Number: "))

    student = find_stu(roll_no)

    if student:
        students.remove(student)
        Student.total_stu -= 1
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")


def show_topper():
    if not students:
        print("No Students Available.")
        return

    topper = students[0]

    for student in students:
        if student.marks > topper.marks:
            topper = student

    print("\nTopper Details")
    topper.display()


def menu():
    while True:

        print("\n============================")
        print(" Student Management System")
        print("=============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stu()

        elif choice == "2":
            view_stu()

        elif choice == "3":
            search()

        elif choice == "4":
            update()

        elif choice == "5":
            delete()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            print("Thank You, For Using My Code")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()