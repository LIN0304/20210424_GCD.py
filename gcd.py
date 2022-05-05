def gcd(x, y):
    if x > y:
        z = x % y
        while (z>0):
            x = y
            y = z
            z = x % y
        return y
    else:
        z = y % x
        while (z>0):
            y = x
            x = z
            z = y % x
        return x
x, y=map(int, input().split())
print(gcd(x, y)) 

