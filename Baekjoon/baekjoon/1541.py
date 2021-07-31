input_string = input().split('-')
list_numbers = []
for i in input_string:
    sum_value = 0
    input_split = i.split('+')
    for j in input_split:
        sum_value += int(j)
    list_numbers.append(sum_value)

result = list_numbers[0]
for i in range(1, len(list_numbers)):
    result -= list_numbers[i]

print(result)

