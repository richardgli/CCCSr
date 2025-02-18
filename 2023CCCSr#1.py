'''
15 points
'''

C = int(input())

grid = []
tileState = [[3] * C for _ in range(2)]

for i in range(2):
    line = list(map(int, input().split()))
    grid.append(line)

tiles = 0

for i in range(2):
    for j in range(C):
        if grid[i][j] == 0:
            tileState[i][j] = 0
        elif grid[i][j] == 1:

            if i == 1 and grid[i - 1][j] == 1 and j % 2 == 0:
                tileState[i][j] -= 1
            
            if i == 0 and grid[i + 1][j] == 1 and j % 2 == 0:
                tileState[i][j] -= 1

            if j - 1 >= 0 and grid[i][j - 1] == 1:
                tileState[i][j] -= 1
            
            if j + 1 < C and grid[i][j + 1] == 1:
                tileState[i][j] -= 1

tileSum = 0
for i in range(2):
    tileSum += sum(tileState[i])
print(tileSum)
