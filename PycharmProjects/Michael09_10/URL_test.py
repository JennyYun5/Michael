import urllib.request
from urllib.error import URLError, HTTPError

print("异常处理 。。。。。。。。。")
# req = urllib.request.Request('http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/index.htm')
# try:
#     response = urllib.request.urlopen(req)
#     print(response.read())
# except HTTPError as e:
#     print('The server couldn\'t fulfill the request')
#     if hasattr(e,'code')
#       print('Error code: ', e.code)
# except URLError as e:  # 网络无连接，即本机无法上网/连接不到特定的服务器/服务器不存在
#     print('We failed to reach a server.')
#     if hasattr(e,'reason')
#       print('Reason: ', e.reason)
# else:
#     print("good!")
#     print(response.read().decode("utf8"))

print("POST 方法模拟登陆 。。。。。。。。。")
# values = {"username":"1016903103@qq.com","password":"XXXX"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib.request.Request(url,data)
# response = urllib.request.urlopen(request)
# print(response.read())     #------这个只是原理啦

print("Header 。。。。。。。。。")
url = 'http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/index.htm'
user_agent = 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = {'User-Agent':user_agent, 'Referer':url}
    # 另外 headers 的一些属性，下面的需要特别注意一下：
    # User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
    # Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
    # application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
    # application/json ： 在 JSON RPC 调用时使用
    # application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
request = urllib.request.Request(url, headers=headers) # 服务器若识别了是浏览器发来的请求，就会得到响应。
response = urllib.request.urlopen(request,timeout=10)
print(response.read())
print("Proxy（代理）的设置 ------ 这个还不会呢")
# # Proxy（代理）的设置  假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了，这酸爽！
# enable_proxy = True
# proxy_handler = urllib.request.urlopen.ProxyHandler({'http':'192.168.1.1:8080'})
# null_proxy_handler = urllib.request.ProxyHandler({})
# if enable_proxy:
#     opener = urllib.request.build_opener(proxy_handler)
# else:
#     opener = urllib.request.build_opener(null_proxy_handler)
# urllib.request.install_opner(opener)

print("Cookie----------没有实现！！！！！！！")
# CookieJar —-派生—->FileCookieJar —-派生—–>MozillaCookieJar 和LWPCookieJar
# #声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print('Name = '+item.name)
#     print('Value = '+item.value)
# 在上面的方法中，我们将 cookie 保存到了 cookie 这个变量中

# 如果我们想将 cookie 保存到文件中该怎么做呢
# #设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #创建一个请求，原理同urllib2的urlopen
# response = opener.open("http://www.baidu.com")
# #保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

# 如果以后想使用，可以利用下面的方法来读取cookie 并访问网站，感受一下
# #创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# #从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# #创建请求的request
# req = urllib2.Request("http://www.baidu.com")
# #利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

print("利用 cookie 模拟网站登录 ----- 唉， 也米有实现!!!!!! ")
# import urllib
# import urllib2
# import cookielib
#
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#             'stuid':'201200131012',
#             'pwd':'23342321'
#         })
# #登录教务系统的URL
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks\_login2.login'
# #模拟登录，并把cookie保存到变量
# result = opener.open(loginUrl,postdata)
# #保存cookie到cookie.txt中
# cookie.save(ignore\_discard=True, ignore\_expires=True)
# #利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()
# 创建一个带有 cookie 的 opener，在访问登录的 URL 时，将登录后的 cookie 保存下来，然后利用这个 cookie 来访问其他网址。