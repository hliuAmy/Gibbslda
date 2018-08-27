# cal doc to word
import numpy as np


def read_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        text = f.read()
    return text
# d_t = read_file('lda5/model-final.theta').split('\n')
# print(len(d_t))
# for i in range(len(d_t)):
#     d_t[i] = d_t[i].split()
# d_t = np.array(d_t)
# print(type(d_t))
# print(d_t.shape)


def doc_word(topicNum):
    d_t = np.loadtxt('lda' + str(topicNum) + '/model-final.theta')
    t_w = np.loadtxt('lda' + str(topicNum) + '/model-final.phi')
    print(d_t.shape)
    print(t_w.shape)
    d_w = np.dot(d_t, t_w)
    print(d_w.shape)
    return d_w


def word2id(topicNum):
    dic = {}
    text = read_file('lda' + str(topicNum) + '/wordmap.txt').split('\n')
    for item in text:
        if item != '' and len(item.split()) == 2:
            dic[item.split()[0]] = item.split()[1]
    return dic


def write_dict(topicNum, name, dic):
    path = 'result/lda' + str(topicNum) + '/' + str(name)
    with open(path, 'w', encoding='utf-8') as f:
        for key, value in dic.items():
            f.write(key + ' ' + str(value) + '\n')


filenams = read_file('filelist').split(',')
data = read_file('Hulth2003.dat').split('\n')
for topic in [5, 10, 20, 50, 100]:
    w2id = word2id(topic)
    d_w = doc_word(topic)
    for i in range(len(data)):
        file = data[i]
        if file != '':
            name = filenams[i]
            words = [word for word in file.split() if word != '']
            values = list(d_w[i, :])
            result = {}
            for word in words:
                result[word] = values[int(w2id[word])]
            write_dict(topic, name, result)
