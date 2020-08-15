subject=["c++","java","c","c#","python","basic"]
sub=(len(subject))
print("1->",sub)
subject.append("assemble")
print("2->",subject)
subject.insert(2,"sajjad")
print("3->",subject)
subject.remove("sajjad")
print("4->",subject)

subject2=subject.copy()
print("5->",subject2)
pos=subject.index("c#") #To find index No. use this formet
print("6->Index",pos)
pos_2=subject2[3] #To find index value use this formet
print("7->The 3 No. index  value is:",pos_2)
subject.sort()
print("8->",subject)


'''
python have lerge number
of builtin function
plz search it
'''