'''
Uses of regular Expression!(re)!
'''
import re
pattern = r"colour"
if re.search(pattern,"Red is a  colour,I love red colour"):
    print("word is exist in this sentence")
else:
    print("word is not  exist in this sentence")

print(re.findall(pattern,"Red is a  colour,I love red colour"))

etc= r"name"
text="My name is sajjad."
src=re.search(etc,text)
if src:
    print(src.start()) #return 1st pattern index
    print(src.end())  #return last pattern  index
    print(src.span())   #return 1st  & last pattern  index
