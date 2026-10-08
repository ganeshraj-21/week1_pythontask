import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nAverage mark:", df["mark"].mean())

print("\nStudents who scored above 80:")
print(df[df["mark"] > 80])