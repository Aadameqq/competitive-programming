from bisect import bisect, bisect_left


arr = [0 for _ in range(10000)]

curr = 1

while curr**3 < 1000000000000:
    arr[curr-1] = curr**3
    curr+=1


t = int(input())

for _ in range(t):
    x = int(input())
    found = bisect_left(arr,x)-1

    good = False

    while found>=0:
        
        if arr[bisect(arr,x-arr[found])-1] == x-arr[found]:
            good = True
            break
        else:
            found-=1

    print("YES" if good else "NO","\n")  

 

    

