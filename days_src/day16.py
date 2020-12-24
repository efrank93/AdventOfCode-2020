def main():
    rules = {}
    myTicket = []
    nearbyTicket = {}
    with open('input_days/day16.txt', 'r') as input:
        inputfile = input.read().split('\n\n')
        inputfile = [x.split('\n') for x in inputfile]
            
    for line in inputfile[0]:
        rule = line.split(':')[0]
        limit = line.split(':')[1].strip()
        rules[rule] = limit
        
    myTicket = inputfile[1][1]
    li = myTicket.split(',')
    myTicket1 = []
    for val in li:
        myTicket1.append(int(val))
            
    inputfile[2].pop(0)
    for i in range (0, len(inputfile[2])):
        ticket = []
        li = inputfile[2][i].split(',')
        for val in li:
            ticket.append(int(val))
            
        nearbyTicket[i] = ticket
        
    day16_1(rules, myTicket1, nearbyTicket)
    day16_2(rules, myTicket1, nearbyTicket)

def day16_1(rules, myTicket, nearbyTicket):
    nearbyTemp = nearbyTicket.copy()
    count = 0
    validTicket = False
    for ticket in range(0, len(nearbyTemp)):
        for column in range(0, len(myTicket)):
            validTicket = validator(rules, column, nearbyTemp[ticket])
            if not validTicket:
                count += nearbyTicket[ticket][column]
                nearbyTicket[ticket] = ''
                break

    print(count)
    
def day16_2(rules, myTicket, nearbyTicket):
    validTicket = []
    listTicket = {}
    
    for ticket in range (0, len(nearbyTicket)):
        if nearbyTicket[ticket] != '':
            validTicket.append(nearbyTicket[ticket])
            
    for i in range(0, len(validTicket)):
        listTicket[i] = validTicket[i]
            
    
    listField = fieldAssignement(listTicket, rules)
    print(listField)

    
def ticketValidator(nearbyTicket, rules):
    count = 0
    for ticket in range(0, len(nearbyTicket)):
        for val in nearbyTicket[ticket]:
            invalid = True
            for rule in rules:
                tor = rules[rule].split('or')
                r1 = int(tor[0].strip().split('-')[0])
                r2 = int(tor[0].strip().split('-')[1])
                r3 = int(tor[1].strip().split('-')[0])
                r4 = int(tor[1].strip().split('-')[1])
                if r1 <= val <= r2 or r3 <= val <= r4:
                    invalid = False
                    break   
                    
            if invalid:
                nearbyTicket[ticket] = ''
                count += val
                break
            
    return count

def validator(rules, column, ticket):
    valid = False
    for rule in rules:
        val = int(ticket[column])
        tor = rules[rule].split('or')
        r1 = int(tor[0].strip().split('-')[0])
        r2 = int(tor[0].strip().split('-')[1])
        r3 = int(tor[1].strip().split('-')[0])
        r4 = int(tor[1].strip().split('-')[1])
        if r1 <= val <= r2 or r3 <= val <= r4:
            valid = True
            break
            
    return valid

def columnValidator(ranges, column, nearbyTicket):
    valid = False
    for ticket in range(0, len(nearbyTicket)):        
        val = nearbyTicket[ticket][column]
        tor = ranges.split('or')
        r1 = int(tor[0].strip().split('-')[0])
        r2 = int(tor[0].strip().split('-')[1])
        r3 = int(tor[1].strip().split('-')[0])
        r4 = int(tor[1].strip().split('-')[1])
        if r1 <= val <= r2 or r3 <= val <= r4:
            valid = True
        else:
            return False
            
    return valid
    

def fieldAssignement(nearbyTicket, rules):
    fieldRule = {}
    rule = list(rules.keys())
    columnMatch = []
    ruleTemp = rule.copy()
    max = len(ruleTemp)
    while len(rule) > 0:
        for r in range (0, max):  
            print(ruleTemp[r])         
            for column in range (0, len(nearbyTicket[0])):
                if not column in columnMatch:
                    if columnValidator(rules[ruleTemp[r]], column, nearbyTicket):
                        if column not in columnMatch:
                            columnMatch.append(column)
                
            if len(columnMatch) == 1:
                fieldRule[columnMatch[0]] = ruleTemp[r]
                rule.pop(r)
                ruleTemp = rule.copy()
                max = len(ruleTemp)
            else:
                del columnMatch[:]


if __name__ == "__main__":
    main()