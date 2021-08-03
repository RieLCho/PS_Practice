def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    # n! = n * (n-1)
    return n * factorial_recursive(n-1)

print('Iterative: ', factorial_iterative(5))
print('Recursive: ', factorial_recursive(5))

