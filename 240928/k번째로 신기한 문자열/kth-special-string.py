n, k, t = input().split()

original = []

data = []

for i in range(int(n)):
    original.append(input())

for word in original:
    if t in word:
        data.append(word)

data.sort()

print(data[int(k) - 1])