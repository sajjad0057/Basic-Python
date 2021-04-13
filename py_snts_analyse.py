n=input("Enter a text:")
list=n.split() #this function convert all data type to string.
print(list)
#In below we find a number of letter, word or digit quantity in a sentence.
text=input("Enter your text:")
No_of_letters=0
No_of_words=0
No_of_digits=0

for x in text:
    if x>='a' and x<='z':
        x=x.lower()
        print(x,end=" ")
        No_of_letters = No_of_letters + 1
print()
print("The no of letter is:",No_of_letters)
for x in text:
    if x>='0' and x<='9':
        print(x,end=" ")
        No_of_digits=No_of_digits+1
print()
print("The No. of digit:",No_of_digits)
for x in text:
    if x==' ':
        No_of_words=No_of_words+1
print("The No. of word is:",No_of_words+1)