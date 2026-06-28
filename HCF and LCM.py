a=int(input())
b=int(input())
x=a
y=b
while b !=0:
    a,b=b,a%b
gcd =a
lcm=(x*y)//gcd
print("hcf:",gcd)
print("lcm:",lcm)
