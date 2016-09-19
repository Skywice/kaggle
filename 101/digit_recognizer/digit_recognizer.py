# -*- coding:utf-8 -*-
import csv
import os
import numpy as np
from numpy import *
# 数据的基本路径
base_dir = 'C:\\Users\\dell\\Desktop\\apps\\kaggle_data\\digit_recognizer'
test_set_dir = os.path.join(base_dir, 'test.csv')
# 载入训练数据

def loadTrainData():
    train_labels = []
    train_array = []
    train_set_dir = os.path.join(base_dir, 'train.csv')
    with open(train_set_dir) as train_set_file:
        lines = csv.reader(train_set_file)
        for line in lines:
            train_array.append(line)
    train_array.remove(train_array[0])  # 去掉表头
    train_set = array(train_array)
    train_labels = [x(0) for x in train_array]
    return toInt(train_set), toInt(train_labels)

# 将字符串转为数字
def toInt(array):
    array = mat(array)
    m, n = shape(array)
    newArray = zeros((m, n))
    for i in xrange(m):
        for j in xrange(n):
            newArray[i, j] = int(array[i, j])
    return newArray

