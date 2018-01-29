x=2
y=7
z=10

if (x<y or x>0) and x+2<y:
    print(x,'is less than',y)

if z > y > x:
    print(z,'>',y,'>',x)

if x>y:
    print(x,'is greater than',y)
else:
    print(x, 'is not greater than',y)

x=7
if x>y:
    print(x,'is greater than',y)
elif x<y:
    print(x, 'is less than',y)
else:
    print(x, 'is equal to',y)
