

import random
N=random.randint(1,10)

for tries in range (1,5):
    #########################
    n=int(input(str(tries)+"GUESS ? >> "))
    if n==N:
        print("YYEESS : ) \nYou win!!! ")
        break
    elif n<N:
        print("try greater")
    else:
        print("try lesser")

print("Game over. correct answer was: ",N)