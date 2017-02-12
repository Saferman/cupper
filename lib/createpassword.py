# -*- coding:utf-8 -*-

import time
import itertools
import re
import os
from lib.oldpasswordAnalyze import AnalyzeGetNumbers
from lib.common import FilterList,CountSpecialCharacter,getNameList
from lib.situationhandle import SituationHandle
from lib.passwordDeform import *
"""
MixedKeywordList性质:每一个元素都在preHandlePhase中直接成为MixedKeywordList的元素得列表
"""

class PasswordGenerator(object):
    '''
    Password generator.
    '''
    #高频通用密码中出现的关键数字
    _numList =['123456', '123123','1314','123','321','52']
    """最初作者选定的数字
    _numList = ['123456', '123123', '123123123', '112233', '445566', '456456', \
    '789789', '778899', '321321', '521','520', '1314', '5201314', '1314520', '147369', \
    '147258', '258', '147', '456', '789', '147258369', '111222', '123', '1234', \
    '12345', '1234567', '12345678', '123456789', '987654321', '87654321', '7654321', \
    '654321', '54321', '4321', '321','52']
    """

    # 常用前缀列表
    _prefixWords = ['a','qq','yy','aa','abc','qwer','woaini']

    #常用后缀列表,是个镶嵌列表，[0]是英文字符列表,[1]是数字字符列表
    _suffixwords = [['a'],[str(x) for x in xrange(0,10)]+['520']]

    #嵌子与嵌子之间，或者嵌子和中心列表的连接字符串
    #注意这里的列表一定要有''元素，不然在Mixed系列函数中for j in self._connList前添加r.append(a+b)
    _connList=['','_']  #['','#','*','_','@','.']

    #伴侣前缀列表
    _partnerPrefixList = ['520','5201314','1314','iloveu','iloveyou']

    #高频通用的不带前后缀变形处理的MixedKeywordList性质词汇
    _commonMixWordsList=['']   #['password']

    #参数设定
    min_len= 5#密码最小长度，不含
    max_len= 17#密码最大长度，不含

    def __init__(self,PI):
        '''
        参数:
            传递的PI参数的各属性值含义:
            fullnameList:  fullname单元:目标全名,每个字的拼音以空格隔开,全小写,最多支持三个字的名字
            nicknameList:  nickname单元:昵称
            dateList:  包括生日在内的重要日期列表,格式:19980405
            phoneList:   电话号码
            oldpasswdList:  旧密码,列表
            keynumbersList:  可能出现的数字，是个列表
            keywordsList:    关键词，是个列表，全小写
            lovername:   爱人的姓名,每个字的拼音之间以空格分开，全小写,最多支持三个字的名字
            organizationList:   所在机构全称(包括工作单位)，每个字的拼音以空格隔开，全小写
            qq:          目标的QQ号
            weakpasswd:  逻辑值，1或者0。1表示在生成的密码前面添加工具内置的弱口令密码
            situation    字典 包含场景信息和该场景下再收集的用户信息
        '''
        self.fullnameList = PI.fullnameList
        self.nicknameList = PI.nicknameList
        self.dateList = PI.dateList
        self.phoneList = PI.phoneList
        self.oldpasswdList = PI.oldpasswdList   #它里面的数字部分发挥了作用,还需要提取出字符串
        self.keynumbersList = PI.keynumbersList
        self.keywordsList = PI.keywordsList
        self.lovernameList = PI.lovernameList
        self.organizationList = PI.organizationList
        self.qq = PI.qq
        self.situation = PI.situation
        self.weakpasswd = PI.weakpasswd  #最后由lastHandlePhase处理


        ###以下是盛放各种需要嵌入其他嵌子和中心列表的词汇的变量
        #推测目标密码可能包含的数字嵌子列表
        self.InnerNumList=[]
        #由一个全名生成的缩写嵌子列表
        self.ShortNameList=[]
        #全名生成的非缩写嵌子列表
        self.FullNameList=[]
        #由公司全名生成的嵌子列表
        self.CompanyList=[]
        #由场景相关信息生成的钳子列表
        self.SituationList=[]

        #前缀列表嵌子
        self.PrefixList=[]
        #后缀列表嵌子
        self.SuffixList=[]

        #嵌子嵌入的中心列表，注意:这个列表会直接添加进self.result
        self.MixedKeywordList=[]
        
    
        self.result=[]#最终生成的密码列表

    def __GetBirthNumList(self):#必须把传递过来的生日参数不变化的返回一个
        r =[]
        for date in self.dateList:
            year = date[0:4]
            month = date[4:6]
            day = date[6:8]
            r += [year+month+day,year,month+day,day,year[2:4],year[2:4]+month+day, \
            day+month+year]
            #如果用month[0]，当用户没传递生日信息时,month=''，这里会引发IndexError
            if month[0:1]=='0' or day[0:1]=='0':
                r += [year+month.lstrip('0')+day.lstrip('0')]
        return r
               

    def _GetInnerNumList(self):
        r=self._numList#前面的常量
        for i in xrange(0,10):
            r+=[str(i)*x for x in xrange(1,5)]#让每个0至9的数字重复1到4次
        endyear = int(time.strftime("%Y"))
        ###是否可以考虑让用户输入年份，而不是瞎猜
        #r += [str(x) for x in range(2000, endyear+1)]#生成年份(2000年至今)

        if self.keynumbersList:
            r+=self.keynumbersList
        r += self.__GetBirthNumList()
        if self.oldpasswdList:  #个人建议从oldpasswd提取出数字内容
            r += AnalyzeGetNumbers(self.oldpasswdList)
        return FilterList(r)
    
    def _GetShortNameList(self,fullnameList=None):
        fullnameList = fullnameList if fullnameList else self.fullnameList
        #print fullnameList
        if not fullnameList:
            return []
        else:
            r = []
            func = lambda x:[x, x.title(), x[0].lower(), x[0].upper(), x.upper()]
            for fullname in fullnameList:
                nameSplited = fullname.split()
                if len(nameSplited) == 1:
                    r += func(nameSplited[0])
                elif len(nameSplited) == 2:
                    shortName = nameSplited[0][0].lower() + nameSplited[1][0].lower()
                    r += func(shortName)
                else:
                    shortName = nameSplited[0][0].lower() + nameSplited[1][0].lower() + nameSplited[2][0].lower()
                    r += func(shortName)
                    shortNameRS = nameSplited[1][0].lower() + nameSplited[2][0].lower() + nameSplited[0][0].lower()
                    shortNameRST = nameSplited[1][0].lower() + nameSplited[2][0].lower() + nameSplited[0][0].title()
                    shortNameR = nameSplited[1][0].lower() + nameSplited[2][0].lower() + nameSplited[0]
                    shortNameRT = nameSplited[1][0].lower() + nameSplited[2][0].lower() + nameSplited[0].title()
                    r += [shortNameRT, shortNameR, shortNameRST, shortNameRS, shortNameRS.upper()]
            return r

    def _GetFullNameList(self,fullnameList=None):
        fullnameList = fullnameList if fullnameList else self.fullnameList
        if not fullnameList:
            return []
        else:
            r = []
            func=lambda x:[x.split(),x.upper().split(),x.title().split()]
            for fullname in fullnameList:
                nameSplited=func(fullname)
                if len(nameSplited[0]) == 1:
                    r += nameSplited[0]
                    r += nameSplited[1]
                    r += nameSplited[2]
                elif len(nameSplited[0]) == 2:
                    func1=lambda x:[x[0]+x[1],x[1]+x[0]]
                    r += func1(nameSplited[0])
                    r += func1(nameSplited[1])
                    r += func1(nameSplited[2])
                else:
                    r += [''.join(nameSplited[0]),''.join(nameSplited[1]),''.join(nameSplited[2])]
                    func2=lambda x:(x[1]+x[2]+x[0])
                    r += [func2(nameSplited[0]),func2(nameSplited[1]),func2(nameSplited[2])]
                    r += [nameSplited[0][1]+nameSplited[0][2]+nameSplited[1][0]]
            return r
        
    def _GetCompanyList(self,organizationList=None):
        organizationList = organizationList if organizationList else self.organizationList
        if not organizationList:
            return []
        else:
            r=[]
            for organization in organizationList:
                r += getNameList(organization)
            return r

    def _GetSituationList(self):
        '''
           需要SituationHandle
        '''
        r=SituationHandle(self.situation)
        return r


    def _OrderMixed(self, listA, listB,samefilter=False):
        if not listA and not listB:
            return []
        r = []
        for a,b in itertools.product(listA, listB):#in后面的部分生成笛卡尔积的元组，这里元组(a,b)
            if samefilter:
                if a==b:
                    continue
            if len(a+b)>self.min_len and len(a+b)<self.max_len:         #设定连接最大长度  
                for j in self._connList:
                    r.append(a+j+b)
        return r

    def _Mixed(self, listA, listB,samefilter=False):
        if not listA and not listB:
            return []
        r = []
        for a,b in itertools.product(listA, listB):#in后面的部分生成笛卡尔积的元组，这里元组(a,b)
            if samefilter:
                if a==b:
                    continue
            if len(a+b)>self.min_len and len(a+b)<self.max_len:         #按长度范围筛选密码
                for j in self._connList:
                    r.append(a+j+b)
                    r.append(b+j+a)
                    #当b=''或者a=''时出现重复
        return r

    def _TwoLevelMixed(self,listA,listB,listC,samefilter=False):
        '''
           等效混合是listA,listB,listC各取元素排列形成r一个元素，但是有相应的过滤规则
           如果在排列成r一个元素的三个元素中有相同的，则这个元素不放入r中
           为了编程方便，只允许listB和listC是相同的
        '''
        if not listA and not listB and not listC:
            return []
        r=[]
        for a,b in itertools.product(listA, listB):
            for c in listC:
                if samefilter:
                    if b==c:
                        continue
                if len(a+b+c)>self.min_len and len(a+b+c)<self.max_len:
                    for j in self._connList:
                        r.append(a+j+b+c)
                        r.append(b+j+a+c)
                        r.append(c+j+a+b)
                        r.append(c+j+b+a)
                        r.append(a+b+j+c)
                        r.append(b+a+j+c)
                        r.append(c+a+j+b)
                        r.append(c+b+j+a)
        return r
            



    def _DecideAddWhat(self,string):#决定是否添加如果添加，添加数字还是字符，主要用于self.SuffixList注意和self._suffixwords不一样
        #返回2代表不添加
        numlist=re.findall(r"\d+",string)
        i=0
        for stringnumber in numlist:
             i += len(stringnumber)
        j=len(string)-i
        if abs(i-j)<=2:
            return -1
        else:
            if ord(string[-1:])>=48 and ord(string[-1:])<=57:
                return 0
            else:
                return 1
        
            
    def preHandlePhase(self):#生成各种嵌子列表
        self.InnerNumList=self._GetInnerNumList()
        self.ShortNameList=self._GetShortNameList()
        self.FullNameList=self._GetFullNameList()
        self.CompanyList=self._GetCompanyList()

        TwoNestedList = self._GetSituationList()
        self.SituationList = TwoNestedList[0]
        self.InnerNumList +=  TwoNestedList[1]

        self.PrefixList=self._prefixWords+[x.upper() for x in self._prefixWords]
        self.SuffixList=self._suffixwords#最后再lastHandlePhase里处理,此处不能做任何加法

    
        self.MixedKeywordList += self.ShortNameList    
        self.MixedKeywordList += self.FullNameList
        if self.nicknameList:
            self.MixedKeywordList += self.nicknameList
        if self.keywordsList:
            self.MixedKeywordList += self.keywordsList

        self.MixedKeywordList += self.SituationList
        self.MixedKeywordList += self._commonMixWordsList

    def mixedPhase(self):
        self.result += self._Mixed(self.MixedKeywordList, self.InnerNumList)
        self.result += self._Mixed(self.MixedKeywordList,self.CompanyList)
        self.result += self._OrderMixed(self.PrefixList,self.MixedKeywordList)
        self.result += self._Mixed(self.InnerNumList,self.CompanyList)
        
        #二级嵌子嵌入的中心列表
        TwoLevelMixKeywordList = []
        TwoLevelMixKeywordList += self._TwoLevelMixed(self.MixedKeywordList,self.InnerNumList,self.InnerNumList,True)
        TwoLevelMixKeywordList += self._OrderMixed(self.MixedKeywordList,self.MixedKeywordList,True)
        
        self.result += TwoLevelMixKeywordList
        
        if self.phoneList:
            self.result += self._OrderMixed(self.PrefixList+self.MixedKeywordList, self.phoneList)
            #电话号码可以单独产生一个，然后后四位也可以取出来作为InnerNumList的一员
        if self.qq:
            self.result += self._OrderMixed(self.PrefixList+self.MixedKeywordList,[self.qq])
        if self.lovernameList:
            temlist = self._GetShortNameList(self.lovernameList)+self._GetFullNameList(self.lovernameList)
            self.result += self._OrderMixed(self._partnerPrefixList, temlist)

        #可以不和其他密码混合而单独作为密码的处理
        self.result += self.result + self.MixedKeywordList + self.InnerNumList  
        

    def lastHandlePhase(self):
        '''
           处理self.SuffixList和self.oldpasswdList,self.weakpasswd  或者扩展更多智能处理
        '''
        PassListWithSuffix=[]
        for i in xrange(0,len(self.result)):
            d=self._DecideAddWhat(self.result[i])
            if d==-1:
                continue
            else:
                for suffixchar in self.SuffixList[d]:
                    PassListWithSuffix.append(self.result[i]+suffixchar)
        SimplePasswordList=[]
        if self.weakpasswd:#数字逻辑型
            f=open('simplepassword','r')#在当前目录打开这个文件
            for p in f.readlines():
                if p.strip("\n")!="":
                    SimplePasswordList.append(p.strip("\n"))
            f.close()
        self.result = self.result+SimplePasswordList + self.oldpasswdList + PassListWithSuffix

    def passFilter(self):
        '''
           这个函数是过滤掉不合适的密码，主要包括以下这些情况
           1.重复的密码
           2.长度不合适的密码
           3.特殊字符过多的密码，这里指超过二个
        '''
        #去除相同元素
        #self.result = sorted(set(self.result),key=self.result.index)
        self.result = FilterList(self.result)
        #去除长度不合适和特殊字符大于等于二个的密码
        self.result = [i for i in self.result if (len(i)>self.min_len and len(i)<self.max_len and CountSpecialCharacter(i)<2)]        


    def deform(self):
        '''
           这个函数是用一些用户可能使用的变换模式来对密码字典处理
           具体内容见passwordDeform.py脚本
           你可以根据你的经验在这个函数里填充或者修改要使用passwordDeform.py脚本
           里的哪些规则.
        '''
        self.result += CapitalizeTheFirstLetter(self.result)
        self.result += charReplace(self.result)
        if '3' in self.situation['mode']:#这里判断是否属于"测试目标懂安全场景"
            self.result += EncodeConvert(self.result)


    def generator(self):
        self.preHandlePhase()
        self.mixedPhase()
        self.lastHandlePhase()
        self.passFilter()  
        self.deform()    #这个可以考虑让用户自己决定是否需要做这个转换
        
        #可以在这使用过滤函数,不过最好在密码生成流程上尽量不要出现相同密码,这里的建议是为了
        #预防_numList和添加的弱口令密码重复。
        return self.result


if __name__=='__main__':
    pass















        

    
