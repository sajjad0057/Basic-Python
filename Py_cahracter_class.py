import re
pattern = r"[aeiou]"
if re.match(pattern,"education"):
    print("1----> matched")
else:
    print("1-----> don't matched")

pattern = r"[aeiou]"
if re.match(pattern,"dhegoijj"):
    print("2----> matched")
else:
    print("2-----> don't matched")