
def add(x,y,z):
    answer = x+y+z
    return answer

res = add(10, 5, 12)
print(res)

def addAndSubract(x, y, z):
    answer = x+y-z
    return answer

res = addAndSubract(10, 5, 12)
print(res)
res = addAndSubract(z=12, y=5, x=10)
print(res)

def funcA(x=6, name="Joan", size=4):
    print('x is',x)
    print('name is',name)
    print('size is',size)

funcA()
funcA(name='Anna', x=1, size=44)
