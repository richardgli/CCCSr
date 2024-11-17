# 10 points

m = int(input())
n = int(input())
k = int(input())
Rvisited = []
Cvisited = []
visited = []
c = 0
r = 0
gold = 0

# Finding duplicates
for i in range(k):
    line = list(input().split())
    brush = line[0] + line[1]

    if brush in visited:
        if line[0] == "R":
            r -= 1
        else:
            c -= 1
        visited.remove(brush)
    else:
        if line[0] == "R":
            r += 1
        else:
            c += 1    
        visited.append(brush)       

gold = n * r + m * c - 2 * r * c
print(gold)
