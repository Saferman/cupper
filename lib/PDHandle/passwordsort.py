# -*- coding:utf-8 -*-
"""
目前我才用的规则：打分制
密码长度
密码是否有特殊字符
密码是否是全数字,0开头的不加分
密码是否全小写字母或者仅开头大写
0开头的密码也要减分
如果不是全数字字母开头要加分
密码是否前半段字母后半段数字
密码是否前半段字母中间特殊字符一个后半段数字

#全字母只有末尾是数字按照http://www.freebuf.com/news/topnews/62052.html给分
"""
from lib.common import CountSpecialCharacter

class passScore:
    def __init__(self):
        self.password=''
        self.score=0

def AlphaNumJudge(string):
    '''
       判断一个字符串是否是有前半段字母和后半段数字构成
    '''
    for i in xrange(0,len(string)):
        if string[0:i].isalpha() and string[i:].isdigit():
            return True
    return False

def AlphaOneSpecialNumJudge(s):
    '''
       判断一个字符串是否是有前半段字母加一个特殊字符后半段数字构成
    '''
    for i in xrange(1,len(s)-1):
        if s[0:i].isalpha() and CountSpecialCharacter(s[i])==1 and s[i+1:].isdigit():
            return True
    return False


def giveScore(p):
    score=0
    LengthRule={6:14,7:10,8:10,9:7,10:6,11:5,12:4} #其余长度没分
    try:
        score += LengthRule[len(p)]
    except KeyError:
        score += 0

    if not p.isalnum():
        score = score - 3*CountSpecialCharacter(p)

    if p.isdigit() and p[0]!='0':
        score += 2
    if p.isalpha() and p[1:].islower():
        score +=2
    if p[0]=='0':
        score -= 3
    if not p.isdigit() and p[0].isalpha():
        score += 1
    if AlphaNumJudge(p) or AlphaOneSpecialNumJudge(p):
        score += 2 

    return score

def merge(left,right):  
    result=[]  
    i,j=0,0  
    while i<len(left) and j<len(right):  
        if left[i].score>=right[j].score:  
            result.append(left[i])  
            i+=1  
        else:  
            result.append(right[j])  
            j+=1  
    result+=left[i:]  
    result+=right[j:]  
    return result 

def merge_sort(seq):
    if len(seq)<=1:
        return seq
    else:
        middle = len(seq)/2
        left = merge_sort(seq[:middle])
        right =merge_sort(seq[middle:])
        return merge(left,right)

def sortByScore(passScoreList):
    '''
       冒泡排序时间效率太低了不推荐
       建议采用归并排序等,诶其实不用自己写算法,python有模块内封装了算法
    '''
    """
    for i in xrange(0,len(passScoreList)):
        for j in xrange(i+1,len(passScoreList)):
            if passScoreList[j].score > passScoreList[i].score:
                passScoreList[i],passScoreList[j] = passScoreList[j],passScoreList[i]
        passScoreList[i] = passScoreList[i].password
    return passScoreList
    """
    passScoreList = merge_sort(passScoreList)

    #raw_input()
    for i in xrange(0,len(passScoreList)):
        passScoreList[i] = passScoreList[i].password
    return passScoreList
    

    

def passwordsort(passwordlist,PL=None):
    '''
       按照这个密码被用户使用的可能性大小排序
       返回排完序的密码列表
    '''
   
    for i in xrange(0,len(passwordlist)):
        p=passScore()
        p.password=passwordlist[i]
        p.score=giveScore(passwordlist[i])
        passwordlist[i]=p
    #上面这个部分很费时间
    #print "[+]所有密码打分完毕,下面开始排序"
    return sortByScore(passwordlist)



