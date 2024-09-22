from collections import Counter

s = input()
ls = len(s)

c = Counter(s)
numA = c["A"]
numB = c["B"]
numC = c["C"]

cAS = Counter(s[:numA])
cBS = Counter(s[numA:numA + numB])
cCS = Counter(s[numA:numA + numC])
minSwaps = float('inf')

s = s + s

for i in range(ls):        

    nonA = cAS["B"] + cAS["C"]
    nonB = cBS["A"] + cBS["C"]
    nonC = cCS["A"] + cCS["B"]
    numSwapsABC = nonA + nonB - (min(cBS["A"], cAS["B"]))
    numSwapsACB = nonA + nonC - (min(cCS["A"], cAS["C"]))
        
    minSwaps = min(minSwaps, numSwapsABC, numSwapsACB)

    cAS[s[i]] -= 1
    cAS[s[numA + i]] += 1
    cBS[s[numA + i]] -= 1
    cBS[s[numA + numB + i]] += 1

    cCS[s[numA + i]] -= 1
    cCS[s[numA + numC + i]] += 1

print(minSwaps)
