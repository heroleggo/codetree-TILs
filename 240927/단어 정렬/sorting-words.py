n = int(input())

wordList = []

for i in range(n):
    wordList.append(input())

wordList.sort()

print('\n'.join(wordList))