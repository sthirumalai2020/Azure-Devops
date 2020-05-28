from index import add,mul,concat,div,minarr
def func(a,b):
    return (a+b)

def func_mul(a,b):
    return (a*b)

def func_concat(a,b):
    return a+b

def func_div(a,b):
    if b > 0:
        return a/b
    return a

def func_minarr(arr):
    return min(arr)

def test_method1():
    assert func(10,20) == add(10,20)

def test_method2():
    assert func_mul(3,2)== mul(3,2)

def test_method3():
    assert func_concat("Str1","Str2")== concat("Str1","Str2")

def test_method4():
    assert func_div(3,2)== div(3,2)

def test_method5():
    assert func_minarr([0,1])== minarr([0,1])

