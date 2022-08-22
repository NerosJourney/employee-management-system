import string, json, os
from company_agent import Company


Skills = ["Fry", "Order", "Drive through"]

class Employee:
    skill_ratings = {}

    def __init__(self, name, company: Company):
        self.name = name
        self.company = company
        self.id = company.nextEmpID()
        for curr in Skills:
            self.skill_ratings[curr] = int(-1)

    def rate(self):
        global Skills
        print(f'Rating: {self.name}  ')
        for curr in Skills:
            print(f'{curr} ({self.skill_ratings[curr]}): ')
            self.skill_ratings[curr] = int(input())
    
    def printEmp(self):
        print(self.skill_ratings)


def saveEmp(emp: Employee) -> string:
    temp = {
        "name": emp.name,
        "company": emp.company.id,
        "id": emp.id,
        "skills": emp.skill_ratings
    }
    obj = json.dumps(temp, indent=4)
    dir = f'../db/{emp.company.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/{emp.id}.emp', 'w+') as file:
        file.write(obj)
    return obj

def saveCompany(comp: Company) -> string:
    temp = {
        "name": comp.name,
        "id": comp.id,
        "num_emps": comp.next_employee_id
    }
    obj = json.dumps(temp, indent=4)
    dir = f'../db/{comp.id}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f'{dir}/company.emp', 'w+') as file:
        file.write(obj)
    return obj


if __name__ == '__main__':
    print("Enter a company name: ")
    comp = Company(input(), 11223344)

    print("Enter an employees name: ")
    emp1 = Employee(input(), comp)
    emp1.rate()
    emp1.printEmp()
    saveEmp(emp1)

    print("Enter an employees name: ")
    emp2 = Employee(input(), comp)
    emp2.rate()
    emp2.printEmp()
    saveEmp(emp2)

    saveCompany(comp)