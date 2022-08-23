class Employee:
    skill_ratings = {}

    skill_bounds = (0, 10)

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def set_skill(self, skill, num):
        self.skill_ratings[skill] = min(self.skill_bounds[1], max(self.skill_bounds[0], num))

    def get_skill(self, skill) -> int:
        if skill in self.skill_ratings:
            return self.skill_ratings[skill]
        else:
            self.set_skill(skill, 0)
            return 0
    
    def print_employee(self):
        print(self.skill_ratings)

