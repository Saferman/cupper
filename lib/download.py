# -*- coding:utf-8 -*-
import urllib2,re
repo="https://github.com/Saferman/password-dictionary/"

def GetHtmlList(url=repo):
    req=urllib2.Request(url)
    f=urllib2.urlopen(req)
    return f.readlines()

    
def CheckUpdate():
    flag = 0
    updateinfo=[]
    for line in GetHtmlList(repo+"blob/master/README.md"):
        if flag==0:
            if re.search('Discription of those dictionaries',line)!=None:
                flag=1
            else:
                continue
        else:
            if line.find('</article>')!=-1:
                break
            m=re.search('<p>DIS_(.*)</p>',line)
            if m==None:
                continue
            else:
                updateinfo.append(m.group(1).split('_'))
    return updateinfo  #一个嵌套列表
    

def downfile(dicfile):
    lines=GetHtmlList(repo+"blob/master/"+dicfile)
    f=open(dicfile,'w')
    flag=0
    for line in lines:
        if flag==0:
            if re.search('<div itemprop="text" class="blob-wrapper data type-text">',line)!=None:
                flag=1
            else:
                continue
        else:
            if re.search('</table>',line)!=None:
                break
            m=re.search('blob-code blob-code-inner js-file-line">(.*)</td>',line)
            if m!=None:
                f.write(m.group(1)+'\n')
            else:
                continue
    f.close()
        


    

def download():
    print "[+]正在从网上更新密码字典情况..."
    try:
        update=CheckUpdate()
    except:
        print "[-]无法得到网站上密码字典信息，请检查网络是否通顺."
        return 0
    print "[+]更新成功,你可以下载的密码字典有:\n"
    for i in xrange(0,len(update)):
        print '    '+str(i+1)+"     "+update[i][0]+" : "+update[i][1]
    while 1:
        down=raw_input("\33[33m> \n请输入你想下载的字典序号,输入99退出:\33[0m")
        if down=='99':
            return 0
        if re.search('^\d+$',down)!=None and int(down)<=i+1 and 1<=int(down):
            break
        else:
            print "[-]输入错误,请重新输入"

    print "[+]正在下载文件,请耐心等待......"
    try:
        downfile(update[int(down)-1][1])
    except:
        print "[-]出错了,下载失败"
        return 0
    print "[+]成功!下载至当前目录"+update[int(down)-1][1]+"文件里"
    return 1
    
    























    
    
