from employee_agent import Employee, saveEmployee
from company_agent import Company, saveCompany

if __name__ == '__main__':
    print("Enter a company name: ")
    comp = Company(input(), 11223344)

    print("Enter an employees name: ")
    emp1 = Employee(input(), comp)
    emp1.rate()
    emp1.printEmp()
    saveEmployee(emp1)

    print("Enter an employees name: ")
    emp2 = Employee(input(), comp)
    emp2.rate()
    emp2.printEmp()
    saveEmployee(emp2)

    saveCompany(comp)