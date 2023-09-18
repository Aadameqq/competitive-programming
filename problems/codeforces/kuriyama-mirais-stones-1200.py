n = int(input())

stones = list(map(int, input().split()))
sortedStones = list(stones)
sortedStones.sort()

m = int(input())

stonesPrefix = [0 for _ in range(n + 2)]
sortedStonesPrefix = [0 for _ in range(n + 2)]

for i in range(n + 1):
    if i != 0:
        stonesPrefix[i] = stonesPrefix[i - 1] + stones[i - 1]
        sortedStonesPrefix[i] = sortedStonesPrefix[i - 1] + sortedStones[i - 1]

for i in range(m):
    option, x, y = list(map(int, input().split()))

    if option == 1:
        print(stonesPrefix[y] - stonesPrefix[x - 1])
    elif option == 2:
        print(sortedStonesPrefix[y] - sortedStonesPrefix[x - 1])
