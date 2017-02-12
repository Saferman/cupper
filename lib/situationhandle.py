# -*- coding: utf-8 -*-
from lib.common import getNameList


def Situation2(websiteName,domainName):
    '''
       websiteName  网站名字的拼音，全部小写，空格分隔
       domainName  ..之间的字符串，大小写敏感，比如baidu
    '''
    word_List = getNameList(websiteName)+[domainName]
    #可以考虑加上'dmm'这类后缀
    number_List=[]
    return word_List,number_List




def SituationHandle(SituationDict):
    '''
       返回二层嵌套列表，
       第一个列表是具有MixedKeywordList性质的关键词列表
       第二个列表是InnerNumList（目标密码可能包含的数字嵌子列表）
       目前支持的情景：
       1.其他
       2.网站用户的密码
       3.测试目标懂安全
    '''
    words_List=[]
    numbers_List=[]
    for mode in SituationDict['mode']:
        if mode=='1':
            continue
        if mode=='2':
            word_List,number_List = Situation2(SituationDict['2websiteName'],SituationDict['2domainName'])
            words_List += word_List
            numsers_List += number_List
            continue 
        if mode=='3':
            continue
    return [words_List,numbers_List]


    