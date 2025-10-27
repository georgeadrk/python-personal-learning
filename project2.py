def countAvg(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    averages.append(avg)

def checkGrade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    result = ""
    if avg >= 85:
        result = "Excellent"
    elif avg >= 70:
        result = "Good"
    else:
        result = "Needs Improvement"
    grades.append(result)

aos = int(input("How many students? "))
names = []
averages = []
grades = []

for i in range(aos):
    print(f"\n--- Student {i + 1} ---")
    name = input("Name: ")
    s1 = int(input("Score 1: "))
    s2 = int(input("Score 2: "))
    s3 = int(input("Score 3: "))
    names.append(name)

    countAvg(s1, s2, s3)
    checkGrade(s1, s2, s3)

print()
for i in range(aos):
    print(f"{names[i]} -> Average: {averages[i]:.2f} -> {grades[i]}")