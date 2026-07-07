# FILE HANDLING

# 1 WRITE

with open("file.txt", "w") as f:
    f.write("Practicing Problem 1 for Day 3.")
    
# 2 READ

with open ("file.txt", "r") as f:
    content = f.read()
print(content)

# 3 APPEND

with open("file.txt", "a") as f:
    f.write("\nAppended new data to the file.")
    
# 4 COUNT NO OF LINES

with open ("file.txt", "r") as f:
    print(len(f.readlines()))
    
# JSON 

# 1 write to json file

import json

student_info = {
    "Student_name": "Ali",
    "Age": 18,
    "Marks": 50.75,
    "City": "Lahore"
    }

with open("json_file.json", "w") as f:
    json.dump(student_info, f, indent=4)
    
# 2 read from json file

with open("json_file.json", "r") as f:
    data = json.load(f)
print(data)

# 3 upadte existing student info

with open("json_file.json", "r") as f:
    data = json.load(f)
    
data["Age"] = 20

with open("json_file.json", "w") as f:
    json.dump(data, f, indent=4)
    
# 4 add new student to json file
with open("json_file.json", "r+") as f:
    data = json.load(f)
    students = [data]
    students.append({
    "Student_name": "Ahmed",
    "Age": 18,
    "Marks": 70.75,
    "City": "Karachi"
    })  
    f.seek(0)
    json.dump(students, f, indent=4)
    