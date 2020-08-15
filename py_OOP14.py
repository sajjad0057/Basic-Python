'''
search & Replace!
using regular Expression!
'''
import re
pattern=r"sajjad"
text1="His name is sajjad, sajjad is a student."
text2=re.sub(pattern,"sakib",text1)
print(text2)
text3=re.sub(pattern,"sakib",text1,count=1)  #using count=1 means just 1st pattern is replace!
print(text3)