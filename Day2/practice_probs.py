
# PROBLEM 1

a = list(range(1,6))
a.extend([50,30,40,2,5])
print(f"Largest number =", max(a))

# PROBLEM 2

largest_number = max(a)
second_largest = None

for num in (a):
    if num != largest_number:
        if second_largest is None or second_largest < num:
            second_largest = num
     
print(f"Second largest number is:", second_largest)

# PROBLEM 3 

## dict.fromkeys(a) -> {3: None, 1: None, 2: None, 4: None}  order preserved
a = list(dict.fromkeys(a))  
print(a)


# PROBLEM 4 

a = a[::-1] #takes one step but in reverse order
print(a)

# PROBLEM 5

b = [20,40,50,9,9]
a = set(a)
b = set(b)
print (list(a & b)) 

# PROBLEM 6 

my_tuple = (1,1,2,3,4,4,5,6,4)
print(my_tuple.count(4))

# PROBLEM 7

print(list(my_tuple))
print(tuple(a))

# PROBLEM 8

b = [1,1,2,3]
unique_vals = list(set(b))
print(unique_vals)

# PROBLEM 9 

set_a = {'a','b','c','d'}
set_b = {'d','c','e','f'}

print(set_a | set_b)
print(set_a & set_b)

# PROBLEM 10

name = input("Enter name of the student: ")
age = int(input("Enter age of the student: "))
marks = float(input("Enter marks for the student: "))
city = input("Enter number city of the student: ")

student_record = {
    "student_name": name,
    "age": age,
    "marks": marks,
    "city": city
    }

print(student_record)

# PROBLEM 11

record = {}

no_of_subj = int(input("Enter number of subjects for the student (atleast 1): "))
for i in range(no_of_subj):
    subj = input("Enter name of the subject: ")
    marks = float(input("Enter marks of the subject: "))
    record[subj] = marks
    
print(record)

avg_marks = sum(record.values())/no_of_subj
print(f"{avg_marks:.2f}")

#PROBLEM 12 

sentence = "This is a a sentence."
words = sentence.strip().split()
print(words)

word_count = {}

for word in words:
    if word in word_count: 
     word_count[word] += 1
    else:    
     word_count[word] = 1

print(word_count)
