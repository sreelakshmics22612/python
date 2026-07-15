x, y = map(int, input().split())

i = max(x, y)

while True:
    if i % x == 0 and i % y == 0:
        print(f"LCM {i}")
        break
    i += 1
