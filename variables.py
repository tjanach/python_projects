exVar  =100
print(exVar)
exVar  ='100'
print(exVar)
exVar  ="100"
print(exVar)
exVar  =1.45
print(exVar)
opVar = exVar / 2.5
print(opVar)

# global and local variables
x =6
def example1():
    z = 10
    print(x, z)

example1()
# we cannot do this a z is local variable
# print(z)


def example2():
    z = 10
    print(x, z)
    # we canot change the global variable x inside a function
    # x+=1
    # print(x)
    # but we can do this
    y = x +1
    print(y)
    return y

example2()
x = example2()
print(x)

# not recommended way of changing global variables
def example3():
    global x
    x+=5
    print(x)

example3()
print(x)

