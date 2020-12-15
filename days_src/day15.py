import time

def main():    
    input = [0,3,1,6,7,5]
    numbers_1 = {}
    numbers_2 = {}
    
    for i in range(0, len(input)):
        numbers_1[int(input[i])] = i
        numbers_2[int(input[i])] = i
        
    start_time = time.time()
    day15(numbers_1, 2020)
    day15(numbers_2, 30000000)
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
def day15(numbers, limit):
    index = len(numbers)
    value = 0
    while index < limit:    
        maxKeys = numbers.keys()
        if not value in maxKeys:
            numbers[value] = index
            value = 0
            index += 1
        else:
            lastIndex = index - numbers[value]
            if lastIndex == 1:
                numbers[value] = index
                value = 1
            else: 
                numbers[value] = index
                value = lastIndex
                
            index += 1

        if index == limit:
            for k, v in numbers.items():
                if v == limit-1:
                    print(k)

if __name__ == "__main__":
    main()