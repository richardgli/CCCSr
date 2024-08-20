numLines = int(input())
l = []
max = -1

for i in range(numLines):
    obs = list(map(int, input().split()))
    time = obs[0]
    pos = obs[1]
    l.append([time, pos])

l = sorted(l)
for i in range(len(l) - 1):
    speed = abs((l[i + 1][1] - l[i][1])/(l[i + 1][0] - l[i][0]))
    if speed > max:
        max = speed

print(max)
