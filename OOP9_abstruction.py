'''
Example for Abstraction!
'''
from abc import ABC,abstractmethod    #Firstly Import abstractmethod!
class shape(ABC):
    def __init__(self,x,y): #constructor!
        self.dim1=x;
        self.dim2=y;
    @abstractmethod # It must be written,    # abstract class has no Object
    def area(self):   #this class can't create any object.
        pass;


class tringle(shape):
    def area(self): # by this action  method has been overwrited
        area=0.5*self.dim1*self.dim2;
        print("Area of Tringle:",area);


class rectangle(shape):
    def area(self): # by this action  method has been overwrited
        area=self.dim1*self.dim2;  #here area method is one type of polymorphysm ,BCz area method perform diferent task
        print("Area of rectangle:", area)                  #in different Time!

x=float(input("Enter the No. of X:"));
y=float(input("Enter thr No. of Y:"));

t=tringle(x,y);
t.area();
r=rectangle(x,y);
r.area();
