def isPhoneNumber(text):
    if len(text) !=11:
        return False
    for i in text:
        if not i.isdecimal():
            return False
    return True



message = "Call me at 411-555-10111 tomorrow . 567-534-66641 is my office . and my another phone no : 017741-35869"
message = message.replace("-",'')
print("----->",message)
for i in range(len(message)):
    chunk = message[i:i+11]
    if isPhoneNumber(chunk):
        print("Phone no : ",chunk)

print(f"Done")