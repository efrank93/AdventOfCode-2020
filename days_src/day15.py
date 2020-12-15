def main():
    #numbers = []
    numbers = open('input_days/day15.txt', 'r').read().split(',')
    #for val in f:
       # numbers.append(int(val))

    day15_1(numbers)
    
def day15_1(numbers):
    min = len(numbers)
    lastIndex = 0
    for i in range(min, 2020):        
        if numbers.count(numbers[i-1]) == 1:
            if '0' not in numbers:
                numbers.append('0')
            else: 
                lastIndex = len(numbers)-numbers[::-1].index('0')-1
                numbers.append('0')                    
        elif numbers[i-1] == numbers[i-2]:
            if '1' not in numbers:
                numbers.append('1')
            else: 
                lastIndex = len(numbers)-numbers[::-1].index('1')-1
                numbers.append('1')
        else:
            value = str(i-1 - lastIndex)
            if not value in numbers:
                numbers.append(value)
            else:
                lastIndex = len(numbers)-numbers[::-1].index(str(value))-1
                numbers.append(value)
            
    print(numbers[2019])

if __name__ == "__main__":
    main()