#
# Assignment01 sample code
#

import random

num_of_players, players, dice_rolling_result, highest_score = 0, [], [], 0


# input: number of players, names of players

num_of_players = int(input("How many players are joining? "))

print("%d people are joining.")

i = 0
while i < num_of_players:
    players.append(input("Enter the name of player %d: " % (i+1)))
    i += 1

print("Players:", players)


# dice rolling

for player in players:
    dice_rolling_result.append(random.randrange(1, 7, 1) + random.randrange(1, 7, 1))

print("Dice rolling result:", dice_rolling_result)


# the largest value in dice rolling result

i = 0
while i < num_of_players:
    if highest_score <= dice_rolling_result[i]:
        highest_score = dice_rolling_result[i]
        last_winner_index = i    
    i += 1

print("The highest score is %d." % highest_score)


# output: winners

print("The winner(s):", end=' ')

for player in players:
    if dice_rolling_result[players.index(player)] == highest_score:        
        if players.index(player) < last_winner_index:
            print(player, end=', ')
        else:
            print(player)