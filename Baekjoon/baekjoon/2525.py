시각, 분 = map(int, input().split())
조리시간 = int(input())

sum = 시각*60 + 분 + 조리시간
if sum//60 >= 24:
    시각 = sum//60 - 24
else:
    시각 = sum//60
분 = sum % 60
print(시각, 분)