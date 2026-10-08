students = [
    {"id": 1, "name": "Arun", "age": 20},
    {"id": 2, "name": "Priya", "age": 21},
    {"id": 3, "name": "Rahul", "age": 19}
]

print("All Students:")

for student in students:
    print(student)

search_id = int(input("Enter student id: "))

for student in students:
    if student["id"] == search_id:
        print("Student matched in list:", student)
        break
else:
    print("Student  not matched in list")