def main():
    with open('input_days/day12.txt', 'r') as input:
        paList = [line.strip() for line in input]
    
    day12_1(paList)
    day12_2(paList)
    
def day12_1(paList):
    move = {'x': 0, 'y': 0}
    face = 'E'
    for command in paList:
        action = command[0]
        value = int(command[1:])
        if action == 'N':
            move['y'] += value
        if action == 'S':
            move['y'] -= value
        if action == 'E':
            move['x'] += value
        if action == 'W':
            move['x'] -= value        
        if action == 'R':
            face = rotateR(face, value)
        if action == 'L':
            face = rotateL(face, value)
        
        if action == 'F':
            if face == 'S':
                move['y'] -= value            
            if face == 'W':
                move['x'] -= value  
            if face == 'N':
                move['y'] += value            
            if face == 'E':
                move['x'] += value  
                
    print(abs(move['x'])+abs(move['y']))
    
def day12_2(paList):
    waypoint = {'x': 10, 'y': 1}
    ship = {'x': 0, 'y': 0}
    degree = 0
    face = 'E'
    for command in paList:
        action = command[0]
        value = int(command[1:])
        if action == 'N':
            waypoint['y'] += value
        if action == 'S':
            waypoint['y'] -= value
        if action == 'E':
            waypoint['x'] += value
        if action == 'W':
            waypoint['x'] -= value        
        if action == 'R':
            face = rotateR(face, value)                       
        if action == 'L':
            face = rotateL(face, value)
        
        if action == 'F':
            if face == 'N':
                #print(face)
                #print(value)
                #print(ship)
                #print(waypoint)
                ship['x'] += -waypoint['y'] * value 
                ship['y'] += waypoint['x'] * value   
                #print(ship)
            if face == 'E':
                #print(face)
                #print(value)
                #print(ship)
                #print(waypoint)
                ship['x'] += waypoint['x'] * value 
                ship['y'] += waypoint['y'] * value 
                #print(ship)
            if face == 'S':
                #print(face)
                #print(value)
                #print(ship)
                #print(waypoint)
                ship['x'] += waypoint['y'] * value 
                ship['y'] += -waypoint['x'] * value
                #print(ship)
            if face == 'W':
                #print(face)
                #print(value)
                #print(ship)
                #print(waypoint)
                ship['x'] += -waypoint['x'] * value   
                ship['y'] += -waypoint['y'] * value 
                #print(ship)
            
    print(ship)            
    print(abs(ship['x'])+abs(ship['y']))   
        
def rotateL(face, value):
    if face == 'N':
        if value == 90:
            face = 'W'
        if value == 180:
            face = 'S'
        if value == 270:
            face = 'E'
    elif face == 'E':
        if value == 90:
            face = 'N'
        if value == 180:
            face = 'W'
        if value == 270:
            face = 'S'
    elif face == 'S':
        if value == 90:
            face = 'E'
        if value == 180:
            face = 'N'
        if value == 270:
            face = 'W'
    elif face == 'W':
        if value == 90:
            face = 'S'
        if value == 180:
            face = 'E'
        if value == 270:
            face = 'N'

    return face

def rotateR(face, value):
    if face == 'N':
        if value == 90:
            face = 'E'
        if value == 180:
            face = 'S'
        if value == 270:
            face = 'W'
    elif face == 'E':
        if value == 90:
            face = 'S'
        if value == 180:
            face = 'W'
        if value == 270:
            face = 'N'
    elif face == 'S':
        if value == 90:
            face = 'W'
        if value == 180:
            face = 'N'
        if value == 270:
            face = 'E'
    elif face == 'W':
        if value == 90:
            face = 'N'
        if value == 180:
            face = 'E'
        if value == 270:
            face = 'S'

    return face
    
if __name__ == "__main__":
    main()