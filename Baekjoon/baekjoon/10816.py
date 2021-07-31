from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashTable = {}
for n in N:
    if n in hashTable:
        hashTable[n] += 1
    else:
        hashTable[n] = 1

print(' '.join(str(hashTable[m]) if m in hashTable else '0' for m in M))