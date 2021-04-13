i = {'name':'sajjad','Age':'21','job':'student'}

'''
#printing values

for x in i.values():
    print(x)

#printing Keys

for x in i.keys():
    print(x)

#printing keys and values

for x,y in i.items():
    print(f'{x} : {y}')
    

#data extruct from dict
x=list(i.keys())
y=list(i.values())
print(x,y)

# use of 'in'  keyword
print('name' in i)
print('pop' in i)

    
'''


# how to work get('key','default')

print(str(i.get('name','Do not exist this key in dict ')))
print(str(i.get('height','Do not exist this key in dict ')))

# how to work setdefault('key','value') method in dict
print(i.setdefault('name','your name'))
print(i.setdefault('height','5 feet 6 inch'))
print(i)



