from student import Student
from faculty import Faculty
from course import Course
from file_handler import save_json, generate_csv
from iterator_gen import student_generator

students=[]
faculty_list=[]
courses=[]

while True:

    print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Enroll\n5 Performance\n6 Compare\n7 Reports\n8 Exit")

    choice=input("Enter your choice: ")

    if not choice.isdigit():
        print("Invalid input! Enter numbers only")
        continue

    ch=int(choice)

    try:

        if ch==1:
            sid=input("ID:")
            if any(s.pid==sid for s in students):
                raise Exception("Student ID already exists")

            name=input("Name:")
            dept=input("Dept:")
            sem=int(input("Semester:"))
            marks=list(map(int,input("Marks:").split()))

            s=Student(sid,name,dept,sem,marks)
            students.append(s)
            print("\nStudent Created Successfully")

        elif ch==2:
            fid=input("ID:")
            name=input("Name:")
            dept=input("Dept:")
            sal=int(input("Salary:"))

            f=Faculty(fid,name,dept,sal)
            faculty_list.append(f)
            print("\nFaculty Created Successfully")

        elif ch==3:
            code=input("Code:")
            name=input("Name:")
            cr=int(input("Credits:"))
            fid=input("Faculty ID:")

            fac=next((f for f in faculty_list if f.pid==fid),None)
            if not fac:
                print("Error: Faculty not found")
                continue

            c=Course(code,name,cr,fac)
            courses.append(c)
            print("\nCourse Added Successfully")

        elif ch==4:
            sid=input("Student ID:")
            code=input("Course Code:")

            s=next((x for x in students if x.pid==sid),None)
            c=next((x for x in courses if x.code==code),None)

            if not s:
                print("Error: Student not found")
                continue
            if not c:
                print("Error: Course not found")
                continue

            s.enroll(c)
            print("\nEnrollment Successful")

        elif ch==5:
            sid=input("ID:")
            s=next(x for x in students if x.pid==sid)
            s.calculate_performance()

        elif ch==6:
            if len(students)<2:
                print("Error: Add at least TWO students")
                continue

            s1=students[0]
            s2=students[1]

            print("\nComparing Students Performance")
            print("--------------------------------")
            print(s1.name,">",s2.name,":",s1>s2)

        elif ch==7:
            save_json(students)
            generate_csv(students)

            print("\nStudent Record Generator")
            for rec in student_generator(students):
                print(rec)

        elif ch==8:
            print("\nThank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:",e)
