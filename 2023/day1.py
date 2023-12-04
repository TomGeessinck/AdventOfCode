f = open("2023/input/day1.txt", "r")
lines = [l.strip() for l in f]

import re

allNumbers = []
for line in lines:
    numbers = re.findall("([0-9])", line)
    number = str(numbers[0]) + str(numbers[len(numbers) - 1])
    allNumbers.append(number)

total = 0
for number in allNumbers:
    total = total + int(number)
    
print('1: ' + str(total))

######################################################## PART 2 ########################################################

arrayText = ['one','two','three','four','five','six','seven','eight','nine']
arrayNumber = [1,2,3,4,5,6,7,8,9]

allNumbers = []
for line in lines:
    lineArray = {}
    count = 0
    for numberText in arrayText:
        count += 1
        if line.find(numberText) != -1:
            for item in re.finditer(numberText, line):
                lineArray[int(item.start())] = count
    count = 0
    for numberText in arrayNumber:
        count += 1
        if line.find(str(numberText)) != -1:
            for item in re.finditer(str(numberText), line):
                lineArray[int(item.start())] = count
    minPlace = 999
    maxPlace = 0
    minNum = 0
    maxNum = -1
    for key in lineArray:
        if int(key) < minPlace:
            minPlace = key
            minNum = lineArray[key]
            
        if int(key) > maxPlace:
            maxPlace = key
            maxNum = lineArray[key]
    if maxNum == -1:
        maxNum = minNum
    number = str(minNum) + str(maxNum)
    allNumbers.append(number)


total = 0
for number in allNumbers:
    total = total + int(number)

print('2: ' + str(total))
