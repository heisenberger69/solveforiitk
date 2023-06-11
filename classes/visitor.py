from classes.student import Student

class Visitor:
    def __init__(self):
        self.name = ""
        self.is_visitor = False
        self.mobile_no = 0
        self.student_ptr = None
        self.visitor_id = 0
        self.vehicle_no = 0
        self.govt_id = 0
        self.inside_status = False

    def set_visitor(self, name, inside_status):
        self.name = name
        self.inside_status = inside_status
        self.is_visitor = True
