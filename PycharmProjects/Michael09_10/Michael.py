from urllib.error import URLError, HTTPError

import bs4,os
import re,urllib.request
import shutil

url = 'http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/index.htm'
pattern = re.compile(r'(.pdf)$')
download_root_url = 'http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/'
download_folder= 'D:\Python\PycharmProjects\Michael09_10\Download_pdf'

def get_html_content(url):
    user_agent='Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    header = {'User-Agent':user_agent}
    try:
        req = urllib.request.Request(url,headers=header)
        res = urllib.request.urlopen(req)
    except HTTPError as e:
        print(e.code)
    except URLError as e:
        print(e.reason)
    else:
        print("Good!")
        content = str(res.read(), 'gb2312')
        # print(content)
    return content


def get_pdf_link(html_content):
    link = []
    if html_content:
        soup = bs4.BeautifulSoup(html_content,'lxml')
        for child in soup.find_all(href=pattern):
            link.append(child.get('href'))
            # print(child.get('href'))
        return link


def download_pdf(all_pdf_link):
    print("-"*20 + 'list all pdf' + "-"*20)
    # print(all_pdf_link)
    for link in all_pdf_link:
        realink = download_root_url+link
        pdf = urllib.request.urlopen(realink).read()
        f = open(os.path.join(download_folder, link), 'wb')
        f.write(pdf)



if __name__=='__main__':
    html_content = get_html_content(url)
    all_pdf_link = get_pdf_link(html_content)

    isexist = os.path.exists(download_folder)
    if isexist:
        remove_old = shutil.rmtree(download_folder)
    newfolder = os.makedirs(download_folder)

    download_pdf(all_pdf_link)

    # http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/DS1-intro.pdf
    # http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/DS2-list-1.pdf
    # http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/DS2-list-2.pdf



