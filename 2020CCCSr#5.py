n = input()
l = list(map(int, input().split()))

dp = [0] * len(l)
li = [0] * len(l)
coach = l[0]
Josh = l[-1]

if coach == Josh:
    print(1)
else :
    for i in range(len(l) - 1, -1, -1):
        if l[i] == coach:
            dp[i] = 1
        elif l[i] == Josh:
            dp[i] = 0
        elif li[l[i]] != 0:
            dp[i] = dp[li[l[i]]]
        else:
            dp[i] = (1/(len(l) - i)) * (1 + sum(dp[i:]))
            li[l[i]] = i
    print(sum(dp)/len(l))
