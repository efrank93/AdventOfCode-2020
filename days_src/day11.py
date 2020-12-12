import numpy as np
import collections

def main():
    with open('input_days/day11.txt', 'r') as input:
        inputfile = np.loadtxt('input_days/day11.txt', dtype='str')
        
    #print(inputfile)
    newinput = inputfile.copy()
    day11_1(inputfile)
           
def day11_1(inputfile):
    #rules -> If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    #         If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    #         Otherwise, the seat's state does not change.
    newinput = inputfile.copy()
    cycle = True
    while cycle :               
        inputfile = newinput.copy()
        checkSeatStatus(inputfile, newinput)          
        #print(newinput)
        if collections.Counter(inputfile) == collections.Counter(newinput):  
            cycle = False

    count = 0            
    for line in newinput:
        count += line.count('#')
       
    print(count)    
    
def checkSeatStatus(inputfile, newinput):
    for row in range(0, len(inputfile)):        
        for seat in range(0, len(inputfile[row])):    
            empty = False      
            if inputfile[row][seat] == 'L' or inputfile[row][seat] == '#':
                count = 0
                if row > 0 :
                    if inputfile[row-1][seat] == '#' :
                        count += 1
                    if seat > 0:
                        if inputfile[row-1][seat-1] == '#':
                            count += 1
                    if seat < len(inputfile[row])-1:
                        if inputfile[row-1][seat+1] == '#':
                            count += 1        
                            
                if seat > 0 :
                    if inputfile[row][seat-1] == '#':
                        count += 1
                if seat < len(inputfile[row])-1:
                    if inputfile[row][seat+1] == '#':
                        count += 1
                            
                if row < len(inputfile)-1:
                    if inputfile[row+1][seat] == '#':
                        count += 1
                    if seat > 0:
                        if inputfile[row+1][seat-1] == '#':
                            count += 1
                    if seat < len(inputfile[row])-1:
                        if inputfile[row+1][seat+1] == '#':
                            count += 1
                
                if count >= 4:
                    newinput[row] = newinput[row][:seat] + 'L' + inputfile[row][seat+1:] 
                if count == 0:                              
                    newinput[row] = newinput[row][:seat] + '#' + inputfile[row][seat+1:] 
            
    #return newinput

if __name__ == "__main__":
    main()