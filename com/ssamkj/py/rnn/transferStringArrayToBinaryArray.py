
class TransferStringArrayToBinaryArray:


    def __init__(self, maxStringLength = 100, maxBinaryLength=17):
        self.__MAX_STRING_LENGTH = maxStringLength
        self.__MAX_BINARY_LENGTH = maxBinaryLength

    """
    문자가 들어오면 2진수로 만들어 준다.
    __MAX_BINARY_LENGTH 길이 만큼 만들어 준다.
    """
    def __toBinary__(self, str=None):
        if (str == None):
            return ['0' for no_meaning in range(self.__MAX_BINARY_LENGTH)]
        return list("{0:b}".format(ord(str)).zfill(self.__MAX_BINARY_LENGTH))

    """
    문자열이 들어오면 문자열을 2진수로 이루어진 배열로 만들어 준다.
    """
    def __toBinaryArr__(self, str=None):
        array = []
        for i in range(self.__MAX_STRING_LENGTH):
            l = i < len(str) and str[i] or None
            array.append(self.__toBinary__(l))
        return array

    """
    문자열 배열을 받아서 2진수 배열로 만들어 준다.
    """
    def transfer(self, list):
        outBinaryArray = []
        for l in list:
            outBinaryArray.append(self.__toBinaryArr__(l))
        return outBinaryArray
