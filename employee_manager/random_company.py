from company_agent import Company
from employee_agent import Employee
import random

# Generates an employee with the name "Randomized" and random skills based on the company and adds it to the company
def generate_random_employee(comp: Company):
    temp = comp.get_next_employee_id()
    emp = Employee(str(temp), temp)
    for x in comp.skills:
        emp.set_skill(x, random.randint(0, 10))
    comp.add_employee(emp)

# Generates n number of random employees and adds them to the company
def generate_random_employees(comp: Company, n: int):
    for x in range(n):
        generate_random_employee(comp)