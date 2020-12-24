def main():
    with open('input_days/day24.txt', 'r') as input:
        inputfile = [line.split() for line in input]
    blackTileFlip = []
    day24_1(inputfile, blackTileFlip)  
    day24_2(blackTileFlip)  
    
def day24_1(inputfile, blackTileFlip):
    for line in inputfile:
        x = y = i = 0
        tile = []
        move = line[0]
        while i < len(move):
            if move[i] == 'e':
                x += 2
                i += 1
            elif move[i] == 'w':
                x -= 2
                i += 1
            else:
                if move[i] == 'n':
                    y += 1
                elif move[i] == 's':
                    y -= 1
                    
                if move[i+1] == 'e':
                    x += 1                        
                elif move[i+1] == 'w':
                    x -= 1
                        
                i += 2

        tile.append(x)
        tile.append(y)

        if tile in blackTileFlip:
            blackTileFlip.pop(blackTileFlip.index(tile))
        else:
            blackTileFlip.append(tile)
            
    print(len(blackTileFlip))

def day24_2(blackTileFlip):
    possibleWhiteFlip = []
    for tile in blackTileFlip:
        count = 0
        neighbours = retNeighbours(tile[0], tile[1])
        for neigh in neighbours:
            if neigh in blackTileFlip:
                count += 1
        
        if count == 0 or count > 2:
            possibleWhiteFlip.append(tile)
            blackTileFlip.pop(blackTileFlip.index(tile))
        
        print(tile)
        
def retNeighbours(x, y):
    return ((x+2,y), (x-2,y), (x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1))
            
if __name__ == "__main__":
    main()