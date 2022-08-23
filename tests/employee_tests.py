########
# Bailey Wimer
# Aug 22, 2022
# company_agent.py
# Unit tests for employees using the unittest python module
#

import unittest, sys

sys.path.insert(0, '/home/nero/code/personal/employee-management-system/employee_manager')

from employee_agent import Employee
from company_agent import Company

class TestEmployeeGeneration(unittest.TestCase):
    def test_employee_skill_assignments(self):
        comp = Company("Test", 1234)
        emp = Employee("John", comp)
        emp.set_skill("Flippin' Burgers", 10)
        emp.set_skill("Fry", 14)
        emp.set_skill("Tacos", -10)
        emp.set_skill("DQ", 0)
        emp.set_skill("Shift Leader", 5)
        emp.set_skill("Popcorn", -1000000000)
        self.assertEqual(emp.get_skill("Flippin' Burgers"), 10)
        self.assertEqual(emp.get_skill("Fry"), 10)
        self.assertEqual(emp.get_skill("Tacos"), 0)
        self.assertEqual(emp.get_skill("DQ"), 0)
        self.assertEqual(emp.get_skill("Shift Leader"), 5)
        self.assertEqual(emp.get_skill("Popcorn"), 0)
        self.assertEqual(emp.name, "John")
        self.assertEqual(emp.id, 0)
        self.assertEqual(emp.company, comp)

if __name__ == '__main__':
    unittest.main()
