""" * Given two integers, a and b, your task is to determine the sum of the cubes of
all numbers in the range from a to b.
sample test case
a = 4
b = 9
ouput: 1989"""
x,y=map(int,input().split())
a=min(x,y)
b=max(x,y)
sum=0
j=1
for i in range(a,b+1):
    j=i*i*i
    sum+=j
    j=1
print(sum)
