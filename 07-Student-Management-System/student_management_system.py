students = []


def is_roll_number_taken(roll_number):
    for student in students:
        if student["roll"] == roll_number:
            return True
    return False


def find_student_by_roll(roll_number):
    for student in students:
        if student["roll"] == roll_number:
            return student
    return None


def add_student():
    print("\n--- Add New Student ---")

    try:
        roll_number = int(input("Enter Roll Number: "))
    except ValueError:
        print("Invalid input. Roll Number must be a whole number.\n")
        return

    if roll_number <= 0:
        print("Roll Number must be a positive number.\n")
        return

    if is_roll_number_taken(roll_number):
        print(f"A student with Roll Number {roll_number} already exists.\n")
        return

    student_name = input("Enter Student Name: ").strip()
    if student_name == "":
        print("Student Name cannot be empty.\n")
        return

    try:
        marks = float(input("Enter Marks (0-100): "))
    except ValueError:
        print("Invalid input. Marks must be a number.\n")
        return

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.\n")
        return

    new_student = {"roll": roll_number, "name": student_name, "marks": marks}
    students.append(new_student)
    print(f"Student '{student_name}' added successfully!\n")


def view_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No student records found.\n")
        return

    print(f"{'Roll No':<10}{'Name':<25}{'Marks':<10}")
    print("-" * 45)

    for student in students:
        print(f"{student['roll']:<10}{student['name']:<25}{student['marks']:<10.2f}")

    print()


def update_student():
    print("\n--- Update Student ---")

    try:
        roll_number = int(input("Enter Roll Number to update: "))
    except ValueError:
        print("Invalid input. Roll Number must be a whole number.\n")
        return

    student = find_student_by_roll(roll_number)
    if student is None:
        print(f"No student found with Roll Number {roll_number}.\n")
        return

    print("Leave a field blank to keep its current value.")

    new_name = input(f"Enter new Name [{student['name']}]: ").strip()
    if new_name != "":
        student["name"] = new_name

    new_marks_input = input(f"Enter new Marks [{student['marks']}]: ").strip()
    if new_marks_input != "":
        try:
            new_marks = float(new_marks_input)
            if new_marks < 0 or new_marks > 100:
                print("Marks must be between 0 and 100. Marks not updated.\n")
            else:
                student["marks"] = new_marks
        except ValueError:
            print("Invalid marks entered. Marks not updated.\n")

    print("Student record updated successfully!\n")


def delete_student():
    print("\n--- Delete Student ---")

    try:
        roll_number = int(input("Enter Roll Number to delete: "))
    except ValueError:
        print("Invalid input. Roll Number must be a whole number.\n")
        return

    student = find_student_by_roll(roll_number)
    if student is None:
        print(f"No student found with Roll Number {roll_number}.\n")
        return

    confirm = input(f"Are you sure you want to delete '{student['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        print("Student deleted successfully!\n")
    else:
        print("Delete cancelled.\n")


def search_student():
    print("\n--- Search Student ---")

    try:
        roll_number = int(input("Enter Roll Number to search: "))
    except ValueError:
        print("Invalid input. Roll Number must be a whole number.\n")
        return

    student = find_student_by_roll(roll_number)
    if student is None:
        print(f"No student found with Roll Number {roll_number}.\n")
        return

    print("\nStudent Found:")
    print(f"Roll No : {student['roll']}")
    print(f"Name    : {student['name']}")
    print(f"Marks   : {student['marks']:.2f}\n")


def show_topper():
    print("\n--- Class Topper ---")

    if len(students) == 0:
        print("No student records found.\n")
        return

    topper = students[0]
    for student in students:
        if student["marks"] > topper["marks"]:
            topper = student

    print(f"Roll No : {topper['roll']}")
    print(f"Name    : {topper['name']}")
    print(f"Marks   : {topper['marks']:.2f}\n")


def calculate_average():
    print("\n--- Average Marks ---")

    if len(students) == 0:
        print("No student records found.\n")
        return

    total_marks = 0
    for student in students:
        total_marks = total_marks + student["marks"]

    average_marks = total_marks / len(students)
    print(f"Average Marks of {len(students)} student(s): {average_marks:.2f}\n")


def total_students():
    print("\n--- Total Students ---")
    print(f"Total number of students: {len(students)}\n")


def display_menu():
    print("=" * 45)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Show Topper")
    print("7. Calculate Average Marks")
    print("8. Total Students")
    print("9. Exit")
    print("=" * 45)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            show_topper()
        elif choice == "7":
            calculate_average()
        elif choice == "8":
            total_students()
        elif choice == "9":
            print("\nThank you for using the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.\n")


if __name__ == "__main__":
    main()