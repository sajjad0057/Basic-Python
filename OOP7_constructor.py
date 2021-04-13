'''
practice:using constructor, method & method  overloading
oR over writing.
'''
class shape:
    def __init__(self,x,y): #constructor!
        self.dim1=x;
        self.dim2=y;
    def area(self):
        print("I am the area method of shape class:");
class tringle(shape):
    def area(self): # by this action  method has been overwrited
        area=0.5*self.dim1*self.dim2;
        print("Area of Tringle:",area);


class rectangle(shape):
    def area(self): # by this action  method has been overwrited
        area=self.dim1*self.dim2;
        print("Area of rectangle:",  area);
x=float(input("Enter the No. of X:"));
y=float(input("Enter thr No. of Y:"));
t=tringle(x,y);
t.area();
r=rectangle(x,y);
r.area();
