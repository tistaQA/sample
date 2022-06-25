class Mono:
    def __init__(self, x, y):
        self.f = x
        self.l = y

    def addition(self):
        return self.f + self.l
    def sub(self):
        return self.f - self.l

obj = Mono(100, 22)
print("The sum is", obj.addition())
print("The subtraction is", obj.sub())
