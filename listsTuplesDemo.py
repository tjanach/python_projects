# tuple example
def exampleFunc():
    return 10,22

a,b = exampleFunc()
print(a, b)

x,y,z,f = 1,'ssss',5,8

print(y,x,z,f)

# in python there is no arrays
# example list

x = [1,4,5,6,2,4,6,7,9,8,0]
print(x)
print(x[5])
x.append(12)
print(x)
x.insert(4,33)
print(x)
# removes only the first occurrence of 5
x.remove(5)
print(x)
# provide an index of the element
print(x.index(12))
# provide the number of occurrences
print(x.count(4))
x.sort()
print(x)
x.reverse()
print(x)

x = ['ala','zela','cela','pela']
x.sort()
print(x)
x.reverse()
print(x)
