class test:
    pass

test.x = 45

test.foo = lambda self: print('hello')

myobj = test()

print(myobj.x)

myobj.foo()