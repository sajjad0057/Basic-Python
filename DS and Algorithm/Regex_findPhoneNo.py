import re

# Finding Phone No with pattern
PhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
num = PhoneNumRegex.search("My number is 523-323-4445 .")
if not num:
    print("Phone Number not found")
else:
    print(f"group 1 : {num.group(1)}\n"
          f"group 2 : {num.group(2)}\n"
          f"group 3 : {num.group(3)}\n"
          f"Phone Number : {num.group()}")

