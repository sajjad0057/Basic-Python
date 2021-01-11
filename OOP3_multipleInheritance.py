class std:
    roll="";
    gpa="";
    def __init__(self,x,y):    #this is a constructor  under a class!
        self.roll=x;           #constructor is one kind of special method/function under a class!
        self.gpa=y;
    def display(self):     #this is  method /function!
        print(f"ROLL is:{self.roll}---GPA is:{self.gpa}");
a=int(input("Enter the Roll no:"));
b=float(input("Enter the GPA:"));
sakib=std(a,b);
print(isinstance(sakib,std));
sakib.display();
