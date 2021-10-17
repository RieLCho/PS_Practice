import sys
from collections import defaultdict


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


word_dict = nested_dict(2, int)

N = int(sys.stdin.readline())
for _ in range(0, N):
    word = sys.stdin.readline().rstrip()
    if len(word) > 1:
        first_key = word[0] + word[-1]
    else:
        first_key = word[0]
    if len(word) > 2:
        second_key = ''.join(sorted(word[1:-1]))
    else:
        second_key = ''
    word_dict[first_key][second_key] += 1

M = int(sys.stdin.readline())
for _ in range(0, M):
    decode_sentence = sys.stdin.readline().rstrip().split()
    answer_list = []
    answer = 1
    for word in decode_sentence:
        if len(word) > 1:
            first_key = word[0] + word[-1]
        else:
            first_key = word[0]
        if len(word) > 2:
            second_key = ''.join(sorted(word[1:-1]))
        else:
            second_key = ''
        answer_list.append(word_dict[first_key][second_key])
    for num in answer_list:
        answer *= num
    print(answer)

if N == 0 and M == 0:
    print("0")
