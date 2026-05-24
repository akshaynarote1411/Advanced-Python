class Student:
    def __init__(self,marks):
        self.__marks = marks


obj = Student(90)
print(obj.__marks)   # we can't acces the private varible directly.