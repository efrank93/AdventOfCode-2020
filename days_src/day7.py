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
    print(rulesBag)
    shinyGoldRules = []
    day7_1(rulesBag, shinyGoldRules)
    day7_2(rulesBag, shinyGoldRules)
    
def day7_1(rulesBag, shinyGoldRules):
    for rule in rulesBag:
        found = searchBag('shiny gold', rule, rulesBag)
        if found:
            shinyGoldRules.append(rule)
            
    print(len(shinyGoldRules))

def day7_2(rulesBag, shinyGoldRules):
    count = 0

        
    print(shinyGoldRules)


def searchBag(searchColor, rule, rulesBag):
    colorInBag = list(rulesBag[rule].keys())
    if searchColor in colorInBag:
        return True
    
    for color in colorInBag:
        if color != rule:
            found = searchBag(searchColor, color, rulesBag)
        
        if(found):
            return True
    
    return False


    
    
if __name__ == "__main__":
    main()