class Company:
    next_employee_id = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def nextEmpID(self):
        self.next_employee_id += 1
        return self.next_employee_id - 1