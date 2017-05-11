# -*- coding: utf-8 -*-
from lib.color import *
from lib.common import isLinuxSystem


class meaningColor:
    def __init__(self):
        if isLinuxSystem():
            self.getInput_Color = O #'\033[33m'
            self.normal_Color = W   #'\033[0m'
            self.title_Color = P    #'\033[31m'
            self.explain_Color = B   #'\033[34m'
            self.choice_Color = B   #'\033[34m'
            self.error_Color = ''
            self.warn_Color = ''
        else:
            self.getInput_Color = ''
            self.normal_Color = ''
            self.title_Color = ''
            self.explain_Color = ''
            self.choice_Color = ''
            self.error_Color = ''
            self.warn_Color  = ''


class PersonalInformation:
    def __init__(self):
        self.fullnameList = []
        self.nicknameList = []
        self.dateList = []
        self.phoneList = []
        self.oldpasswdList = []
        self.keynumbersList = []
        self.keywordsList = []
        self.lovernameList = []
        self.organizationList =[]
        self.qq =''
        self.weakpasswd = 0
        self.situation = {}
