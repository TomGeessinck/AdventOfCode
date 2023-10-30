f = open("2022/input/day2.txt", "r")
lines = f.readlines()

totalpoints = 0
for line in lines:
    line = line.strip()
    points = 0
    me = line.split()[1]
    
    if me == 'X': # Rock AX
        points += 1
    elif me == 'Y': # Paper BY
        points += 2
    elif me == 'Z': # Scissors CZ
        points += 3
        
    # Draw
    if line == 'A X':
        points += 3
    elif line == 'B Y':
        points += 3
    elif line == 'C Z':
        points += 3
    # WIN
    elif line == 'A Y':
        points += 6
    elif line == 'B Z':
        points += 6
    elif line == 'C X':
        points += 6
    totalpoints += points
    
print(totalpoints)

# P2
# X = Lose
# Y = draw
# Z = Win
totalpoints = 0
for line in lines:
    line = line.strip()
    points = 0
    
    target = line.split()[1]
    you = line.split()[0]
    
    if target == 'X':
        points += 0
        if you == 'A':
            points += 3
        elif you == 'B':
            points += 1
        elif you == 'C':
            points += 2
    elif target == 'Y':
        points += 3
        if you == 'A':
            points += 1
        elif you == 'B':
            points += 2
        elif you == 'C':
            points += 3
    elif target == 'Z':
        points += 6
        if you == 'A':
            points += 2
        elif you == 'B':
            points += 3
        elif you == 'C':
            points += 1
    totalpoints += points
    
print(totalpoints)