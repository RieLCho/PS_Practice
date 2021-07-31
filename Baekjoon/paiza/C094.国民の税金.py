def calculateTax(income):
    tmp = 0
    if income >= 1500001:
        tmp = int((income - 1500000)*0.4)
        result = 65000 + 150000 + tmp
    elif 750001 <= income <= 1500000:
        tmp = int((income - 750000)*0.2)
        result = 65000 + tmp
    elif 100001 <= income <= 750000:
        tmp = int((income - 100000)*0.1)
        result = tmp
    else:
        result = 0

    return result

n = int(input())
x = []
for i in range(n):
    temp = int(input())
    temp = calculateTax(temp)
    x.append(temp)

print(sum(x))



