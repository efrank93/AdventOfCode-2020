def main():
    with open('input_days/day22.txt', 'r') as input:
        inputfile = input.read().split('\n\n')
        inputfile[0] = inputfile[0].split(':')[1]
        inputfile[1] = inputfile[1].split(':')[1]
        inputfile = [x.replace('\n', ' ').split() for x in inputfile] 
        
    day22_1(inputfile[0], inputfile[1])
    
def day22_1(player1, player2):
    round = result = 0
    winner = False
    while not winner:
        round += 1
        print('---- Round ' + str(round) + ' ----')
        print('Player 1 deck: ' + ' '.join(player1))
        print('Player 2 deck: ' + ' '.join(player2))
        print('Player 1 plays: ' + player1[0])
        print('Player 2 plays: ' + player2[0])
        
        if int(player1[0]) > int(player2[0]):
            player1.append(player1[0])
            player1.append(player2[0])
            print('Player 1 wins')
        else:
            player2.append(player2[0])
            player2.append(player1[0])            
            print('Player 2 wins')
        
        player1.pop(0)
        player2.pop(0)
        if len(player1) == 0 or len(player2) == 0:
            winner = True
    
    winnerDeck = []        
    if len(player1) > 0:
        player1.reverse()
        winnerDeck = player1
    if len(player2) > 0:
        player2.reverse()
        winnerDeck = player2

    for i in range(1, len(winnerDeck)+1):
        result += i * int(winnerDeck[i-1])
        
    print(result)
        
if __name__ == "__main__":
    main()