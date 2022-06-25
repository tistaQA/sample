# self keyword is mandatory for calling variable names inside methods
# constructor name should be __init__
# value of instance variable varies from object to object, but class variable is constant

class operation:
    num = 200
    # default constructor
    def __init__(self, a, b):
         self.x = a
         self.y = b
         print("This is from a constructor")

    def myFun(self):
        print("Hello world")

    def sub(self):
        return self.x - self.y+ self.num

obj1 = operation(20, 4)
print(obj1.sub())

