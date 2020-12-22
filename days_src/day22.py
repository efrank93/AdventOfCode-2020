def main():
    with open('input_days/day22.txt', 'r') as input:
        inputfile = input.read().split('\n\n')
        inputfile[0] = inputfile[0].split(':')[1]
        inputfile[1] = inputfile[1].split(':')[1]
        inputfile = [x.replace('\n', ' ').split() for x in inputfile] 
        
    day22_1(inputfile[0], inputfile[1])
    
def day22_1(player1, player2):
    print(player1, player2)
        
if __name__ == "__main__":
    main()