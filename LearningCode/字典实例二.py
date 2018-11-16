##利用字典将两个通讯录文本合并为一个文本

def main():
    infile1=open('TeleAddressBook.txt','rb')
    infile2=open('EmailAddressBook.txt','rb')##rb 和 r 的区别

    infile1.readline()
    infile2.readline()

    lines1=infile1.readlines()
    lines2=infile2.readlines()

    dict1={}
    dict2={}

    for line in lines1:
        line=line.strip()
        elements=line.split()
        dict1[elements[0]]=str(elements[1].decode('gbk'))##gdk 编码->unicode 编码

    for line in lines2:
        line = line.strip()
        elements=line.split()##split函数自动去掉换行符
        dict2[elements[0]]=str(elements[1].decode('gbk'))

    lines=[]
    for key in dict1:
        if key in dict2.keys():
            ##s=key+'\t'+dict2[key]+'\t'+dict1[key]+'\n'
            ##s='\t\t'.join([str(key.decode('gbk')),dict1[key],dict2[key]])
            s='\t\t'.join([str(key.decode('gbk')),dict2[key],dict1[key]])
            s=s+'\n'
        else:
            ##s=key+'\t'+'-----------------'+'\t'+dict1[key]+'\n'
            ##s = '\t\t'.join([str(key.decode('gbk')),dict1[key], '------'])
            s = '\t\t'.join([str(key.decode('gbk')),'------',dict1[key]])
            s=s+'\n'
        lines.append(s)

    for key in dict2:
        if key not in dict1.keys():
            ##s=key+'\t'+dict2[key]+'\t'+'-----------------'+'\n'
            ##s = '\t\t'.join([str(key.decode('gbk')),'------' , dict2[key]])
            s = '\t\t'.join([str(key.decode('gbk')),dict2[key],'------'])
            s=s+'\n'
            lines.append(s)

    infile3=open('AddressBook.txt', 'w')
    infile3.writelines(lines)

    infile1.close()
    infile2.close()
    infile3.close()
    print("The addressBooks are merged!")

if __name__ == "__main__":
        main()

