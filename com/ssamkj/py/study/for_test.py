import time

a = [1,2,3,4]

def test1():
    result = []
    for num in a:
        result.append(num*3)
    print(result)

def test2():
    result = [num *3 for num in a]
    print(result)

def test3():
    result = [num *3 for num in a if num%2 == 0]
    print(result)

test3()

def test4():
    result = [ x*y for x in range(2, 10)
                        for y in range(1, 10)]
    print(result)

test4()


now = time.time()
print()
ii=0
ii+=1
print(ii)


def helloworld(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

helloworld(arg3='1', arg1='2', arg2='3')