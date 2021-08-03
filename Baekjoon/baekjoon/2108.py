from math import ceil
from collections import Counter

varArithmeticMean = 0  # 산술평균
varMedian = 0          # 중앙값
varMode = 0            # 최빈값
varRange = 0           # 범위

# 데이터 입력받기
n = int(input())
listInput = []
for _ in range(n):
    listInput.append(int(input()))


# 산술평균 구하기 (소수점 이하 첫째 자리에서 반올림)
for i in range(len(listInput)):
    varArithmeticMean += listInput[i]
varArithmeticMean = int(round((varArithmeticMean / len(listInput)), 0))

# 중앙값 구하기
listInput.sort()
varMedian = listInput[len(listInput)//2]

# 최빈값 구하기
counter = Counter(listInput)
counter = counter.most_common()
if len(listInput) > 1:
    if counter[0][1] == counter[1][1]:
        varMode = counter[1][0]
    else:
        varMode = counter[0][0]
else:
    varMode = counter[0][0]

# 범위 구하기
varRange = max(listInput) - min(listInput)


print(varArithmeticMean)
print(varMedian)
print(varMode)
print(varRange)