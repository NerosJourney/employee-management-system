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
    # The list of skills which employees of this company could have

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.number_of_employees = 0
        self.skills = []
        self.employees = {}
    
    # Returns the next available employee ID for this company
    def get_next_employee_id(self):
        self.number_of_employees += 1
        return self.number_of_employees - 1

    # Adds an employee to the list of employees within this company
    def add_employee(self, emp: Employee):
        self.employees[emp.id] = emp

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
            self.employees[employee_ID].set_skill(curr, int(input()))

    def search_employees_by_skill(self, skill: string) -> Employee:
        if len(self.employees) == 0:
            return None
        highest_skill = 0
        for x in range(0, self.number_of_employees):
            if self.employees[x].get_skill(skill) > self.employees[highest_skill].get_skill(skill):
                highest_skill = x
        return self.employees[highest_skill]

