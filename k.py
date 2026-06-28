n=int(input())
arr=list(map(int,input().split()))

arr=sorted(set(arr))

if len(arr) <2:
    print("no second largest")
else:
    print(arr[-2])
