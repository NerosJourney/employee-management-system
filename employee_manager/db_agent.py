########
# Bailey Wimer
# Aug 22, 2022
# db_agent.py
# Contains functions for saving data to files to act as a makeshift database
#

from company_agent import Company
from employee_agent import Employee

import json, os

# Converts key company data (except employees) into a json object to save in the directory:
# /db/<company_id>/company.emp
def save_company(comp: Company):
    temp = {
        "name": comp.name,
        "id": comp.id,
        "num_emps": comp.number_of_employees,
        "skills": comp.skills
    }
    obj = json.dumps(temp, indent=4)
    dir = f'../db/{comp.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/company.emp', 'w+') as file:
        file.write(obj)
    return obj

# Converts key employee data into a json object to save in the directory:
# /db/<company_id>/<employee_id>.emp
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