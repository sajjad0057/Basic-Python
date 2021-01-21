'''
getattr() function is used to access the attribute value of an object and also give an option of executing the default value in case of unavailability of the key.
This has greater application to check for available keys in web development and many other phases of day-to-day programming.

Syntax : getattr(obj, key, def)

Parameters :
obj : The object whose attributes need to be processed.
key : The attribute of object
def : The default value that need to be printed in case attribute is not found.

Returns :
Object value if value is available, default value in case attribute is not present
and returns AttributeError in case attribute is not present and default value is not
specified.
'''


class Person:
    name = "sajjad"
    age = 23

    def __str__(self):
        return f'name is : {self.name}'


person = Person()
print(person)

print("The name is :"+getattr(person,"name"))
print("Ocupation : "+getattr(person,"ocupation","student"))
