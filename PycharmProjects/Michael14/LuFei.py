import os, re
import urllib.request
from urllib.error import URLError, HTTPError

import bs4
Downfolder = os.path.join(os.path.dirname(__file__),'LufeiPic')
url = 'https://tieba.baidu.com/p/1934517246#!/l/p1'
pattern = re.compile(r'^(https://imgsa.baidu.com/forum/)')
def get_url_link():
    user_Agent = 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    header = {'User-Agent':user_Agent}
    try:
        req = urllib.request.Request(url,headers=header)
        res = urllib.request.urlopen(req)
    except HTTPError as e:
        print(e.code)
    except URLError as e:
        print(e.reason)
    else:
        print('Good!')
        content = str(res.read(), 'utf-8')
        print(content)
    return content


def get_pic_link(url_content):
    soup = bs4.BeautifulSoup(url_content, 'lxml')
    list = []
    # father_tag = soup.find_all('div', attrs={"class":re.compile(r'^(ag_ele)')})
    father_tag = soup.find_all('div', class_='ag_ele ag_ele_v')
    print(father_tag)
    for child in father_tag:
        print(child)
        a = child.find(name='img')
        list.append(a.get('src'))
        print(a.get('src'))
    return list


def down_Pic(list, Downfolder):
    JPGnbr = 0
    for child in list:
        loc = os.path.join(Downfolder, str(JPGnbr)+'.jpg')
        with open(loc, 'wb') as f:
            Piclink = urllib.request.urlopen(child).read()
            f.write(Piclink)
        JPGnbr += 1



if __name__=='__main__':
    if os.path.exists(Downfolder):
        print("目录已经存在了！")
        os.rmdir(Downfolder)
    Newfolder = os.makedirs(Downfolder)

    url_content = get_url_link()
    list = get_pic_link(url_content)
    down_Pic(list, Downfolder)

