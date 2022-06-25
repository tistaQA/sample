from Practice.constructor import operation


class childone(operation):
    def __init__(self):
        operation.__init__(self, 11, 9)

    def myf1(self):
        print("hi")

    def getCompleteData(self):
        return self.num + self.sub()


obje = childone()
obje.myFun()
obje.myf1()