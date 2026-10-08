import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

print("\nAverage Salary:", df["salary"].mean())
print("Highest Salary:", df["salary"].max())

plt.hist(df["salary"], bins=5, edgecolor="brown")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()