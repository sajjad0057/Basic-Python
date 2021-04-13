class tringle:
    def __init__(self,x,y):
        self.base=x;
        self.height=y;
    def calculate_area(self):
        area=0.5*self.base*self.height;
        print("Area=",area);
t1=tringle(10,20);
t1.calculate_area();
t2=tringle(15,30);
t2.calculate_area();
