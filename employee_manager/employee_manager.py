########
# Bailey Wimer
# Aug 22, 2022
# company_agent.py
# A simple main file for early stage debugging and verification of functionality
#

import random
from employee_agent import Employee, default_avail, find_all_with_skill_above, search_employees_by_skill
from company_agent import Company
from db_agent import *
from random_company import generate_random_employees, generate_random_employee

if __name__ == '__main__':
    comp = Company("Dq", 11223344)
    comp.add_skill("Fry")
    comp.add_skill("Cook")
    comp.add_skill("DTO")
    generate_random_employee(comp)
    emp = comp.employees[0]
    emp.print_employee()
    count = 0
    for x in range(0, 7):
        count += emp.get_avail(x)[1] - emp.get_avail(x)[0] + 1
    print(f'{count} hours for the week')