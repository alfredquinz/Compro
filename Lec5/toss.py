import random

Head = 1
Tail = 2
Tosses = 10

def toss_cion():
    for toss in range(Tosses):
        if random.randint(Head,Tail) == Head:
            print("Head")
        else:
            print("Tail")
toss_cion()