import random

aaronAccuracy = 2.0/7
bobAccuracy = 4.0/7
charlieAccuracy = 1.0


def shoot(targetAlive, accuracy):
    r = None
    if targetAlive:
        r = random.uniform(0, 1)

    if (r < accuracy):
        targetAlive = False

    return targetAlive


def startDuel():
    aliveAaron = True
    aliveBob = True
    aliveCharlie = True

    while ((aliveAaron and aliveBob) or
           (aliveAaron and aliveCharlie) or
           (aliveBob and aliveCharlie)):
        if aliveBob:
            if aliveCharlie:
                aliveCharlie = shoot(aliveCharlie, bobAccuracy)
            elif aliveAaron:
                aliveAaron = shoot(aliveAaron, bobAccuracy)
        if aliveCharlie:
            if aliveAaron:
                aliveAaron = shoot(aliveAaron, charlieAccuracy)
            elif aliveBob:
                aliveBob = shoot(aliveBob, charlieAccuracy)
        if aliveAaron:
            if aliveBob:
                aliveBob = shoot(aliveBob, aaronAccuracy)
            elif aliveCharlie:
                aliveCharlie = shoot(aliveCharlie, aaronAccuracy)

    if aliveAaron:
        return 'Aaron'
    elif aliveBob:
        return 'Bob'
    elif aliveCharlie:
        return 'Charlie'


AaronWins = 0
BobWins = 0
CharlieWins = 0

for i in range(1000):
    winner = startDuel()

    if winner == 'Aaron':
        AaronWins += 1
    elif winner == 'Bob':
        BobWins += 1
    elif winner == 'Charlie':
        CharlieWins += 1

print('Aaron Wins', AaronWins)
print('Bob Wins', BobWins)
print('Charlie Wins', CharlieWins)
