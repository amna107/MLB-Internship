name = input("Enter student name : ")
student_class = input("Enter student class : ")
no_of_subjects = int(input("Enter no. of subjects: "))

while no_of_subjects <= 0:
    print("Number of subjects must be at least 1.")
    no_of_subjects = int(input("Enter no. of subjects: "))

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

mark_sheet = {}

for i in range(no_of_subjects):
    subject_name = input("Enter subject name : ")
    marks = int(input("Enter marks obtained : "))
    while marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        marks = int(input("Enter marks obtained : "))
        
    grade = calculate_grade(marks)
        
    mark_sheet[subject_name] = {'marks': marks, 'grade': grade}
    
overall_marks = sum(subject['marks'] for subject in mark_sheet.values())

avg_marks = overall_marks / no_of_subjects
overall_grade = calculate_grade(avg_marks)
    
print("\nMark Sheet for", name)
print("Class:", student_class)

print("Subject-wise Marks and Grades:")

for subject, details in mark_sheet.items():
    print(f"Subject: {subject}, Marks: {details['marks']}, Grade: {details['grade']}")
    
print(f"Overall Average Marks: {avg_marks:.2f}")
print(f"Overall Grade: {overall_grade}")