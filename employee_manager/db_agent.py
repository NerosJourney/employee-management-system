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

# Saves all employees that belong to the specified company
def save_all_employees(comp: Company):
    for x in comp.employees.values():
        save_employee(x, comp)

# TODO increment/determine if need to increment next id in company
def load_employee(comp: Company, id) -> Employee:
    dir = f'../db/{comp.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
        return None
    with open(f'{dir}/{id}.emp', 'r') as file:
        obj = json.loads(file.read())
    emp = Employee(obj["name"], id)
    emp.skill_ratings = obj["skills"]
    comp.add_employee(emp)

def load_company(comp_id) -> Company:
    dir = f'../db/{comp_id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
        return None
    with open(f'{dir}/company.emp', 'r') as file:
        obj = json.loads(file.read())
    comp = Company(obj["name"], comp_id)
    comp.number_of_employees = obj["num_emps"]
    comp.skills = obj["skills"]
    return comp