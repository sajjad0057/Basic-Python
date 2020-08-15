'''
MAGIC method!
'''
class bike:
    def __init__(self,name,color):                     #it is one type of magic method!
        self.name=name
        self.color=color

    def __str__(self):                             #Also it is another type of magic method!
        return  (f"Name={self.name}, color={self.color}")
    def __eq__(self, other):                       #it is another type of magic method!
        return self.name==other.name and self.color==other.color;

    def display(self):
        print(f"Name={self.name}, color={self.color}")

bike1=bike("Yamaha R15","red")
bike2=bike("SZuki GxR","blue")
print(str(bike1));
print(str(bike2));
print(bike1==bike2);