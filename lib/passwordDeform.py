# -*- coding: utf-8 -*-
"""
在实际环境中，我们发现用户想出一个密码后可能会
因为某些原因对密码再度处理，比如大小写变化，字符替换，base64编码,md5加密等
注意：前后缀的添加暂时不属于这个脚本需要考虑的事情
为了下一个版本的拓展，这里先保留mode参数，这个参数有二种值
一种是全面覆盖的生成密码，另一种是尽可能少的生成密码，还有适当的生成密码（默认）
这个脚本目前的处理规则都是"""
#尽可能少的生成密码
"""
注意：这些处理函数在使用的使用，用户可能会选择串行处理而不是并行处理
保证好相互之间的不冲突.
所有函数只是返回处理过后的密码，不包含未处理的密码和处理前的密码
"""
#每一个函数会说明三件事情
#1.建议的这个函数使用前需要什么由用户编写的判断条件
#2.这个函数会对符合什么条件的密码做出处理
#3.做出什么处理
#extra:说明为什么这么做

#passL 代表密码列表
import re
import base64
import hashlib
from lib.common import uppercase,lowercase,number,CountSpecialCharacter
uppers = uppercase()  #大写字母字符串
lowers = lowercase()  #小写字母字符串
numbers =number()     #数字字符串

####注意，本文件放置于前面的函数不能用于处理后面函数处理过的结果

def CapitalizeTheFirstLetter(passL):
    '''
       将所有开头不是大写，全部字符为字母(不含最后一位）的密码首字母大写
    '''
    r=[]
    for p in passL:
        if p[0] in lowers:
            if p[:-1].isalpha():
                r.append(p.title())#r += p.title()《=这是错误的，因为列表加上字符串是有问题的!
        else:
            pass
    #print r
    return r

def charReplace(passL):
    '''
       没有特殊字符,a-@,o-0,e-3，首字母不替换
       没有数字,a-4,o-0,e-3，首字母不替换
    '''
    r=[]
    for p in passL:
        if p.isalnum():
            tp=p
            tp=tp[0]+tp[1:].replace('a','@')
            tp=tp[0]+tp[1:].replace('o','0')
            tp=tp[0]+tp[1:].replace('e','3')
            if tp!=p:
                r.append(tp)
        if  re.search('.*([0-9]+).*', p) == None:
            tp=p
            tp=tp[0]+tp[1:].replace('a','4')
            tp=tp[0]+tp[1:].replace('o','0')
            tp=tp[0]+tp[1:].replace('e','3')
            if tp!=p:
                r.append(tp)
    #print r
    return r

def EncodeConvert(passL):
    '''
       使用前需要判断测试目标是否属于"测试目标懂安全"的情景
       只用于处理不含特殊符号的密码
       进行base64,md5加密取全长密码或者截取前8位或者后8位（10位暂时不考虑）
    '''
    r=[]
    for p in passL:
        if CountSpecialCharacter(p)!=0:
            continue
        try:
            r.append(base64.b64encode(p))
            r.append(base64.b64encode(p)[-8:])
        except:
            pass
        try:
            m = hashlib.md5()
            m.update(p)
            r.append(m.hexdigest())
            r.append(m.hexdigest()[0:8])
        except:
            pass
    print r
    return r



def RandChange(passL):
    '''
       进行随机变换，之所以想到这个是因为考虑到实际环境的复杂性，作者
       不可能把握每个人的心理状态，所以增加了这个随机变化的处理
       该函数处理不许哟具备任何合理性，只要喜欢就可以，说不定哪天蒙对了，HH
    '''
    pass

if __name__=='__main__':
    pass
    raw_input()
    