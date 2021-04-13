class std:
    roll="";
    gpa="";
    def setValue(self,x,y):    #this is called method /function under a class!
        self.roll=x;
        self.gpa=y;
    def display(self):     #this is another method /function!
        print(f"ROLL is:{self.roll}---GPA is:{self.gpa}");

sakib=std();
print(isinstance(sakib,std));
sakib.setValue(5,3.33);
sakib.display();
sajjad=std();
print(isinstance(sajjad,std));
sajjad.setValue(88,4.4)
sajjad.display();