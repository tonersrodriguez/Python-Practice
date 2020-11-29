class Student:
    #this is the representation of student data type and everything needed
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    #importance of putting functions in classes to modify or code easier
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
'''
class is template defines what a student is 
object is actual entity (student)
'''