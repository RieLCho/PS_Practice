treeNum, basketNum = map(int, input().split())
berries = list(map(int, input().split()))
m = max(berries)
mod = 0
result = 0
for i in range(1, m + 1):
    mod = i
    fullBasket = 0
    k = 0
    for j in range(treeNum):
        fullBasket = int(fullBasket + (berries[j] / mod))
    if fullBasket < (basketNum/2):
        break
    if fullBasket >= basketNum:
        result = max(result, i * (basketNum/2))
        continue
    cnt = i * (fullBasket - basketNum/2)
    berries.sort(key=lambda x: (x % mod), reverse=True)
    while k < basketNum - fullBasket:
        try:
            cnt += berries[k] % mod
            k += 1
        except IndexError:
            break
    result = max(result, cnt)
print(int(result))
