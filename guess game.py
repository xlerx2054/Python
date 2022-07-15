import random
from random import randint
class competition:
    def game(self):
        for j in range(3):
            randm = random.randint(1,100)
            print(randm)
            for i in range(3):
                n = int(input('Enter your number: '))
                if n > randm:
                    print("Too high.")
                elif n<randm:
                    print("Too low.")
                elif n == randm:
                    print('Congrats, number matched.') 
                    break
            print("\n")
        else:
            print('\nBetter try next time.') 
win_lose = competition()
win_lose.game()
