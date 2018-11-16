#CrawBaiduStocksA.py
import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']#标签属性方法
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
 
def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}   
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})#find返回第一个，作用同find_all()[0]
 
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})#合并字典,tag.text指的是标签夹得那部分内容，tag.string指标签里面的非属性字符串
             
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text#获得所需内容的方法 .string .text(.split)
                val = valueList[i].text
                infoDict[key] = val
             
            with open(fpath, 'r', encoding='utf-8') as f:
                f.write( str(infoDict) + '\n' )
        except:
            traceback.print_exc()
            continue
 
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
main()
