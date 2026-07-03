import json

def search(student_id):
    students= read_students()
    for index,student in enumerate(students):
        if student["std_id"] == student_id:
            return index
    return -1;

def read_students():
    with open("data/students.json","r") as file:
        students = json.load(file) 
        return students

def write_students(students):
    with open("data/students.json","w") as file:
        json.dump(students,file,indent=4)
        