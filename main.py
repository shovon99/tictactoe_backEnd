import board

import random

import pickle

states = []
import time


Game = board.Board()

GamesWon = 0


while GamesWon < 40000:
    

    p1moveSuccess = False

    while p1moveSuccess == False:
        p1move = random.randint(1,9)
        #print("Player 1 Supposed Move ", p1move)
        
        p1moveSuccess = Game.player1Move(p1move)
        if Game.getSnapshot() not in states:
             states.append(Game.getSnapshot())

        if Game.Won == True:
            Game.reset()
            GamesWon += 1
            print("### GamesWon Total: ", GamesWon, " ###" )
            continue
    
    p2moveSuccess = False

    while p2moveSuccess == False:
        p2move = random.randint(1,9)
        #print("Player 2 Supposed Move ", p2move)
        
        p2moveSuccess = Game.player2Move(p2move)
        if Game.getSnapshot() not in states:
             states.append(Game.getSnapshot())

        if Game.Won == True:
            Game.reset()
            GamesWon += 1
            print("### GamesWon Total: ", GamesWon, " ###" )
            continue
    
    print()


print("Total Unique States, ", len(states))

for i in range(0, 21):
    board.boardViewer(states[i])
    time.sleep(1)
