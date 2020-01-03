class First(object):

    def __init__(self, temp):
        self.temp = temp

    def func1(self):
        a = 0
        while a <=10:
            a +=1
            print(a)
data = First("This is inside First class")
out_data = data.func1()
print(out_data)