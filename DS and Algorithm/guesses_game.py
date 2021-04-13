import random as r
s_age = r.randint(1,10)
flag=True

def game_func(guessed_age,secret):
    if guessed_age<secret:
        return 'Too low'
    elif guessed_age>secret:
        return 'Too high'
    else:
        return 'CORRECT'

for i in range(6):
    guesses_age = int(input(f'Take a guesse, you have {6-i} guesses left : '))
    result=game_func(guesses_age,s_age)
    if result =='CORRECT':
        flag=False
        print("CONGRATULATIONS !! , You  Are Win")
        break
    else:
        print(f"{result}, TRY AGAIN....")

if flag:
    print("Sorry !! You are Lost The game....")
