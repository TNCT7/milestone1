class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary

    @property
    def Weekly_salary(self):
        return self.salary *37.5

s1 = WorkingStudent('Rolf','XYZ',2000)
"""
print(s1.salary)
print(s1.school)
s1.marks.append(50)
s1.marks.append(100)
print(s1.marks)
print(s1.avg())

print(s1.Weekly_salary())
"""
print(s1.Weekly_salary)
#anna = Student('Anna','MIT')
#print(anna.Weekly_salary())
