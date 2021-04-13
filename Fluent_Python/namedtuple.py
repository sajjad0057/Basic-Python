'''
Python supports a type of container like dictionaries called “namedtuple()” present in module,
“collections“. Like dictionaries they contain keys that are hashed to a particular value. But on contrary, 
it supports both access from key value and iteration, the functionality that dictionaries lack.
'''
import collections
# Declaring namedtuple()
Student = collections.namedtuple('Student',['name','age','DOB'])
  
# Adding values
S = Student('sajjad','24','2541997')
  
# initializing iterable 
li = ['nafiul', '23', '411997' ]
  
# initializing dict
di = { 'name' : "zahan", 'age' : 23, 'DOB' : '1391997' }
  
# using _make() to return namedtuple()
print ("The namedtuple instance using iterable is  : ")
print (Student._make(li))
  
# using _asdict() to return an OrderedDict()
print ("The OrderedDict instance using namedtuple is  : ")
print (S._asdict())
  
# using ** operator to return namedtuple from dictionary
print ("The namedtuple instance from dict is  : ")
print (Student(**di))