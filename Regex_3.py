'''
Meta character!
Meta character very important for -
regular expression!
see internet!
'''
import re
pattern=r"colo..r"    #here .. meta character! thats indicate character.
if re.match(pattern,"coloiur"):
    print("1----> matched")
else:
    print("1-----> don't matched")
pattern=r"^colo..r"    #here .. meta character! ^  indicate something ,see net.
if re.match(pattern,"ciloiur"):
    print("2-----> matched")
else:
    print("2-----> don't matched")
pattern=r"c*olo..r"   #here .. meta character! * indicate something ,see net.
if re.match(pattern,"ccccccoloiur"):
    print("3------> matched")
else:
    print("3-----> don't matched")
