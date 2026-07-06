
students = []

def input_name():
    while True:
        name = input("Enter student name: ")
        if name.strip() != "":
            return name       
        print("Name can't be empty.")


def input_age():
    while True:
        age_str = input("Enter student age: ")
        try:
            age = int(age_str)   
        except ValueError:
            print("Age must be a whole number.")
            continue            
        if age <= 0:
            print("Age must be a positive number.")
            continue
        return age                


def input_course():
    while True:
        course = input("Enter course: ")
        if course.strip() != "":
            return course
        print("Course can't be empty.")


def input_roll_no():
    while True:
        roll_str = input("Enter roll number: ")
        try:
            return int(roll_str)
        except ValueError:
            print("Roll number must be a whole number.")


def add_student():
    name = input_name()         
    age = input_age()
    course = input_course()

    new_student = {
        "Name": name,
        "Roll_no": len(students) + 1,   
        "Age": age,
        "Course": course,
    }
    students.append(new_student)
    print(f"Added {name} with Roll_no {new_student['Roll_no']}.\n")


def view_all_students():
    if not students:
        print("No students yet.\n")
        return
    for student in students:
        print(student)
    print()


def search_student():
    if not students:
        print("No students yet.\n")
        return

    roll_no = input_roll_no()
    for student in students:
        if student["Roll_no"] == roll_no:    
            print("Found:", student, "\n")
            return                              
    print("No student with that roll number.\n")


def update_student_info():
    if not students:
        print("No students yet.\n")
        return

    roll_no = input_roll_no()
    for student in students:
        if student["Roll_no"] == roll_no:
            print(f"Editing: {student}")
            print("""
1. Name
2. Age
3. Course
4. Cancel
""")
            field_choice = input("Which field do you want to update? ")

            if field_choice == "1":
                student["Name"] = input_name()          
            elif field_choice == "2":
                student["Age"] = input_age()
            elif field_choice == "3":
                student["Course"] = input_course()
            elif field_choice == "4":
                print("Cancelled.\n")
                return
            else:
                print("Invalid choice, nothing updated.\n")
                return

            print("Updated:", student, "\n")
            return
    print("No student with that roll number.\n")


def delete_student():
    if not students:
        print("No students yet.\n")
        return

    roll_no = input_roll_no()
    for student in students:
        if student["Roll_no"] == roll_no:
            students.remove(student)
            print("Deleted.\n")
            return
    print("No student with that roll number.\n")


def total_students():
    print(f"Total students: {len(students)}\n")


def show_menu():
    print("""
1. Add Student
2. View All Students
3. Search Student (by Roll No)
4. Update Student Information
5. Delete Student
6. Display Total Number of Students
7. Exit
""")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student_info()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            total_students()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1-7.\n")


if __name__ == "__main__":
    main()