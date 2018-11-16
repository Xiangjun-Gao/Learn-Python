import requests
url="http://music.163.com/#/artist?id=205795"
try:
    kv={"User-Agent":"Mozilla/5.0"}
    r=requests.get(url,headers=kv)
    #r.headers表示Response对象的headers，
    #r.request.headers  （服务器内容）表示Requsets对象的headers （爬虫接口内容）
    r.raise_for_status()#判断是否爬取成功
    r.encoding=r.apparent_encoding
    print(r.text[:2000])
except:
    print("爬取失败")
