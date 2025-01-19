n, m, k = map(int, input().split())

def findPiece(n, m, k):
    piece = [1]
    goodSamples = 1
    for i in range(n - 1):
        samplesLeft = k - goodSamples
        notesLeft = n - len(piece)
        if samplesLeft - notesLeft + 1 < m and samplesLeft - notesLeft + 1 > 0:
            note = piece[i - (samplesLeft - notesLeft)]
            piece.append(note)
            goodSamples += samplesLeft - notesLeft + 1
        else:
            note = piece[i] + 1
            if note > m:
                piece.append(1)
                goodSamples += m
            else:
                piece.append(note)
                if len(piece) > m:
                    goodSamples += m
                else:
                    goodSamples += note
    if goodSamples != k:
        return -1
    return piece

res = findPiece(n, m, k)
if res == -1:
    print(res)
else:
    for i in range(len(res)):
        print(res[i], end=" ")
