n = int(input())
for i in range(n):
    num_original = int(input())
    num = num_original
    print(num)
    while num > 11 and ((num - (num % 10)) > 11) and (len(str(num)) >= 3):
        leftover = num % 10
        num //= 10
        num -= leftover
        print(num)
    if num == 11:
        print("The number " + str(num_original) + " is divisible by 11.")
    else:
        print("The number " + str(num_original) + " is not divisible by 11.")
    print()