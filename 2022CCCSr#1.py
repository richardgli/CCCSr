#15 points

n = int(input())
multipleFour = 0
numFours = 0

if n < 4:
    numSums = 0
else:
    for i in range(n):
        multipleFour += 4
        dif = n - multipleFour
        if dif < 4 and dif >= 0:
            numFours = i + 1
            break

    dif = n - multipleFour
    if dif > numFours:
        numSums = 0
    else:
        numFours = numFours - dif
        numSums = 1
        for i in range(n):
            if numFours > 4:
                numFours -= 5
                numSums += 1
            else:
                break
print(numSums)
