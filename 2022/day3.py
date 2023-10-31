f = open("2022/input/day3.txt", "r")
lines = f.readlines()

duplicateletterstotal = [];
for line in lines:
    line = line.strip()
    duplicateletters = [];
    length = len(line)
    half = int(length/2)
    # print(half)
    firsthalf = line[0:half]
    secondhalf = line[half:]
    firsthalf = [*firsthalf]
    firsthalf.sort();
    secondhalf = [*secondhalf]
    secondhalf.sort();
    for i1 in firsthalf:
        for i2 in secondhalf:
            if i1 == i2:
                if i1 not in duplicateletters:
                    duplicateletters.append(i1)
    duplicateletterstotal = duplicateletterstotal + duplicateletters
    

points = 0
for item in duplicateletterstotal:
    if item.isupper():
        points += 26 + ord(item.lower()) - 96
    else:
        points += ord(item.lower()) - 96
print(points)

first = ''
second = ''
third = ''
points = 0
for line in lines:
    line = line.strip()
    if first == '':
        first = line
    elif second == '':
        second = line
    elif third == '':
        third = line
        duplicateletter = ''
        first = [*first]
        second = [*second]
        third = [*third]
        for i1 in first:
            for i2 in second:
                for i3 in third:
                    if i1 == i2 == i3:
                        duplicateletter = i1
        
        if duplicateletter.isupper():
            points += 26 + ord(duplicateletter.lower()) - 96
        else:
            points += ord(duplicateletter.lower()) - 96
        first = ''
        second = ''
        third = ''
print(points)