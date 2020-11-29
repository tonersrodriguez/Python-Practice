#application that uses student.py
from student import Student
#when you create a student you are using the init function from student.py
student1 = Student("Tony", "Computer Science", 3.1 , False)
student2 = Student("Emily", "Cinema", 3.3 , False)
student3 = Student("Ana", "Criminal Justice", 3.4 , False)
student4 = Student("Marcelo", "Civil Engineer", 2.8 , False)
student5 = Student("Staphany", "Education", 3.9, False)
print(student1.major)
print(student1.on_honor_roll())

