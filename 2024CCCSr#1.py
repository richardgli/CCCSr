# 15 points
N = int(input())

people = []
num = 0
for i in range(N):
    person = int(input())
    people.append(person)
for i in range(int(N / 2)):
    if people[i] == people[int(N / 2) + i]:
        num += 2
print(num)
