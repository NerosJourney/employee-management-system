########
# Bailey Wimer
# Aug 22, 2022
# company_agent.py
# Contains the Company class for managing a company's data
#

import string
from employee_agent import Employee

# The Company class contains all necessary data required for the corresponding company.
# Responsible for managing a list of employees, finding employees within that list, and handling a list of skills
class Company:
    next_employee_id = 0
    skills = []
    employees = []
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_next_employee_id(self):
        self.next_employee_id += 1
        return self.next_employee_id - 1

    def add_employee(self, emp: Employee):
        self.employees.append(emp)

    def add_skill(self, skill: string) -> bool:
        if skill in self.skills:
            return False
        self.skills.append(skill)
        return True

    def rate_employee(self, employee_ID):
        temp = self.employees[employee_ID]
        print(f'Rating: {temp.name}  ')
        for curr in self.skills:
            #print(f'{curr} ({temp.skill_ratings[curr]}): ')
            print(curr, ": ", sep='')
            temp.set_skill(curr, int(input()))
