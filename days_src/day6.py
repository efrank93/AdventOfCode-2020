def main():
    answerList = {}
    with open('input_days/day6.txt', 'r') as input:
        inputfile = input.read().split('\n\n')
        
    answerList = [line.split('\n') for line in inputfile]
    groupUniqueAnswer = {}
    day6_1(answerList, groupUniqueAnswer)
    day6_2(answerList, groupUniqueAnswer)

def day6_1(answerList, groupUniqueAnswer):
    count = 0
    for i in range (0, len(answerList)):
        groupAnswer = ''
        for person in answerList[i]:
            groupAnswer = groupAnswer + person
        combinedAnswer = ''.join(set(groupAnswer))
        groupUniqueAnswer[i] = combinedAnswer
        count += len(combinedAnswer)
    
    print(count)
    
def day6_2(answerList, groupUniqueAnswer):
    count = 0
    for i in range (0, len(answerList)):
        groupAnswer = ''
        for person in answerList[i]:
            groupAnswer = groupAnswer + person
        for char in groupUniqueAnswer[i]:
            if groupAnswer.count(char) == len(answerList[i]):
                count += 1
                    
    print(count)

if __name__ == "__main__":
    main()