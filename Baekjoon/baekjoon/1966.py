t = int(input())
target = 0

for i in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    importance = list(0 for i in range(len(queue)))
    importance[m] = 1

    order = 0
    while True:
        if queue[0] == max(queue):
            order += 1
            if importance[0] == 1:
                print(order)
                break
            else:
                importance.pop(0)
                queue.pop(0)
        else:
            importance.append(importance.pop(0))
            queue.append(queue.pop(0))

