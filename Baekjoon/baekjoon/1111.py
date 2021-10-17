n = int(input())
inputs = list(map(int, input().split()))
if n == 1:
    print("A")
elif n == 2:
    if inputs[0] == inputs[1]:
        print(inputs[0])
    else:
        print("A")
else:
    if inputs[0] - inputs[1] == 0:
        a = 0
    else:
        a = (inputs[1] - inputs[2]) // (inputs[0] - inputs[1])
    b = inputs[1] - inputs[0] * a
    for i in range(n - 1):
        expect = inputs[i] * a + b
        if inputs[i + 1] != expect:
            print("B")
            exit()

    print(inputs[-1] * a + b)