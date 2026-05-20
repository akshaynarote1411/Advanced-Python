# step-1: first we need to intialize the class
# step-2: every function need to provide **self**
#         self is not a an argument
# Step-3: First call the class
# Step-4: using the class object call the function

class GREET:
    def greet1(self):
        print('good morning')
    def greet2(self):
        print('good afternoon')
    def greet3(self):
        print('good eve')

obj=GREET()
obj.greet1()