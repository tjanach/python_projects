
try:
    print("running the try ...")
    print('5'+5)

# except Exception as e:
#     print(str(e))
#     print("do more things in the except block")
except TypeError as t:
    print('TypeError:',str(t))
    print("do more things in the except block")

print("the code continue onward ...")


try:
    print("running the try with name or type error ...")
    # we do not have such a module
    import mars
    print('5'+x)

except TypeError as t:
    print('TypeError:',str(t))
    print("do more things in the except block of typeError")
except NameError as n:
    print('NameError:',str(n))
    print("do more things in the except block of NameError")
except Exception as e:
    print('General exception:',str(e))
    print("do more things in the except block of General exception")
