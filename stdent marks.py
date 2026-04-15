class student:
    def __init__(self,mark):
        self.mark = mark
    def update(self,new_marks):
        self.mark = new_marks
    def show(self):
        print("Mark:",self.mark)
s1=student(80)
s1.show()

s1.update(99)
s1.show()