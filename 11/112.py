def is_1(x):
    return str(x)==str(x)[::-1]
#test
print(is_1(1234))
print(is_1('abccc'))
print(is_1('abcccba'))