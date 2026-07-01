from database import students

def search(student_id):
    for index,student in enumerate(students):
        if student.std_id == student_id:
            return index
    return -1;
   