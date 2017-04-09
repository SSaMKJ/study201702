
import re
from konlpy.tag import Twitter


class MakeDataFile():

    def __init__(self, x_data_path, y_data_path):
        self.x_data_path = x_data_path
        self.x_data_path_train = x_data_path+'.train'
        self.x_data_path_test = x_data_path+'.test'

        self.y_data_path = y_data_path
        self.y_data_path_to_char = y_data_path+'.char'
        self.y_data_path_train = y_data_path+'.train'
        self.y_data_path_test = y_data_path+'.test'
        self.twitter = Twitter()

        self.removeText=['기획구성','이마트','배송비무료','무료배송', '부터 순차발송', '과내외', '당일', '산지직송', '국내산', '미국산']

        self.notAllowedNoun = ['입', '포', '개', '예', '과', '내외', '개입', '기획', '택', '년산']

    def __removePunctuationPoint__(self, text):
        # 대괄호에 있는거 제거.
        # patName = re.compile('\[[a-zA-Zㄱ-힣0-9 -/*\(\)]{1,}\]')
        # # if CHAT_READ_TEST : print('ori 1 ',text)
        # text = patName.sub(' ', text)
        # # 대괄호에 있는거 제거.
        # patName = re.compile('\([a-zA-Zㄱ-힣0-9 -/*]{1,}\)')
        # # if CHAT_READ_TEST : print('ori 1 ',text)
        # text = patName.sub(' ', text)
        # if CHAT_READ_TEST: print('level2 ', text)
        # 한글, 영어, 숫자, * / + 빼고 제거.
        pat = re.compile('[^ㄱ-힣a-zA-Z0-9+*/ ]{1,}')

        # # 한글 영어 빼고 제거
        # pat = re.compile('[^ㄱ-힣a-zA-Z]{1,}')
        # if CHAT_READ_TEST: print('level3 ',text)

        text = pat.sub(' ',text)
        # if CHAT_READ_TEST: print('level4', text)
        for t in self.removeText:
            text = text.replace(t,'')
            # if CHAT_READ_TEST: print('level5', text)

        return text

    def __allowedName__(self, noun):
        for t in self.notAllowedNoun:
            if(t == noun):
                return False

        return True


    def remain_noun(self, text):

        tokens_koPos = self.twitter.pos(self.__removePunctuationPoint__(text))
        nouns = []
        for key, pos in tokens_koPos:
            if pos == 'Noun':
                if(self.__allowedName__(key)):
                    nouns.append(key)


        return ' '.join(nouns)

    def makeFiles(self):
        self.__makeYFile__()
        self.__makeTrain_And_Test_File()


    def __limit27__(self, i):
        ret = i + 65
        return ret

    def __toChat__(self, i):
        string = ''
        while True:
            string += chr(self.__limit27__(i % 26))
            i = int(i / 26)
            if i == 0:
                break;
        return string

    def __makeYFile__(self):
        text_file = open(self.y_data_path, "r")

        textLines = text_file.read().splitlines()
        yMap = list(set(textLines))
        print(len(yMap))

        dictionary = dict(zip(yMap, range(1, len(yMap) + 1)))

        write_file = open(self.y_data_path_to_char, "w")

        for ttt in textLines:
            write_file.writelines(self.__toChat__(dictionary.get(ttt)) + '\n')

        write_file.close()

    def __makeTrain_And_Test_File(self):

        from_ori_file = open(self.x_data_path, "r")

        to_ori_file = open(self.y_data_path_to_char, "r")

        textLines = from_ori_file.read().splitlines()
        toLines = to_ori_file.read().splitlines()

        from_train_file = open(self.x_data_path_train, 'w')
        from_test_file = open(self.x_data_path_test, 'w')

        to_train_file = open(self.y_data_path_train, 'w')
        to_test_file = open(self.y_data_path_test, 'w')

        for index in range(len(textLines)):
            nouns = self.remain_noun(textLines[index])
            if(len(nouns) == 0):
                continue

            if index % 10 == 0:
                from_test_file.writelines(nouns + '\n')
                to_test_file.writelines(toLines[index] + '\n')
            else:
                from_train_file.writelines(nouns + '\n')
                to_train_file.writelines(toLines[index] + '\n')













