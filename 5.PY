print("STUDENT ATTENDANCE AND PERFORMANCE TRACKING")

eligible_students = []
attendance_list = []
remedial_list = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    attendance = float(input("Enter attendance percentage: "))

    s1 = float(input("Enter marks in Subject 1: "))
    s2 = float(input("Enter marks in Subject 2: "))
    s3 = float(input("Enter marks in Subject 3: "))

    average = (s1 + s2 + s3) / 3

    if attendance >= 75 and average >= 60:
        eligible_students.append(name)

    if attendance < 75:
        attendance_list.append(name)

    if average < 60:
        remedial_list.append(name)

# Display results
print("\n========== STUDENT REPORT ==========")

print("\nEligible Students:", len(eligible_students))
for name in eligible_students:
    print(name)

print("\nAttendance Improvement List:", len(attendance_list))
for name in attendance_list:
    print(name)

print("\nRemedial Class List:", len(remedial_list))
for name in remedial_list:
    print(name)

print("====================================")