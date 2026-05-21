# class level arguments
# we will define class arguments by using __init__
# these areguments directly use by any function
# but while using these aregumts we need display as **self.arg**

class MATH:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,c):
        print('the addition of:',self.a + self.b + c)
    def sub(self):
        print('the Subtraction of:',self.a-self.b)
    def mul(self):
        print('the multilication of:',self.a*self.b)
    def div(self):
        print('the division of:',self.a/self.b)


if __name__=="__main__":
    MATH(100,200).add(300)
    MATH(10,20).sub()
    MATH(1,200).mul()
    MATH(100,2).div()