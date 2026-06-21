n= int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
m=arr[0]
count=0
for i in range(1,n):
    if arr[i] > m:
        count += 1
print(count)
