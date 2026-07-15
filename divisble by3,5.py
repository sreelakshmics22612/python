"""find the number that are divisble by both 3 and 5 between the range 1 to 100"""
arr=[]
for i in range(1,100):
    if i%3==0 and i%5==0:
       print(i)
