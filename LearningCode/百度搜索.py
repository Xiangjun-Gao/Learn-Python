import requests
keyword="Lebron"

try:
    kv={"wd":keyword}
    r=requests.get("https://www.baidu.com/s",params=kv)
    print(r.request.url)# 千万不要写成r.requests.url        ？？？？？
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(len(r.text))#KB
    print(r.text[:3000])#？？为什么输出了这么少的东西
except:
    print("爬取失败")
