def main():
    with open('input_days/day22.txt', 'r') as input:
        inputfile = input.read().split('\n\n')
        inputfile[0] = inputfile[0].split(':')[1]
        inputfile[1] = inputfile[1].split(':')[1]
        inputfile = [x.replace('\n', ' ').split() for x in inputfile] 
    
    player1 = list(map(int, inputfile[0]))
    player2 = list(map(int, inputfile[1]))
    prevPlayer1 = []
    prevPlayer2 = []
    result = 0

    #combat(player1, player2)
    winner = recursiveCombat(player1, player2, 1, prevPlayer1, prevPlayer2)
    print(winner)
    winnerDeck = list(winner.values())[0]
    winnerDeck.reverse()
    for i in range(1, len(winnerDeck)+1):
        result += i * winnerDeck[i-1]
    print(result)

def combat(player1, player2):
    round = result = 0
    
    while player1 and player2:
        round += 1
        print('---- Round ' + str(round) + ' ----')
        print('Player 1 deck: ' + ''.join(str(player1)))
        print('Player 2 deck: ' + ''.join(str(player2)))
        print('Player 1 plays: ' + str(player1[0]))
        print('Player 2 plays: ' + str(player2[0]))
        
        if player1[0] > player2[0]:
            player1.append(player1[0])
            player1.append(player2[0])
            print('Player 1 wins')
        else:
            player2.append(player2[0])
            player2.append(player1[0])            
            print('Player 2 wins')
        
        player1.pop(0)
        player2.pop(0)
    
    winnerDeck = []        
    if len(player1) > 0:
        player1.reverse()
        winnerDeck = player1
    if len(player2) > 0:
        player2.reverse()
        winnerDeck = player2

    for i in range(1, len(winnerDeck)+1):
        result += i * winnerDeck[i-1]
        
    print(result)
    
#def day22_2(player1, player2):
    #recursive combat
    #rule: 
    # - each round check if deck structure of both players was in a previous round of this game. if yes, player1 win
    # - each player drawing first card of their deck; if both players have at least as many cards remaining in their deck
    #   >= at the value of drawed card, the winner is determinder by playing new game of recursive combat
    # - otherwise, the winner will be the player with the higher-value card
    # winner takes the two cards played and places them on the bottom of their own deck. The winner card must be the lower-valie card
def recursiveCombat(player1, player2, game, prevPlayer1, prevPlayer2):
    #player1 = [9, 2, 6, 3, 1]
    #player2 = [5, 8, 4, 7, 10]

    #print('---- Game ' + str(game) + ' ----')
    game += 1
    round = 0
    winner = {}
    
    while player1 and player2:
        round += 1
        #print('---- Round ' + str(round) + ' ----')
        #print('Player 1 deck: ' + ''.join(str(player1)))
        #print('Player 2 deck: ' + ''.join(str(player2)))
        #print('Player 1 plays: ' + str(player1[0]))
        #print('Player 2 plays: ' + str(player2[0]))
        
        #check if same round already happened. win player1
        if player1 in prevPlayer1 or player2 in prevPlayer2:
            winner['player1'] = player1.copy()
            break
            
        prevPlayer1.append(player1.copy())
        prevPlayer2.append(player2.copy())
        
        if player1[0] <= len(player1)-1 and player2[0] < len(player2)-1:
            #print('Playing a sub-game to determine the winner...')
            player1Copy = player1[1:player1[0]+1].copy()
            player2Copy = player2[1:player2[0]+1].copy()
            prevPlayer1Copy = prevPlayer1.copy()
            prevPlayer2Copy = prevPlayer2.copy()
            winner = recursiveCombat(player1Copy, player2Copy, game, prevPlayer1Copy, prevPlayer2Copy)
            #print('...anyway, back to game ' + str(game) + '.')
            #print(list(winner.keys())[0] + ' wins round ' + str(round) + ' of ' + str(game) + '!')
            if list(winner.keys())[0] == 'player1':
                player1.append(player1[0])
                player1.append(player2[0])
                print('Player 1 wins')
            else:                
                player2.append(player2[0])
                player2.append(player1[0])
                print('Player 2 wins')
                
            player1.pop(0)
            player2.pop(0)
        else: 
            if player1[0] > player2[0]:
                winner.clear()
                player1.append(player1[0])
                player1.append(player2[0])
                winner['player1'] = player1
            else:
                winner.clear()
                player2.append(player2[0])
                player2.append(player1[0])    
                winner['player2'] = player2  
            
            player1.pop(0)
            player2.pop(0)              
                
    return winner            
        
if __name__ == "__main__":
    main()