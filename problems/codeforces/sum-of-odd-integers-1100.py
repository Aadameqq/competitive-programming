t = int(input())

for _ in range(t):
    x, y = list(map(int, input().split()))
    a = (y) ** 2

    b = x - a

    if b < 0 or b % 2 != 0:
        print("NO")
    else:
        print("YES")
