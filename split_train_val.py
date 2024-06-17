import os
import random

trainval_percent = 0.9  #训练验证集占90%，测试10%
train_percent = 0.8     #训练占80%，验证10%
xmlfilepath = './Annotations'
txtsavepath = './images'
if not os.path.exists('./images/'):
    os.makedirs('./images/')
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(num * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('./images/trainval.txt', 'w')
ftest = open('./images/test.txt', 'w')
ftrain = open('./images/train.txt', 'w')
fval = open('./images/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)


ftrainval.close()
ftrain.close()
fval.close()
ftest.close()