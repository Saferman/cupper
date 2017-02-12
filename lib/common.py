# -*- coding:utf-8 -*-
import platform
 
def isWindowsSystem():
    return 'Windows' in platform.system()
 
def isLinuxSystem():
    return 'Linux' in platform.system()

def uppercase():
    r=''
    for s in xrange(65,91):
        r+=chr(s)
    return r

def lowercase():
    r=''
    for s in xrange(97,123):
        r+=chr(s)
    return r
def number():
    r=''
    for s in xrange(48,58):
        r+=chr(s)
    return r

def CountSpecialCharacter(s):
    '''
       计算一个字符串里出现的特殊字符，返回数量
       这里的特殊字符包括:@_#$!%^&*.
    '''
    r=0
    r += s.count('@')
    r += s.count('_')
    r += s.count('#')
    r += s.count('$')
    r += s.count('!')
    r += s.count('%')
    r += s.count('^')
    r += s.count('&')
    r += s.count('*')
    r += s.count('.')
    return r

    
def FilterList(alist):#过滤列表相同元素
    return list(set(alist))

def addWord(dic,key,value):
    #存在就天机key:value到字典dic，不存在就新建个字典key
    dic.setdefault(key,value)

def getNameList(name):
    '''
     由全名name得到钳子，这个name必须服从如下格式
     最好用来处理公司名称，网站全名这类name      
     全名的拼音，全部小写，以空格分隔
    '''
    r=[]
    nameSplited = name.split()
    func = lambda x:[x.lower(),x[0],x[0].upper()]#3，所以下面循环也是3
    for i in xrange(0,len(nameSplited)):
        nameSplited[i]=func(nameSplited[i])
    for j in xrange(0,3):
        s=''
        for i in xrange(0,len(nameSplited)):
            s += nameSplited[i][j]
        r.append(s)
    return r

def SessionCommandInput(mColor):
    '''
       这个脚本写的是持久性命令模式的输入
       主要给session文件管理使用
    '''




if __name__=='__main__':
    d={}
    addWord(d,'1',1)
    print d['1']+1
    
