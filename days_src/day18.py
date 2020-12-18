
def main():
    with open('input_days/day18.txt', 'r') as input:
        inputfile = [line.split(',') for line in input]
    expressionList = {}
        
    day18_1(inputfile)
    
def day18_1(expressionList):
    count = 0
    for expression in expressionList:
        count += evaluateExp(expression)
                
    print(count)
    
def evaluateExp(expression):
    if '(' not in expression:
            return (eval(expression[0]))
    else:
        for index in range (0, len(expression)):
            if expression[index] == '(':
                evaluateExp(expression[index:])
            
if __name__ == "__main__":
    main()