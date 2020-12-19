def main():
    rules = {}
    myTicket = []
    nearbyTicket = []
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
    for line in inputfile[2]:
        ticket = []
        li = line.split(',')
        for val in li:
            ticket.append(int(val))
            
        nearbyTicket.append(ticket)
        
    day16_2(rules, myTicket1, nearbyTicket)

def day16_1(rules, myTicket, nearbyTicket):
    print(ticketValidator(nearbyTicket, rules))
    
def day16_2(rules, myTicket, nearbyTicket):
    count = 1
    validTicket = [] 
    print(ticketValidator(nearbyTicket, rules))
    
    for ticket in range (0, len(nearbyTicket)):
        if nearbyTicket[ticket] != '':
            validTicket.append(nearbyTicket[ticket])
            
    vk = {}
    listField = fieldAssignement(validTicket, rules)
    sort_orders = sorted(listField.items(), key=lambda x: x[1])

    for i in sort_orders:
        vk[i[0]] = i[1]
    l = list(vk.keys())
    for i in range (0, len(l)):
        if 'departure' in l[i]:
            count *= int(myTicket[i])
    print(count)
    
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

def fieldAssignement(nearbyTicket, rules):
    fieldRule = {}
    rule = list(rules.keys())
    while True:
        for i in range (0, len(nearbyTicket[0])):
            for r in range (0, len(rules)):
                tor = rules[rule[r]].split('or')
                r1 = int(tor[0].strip().split('-')[0])
                r2 = int(tor[0].strip().split('-')[1])
                r3 = int(tor[1].strip().split('-')[0])
                r4 = int(tor[1].strip().split('-')[1])
                for ticket in range(0, len(nearbyTicket)):
                    val = int(nearbyTicket[ticket][i])
                    if r1 <= val <= r2 or r3 <= val <= r4:
                        fieldRule[r]=rule[r]

    return fieldRule

if __name__ == "__main__":
    main()