import re

def main():
    ruleMessages = {}
    messages = []
    with open('input_days/day19.txt', 'r') as input:
        for line in input:
            line = line.replace('\n', '')
            if ':' in line:
                index = int(line.split(':')[0].strip())
                if 'a' in line:
                    line = line.replace('"a"', 'a')
                if 'b' in line:
                    line = line.replace('"b"', 'b')
                rule = line.split(':')[1].strip()
                rule = rule.split(' ')
                ruleMessages[index] = rule
            elif ':' not in line and line != '':
                messages.append(line)
        
    day19_1(ruleMessages, messages)
    
def day19_1(ruleMessages, messages):
    regex = '('
    count = 0
    regex = createRegex(regex, ruleMessages[0], ruleMessages) + ')'
    print(regex)
    for message in messages:
        match = re.match('\b' + regex, message)
        if match:
            count += 1
            print(message)
    
    print(count)
#(a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b)        
def createRegex(regex, rules, ruleMessages):
    charList = 'ab|'
    if '|' in rules:
        regex = regex + '('
    for rule in rules:
        if rule != ' ':
            if rule == '|':
                regex = regex + '|'
            elif str(ruleMessages[int(rule)]) in charList:
                regex = regex + ruleMessages[rule]
            else:
                regex = createRegex(regex, ruleMessages[int(rule)], ruleMessages) + ')'
        
    return regex    
    
if __name__ == "__main__":
    main()