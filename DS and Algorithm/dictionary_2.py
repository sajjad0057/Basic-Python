# This program counts the frequency of characters  on a string
import pprint as pp
text = 'this is a simple text To tesT the Code'
result = {}
for i in text.lower():
    if i != ' ':
        result.setdefault(i,0)
        result[i]=result[i]+1
pp.pprint(result)
