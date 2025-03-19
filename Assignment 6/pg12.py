classesheld = int(input("Enter total classes held"))
classesattended = int(input("Enter total classes held"))
percent = (classesattended/classesheld)*100

if percent<75:
    print(f"Attendance percentage : {percent}")
    print("You are not allowed to sit for exams")
else:
    print(f"Attendance percentage : {percent}")
    print("You are allowed to sit for exams")
