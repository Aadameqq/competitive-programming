n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()
if k == 0 and arr[0] != 1:
    print(1, "\n")
elif (k < n and arr[k - 1] == arr[k]) or (k == 0 and arr[0] == 1):
    print(-1, "\n")
else:
    print(arr[k - 1], "\n")
