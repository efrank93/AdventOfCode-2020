def main():
    with open('input_days/day3.txt', 'r' ) as input:
        listTrees = [line.strip() for line in input]
    slopes = [{'right': 1, 'down': 1},
              {'right': 3, 'down': 1},
              {'right': 5, 'down': 1},
              {'right': 7, 'down': 1},
              {'right': 1, 'down': 2}]
    
    day3_1(listTrees, slopes[1])
    trees = 1
    for x in range (0, len(slopes)):
        trees *= day3_1(listTrees, slopes[x])

    
def day3_1(listTrees, slopes):
    trees = column = row = 0    
    while row < len(listTrees)-1:
        column += slopes.get('right')
        row += slopes.get('down')
        
        if column >= len(listTrees[row]):
            column -= len(listTrees[row])
        if column < len(listTrees[row]) and listTrees[row][column] == '#':
            trees += 1
 
    return trees       
    
if __name__ == "__main__":
    main()