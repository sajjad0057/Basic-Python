'''
Exaple for multi-level Inheritance!
'''
class A:
    def display1(self):
        print("I am inside A class");
class B(A):
    def display2(self):
        super().display1();
        print("I am inside B class");
class C(B):
    def display3(self):
        super().display2()
        print("I am inside C class");

c=C();
c.display3();

'''
Example for Multiple Inheritance!
'''
class X:
    def display11(self):
        print("I am inside X class");
class Y():
    def display22(self):

        print("I am inside Y class");
class Z(X,Y):
    def display33(self):
        super().display11()
        super().display22()
        print("I am inside Z class");

z=Z();
z.display33();



