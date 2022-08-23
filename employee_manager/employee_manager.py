########
# Bailey Wimer
# Aug 22, 2022
# company_agent.py
# A simple main file for early stage debugging and verification of functionality
#

from employee_agent import Employee
from company_agent import Company
from db_agent import save_company, save_employee

if __name__ == '__main__':
    print("Enter a company name: ")
    comp = Company(input(), 11223344)
    comp.add_skill("Fry")
    comp.add_skill("Cook")
    comp.add_skill("Manager")

    print("Enter an employees name: ")
    emp1 = Employee(input(), comp.get_next_employee_id())
    comp.add_employee(emp1)
    comp.rate_employee(emp1.id)
    emp1.print_employee()
    save_employee(emp1, comp)

    print("Enter an employees name: ")
    emp2 = Employee(input(), comp.get_next_employee_id())
    comp.add_employee(emp2)
    comp.rate_employee(emp2.id)
    emp2.print_employee()
    save_employee(emp2, comp)

    save_company(comp)