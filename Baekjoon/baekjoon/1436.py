n = int(input())
adder = 0
counter = 0
while True:
    adder += 1
    if "666" in str(adder):
        counter += 1
        if counter == n:
            print(adder)
            break