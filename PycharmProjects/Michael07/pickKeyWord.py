import os, re, jieba
import jieba.analyse

note = 'note'
Stopword = 'stop_words.txt'
txtype = re.compile(r'(.txt)$')

def findKeyWord(srcpath):
    dirlist = os.listdir(srcpath)
    for f in dirlist:
        dirloc = os.path.join(srcpath, f)
        if os.path.isdir(dirloc):
            findKeyWord(dirloc)
        else:
            # print(dirloc)
            name, type = os.path.splitext(dirloc)
            if txtype.match(type):
                with open(dirloc,encoding='utf-8') as f1:
                    content = f1.read()
                    jieba.analyse.set_stop_words(os.path.join(os.path.dirname(__file__), Stopword))
                    tags = jieba.analyse.extract_tags(content, topK = 10)
                    print(' '.join(tags))


if __name__ == '__main__':
    findKeyWord(os.path.join(os.path.dirname(__file__), note))

