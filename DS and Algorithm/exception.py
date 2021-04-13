class x:
    def __init__(self,name,roll,point):
        self.name = name
        self.roll = roll
        self.point = point

    def test(self):
        print(f'Your Point is : {self.point} ')

class y(x):
    def test_1(self):
        print(f'Your new point is {self.point + 2}')
        x.test(self)


x1=x('sajjad',12,3.6)
x1.test()
y1=y('zahan',12,3.6)
y1.test_1()