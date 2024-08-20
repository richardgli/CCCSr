m = int(input())
n = int(input())

d = {}
l = []
escapable = False

for i in range(m):
    coords = list(map(int, input().split()))
    for j in range(n):
        l.append([[i + 1, j + 1], coords[j]])
    d[i + 1] = l
    l = []

frontier = [[[1, 1], d[1][0][1]]]
visited = []

while frontier:
    cur = frontier.pop()
    for key, value in d.items():
        for i in range(len(value)):
            temp = [[value[i][0][0], value[i][0][1]], value[i][1]]
            if temp not in frontier and temp not in visited and (temp[0][0] * temp[0][1]) == cur[1]:
                frontier.append(temp)
                visited.append(temp)
                if temp[0] == [m, n]:
                    escapable = True
                    break

if escapable == True:
    print("yes")
else:
    print("no")
    
