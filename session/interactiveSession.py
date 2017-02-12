# -*- coding: utf-8 -*-
import time
import os
import pickle

def CheckSession(mColor,path=os.path.abspath("session")):
    sessionList = []
    for item in os.listdir(path):
        if os.path.isdir(path+item) or item[-2:]=='py' or item[-3:]=='pyc':
            continue
        else:
            sessionList.append(item)
            print mColor.normal_Color + "[+]发现一个session文件 : "+item
    if not sessionList:
        print mColor.normal_Color + "[-]没有session文件"
    return sessionList


def DeleteSession(sessionname,mColor,path=os.path.abspath("session")):
    try:
        os.remove(path+os.sep+sessionname)
    except WindowsError or OSError:
        print mColor.error_Color + "[-]No such session file"
        return 0
    else:
        print "[+]成功删除"+sessionname+"文件"
        return 1


def LoadSession(sessionname,mColor,path=os.path.abspath("session")):
    if os.path.exists(path+os.sep+sessionname):
        sf = open(path+os.sep+sessionname,'rb')
        PI = pickle.load(sf)
        print "[+]成功加载"+sessionname+"的交互式信息内容"
        sf.close()
        return PI
    else:
        print mColor.error_Color + "[-]没有"+sessionname+"文件"
        return False

def ShowAllSession(mColor,path=os.path.abspath("session")):
    sessionList = CheckSession(mColor,path)
    for sessionname in sessionList:
        PI = LoadSession(sessionname,mColor,path)
        if PI:
            print mColor.normal_Color + "[+]"+sessionname+"内容如下:"
            for attri in PI.__dict__.keys():
                print mColor.normal_Color +attri+" : ",
                print PI.__dict__[attri]
        else:
            pass

def ShowSession(sessionname,mColor,path=os.path.abspath("session")):
    PI = LoadSession(sessionname,mColor,path)
    if PI:
        print mColor.normal_Color + "[+]"+sessionname+"内容如下:"
        for attri in PI.__dict__.keys():
            print mColor.normal_Color +attri+" : ",
            print PI.__dict__[attri]
    else:
        pass

def SaveSession(PI,mColor,path=os.path.abspath("session")):
    sessionname = raw_input(mColor.getInput_Color+">请输入sessionfile的名字(不含后缀,建议以目标对象的名称和日期命名):")
    if os.path.exists(path+os.sep+sessionname):
        print mColor.warn_Color+"[!]警告:"+sessionname+"已经存在"
        if raw_input(mColor.getInput_Color+">你想覆盖这个sessionfile吗?y|Y,其余不覆盖:").lower()=='y':
          pass
        else:
            if raw_input(mColor.getInput_Color+">你想重新输入sessionfile名字吗?n|N,其余是:").lower()=='n':
                return 0  
            else:
                if SaveSession(PI,mColor,paths)==1:
                    return 1
                else:
                    return 0
    sf = open(path+os.sep+sessionname,"wb")
    pickle.dump(PI,sf)
    sf.close()
    return 1


def SessionCommandInput(sessionList,mColor):
    '''
       这个脚本写的是持久性命令模式的输入
       主要给session文件管理使用
    '''
    print "[+]请输入help查看帮助信息"
    while 1:
        c = raw_input(mColor.getInput_Color + "ManageSession>").lower().strip()
        cL = c.split()#''.split()结果为[]除非是''.split(',')为['']
        if cL == []:
            continue
        if cL[0] == "help":
            if len(cL)!=1:
                print  mColor.error_Color + "[-]请不要输入多余字符!"
                continue
            else:
                print mColor.choice_Color
                preSpace = 10
                middleSpace = 4
                print " "*preSpace+"show sessionname"+" "*middleSpace + "查看该session文件的内容"
                print " "*preSpace+"delete sessionname"+" "*middleSpace + "删除session文件"
                print " "*preSpace+"list sessionname"+" "*middleSpace + "列出所有session文件"
                print " "*preSpace+"help"+" "*middleSpace + "查看支持的命令"
                print " "*preSpace+"exit"+" "*middleSpace + "退出"
                continue
        if cL[0] == "show":
            ShowSession(cL[1],mColor)
            continue
        if cL[0] == "delete":
            DeleteSession(cL[1],mColor)
            continue
        if cL[0] == 'list':
            if len(cL)!=1:
                print  mColor.error_Color + "[-]请不要输入多余字符!"
                continue
            else:
                CheckSession(mColor)
                continue
        if cL[0] == "exit":
            if len(cL)!=1:
                print  mColor.error_Color + "[-]请不要输入多余字符!"
                continue
            else:
                break
        print mColor.error_Color + "[-]命令格式输入错误!请按照help显示的要求输入"