# -*- coding:utf-8 -*-
import re

def AnalyzeGetNumbers(oldpasslist):#从旧密码列表里提取出现的关键数字，返回关键数字列表
    r = []
    renum=re.compile('\d+')
    for oldpass in oldpasslist:
        r += renum.findall(oldpass)
    return r
        
