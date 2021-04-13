class person:
    def __init__(self,person_name,date_of_birth,ht):
        self.__name = person_name
        self.__date_of_birth= date_of_birth
        self.__height= ht
        self.abc= None

    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        if (self.__has_any_number(new_name)):
            print("Sorry person name can't have any number")
            return
        self.__name=new_name

    def __has_any_number(self,string):
        return "0" in string

    def get_summery(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth},Height: {self.__height}"




a_person=person("sajjad","1990","5 feet 6 inch")
print(a_person)
print(a_person.get_summery())
a_person.set_name("sajjad Hossain")
print(a_person.get_summery())
print(a_person._person__date_of_birth)
a_person.set_name('0sajjad sakib')
print(a_person.get_name())
