# -*- coding: utf-8 -*-

def check(modeList):
    for i in modeList:
        #增加新场景，这里也需要修改
        if i.isdigit() and i in ['1','2','3']:
            pass
        else:
            return False
    return True

def situationInput(mColor):
    SituationDict={}
    '''
       SituationDict字典结构:
       'mode':[一个字符列表，包括适用的场景]
       其他信息key-value储存
    '''
    while 1:
        print mColor.getInput_Color+"请选择下面符合的场景，没有则选择其他:"
        print mColor.choice_Color
        #这里的这个顺序不可以随便改
        print "1.其他（默认）"
        print "2.密码字典用于猜解某用户网站账号的密码"
        print "3.测试目标懂安全相关的知识(尤其是一些编码加密知识)"
        numbers = raw_input(mColor.getInput_Color+">输入你想选择的数字(多个数字用,分隔):")
        modeList=[]
        if numbers=='':
            modeList.append('1')
        else:
            modeList=numbers.split(',')
            if check(modeList):
                pass
            else:
                print mColor.error_Color+"[-]输入错误，请输入可以选择的数字或者直接回车!"
                continue

        SituationDict['mode']=modeList

        for mode in modeList:
            if mode=='1':
                pass
            if mode=='2':
                SituationDict['2WebsiteName'] = raw_input(mColor.getInput_Color+">请输入网站全名的拼音,全小写,用空格分隔,比如:wang yi you xiang:")
                SituationDict['2domainName'] = raw_input(mColor.getInput_Color+">请输入网站一级域名..之间的内容(大小写敏感),比如baidu:")
                pass
            if mode=='3':
                pass
        break


    return SituationDict
