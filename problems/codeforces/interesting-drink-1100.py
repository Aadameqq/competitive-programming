from bisect import bisect

n = int(input())

prices = list(map(int, input().split()))

prices.sort()

q = int(input())

for _ in range(q):
    x = int(input())
    index = bisect(prices, x)
    print(index, '\n')
