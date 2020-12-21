def main():    
    with open('input_days/day21.txt', 'r') as input:
        inputfile = [line.replace('\n', '').replace('(','').replace(')','') for line in input]        

    shareAllergen = {}
    allergenList = []

    for index in range (0, len(inputfile)):
        ingredients = inputfile[index].split('contains')[0].strip().split(' ')
        allergens = inputfile[index].split('contains')[1].strip().replace(', ', ',').split(',')
        shareAllergen[index] = [allergens] + [ingredients]
        for al in allergens:
            if al not in allergenList:
                allergenList.append(al)
    
    #print(shareAllergen)
    #print(uniqueAllergen)
    day21_1(shareAllergen, sorted(allergenList))
    
def day21_1(shareAllergen, allergenList):
    #per ogni allergeno, estraggo ogni food dove è presente e tramite intersection
    #ritorno il set di ingredienti che matchano con l'allergeno
    possibleVal = set()
    allerIng = {}
    for allergen in allergenList:
        possibleIng = []
        for food in range(0, len(shareAllergen)):
            if allergen in shareAllergen[food][0]:
                possibleIng.append(shareAllergen[food][1])
        possibleIng = set.intersection(*map(set,possibleIng))
        #print(len(possibleIng))
        possibleVal = possibleVal.union(possibleIng)
        allerIng[allergen] = possibleIng
        
        for allergen in allerIng:
            allerIng[allergen] = list(allerIng[allergen])
    
    order = True
    while order:
        al = ''
        count = 0
        
        for allergen in allergenList:
            for ingredient in allerIng[allergen]:
                if len(allerIng[allergen]) == 1:
                    al = ingredient
                    count += 1
                    break
            for allergen in allergenList:       
                if len(allerIng[allergen]) != 1 and al in list(allerIng[allergen]):
                    index = list(allerIng[allergen]).index(al)
                    allerIng[allergen].pop(index)

        
        if count == len(allergenList):
            order = False
        
            
    dangerous = ''
    # occorre ripulire l'output da [] e ,
    for val in allergenList:
        dangerous = dangerous + str(allerIng[val]).strip() + ',' 
        
    print(dangerous)
    
    #ciclo sugli ingredienti e aggiungo a count le instanze di quelli non validi
    
    count = 0
    for food in range(0, len(shareAllergen)):
        for ingredient in shareAllergen[food][1]:
            if ingredient not in possibleVal:
                count += 1
    
    print(count)
    
if __name__ == "__main__":
    main()