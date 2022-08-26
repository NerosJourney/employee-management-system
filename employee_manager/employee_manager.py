########
# Bailey Wimer
# Aug 22, 2022
# company_agent.py
# A simple main file for early stage debugging and verification of functionality
#

from employee_agent import Employee
from company_agent import Company
from db_agent import *
from random_company import generate_random_employees

if __name__ == '__main__':
    comp = load_company(11223344)
    generate_random_employees(comp, 2)
    save_all_employees(comp)
    save_company(comp)
    # print("Enter a company name: ")
    # comp = Company(input(), 11223344)
    # comp.add_skill("Fry")
    # comp.add_skill("Cook")
    # comp.add_skill("Manager")

    # print("Enter an employees name: ")
    # emp1 = Employee(input(), comp.get_next_employee_id())
    # comp.add_employee(emp1)
    # comp.rate_employee(emp1.id)
    # emp1.print_employee()
    # save_employee(emp1, comp)

    # # print("Enter a number of employees: ")
    # # generate_random_employees(comp, int(input()))

    # save_all_employees(comp)
    # save_company(comp)

    # print("Waiting for input...")
    # input()

    # emp = load_employee(comp, 0)

    # save_all_employees(comp)

    # print(comp.search_employees_by_skill('Fry').name)