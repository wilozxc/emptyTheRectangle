p1 = [0,0,0,0,0,0]
p2 = [0,0,0,0,0,0]

print 'player 1'
for i in range(6):
    p1[i] = input("How many tokens do you want on square #"+ str(i))

print 'player 2'
for i in range(6):
    p2[i] = input("How many tokens do you want on square #"+ str(i))

p1b = list(p1)
p2b = list(p2)


p1won = 0
p2won = 0

z =0

x = input("How many times do you want to play?")

import random

while z < x:
    dice1 = random.randrange(1,7,1)
    dice2 = random.randrange(1,7,1)

    dices = [dice1,dice2]

    dices.sort()

    dif = dices[1] - dices[0]

    if p1[dif] != 0:
        p1[dif] -= 1

    if p2[dif] != 0:
        p2[dif] -= 1

    



    if p1 == [0,0,0,0,0,0]:
        p1won += 1
        
        
        
        z += 1
        p1 = list(p1b)
        p2 = list(p2b)


    if p2 == [0,0,0,0,0,0]:
        p2won += 1
        
        
        z += 1
        
        p2 = list(p2b)
        p1 = list(p1b)

        
print 'player 2 won ' + str(p2won) +' times'
print 'player 1 won '+ str(p1won) +' times'
