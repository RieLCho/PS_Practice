n = int(input())
wordList = []
for i in range(n):
    temp = str(input())
    wordList.append((temp, len(temp)))

wordList = list(set(wordList))
wordList.sort(key=lambda w: (w[1], w[0]))
for i in wordList:
    print(i[0])