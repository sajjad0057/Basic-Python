from random import randint
for x in range(10):
    print("game:",x)
    guess_number=int(input("Enter your (1 to 5) no:"))
    randomNumber=randint(1,5)
    if guess_number==randomNumber:
        print("Congratulation,\nYou have WON")
    else:
        print("You have lost")

    print("The Random No. was:",randomNumber)