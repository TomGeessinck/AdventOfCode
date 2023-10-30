f = open("2022/input/day1.txt", "r")
X = [l.strip() for l in f]

elves = []
q = 0
for line in X:
    if line == '':
        elves.append(q)
        q = 0
    else:
        q += int(line)
        
elves.sort(reverse=True)
print('Highest calorie: ' + str(elves[0]))

top3 = 0
for x in range(3):
    top3 += elves[x]
    
print('Top 3: ' + str(top3))