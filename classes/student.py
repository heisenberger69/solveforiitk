class Student:
    def __init__(self):
        self.name = ""
        self.is_student = False
        self.roll_no = 0
        self.inside_status = False
        self.visit_place = ""

    def set_student(self, name, inside_status):
        self.name = name
        self.inside_status = inside_status
        self.is_student = True
