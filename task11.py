
import json
employees =[
    {
        "id": 1,
        "name": "karthick",
        "department": "AI/ML"
    },
    {
        "id": 2,
        "name": "suresh",
        "department": "HR"
    },
    {
        "id": 3,
        "name": "sameera",
        "department": "IT support"
    }
]


file =open("employees.json","w")
json.dump(employees,file,indent=4)

file = open("employees.json", "r") 
employees = json.load(file)

for employee in employees:
    print(employee["name"], "-", employee["department"])