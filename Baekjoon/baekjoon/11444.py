mod = 1000000007
def matrix_mul_self(x):
    base = [[1, 1], [1, 0]]
    result = [[1, 1], [1, 0]]
    for _ in range(x):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (base[i][k] * base[k][j]) % mod
        base = result
    return result
def matrix_mul(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j]) % mod
    return result
n = bin(int(input()))[2:]
result = [[1, 0], [0, 1]]
for i in range(len(n)):
    if n[-i - 1] == '1':
        result = matrix_mul(result, matrix_mul_self(i))
print(result[0][1] % mod)