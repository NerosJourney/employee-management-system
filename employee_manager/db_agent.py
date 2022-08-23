from company_agent import Company
from employee_agent import Employee

import json, os

def save_company(comp: Company):
    temp = {
        "name": comp.name,
        "id": comp.id,
        "num_emps": comp.next_employee_id,
        "skills": comp.skills
    }
    obj = json.dumps(temp, indent=4)
    dir = f'../db/{comp.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/company.emp', 'w+') as file:
        file.write(obj)
    return obj


def save_employee(emp: Employee, comp: Company):
    temp = {
        "name": emp.name,
        "id": emp.id,
        "skills": emp.skill_ratings
    }
    obj = json.dumps(temp, indent=4)
    dir = f'../db/{comp.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/{emp.id}.emp', 'w+') as file:
        file.write(obj)
    return obj