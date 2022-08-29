########
# Bailey Wimer
# Aug 22, 2022
# company_agent.py
# A simple main file for early stage debugging and verification of functionality
#

import random
from employee_agent import Employee, find_all_with_avail, find_all_with_skill_above, search_employees_by_skill
from company_agent import Company
from db_agent import *
from random_company import generate_random_employees, generate_random_employee

if __name__ == '__main__':
    comp = Company("Dq", 11223344)
    comp.add_skill("Fry")
    comp.add_skill("Cook")
    comp.add_skill("DTO")
    generate_random_employees(comp, 100)
    print("Highest Fry skill: ")
    search_employees_by_skill(comp.employees, "Fry").print_employee()
    available = find_all_with_avail(comp.employees, 2, 14)
    print("All employees available on Wednesday at 14:00")
    for x in available.values():
        x.print_employee()
    skill = find_all_with_skill_above(comp.employees, "DTO", 8)
    print("All employees with an 8 or better DTO")
    for x in skill.values():
        x.print_employee()
    print("Combination: ")
    combo = find_all_with_avail(skill, 2, 14)
    for x in combo.values():
        x.print_employee()
    print("Best frier on Wednesday at 14:00: ")
    search_employees_by_skill(available, "Fry").print_employee()