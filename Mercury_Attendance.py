

def grade(quiz_mark):
    if quiz_mark>=50:
        return("Pass")
    else:
        return("Fail")

def safe_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number")

names=[]
attendance=[]
marks=[]
n=safe_int("How many students to process? ")
for i in range(n):
    print(f"---student{i+1}---")
    name = input("Enter the students' names: ")
    while True:
        attendance_status= input("Enter the attendance status(P/A): ").strip().upper()
        if attendance_status=="P" or attendance_status=="A":
            break
        print("Enter P or A only.")
    while True:
            quiz_mark= safe_int("Enter the studen's quiz mark: ")
            if (quiz_mark>=0 and quiz_mark<=100):
                break
            print("Quiz mark must be between 0 and 100")

    names.append(name)
    attendance.append(attendance_status)
    marks.append(quiz_mark)

print("\n=====SESSION SUMMARY======")
present = 0
absent = 0
passed = 0
failed = 0
total = 0
for i in range(len(names)):
    result = grade(marks[i])
    print(names[i],attendance[i],marks[i], result)

    if attendance[i]=="P":
        present +=1
    else:
        absent +=1
    if result == "Pass":
        passed +=1
    else:
        failed +=1
    total += marks[i]

print(f"Present:{present} Absent:{absent}")

if len(marks)>0:
    print(f"Average mark:{total/len(marks)}")
else:
    print(f"Average mark: no student entered")

print(f"Pass:{passed} Fail:{failed}")
        
        
