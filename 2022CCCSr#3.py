#15 points
n, m, k = map(int, input().split())

piece = []
goodSamples = 0

for i in range(n):
    samplesLeft = k - goodSamples
    notesLeft = n - i - 1

    value = min(samplesLeft - notesLeft, m)

    if value <= 0:
        break
    elif value > i:
        note = min(m, i + 1)
        value = note
    else:
        note = piece[i - value]
    
    piece.append(note)
    goodSamples += value

if goodSamples == k and len(piece) == n:
    print(" ".join(map(str, piece)))
else:
    print(-1)
