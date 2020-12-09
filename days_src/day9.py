def main():
    with open('input_days/day9.txt', 'r') as input:
        numsInput = [line.strip() for line in input]
        numsInput = list(map(int, numsInput))
        notValue = day9_1(numsInput)
        print("Value not found ->", notValue)
        sumMaxNotValue = day9_2(numsInput, notValue)
        print(sumMaxNotValue)
    
    
def day9_1(numsInput):
    for i in range (0, len(numsInput)-25):
        maxRange = 25
        numsIntoRange = numsInput[i:maxRange+i]
        numsToSum = numsInput[maxRange+i]
        check = None       
        if(checkSum(numsIntoRange, numsToSum, check)):
            return numsToSum
    
def day9_2(numsInput, notValue):    
    sum = 0
    rangedValue = []
    for i in range (0, len(numsInput)):
        for j in range(i, len(numsInput)):
            rangedValue.append(numsInput[j])
            sum += numsInput[j]

            if sum > notValue:
                del rangedValue[:]
                sum = 0
                break
            elif sum == notValue:
                rangedValue.sort()
                result = rangedValue[0]+rangedValue[len(rangedValue)-1]
                return result
        
    
def checkSum(numsIntoRange, numsToSum, check):
    for i in range(0, len(numsIntoRange)):
        check = True
        for j in range (i+1, len(numsIntoRange)):
            if numsToSum == numsIntoRange[i] + numsIntoRange[j]:
                check = False
                return check
    
    return check
    
if __name__ == "__main__":
    main()