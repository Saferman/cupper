# -*- coding: utf-8 -*-
import re

def qqCheck(qq):
    if re.search("^\d+$",qq)!=None or qq=='':
        return True
    else:
        return False

def dateCheck(date):
    if re.search("^\d\d\d\d\d\d\d\d$",date)!=None or date=='':
        return True
    else:
        return False

def dateStringCheck(dateString):
    dateList = dateString.split(',')
    for date in dateList:
        if dateCheck(date):
            continue
        else:
            return False
    return True

def phoneCheck(phone):
    if re.search("^\d+$",phone)!=None or phone=='':
        return True
    else:
        return False

def phoneStringCheck(phoneString):
    phoneList = phoneString.split(",")
    for phone in phoneList:
        if phoneCheck(phone):
            continue
        else:
            return False
    return True

def numberCheck(number):
    if re.search("^\d+$",number)!=None or number=='':
        return True
    else:
        return False

def numberStringCheck(numberString):
    numberList = numberString.split(",")
    for number in numberList:
        if numberCheck(number):
            continue
        else:
            return False
    return True