# -*- coding:utf-8 -*-
import re
from lib.common import addWord

def printpasslistinfo(PL):#passwordlist==PL
    total=0#密码总数
    number=0#纯数字密码个数
    letter=0#纯字母密码个数
    specialchar=0#含有特殊字符的密码个数
    mixNL=0#数字字母混合密码个数
    maxlen=0#最长密码长度
    minlen=99#最短密码长度
    mostlen=''#出现密码次数最多的长度
    maxsame='no'#有无重复密码
    samecount=0 #重复密码次数
    lendic={}
    lenlist=[]
    mosttime=0

    for i in xrange(0,len(PL)):
        p = PL[i]
        total += 1
        #range3 = 0
        if p.isdigit():
            number += 1
            #range3=1
        if p.isalpha():
            letter += 1
            #range3=1
        if not p.isalnum():
            specialchar +=1
            #range3=1
        else:
            mixNL += 1
        #if range3==0:
            #print p
            #raw_input()
        length=len(p)
        if length > maxlen:
            maxlen = length
        if length < minlen:
            minlen = length
        try:
            lendic[str(length)] += 1
        except KeyError:
            addWord(lendic,str(length),1)#key字符,value整形
            lenlist.append(str(length))#字符

    samecount = len(PL) - len(set(PL))
    if samecount:
        maxsame='yes'

    print "[+]调试过程查看的信息:"
    print lendic
    print lenlist
    #print mosttime
    for l in lenlist:
        if lendic[l] > mosttime:
            mostlen = l
            mosttime = lendic[l]
            continue
        if lendic[l]==mosttime:
            mostlen += ','+str(lendic[l])
            continue
        
    print "\n[+]你选择的密码文件信息如下:"
    print "                                 *密码总数(按行算) : "+str(total)
    print "                                 *纯数字密码个数 : "+str(number)
    print "                                 *纯大小写字母密码个数 : "+str(letter)
    print "                                 *数字字母混合密码个数 : "+str(mixNL)
    print "                                 *含有特殊字符密码个数 : "+str(specialchar)
    print "                                 *最大密码长度 : "+str(maxlen)
    print "                                 *最小密码长度 : "+str(minlen)
    print "                                 *出现次数最多的密码长度 : "+mostlen+' 共出现:'+str(mosttime)+'次'
    print "                                 *出现重复密码 : "+ maxsame +" 次数 : " + str(samecount)

if __name__=="__main__":
    printpasslistinfo(['abcd','1234','123456','1234','we'])
    
        
            
        
    
