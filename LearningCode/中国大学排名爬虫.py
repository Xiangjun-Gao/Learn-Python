#CrawUnivRankingB.py
import requests
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'#明显提升爬取速度
        return r.text
    except:
        return ""
 
def fillUnivList(ulist, html):#规范化编程，将列表当参数传入下来
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:#对表格，先找Tbody，再找Tr
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')#tr下面有多个td标签
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
            #[[],[],[]]
 
def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):#打印学校的个数
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
     
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)#并不需要返回 uinfo
    printUnivList(uinfo, 20) # 20 univs
main()
