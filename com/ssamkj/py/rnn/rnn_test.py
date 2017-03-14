import codecs

from tensorflow.contrib import rnn
from com.ssamkj.py.rnn import transferStringArrayToBinaryArray

import numpy as np

import tensorflow as tf

x_data = []
y_data = []


myfile = './data/productData.txt'
def load_X_data(myfile):
    text_file = open(myfile, "r")
    return text_file.read().splitlines()


x_data, y_data = load_X_data(myfile), load_X_data('./data/categoryData.txt')


trns = transferStringArrayToBinaryArray.TransferStringArrayToBinaryArray(maxBinaryLength=16, maxStringLength=100)

x_data_binary = trns.transfer(x_data)
# print(x_data_binary)


y_data_binary = set(y_data)
print(len(y_data))
print(len(y_data_binary))
print('----------')
for y in y_data_binary:
    print(y)
