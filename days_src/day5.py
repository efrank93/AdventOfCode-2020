import math
import numpy as np

def main():
    
    with open('input_days/day5.txt', 'r') as input:
        inputfile = [line[:10] for line in input]
        
    boardingPassList = {}
    
    day5_1(inputfile, boardingPassList)
    day5_2(boardingPassList)
    
def day5_1(inputfile, boardingPassList):
    for i in range (0, len(inputfile)):
        upperHalfRow = maxRow = 127
        upperHalfColumn = maxColumn = 7
        lowerHalfRow = lowerHalfColumn = row = seat = 0
        
        for char in inputfile[i]:
            if char == 'F':
                maxRow = math.ceil(maxRow/2)
                upperHalfRow -= maxRow
                row = upperHalfRow 
            elif char == 'B':
                maxRow = math.ceil(maxRow/2)
                lowerHalfRow += maxRow
                row = lowerHalfRow
            elif char == 'L':
                maxColumn = math.ceil(maxColumn/2)
                upperHalfColumn -= maxColumn
                seat = upperHalfColumn
            elif char == 'R':
                maxColumn = math.ceil(maxColumn/2)
                lowerHalfColumn += maxColumn
                seat = lowerHalfColumn
        
        boardingPassList[inputfile[i]] = row*8 + seat
    
    print(max(boardingPassList.values()))
    
def day5_2(boardingPassList):
    listSeatId = list(boardingPassList.values())
    listSeatId.sort()
    for position in range (1, len(listSeatId)-1):
        if listSeatId[position-1] == listSeatId[position]-2:
            print(listSeatId[position]-1)
    
if __name__ == "__main__":
    main()