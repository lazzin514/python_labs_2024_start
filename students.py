import json

# Step 2: Open the JSON file
with open('students.json', 'r') as file:
    # Step 3: Load the JSON data
    data = json.load(file)

# Step 4: Extract the list of students
students = data.get('students', [])

# Step 5: Print each student object
for student in students:
    print(student)


# print second student name 
second_student = students[1]
print(second_student['name'])
