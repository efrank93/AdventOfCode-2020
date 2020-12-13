def main():
    with open('input_days/day13.txt', 'r') as input:
        inputfile = [line.strip() for line in input]
    busWithX = []
    busWithoutX = []
    busWithX = inputfile[1].split(',')
    busWithoutX = inputfile[1].replace('x,', '').split(',')
    busList = {}
    for data in busWithoutX:
        busList[data] = 0
    #day14_1(int(inputfile[0]), busList)
    day14_2(busWithX)

def day14_1(timestamp, busList):
    for bus in busList:
        if (timestamp % int(bus)) < int(bus):
            busList[bus] = int(bus) - timestamp % int(bus)
    firstBus = min(busList, key=busList.get)
    print(int(firstBus) * int(busList[firstBus]))

def day14_2(busList):
    busWithoutX = []
    for el in busList:
        if not el == 'x':
            busWithoutX.append(el)        
    #firstBus = int(busList[0])
    maxBus = max(list(map(int, busWithoutX)))
    maxOffset = busList.index(str(maxBus))
    offset = []
    for v in range(0, len(busList)):
        if busList[v] == 'x':
            offset.insert(v, 0)
        else:
            offset.insert(v, v-maxOffset)
        
    cycle = True
    timestamp = 0
    while cycle:
        timestamp += maxBus
        found = True
        #if timestamp == 3417: 
        for diff in range (0, len(busList)):            
            if not busList[diff] == 'x':
                if (timestamp+offset[diff]) % int(busList[diff]) != 0:
                    found = False
        
        if timestamp % 100000 == 0:
            print(timestamp)
    
        if(found):
            cycle = False
            if offset[0] > 0:
                print('timestamp : ' + str(timestamp-offset[0]))
            else:
                print('timestamp : ' + str(timestamp+offset[0]))



if __name__ == "__main__":
    main()