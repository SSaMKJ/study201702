
people = ['송경자', '김태양', '김태리']

people.append('동생')

print('Hello' in people)

startIndex = 1
for i, name in enumerate(people, startIndex):
    print('{} - {}'.format(i, name))


print(people[0])
print(people[-1])   # 뒤로 돌아가네.

print('print(people[1:2])')
print(people[1:2])
print(people[:1])
print(people[1:])

print("startAt:endBefore:skip 단위...")
print(people[::1])  # startAt=0 : endBefore=0 : skip=1 ==> ['송경자', '김태양', '김태리', '동생'] ???
print(people[0:3:3])

print(people[::2])
print(people[::3])
print(people[::4])

print('reverse')
print(people[::-1]) # reverse 거꾸로~~

x = range(100)


def printCollon(r):
    for i in r:
        print(i, end=', ')


printCollon(x[::2])
print()
printCollon(x[::3])
print()
printCollon(x[10:40:6])
print()

print(people+['막내1'])    # return value가 있다.
print(people.extend(['막내2']))    # return value가 없다.
print(people)

print(people.append(['막내3']))   # append 하면 리스트의 리스트로 들어간다.
print(people)