
def condi1():
    print('condi1()')
    return 'return is condi1'

def condi2():
    print('condi2()')
    return None

def condi3():
    print('condi3()')
    return 'return is condi3'


def condi4():
    print('condi4()')
    return 'not None and False'

'''
target = value if not 조건 else 조건2
"조건"이 False or None 이면 value가 target에 들어간다.
'''
cond = condi1() if not condi2() else condi3()

print(cond)

print('--------------')

cond = condi1() if not condi4() else condi3()

print(cond)

print('--------------')

'''
"condi4()"이
False 나 None 인 경우 : condi3() 이 cond에 들어간다.
            아닌 경우 : condi1()

'''
cond = condi1() if condi4() else condi3()

print(cond)

print('--------------')