import json
import csv

def save_json(students):
    data=[]
    for s in students:
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.dept,
            "semester": s.sem,
            "marks": s.marks
        })

    with open("students.json","w") as f:
        json.dump(data,f,indent=4)

    print("Student data successfully saved to students.json")


def generate_csv(students):
    with open("students_report.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["ID","Name","Department","Average","Grade"])

        for s in students:
            avg=sum(s.marks)/len(s.marks)
            grade="A" if avg>=80 else "B"
            writer.writerow([s.pid,s.name,s.dept,round(avg,2),grade])

    print("\nCSV Report (students_report.csv) generated")
