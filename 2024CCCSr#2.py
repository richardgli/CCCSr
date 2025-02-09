# 15 points
from collections import Counter

T, N = map(int, input().split())
res = []
last = 0

for i in range(T):
    alternate = True

    string = input()
    cL = Counter(string)

    for j in range(N):
        if j == 0 and cL[string[j]] == 1:
            last = 0
        elif j == 0 and cL[string[j]] > 1:
            last = 1
        elif cL[string[j]] > 1 and last == 0:
            last = 1
        elif cL[string[j]] == 1 and last == 1:
            last = 0
        else:
            alternate = False

    if alternate:
        res.append("T")
    else:
        res.append("F")

for i in range(len(res)):
    print(res[i])


