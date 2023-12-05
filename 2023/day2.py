f = open("2023/input/day2.txt", "r")
lines = [l.strip() for l in f]

count = 0
total = 0
for line in lines:
    count += 1
    
    line = line.split(': ')[1]
    line = line.split(';')
    valid = True
    
    for set in line:
        set = set.split(',')
        for cube in set:
            cube = cube.strip()
            if 'blue' in cube:
                if int(cube.split(' ')[0]) > 14:
                    valid = False
                
            if 'red' in cube:
                if int(cube.split(' ')[0]) > 12:
                    valid = False
                
            if 'green' in cube:
                if int(cube.split(' ')[0]) > 13:
                    valid = False
    if valid:
        total += count
      
print('1: ' + str(total))

count = 0
total = 0
for line in lines:
    count += 1
    blue = 0
    red = 0
    green = 0
    
    line = line.split(': ')[1]
    line = line.split(';')
    valid = True
    
    for set in line:
        set = set.split(',')
        for cube in set:
            cube = cube.strip()
            if 'blue' in cube:
                if int(cube.split(' ')[0]) > blue:
                    blue = int(cube.split(' ')[0])
                
            if 'red' in cube:
                if int(cube.split(' ')[0]) > red:
                    red = int(cube.split(' ')[0])
                
            if 'green' in cube:
                if int(cube.split(' ')[0]) > green:
                    green = int(cube.split(' ')[0])
                    
    sum = blue * green * red
    total = total + sum
      
print('2: ' + str(total))
