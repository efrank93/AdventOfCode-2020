def main():
    inputfile = open("C:\\Users\\Enrico\\Desktop\\AdventOfCode\\input_days\\day1.txt", "r").read().splitlines()
    array = [line for line in inputfile]
    array.sort()

    print(day1_1(array))


def day1_1(array):
    for i in range(0, len(array)):
        lowNumb = 2020 - int(array[i])
        for j in range(0, len([numb for numb in array if int(numb) < lowNumb])):
            year = int(array[i])+int(array[j])
            if year == 2020:
                return(int(array[i])*int(array[j]))

#def day1_2(array):


if __name__ == "__main__":
    main()