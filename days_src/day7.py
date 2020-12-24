import re
def main():
    with open('input_days/day7.txt', 'r') as input:
        inputfile = [line.replace('\n', '').replace('.', '') for line in input]

    rulesBag = {}
    
    for rule in inputfile:
        colorBagQty = {}
        colorBag = rule.split('bags', 1)[0].strip()
        insideBags = rule.split('contain')[1].split(',')
        for bags in insideBags:
            bags = bags.strip()
            if not 'no other bag' in bags:
                qty = re.findall('\d+', bags )[0]
                color = re.findall('\D+', bags )[0].strip().split('bag')[0].strip()
                colorBagQty[color] = qty
                rulesBag[colorBag] = colorBagQty    
            else: 
                rulesBag[colorBag] = '0'
        

    #day7_1(rulesBag)
    day7_2(rulesBag)
    
def day7_1(rulesBag):
    shinyBag = []
    for rule in rulesBag:
        found = searchBag('shiny gold', rule, rulesBag)
        if found:
            shinyBag.append(rule)
            
    print(len(shinyBag))

def day7_2(rulesBag):
    count = number = 1
    count = sumInsideBags('shiny gold', rulesBag, number, count)
    print(count)

def searchBag(searchColor, rule, rulesBag):
    colorInBag = list(rulesBag[rule].keys())
    if searchColor in colorInBag:
        return True
    
    for color in colorInBag:
        if color != rule:
            found = searchBag(searchColor, color, rulesBag)
        
        if found:
            return True
    
    return False

def sumInsideBags(rule, rulesBag, number, count):
    if rulesBag[rule] == '0':
        count = count * int(number)
        print(rulesBag[rule])

    else :
        for rules in rulesBag[rule]:
            print(rulesBag[rule])
            count = int(rulesBag[rule][rules]) + sumInsideBags(rules, rulesBag, rulesBag[rule][rules], count)
            
    print(count)
    return count
    
if __name__ == "__main__":
    main()