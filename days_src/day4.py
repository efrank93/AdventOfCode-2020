import re

def main():
    with open('input_days/day4.txt', 'r') as input:
        formatList = input.read().split('\n\n')
        formatList = [x.replace('\n', ' ').split() for x in formatList]   
    passportList = []
    for format in formatList:
        passportList.append(dict(data.split(':') for data in format))

    day4_1(passportList)

def day4_1(passportList):
    count = 0
    for passport in passportList:
        if fieldsValidator(passport):
            count += 1

    #print(passportList)
    print(count)


def fieldsValidator(passport):
    validFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for fields in validFields:
        if fields not in passport:
            return False
        else :
            if fields == 'byr':
                if not int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
                    return False
            if fields == 'iyr':
                if not int(passport['iyr']) >= 2010 and int(passport['byr']) <= 2020:
                    return False
            if fields == 'eyr':
                if not int(passport['eyr']) >= 2020 and int(passport['byr']) <= 2030:
                    return False
            if fields == 'hgt':
                if not passport['hgt'][-2:] == 'cm' and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193:
                    return False
            if fields == 'hgt':
                if not passport['hgt'][-2:] == 'in' and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76:
                    return False
            if fields == 'hcl':
                if not re.match(r'[0-9a-f]{6}', passport['byr']):
                    return False
            if fields == 'ecl':
                if not int(passport['ecl']) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    return False
            if fields == 'pid':
                if not re.match(r'\d[0-9]', passport['pid']):
                    return False

    return True

if __name__ == "__main__":
    main()