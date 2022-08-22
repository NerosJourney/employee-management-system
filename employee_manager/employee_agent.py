import string, json, os
from company_agent import Company

class Employee:
    skill_ratings = {}

    skill_bounds = (0, 10)

    def __init__(self, name, company: Company):
        self.name = name
        self.company = company
        self.id = company.nextEmpID()
        for curr in company.skills:
            self.skill_ratings[curr] = int(-1)

    def set_skill(self, skill, num):
        self.skill_ratings[skill] = min(self.skill_bounds[1], max(self.skill_bounds[0], num))


    def rate(self):
        global Skills
        print(f'Rating: {self.name}  ')
        for curr in self.company.skills:
            print(f'{curr} ({self.skill_ratings[curr]}): ')
            self.set_skill(curr, int(input()))
    
    def print_employee(self):
        print(self.skill_ratings)


def save_employee(emp: Employee) -> string:
    temp = {
        "name": emp.name,
        "company": emp.company.id,
        "id": emp.id,
        "skills": emp.skill_ratings
    }
    obj = json.dumps(temp, indent=4)
    dir = f'../db/{emp.company.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/{emp.id}.emp', 'w+') as file:
        file.write(obj)
    return obj

