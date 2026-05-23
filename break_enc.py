class Student:
    def __init__(self,marks):
        self.__marks = marks


obj = Student(90)
print(obj._Student__marks)      # *** _classname__variablename *** this is used to access the private varibles from function. 