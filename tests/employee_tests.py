import sys

sys.path.insert(0, '../employee_manager')

from employee_agent import Employee
from company_agent import Company

if __name__ == '__main__':
    comp = Company('Test', 1234)
    tom = Employee('tom', comp)
    tom.rate()
    tom.print_employee()