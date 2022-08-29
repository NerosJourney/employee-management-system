########
# Bailey Wimer
# Aug 22, 2022
# company_agent.py
# Contains the Employaee class for managing an employee's data
#

default_avail = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

# Manages all data associated with a single employee, including individual skill ratings.
class Employee:

    # The upper and lower bound of a rating for an employee's skill
    skill_bounds = (0, 10)

    def __init__(self, name, id, avail=default_avail):
        self.name = name
        self.id = id
        self.skill_ratings = {}
        self.avail = avail

    # Sets a skill to the value (constrained within skill_bounds) or creates it if it doesn't exist
    def set_skill(self, skill, num):
        self.skill_ratings[skill] = min(self.skill_bounds[1], max(self.skill_bounds[0], num))

    # Returns the rating of a given skill, or creates the skill and returns zero if it doesn't exist
    def get_skill(self, skill) -> int:
        if skill in self.skill_ratings:
            return self.skill_ratings[skill]
        else:
            self.set_skill(skill, 0)
            return 0
    
    def get_avail(self, day) -> tuple:
        return self.avail[day]

    def set_avail(self, day, hours: tuple):
        self.avail[day] = hours

    def check_avail(self, day, hr) -> bool:
        return hr >= self.avail[day][0] and hr <= self.avail[day][1]

    def print_employee(self):
        print(self.name, self.skill_ratings, self.avail)

