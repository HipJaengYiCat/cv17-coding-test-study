def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

a, b = map(int,input().split())
c = gcd(a,b)
print('1'*c)