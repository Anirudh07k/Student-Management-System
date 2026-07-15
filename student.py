class Student:
    total_stu = 0

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        Student.total_stu += 1

    def display(self):
        print("---------------------------------------")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Grade   : {Student.grade(self.marks)}")
        print("---------------------------------------")

    def update_marks(self, marks):
        self.marks = marks

    @staticmethod
    def grade(marks):
        if 90 <= marks <= 100:
            return "A+"
        elif 80 <= marks:
            return "A"
        elif 70 <= marks:
            return "B"
        elif 60 <= marks:
            return "C"
        elif 40 <= marks:
            return "D"
        else:
            return "Fail"

    @classmethod
    def get_total_students(cls):
        return cls.total_students