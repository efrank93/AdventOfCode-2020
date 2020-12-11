import itertools
from collections import defaultdict

def main():
    with open('input_days/day10.txt', 'r') as input:
        joltageInput = list(map(int, [line.strip() for line in input]))
        # sortinjg list in ascending
        joltageInput.sort()
        #insert value 0 (charging outlet) and max joltage (max device's built-in adapter + 3)
        joltageInput.insert(0, 0)
        joltageInput.append(max(joltageInput)+3)
        day10_1(joltageInput)
        day10_2(joltageInput)

        
def day10_1(joltageInput):  
    dictDifferences = {1:0, 2:0, 3:0}
    
    #for each adapter from the input, search if exists the next in a range from 1-4 (max 3) and add the jolt differences
    for adapter in joltageInput[:-1]:
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in joltageInput:
                dictDifferences[diff] += 1
                break
        
    print(dictDifferences[1]*dictDifferences[3])

def day10_2(joltageInput):

    paths = defaultdict(int)
    paths[0] = 1
    #for each adapter from the input, search if exists the next and the possible path with the other adapters inside the range
    for adapter in joltageInput:
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in joltageInput:
                paths[next_adapter] += paths[adapter]        
    
    print(paths[max(joltageInput)])    
    
if __name__ == "__main__":
    main()