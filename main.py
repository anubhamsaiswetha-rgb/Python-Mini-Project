students = {}
def add_student(name, marks):
    students[name]=marks
    print("student added")
def display_students():
    for name, marks in students.items():
        print(name, ":", marks)
add_student("swetha", 90)
add_student("kavithri",89)
display_students()