"""Given a number N, your task is to calculate and print the sum of the table of N.
Sample test case 1:
Input:
N = 10
ouput: 55 * 10 = 550
550
Sample test case 2:
Input:
N = 68 N * (1-10) -> 55 * 68 = 3740
ouput:
3740"""
n=int(input())
s=0
for i in range(1,n+1):
    s+=i
print(s*n)
