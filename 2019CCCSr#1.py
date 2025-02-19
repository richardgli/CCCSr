'''
15 points
'''

from collections import Counter

flips = input()

cF = Counter(flips)
grid = [[1, 2], [3, 4]]

if cF["H"] % 2 == 1:
    row = grid.pop(0)
    grid.append(row)

if cF["V"] % 2 == 1:
    num1 = grid[0].pop(0)
    grid[0].append(num1)

    num2 = grid[1].pop(0)
    grid[1].append(num2)

print(" ".join(map(str, grid[0])))
print(" ".join(map(str, grid[1])))
