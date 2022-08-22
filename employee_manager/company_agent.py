import os, json
import string

class Company:
    next_employee_id = 0
    skills = []
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def nextEmpID(self):
        self.next_employee_id += 1
        return self.next_employee_id - 1

    def add_skill(self, skill: string) -> bool:
        if skill in self.skills:
            return False
        self.skills.append(skill)
        return True


def save_company(comp: Company):
    temp = {
        "name": comp.name,
        "id": comp.id,
        "num_emps": comp.next_employee_id
    }
    obj = json.dumps(temp, indent=4)
    dir = f'../db/{comp.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/company.emp', 'w+') as file:
        file.write(obj)
    return obj
