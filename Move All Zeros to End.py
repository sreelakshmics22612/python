n=int(input())
arr=list(map(int,input().split()))
j=0
for i in range(n):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1
while j < n:
    arr[j] = 0
    j += 1
print(*arr)
