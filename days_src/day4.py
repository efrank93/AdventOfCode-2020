import re

def main():
    with open('input_days/day4.txt', 'r') as input:
        formatList = input.read().split('\n\n')
        formatList = [x.replace('\n', ' ').split() for x in formatList]   
    passportList = []
    validPassport = []
    finalList = []
    for format in formatList:
        passportList.append(dict(data.split(':') for data in format))

    day4_1(passportList, validPassport)
    print(len(validPassport))
    day4_2(validPassport, finalList)
    print(len(finalList))

def day4_1(passportList, validPassport):
    count = 0
    for passport in passportList:
        if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport.keys()):
            validPassport.append(passport)

def day4_2(validPassport, finalList):
    
    for passport in validPassport:
        passportValidator(passport, finalList)

def passportValidator(passport, finalList):
    #print(passport)
    if (1920 <= int(passport['byr']) <= 2002
        and 2010 <= int(passport['iyr']) <= 2020
        and 2020 <= int(passport['eyr']) <= 2030
        and ((passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) 
             or (passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76)) 
        and re.match(r'#[\da-f]{6}', passport['hcl']) 
        and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] 
        and (len(passport['pid']) == 9 and re.match(r'\d{9}', passport['pid']))):
        finalList.append(passport)   

if __name__ == "__main__":
    main()