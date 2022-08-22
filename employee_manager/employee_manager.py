from employee_agent import Employee, save_employee
from company_agent import Company, save_company

if __name__ == '__main__':
    print("Enter a company name: ")
    comp = Company(input(), 11223344)
    comp.add_skill("Fry")
    comp.add_skill("Cook")
    comp.add_skill("Manager")

    print("Enter an employees name: ")
    emp1 = Employee(input(), comp)
    emp1.rate()
    emp1.print_employee()
    save_employee(emp1)

    print("Enter an employees name: ")
    emp2 = Employee(input(), comp)
    emp2.rate()
    emp2.print_employee()
    save_employee(emp2)

    save_company(comp)