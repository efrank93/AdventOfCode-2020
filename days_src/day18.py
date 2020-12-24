import re
def main():
    with open('input_days/day18.txt', 'r') as input:
        inputfile = [line.strip().split(',') for line in input]
        
    day18_1(inputfile)
    
def day18_1(expressionList):
    count = 0
    for expression in expressionList:
        start = []
        end = []
        exp = expression[0].strip()
        if '(' not in exp:
            count += (expVal(exp.split(' ')))
            print(expression)
            print(count)
        else :
            count += evaluateExp(exp, start, end)
            print(expression)
            print(count)
                
    print(count)
    
def evaluateExp(expression, start, end):
    l = re.split('\(.+?\)?)\)', expression)
    count = 0  
    expression.strip()

    print('l')
    
    
    
    
    
    while '(' in expression:
        for i in range (0, expression.count('(')):
            p1 = expression.find('(')
            start.append(expression[:p1].strip().split(' '))
            p2 = expression.rfind(')')
            end.append(expression[p2+1:].strip().split(' '))
            expression = expression[p1+1:p2]
    
    removeInvEl(start, end)
    
    expression = expression.split(' ')
    count = expVal(expression)
    for i in range (len(start), 0, -1):
        start[i-1].append(str(count))
        end[i-1] = list(filter(lambda a: a != '', end[i-1]))
        expression = start[i-1] + end[i-1]
        count = expVal(expression)
      
    return count

def expVal(expression):
    count = expression[0]
    expression.pop(0)
    operator = ''
    for v in expression:
        if v == '+' or v == '*':
            operator = v
        elif not not v:
            count = eval(str(count) + operator + v)
    
    return count

def removeInvEl(start, end):
    for i in range (0, len(start)):
        start[i] = list(filter(lambda a: a != '', start[i]))
        end[i] = list(filter(lambda a: a != '', end[i]))

 
if __name__ == "__main__":
    main()