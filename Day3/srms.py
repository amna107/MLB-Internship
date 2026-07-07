
import json

def load_students():
    try:
        with open("json_records.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File is corrupted or empty. Start fresh")
        return []

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


def add_student(students):   
    if students:
            new_roll_no = students[-1]["Roll_no"] + 1
    else: 
        new_roll_no = 1    
        
    new_student = {
        "Name": input_name(),  
        "Roll_no": new_roll_no,   
        "Age": input_age(),
        "Course": input_course()
    }
    students.append(new_student) 
    print("Student added.\n")
    save_in_json_file(students)
 

def view_all_students(students):
    if not students or len(students) == 0:
        print("No students yet.")
    else:
        for student in students:
            print(student)   
   

def search_student(students):
    if len(students) > 0:
        roll_no = input_roll_no()
        for student in students:
            if student["Roll_no"] == roll_no:    
                print("Found:", student, "\n")
                return                              
        print("No student with that roll number.\n")
    else: 
        print("No students yet.\n")


def update_student_info(students):
    if len(students) > 0:
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
                save_in_json_file(students)
                return
        print("No student with that roll number.\n")
    else:
        print("No students yet.\n")
    

def delete_student(students):
        if len(students) > 0:
            roll_no = input_roll_no()
            for student in students:
                if student["Roll_no"] == roll_no:
                    students.remove(student)
                    print("Deleted.\n")
                    save_in_json_file(students)
                    return
            print("No student with that roll number.\n")
        else:
            print("No students yet.\n")
            

def total_students(students):
    print(f"Total students: {len(students)}\n")

    
def save_in_json_file(students):
    if not students:
        print("No record to save.")
        return
    try:
        with open ("json_records.json", "w") as f:
            json.dump(students, f, indent=4)
            print("Records saved successfully.\n")
    except Exception as e:
        print("Error file saving:", e)

def show_menu():
    print("""
1. Add Student
2. View All Students
3. Search Student (by Roll No)
4. Update Student Information
5. Delete Student
6. Display Total Number of Students
7. Save students records to a JSON file
8. Exit
""")


def main():
    students = load_students() 

    while True:
        print("Existing Records:\n", students)
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student_info(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            total_students(students)
        elif choice == "7":
            save_in_json_file(students)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1-8.\n")

if __name__ == "__main__":
    main()