class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print()


employee1 = Employee("santhosh", 28, 30000)
employee2 = Employee("abdhul", 26, 35000)

employee1.display_details()
employee2.display_details()