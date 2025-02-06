
# class variable - define outside the class
#                  shared among all instances of the class

class Student:

    class_year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Raveen", 22)
student2 = Student("Navi", 33)
print(student2.class_year)
print(student2.name)