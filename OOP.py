
class Students:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def avgCal(self):
        return sum(self.grades)/ len(self.grades)


Student1 = Students('Tejas',[10,20,30,40,50])
Student2 = Students('Amruta',[60,70,80,90,100])

print(Student1.name)
print(Student2.name)

print(Student1.avgCal())

def avg(Students):
    return sum(Students.grades)/ len(Students.grades)

print(avg(Student2))