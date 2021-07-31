from sys import stdin, stdout
from collections import deque

n = int(stdin.readline())
deck = deque()
for i in range(n):
    deck.append(i+1)
while len(deck) > 1:
    deck.popleft()
    deck.append(deck.popleft())
stdout.write(str(deck[0]))
