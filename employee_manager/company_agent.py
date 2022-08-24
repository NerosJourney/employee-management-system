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
    number_of_employees = 0
    # The list of skills which employees of this company could have
    skills = []
    employees = {}

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    # Returns the next available employee ID for this company
    def get_next_employee_id(self):
        self.number_of_employees += 1
        return self.number_of_employees - 1

    # Adds an employee to the list of employees within this company
    def add_employee(self, emp: Employee):
        self.employees[emp.id] = emp
        print(self.employees)

    # Defines a new skill which should be included in every employee's review for this company
    def add_skill(self, skill: string) -> bool:
        if skill in self.skills:
            return False
        self.skills.append(skill)
        return True

    # Allows the user to input a rating for each skill for a given employee based on ID
    def rate_employee(self, employee_ID):
        temp = self.employees[employee_ID]
        print(f'Rating: {temp.name}  ')
        for curr in self.skills:
            #print(f'{curr} ({temp.skill_ratings[curr]}): ')
            print(curr, ": ", sep='')
            temp.set_skill(curr, int(input()))
