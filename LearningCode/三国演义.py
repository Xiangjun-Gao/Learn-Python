#三国演义
import jieba
excludes={"将军",'却说','荆州','二人','不可','不能','如此'}
txt=open("三国演义.txt","r",encoding='utf-8').read()
txt=jieba.lcut(txt)
count={}
for word in txt:
    count[word]=count.get(word,0)+1

for word in excludes:
    del(count[word])
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(10):
    print("{0:<10}{1:>5}".format(items[i]))
