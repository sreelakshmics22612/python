a=238
print(ord('a'))
print(bin(a))
print(hex(a))
"""give input in octual number system convert given number into binary,decimal,hexdecimal"""
n=int(input("enter sample input:"))
a=bin(n)
b=hex(n)
print("sample output")
print("binary",a[2:])
print("decimal:",ord('n'))
print("hexadecimal:",b[2:])


 
s=input()
num=int(s)
de=int(s,8)
bi=bin(de)
he=hex(de)
print("binary",bi[2:])
print("decimal:",de)
print("hexadecimal:",he[2:])
