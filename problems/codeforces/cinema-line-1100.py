n = int(input())

money = [0,0,0]
moneyValues = (25,50,100)

arr = list(map(lambda x: int(x),input().split()))

good = True

for i in range(n):
    x = arr[i]
    change = x - 25

    curr = 2

    while change != 0:
        if money[curr] == 0 or moneyValues[curr] > change:
            curr-=1
            if curr < 0:
                break
        else:
            change -= moneyValues[curr]
            money[curr]-=1
    if change != 0:
        good=False
        break
    else: 
        money[moneyValues.index(x)] += 1

print("YES" if good else "NO")   
    