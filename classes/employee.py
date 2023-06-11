class Employee:
    def __init__(self):
        self.name = ""
        self.employee_no = 0
        self.is_employee = False
        self.inside_status = False

    def set_employee(self, name, inside_status):
        self.name = name
        self.inside_status = inside_status
        self.is_employee = True
