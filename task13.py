import numpy as np

marks = np.array([35, 85, 62, 108, 88, 565, 22])

print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

print("Marks greater than 80:")
print(marks[marks > 80])