file = open("students.txt", "w") 
file.write("sakthi - 85\n")
file.write("dharun - 90\n")
file.write("san nayak - 78\n")

file=open("students.txt", "r") 
contents = file.read()

print(contents)