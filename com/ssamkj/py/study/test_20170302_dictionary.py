
helloWorld = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'에프'}


for k in helloWorld:
    print('{}-{}'.format(k, helloWorld[k]))

print('delimiters')


def printKeyValue():
    global k
    for k, v in helloWorld.items():
        print("{} - {}".format(k, v))


printKeyValue()

print('update')
helloWorld.update({'c':'씨'})

printKeyValue()


tuple1= ('m1', ',2', 'm3')

print(tuple1)


def tupleTest11():
    return 1, 'm2', 'k2'




print(tupleTest11())

t1, t2, t3 = tupleTest11()
print(t1)
print(t2)

digits = [0,1,2,3,4,5,6,7,8,9]
digit_set = set(digits)

print(9 in digit_set)

odd = {1,3,5,7,9}
prime = set([2,3,5,7])
even = digit_set - odd   # 차집합
print(even)

print(prime & even) # 교집합

print(odd | even)   # 합집합
print(prime ^ even) # 여집합

