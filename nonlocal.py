# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

def myfunc1():
    x = "John"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1()) # hello

def myfunc1():
    x = "John"
    def myfunc2():
        x = "hello" # does not change the nonlocal x because it is only a local x
    myfunc2()
    return x

print(myfunc1()) # John
