from os import curdir


def main():
    f = open('input_days/day23.txt', 'r').readline()
    print(f)
    cupGame_1(list(map(int, f)), 10)
    
def cupGame_1(cups, moves):
 
    for i in range(0, moves):
        destination = ''
        print('-- move ' + str(i+1) + ' --')
        currentCup = cups[i%10]
        print('cups ' + str(cups))
        print('currentcups: ' + str(currentCup))
        currentCupIndex = cups.index(currentCup)+1
        if len(cups)-currentCupIndex < 3:
            pickedUp = cups[currentCupIndex:] + cups[:len(cups)-currentCup]
        else:
            pickedUp = cups[currentCupIndex:currentCupIndex+3]
        print('pick up: ' + str(pickedUp))        
        tempCups = [cup for cup in cups if cup not in pickedUp]
        for i in range(0, currentCup):
            currentCup -= 1
            if currentCup in tempCups[:tempCups]:
                destination = currentCup
        if destination == '':
            destination = max(tempCups)
        
        print('destination ' + str(destination))
        cups = tempCups[:tempCups.index(destination)+1] + pickedUp  + tempCups[tempCups.index(destination)+1:] 
        
    result = cups


    

if __name__ == "__main__":
    main()