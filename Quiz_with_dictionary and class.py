# quiz = {1: {'5+5= ?\n A:10 B:15': 'A'},
#         2: {'What is the name of our national animal ?\n A:Dog B:Tiger C:Lion': 'B'},
#         3: {'What is the name of our running prime minister ?\n A:shaik Hasina B:khaleda Jia C:Abdul Hamid': 'A'},
#         4: {'5-2*2= ?\n A:6 B:1 C:0 ': 'B'}
#         }
#
# score = 0
# for x in quiz.values():
#     for y, z in x.items():
#         print(y)
#         Answer = input('Please choose your Answer:\n')
#         if Answer.lower() == z.lower():
#             print('Yes , You Are Absolutely Right!')
#             score += 10
#
#         else:
#             print('Sorry You Are Wrong \n')
#
# print("You Have GAINED A TOTAL OF : ",score)


class Quiz:
    score = 0

    def __init__(self,x):
        self.x = quiz

    def startTheQuiz(self):

        for x in quiz.values():
            for y, z in x.items():
                print(y)
                Answer = input('Please choose your Answer:\n')
                if Answer.lower() == z.lower():
                    print('Yes , You Are Absolutely Right!')
                    self.score += 10

                else:
                    print('Sorry You Are Wrong \n')

        return self.score




quiz = {1: {'5+5= ?\n A:10 B:15': 'A'},
        2: {'What is the name of our national animal ?\n A:Dog B:Tiger C:Lion': 'B'},
        3: {'What is the name of our running prime minister ?\n A:shaik Hasina B:khaleda Jia C:Abdul Hamid': 'A'},
        4: {'5-2*2= ?\n A:6 B:1 C:0 ': 'B'}
        }
start = Quiz(quiz)
print('Your Score Is : ',start.startTheQuiz())