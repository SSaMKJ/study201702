import math

firstNum = 5
secondNum = 3

# // 이면 정수로 나누기, /이면 실수로 나누기.
print(firstNum // secondNum)
# ==> 1
print(firstNum / secondNum)
# ==> 1.66666...


# 바이트 자리수.
print(firstNum.__sizeof__())
# => 28
print(math.trunc(5.9))
# ==>5

def asIntegerRatio():
    try:
        print(secondNum.as_integer_ratio())
    except:
        print("에러가 발생한다. as_integer_ratio는 float에서만 사용할 수 있다.")
        pass




asIntegerRatio()


def isInteger():
    try:
        print(secondNum.is_integer())
    except:
        print("secondNum 은 실수가 아니기 때문에 에러가 발생한다.")
        pass

    print(3..is_integer()) # true
    print(3.6.is_integer()) # false


isInteger()