'''
* The map() function executes a specified function for
  each item in a iterable. The item is sent to the
  function as a parameter.
*Syntax:
    "map(function, iterables)"
here,
--function : It is a function to which map passes each element of given iterable.
--iterables : It is a iterable which is to be mapped.
*NOTE : You can pass one or more iterable to the map() function.
'''

def square(x):
    return x*x
num=[1,2,3,4,5 ]
result=map(square,num)
final_result=list(result)
print(final_result)

'''
*The filter() method filters the given sequence with
 the help of a function that tests each element in the
 sequence to be true or not.
*Syntax:
    "filter(function, sequence/iterable)"
*Parameters:
  function: function that tests if each element of a 
  sequence true or not.
  sequence: sequence which needs to be filtered, it can 
  be sets, lists, tuples, or containers of any iterators.
*Returns:
  returns an iterator that is already filtered.
'''
#check even No. using named function & filter function.
num2=[2,4,6,7,8,9,11]
def check(x):
    return x%2==0
result=filter(check,num2)
final_result=list(result)
print(final_result)

#again check odd No. using lambdafunction & filter function.

final_result=tuple(filter(lambda x:x%2==1,num2))
print(final_result)

#using List Comprehensions: it is easly can do the work of map,filter or other function.
result=[x*x for x in num2]
print(result)

#using List Comprehensions find even no in list num2:
result2=[x for x in num2 if x%2==0]
print(result2)