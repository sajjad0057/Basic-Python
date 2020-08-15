class std:
    roll="";
    gpa="";
    def display(self): #this is called method /function!
        print(f"ROLL is:{self.roll}---GPA is:{self.gpa}");

sakib=std();
print(isinstance(sakib,std));
sakib.roll=11;
sakib.gpa=3.3;
sakib.display();
sajjad=std();
print(isinstance(sajjad,std));
sajjad.roll=22;
sajjad.gpa=5;
sajjad.display();