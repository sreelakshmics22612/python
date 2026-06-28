n=int(input())
temp=n
digit=len(str(n))
s=0

while n >0:
    d=n%10
    s += d ** digit
    n //=10
if temp == s:
    print("armstrong")
else:
    print("not armstrong")
    
