import csv
import os
import re
from collections import Counter

import jieba
import jieba.analyse
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

_path = r'D:\Python\PycharmProjects\Michael05'


def print_to_txt(content):
    wordlist = []
    # result, number = re.subn(r'\s', '',content)
    result, number = re.subn(r'[^a-zA-Z0-9]+', ' ',content)
    # print(result.lower())  helloiamjennyhelloiamjenny
    # print(result.lower()) hello i am jenny hello i am jenny   -- 后来的
    # print(result.lower().split())  ['helloiamjennyhelloiamjenny']
    # print(result.lower().split()) ['hello', 'i', 'am', 'jenny', 'hello', 'i', 'am', 'jenny']   -- 后来的
    # print(result, number)  HelloiamJennyhelloIAMjenny 8
    # print(result, number)  Hello i am Jenny hello I AM jenny  8  -- 后来的
    # print([i for i in result.lower().split()])  ['helloiamjennyhelloiamjenny']
    wordlist.extend([w for w in result.lower().split()])
    # print(wordlist) ['hello', 'i', 'am', 'jenny', 'hello', 'i', 'am', 'jenny']    -- 后来的
    # print(wordlist)   ['helloiamjennyhelloiamjenny']
    # print(Counter(wordlist))  Counter({'helloiamjennyhelloiamjenny': 1})
    # print(dict(Counter(wordlist))) {'helloiamjennyhelloiamjenny': 1}
    # dict_wordlist = dict(Counter(wordlist))  跟下面一句是等同的 ！
    dict_wordlist = dict(Counter(result.lower().split()))

    fout = open(os.path.join(_path, 'English count.txt'), 'w')
    for k, v in dict_wordlist.items():
        # print(k, v)  helloiamjennyhelloiamjenny 1   突然意识到正则的地方， 那里应该是‘ space ’， 唉
        fout.write("word : %s \t number :  %d\n"% (k, v))


def print_to_csv(content):
    word_lists = []
    print(content)
    list = re.findall(r'[^a-zA-Z0-9]+', content) # findall 两个参数,返回list ， subn三个参数, 返回（）
    print(list)
    for i in list:
        content = content.replace(i, ' ') # 这里需要refesh content
    print(content)
    word_lists.extend([word for word in content.lower().split()])
    word_dict = dict(Counter(word_lists))

    csvfile = open(os.path.join(_path, 'English Count.csv'), 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['word', 'count'])

    for k, v in word_dict.items():
        print(k, v)
        # writer.writerows([k, str(v)])
        writer.writerow([k, str(v)])
    csvfile.close()


def Cloud_Word(content):
    # MichaelPic = Image.open(os.path.join(_path, 'Libai.jpg'))
    MichaelPic = Image.open(os.path.join(_path, 'Final.jpg'))
    Michaelnumpy = numpy.array(MichaelPic)
    print(Michaelnumpy)

    cloudwd = WordCloud(font_path=r'D:\Python\PycharmProjects\Michael01\AddnbrInPic\font\simsun.ttc',
                        mask=Michaelnumpy, max_words=200, random_state=100,
                        background_color='black').generate(content)

    # if mask 不是Michaelnumpy 是MichaelPic的话， 是显示不出来图片的

    plt.imshow(cloudwd)
    plt.axis("off")
    plt.show()


def Chinese_print_to_txt(content):

    dictContent = dict(Counter(jieba.lcut(content)))
    fout = open(os.path.join(_path,'Chinese.txt'), 'w',encoding='utf-8')
    for k, v in dictContent.items():
        fout.write("word : %s \t number :  %d\n" % (k, v))


def Chinese_print_to_csv(content):
    dictContent = dict(Counter(jieba.lcut(content)))
    fout = open(os.path.join(_path, 'Chinese.csv'), 'w', encoding='utf-8', newline='')
    writer = csv.writer(fout)
    writer.writerow(["jieba中文 ： ", "出现次数 ："])
    for k, v in dictContent.items():
        writer.writerow([k, str(v)])


def Render_word(word_dict):
    f = Image.open(os.path.join(_path,'Libai.jpg'))
    farray = numpy.array(f)
    cloudwd = WordCloud(font_path=r'D:\Python\PycharmProjects\Michael01\AddnbrInPic\font\simsun.ttc',
                        mask=farray, max_words=200, random_state=20,
                        background_color='white')
    cloudwd.generate_from_frequencies(word_dict)
    plt.imshow(cloudwd)
    plt.axis('off')
    # plt.show()
    image_color = ImageColorGenerator(farray)
    plt.imshow(cloudwd.recolor(color_func=image_color))
    plt.axis('off')
    # plt.show()
    cloudwd.to_file(os.path.join(_path, 'Chinese_WordCloud.jpg'))


if __name__ == '__main__':
    # print(os.path) <module 'ntpath' from 'D:\\Anaconda3\\lib\\ntpath.py'>
    f = open(os.path.join(_path, 'English.txt'))
    content = f.read()
    # print_to_txt(content)
    # print_to_csv(content)
    # Cloud_Word(content)

    fc = open(os.path.join(_path, '我们的时光.txt'))
    contentc = fc.read()
    # Chinese_print_to_txt(contentc)
    # Chinese_print_to_csv(contentc)

    # print(jieba.analyse.textrank(contentc, topK=10))
    #  ['时光', '情节', '推开', '规定', '形状', '了对', '飞过', '路过', '赖床', '无人']
    # print(jieba.analyse.textrank(contentc, topK=10, withWeight=True))   withWeight=True 这个不能少了
    # [('时光', 1.0), ('情节', 0.7340607077296143), ('推开', 0.6942544295008718), ('规定', 0.6242664972502522),
    #  ('形状', 0.5917947115596076), ('了对', 0.589390028177703), ('飞过', 0.4970966168335538), ('路过', 0.4969554084907812),
    #  ('赖床', 0.4969554084907812), ('无人', 0.4969554084907812)]
    list = jieba.analyse.textrank(contentc, topK=500, withWeight=True)
    word_dict = dict()
    for i in list:
        word_dict[i[0]] = i[1]
    print(word_dict)

    Render_word(word_dict)


