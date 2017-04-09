
import re

_WORD_SPLIT = re.compile(" ")


print(re.split(_WORD_SPLIT, "hello world"))