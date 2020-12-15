import re
def main():
    with open('input_days/day14.txt', 'r') as input:
        inputfile = [line.strip() for line in input]

    day14_1(inputfile)
    day14_2(inputfile)
    
def day14_1(inputfile):
    mask = ''
    memoryMap = {}
    for line in inputfile:        
        if 'mask' in line:
            mask = line.split('=')[1].strip()
        else:
            keyMap = int(re.search(r"\[([0-9]+)\]", line).group(1))
            valueMap = int(line.split('=')[1].strip())
            valueBin = bin(valueMap)[2:].zfill(36)

            for i in range (0, len(mask)):
                if mask[i] != 'X':
                    if mask[i] != valueBin[i]:
                        valueBin = valueBin[:i] + mask[i] + valueBin[i+1:]
    
            memoryMap[keyMap] = int(valueBin, 2)

    print('count: ' + str(sum(memoryMap.values())))
            
def day14_2(inputfile):
    mask = ''    
    result = {}
    listPow = []
    for line in inputfile:  
        memoryMap = {}          
        if 'mask' in line:
            del listPow[:]  
            mask = line.split('=')[1].strip()  
            for i in range(0, len(mask)):
                if mask[i] == 'X':
                    listPow.append(35-i)          
        else:
            keyMap = int(re.search(r"\[([0-9]+)\]", line).group(1))
            valueMap = int(line.split('=')[1].strip())
            valueBin = bin(keyMap)[2:].zfill(36)
            
            for i in range (0, len(mask)):                
                if mask[i] != '0':
                    valueBin = valueBin[:i] + mask[i] + valueBin[i+1:]

            minmem = int(valueBin.replace('X', '0') , 2)
            memoryMap[minmem] = valueMap
            listPow.sort()
            for i in range(0, len(listPow)):
                for m in list(memoryMap):
                    memoryMap[m + pow(2, listPow[i])] = valueMap
                  
            for x in list(memoryMap):
                result[x] = memoryMap[x]
                
    print('count: ' + str(sum(result.values())))
   
if __name__ == "__main__":
    main()