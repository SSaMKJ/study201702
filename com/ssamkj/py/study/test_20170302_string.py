s = 'str'
s2 = 'str2'

print(s + s2)  # strstr2

# if문이다.
print(s in s2)  # true - 속해있는지 묻는거다.
print(s2 in s)  # false

for ssss in s2:
    print(ssss)
    # s
    # t
    # r
    # 2
# for 문이 붙으면 하나씩 꺼내는거다.

print(s >= s2)  # false
print(s2 > s)  # true


def stringFormatting1():
    try:
        formatting = '%s is String, %s is variable'
        print(formatting % (1, s, 'a'))
    except:
        print('argument 개수가 안 맞으니까 에러.')
        pass


stringFormatting1()

formatting = '%s is String, %s is variable'
formattedStr = formatting % (1, s)
print(formattedStr)

print(s * 3)  # strstrstr

print(repr(s2))  # toString 같은거다.

person = {'name': 'Paul',
          'instrument': 'Bass'}

inst = person['instrument']

print("Name : {}, plays:{}".format(person['name'], inst))

print("Name : {name} plays: {inst}".format(
    name=person['name'], inst='hello'
))

s3 = 'str3'
s4 = 'CamelExpress'

print(s3.capitalize()) # 첫글자만 대문자로.
print(s4.casefold())    # 전부 소문자로
print(s4.capitalize()) # 첫글자만 대문자로.

print("-----")
print(s4.center(10))
print(s4.center(100))
print(s4.center(len(s4)+2)) # 이거 왼쪽 패딩이네.
print(s4.center(len(s4)+5, '@')) # @@@CamelExpress@@ 길이를 늘리고, 양쪽을 묶는거구나.


def countStr(argString):
    print(argString.count('e', 0, len(argString)))
    print(argString.casefold().count('e', 0, len(argString)))   # 소문자로 변환했으므로 3개가 나온다.


countStr(s4)    # 소문자 e는 2개 밖에 없다.

print(s4.encode())

print("ddddddddd")
print(s4.endswith('a')) # if문이구만.


def expandTabs(s4):
    print(s4.expandtabs(tabsize=1) + '!')
    print(s4.expandtabs(tabsize=10) + '!')
    print(s4.expandtabs(tabsize=100) + '!')


expandTabs('aaa\tbb\tcc')

print(s4.isalnum())
print(s4.isalpha())

print('print(str(number).isalnum())')
number = 1.
print(str(number).isalnum())
print(str(number).isalpha())

print('print(s4.partition())')
print(s4.partition('E'))    # ('Camel', 'E', 'xpress')

partitionss = s4.partition('E')

print(partitionss[0])
print(partitionss[1])
print(partitionss[2])


print('print(s4.swapcase())')
print(s4.swapcase())
