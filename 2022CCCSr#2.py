#15 points
from collections import defaultdict

x = int(input())
mustPair = defaultdict(list)
for i in range(x):
    line = input().split()
    mustPair[line[0]].append(line[1])

y = int(input())
cannotPair = defaultdict(list)
for i in range(y):
    line = input().split()
    cannotPair[line[0]].append(line[1])

g = int(input())
violations = 0
for i in range(g):
    line = input().split()
    for j in range(3):
        violated = 0
        if line[j] in mustPair:
            for k in range(3):
                if line[k] in mustPair[line[j]]:
                    violated += 1
            violations += len(mustPair[line[j]]) - violated
        if line[j] in cannotPair:
            for k in range(3):
                if line[k] in cannotPair[line[j]]:
                    violations += 1

print(violations)

