def main():
    with open('input_days/day1.txt', 'r') as input:
        numsInput = list(map(int, [line.strip() for line in input]))
    numsInput = list(map(int, numsInput))
    numsInput.sort()
    day1_1(numsInput)
    print(day1_2(numsInput))


def day1_1(numsInput):
    for current in range(0, len(numsInput)):
        numberToSum = 2020 - numsInput[current]
        if numberToSum in numsInput:
            indexOfNumberToSum = numsInput.index(numberToSum)
            return numsInput[indexOfNumberToSum] * numsInput[current]
            
def day1_2(numsInput):
    for x in range(0, len(numsInput)):
        numberToFound = 2020 - numsInput[x]
        for y in range(0, len(val for val in numsInput if numsInput[x] not in numsInput)):
            numberToFound = numberToFound - numsInput[y]
            if numberToFound in numsInput:
                return numberToFound * numsInput[y] * numsInput[x]
                

if __name__ == "__main__":
    main()