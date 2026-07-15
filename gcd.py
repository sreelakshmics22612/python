x,y=map(int,input().split())
i=min(x,y)
l=[]
for i in range(1,i+1):
    if x%i==0 and y%i==0:
        l.append(i)
print(l[-1])
