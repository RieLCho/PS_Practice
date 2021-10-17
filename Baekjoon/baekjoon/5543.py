burger = [0 for i in range(3)]
nomimono = [0 for i in range(2)]
burger[0] = int(input())
burger[1] = int(input())
burger[2] = int(input())
nomimono[0] = int(input())
nomimono[1] = int(input())

result = 10**9

for i in range(3):
    for j in range(2):
        temp = burger[i] + nomimono[j] - 50
        result = min(result, temp)

print(result)
