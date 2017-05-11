# -*- coding: utf-8 -*-
#!/usr/bin/env python
#  [工具]
#  cupper 2.0
#  密码生成工具
#
#  [作者]
#  姓名:Saferman
#  
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.
import sys
import re
import os
import argparse
from logo.logo import logo
from lib.createpassword import PasswordGenerator
from lib.PDHandle.handlefile import HandleFile
from lib.download import download
from lib.common import SessionCommandInput
from userinput.informationInput import informationInput
from structure.structure import *
from session.interactiveSession import *
from stdout.Windows_stdout import UnicodeStreamFilter


##定义需要的结构体数据:
mColor = meaningColor()


def tag():
    print "\n[+]Thanks for using"
    print ""
    exit()


def checkYourPassword():
    if raw_input(">你想检查密码文件里有你的密码吗？y|Y,默认不检查:").lower()=='y':
        passwordlist=raw_input(">请输入你的密码,多个密码以,分隔:").split(',')
        print "[+]正在socialpass.dic里查找是否有你输入的密码......"
        filelist=open('socialpass.dic','r').readlines()
        flag=0#标志是否有任何一个密码被发现
        for inputpassword in passwordlist:
            for filepassword in filelist:
                if filepassword.strip('\n')==inputpassword:
                    print "[+]socialpass.dic include password : "+inputpassword
                    flag=1
        if flag==0:
            print "[-]no result"

def ClearNull(PI):
    for attri in PI.__dict__.keys():
        if isinstance(PI.__dict__[attri], list):
            PI.__dict__[attri] = filter(lambda x:x!='', PI.__dict__[attri])
    return PI


def print_version():
    logo()
    print "\r\n	"+mColor.title_Color+"[ cupper.py ]  v2.0"+mColor.normal_Color+"\r\n"
    print "	* 作者:Saferman"
    print "	* 下载链接:https://github.com/Saferman/cupper/\r\n"
    print "     * 关于本工具更多说明或者有任何疑惑，请查阅README或者github wiki\r\n"
    exit()


def ManageSession():
    print "[+]欢迎进行session管理,session文件是一个保存了用户在交互式密码生成过程中输入的信息的文件，目的是方便用户下一次直接加载文件而不需要重复输入相同的信息"
    print "[+]正在列举已有的session文件"
    sessionList = CheckSession(mColor)
    if not sessionList:
        exit()
    else:
        SessionCommandInput(sessionList,mColor)


def interactive():
    sessionList = CheckSession(mColor)
    if not sessionList:
        PI = False
    else:
        sessionname = raw_input(mColor.getInput_Color+">你想加载session文件作为你交互式输入的信息吗?想则请输入上面列出的文件名,否则跳过:")
        if sessionname in sessionList:
            PI = LoadSession(sessionname,mColor)

    if not PI:
        PI = PersonalInformation()
        PI = informationInput(PI,mColor)
        PI = ClearNull(PI)  #将所有['']设置为[]
        while 1:
            saveYN = raw_input(mColor.getInput_Color + ">你想保存你输入的信息为一个session文件吗?可以方便下次直接加载这个文件而不需要重新输入(y|Y|n|N,默认不保存):").lower()
            if saveYN == 'y':
                if SaveSession(PI,mColor):
                    print mColor.normal_Color + "[+]输入的信息保存进session文件成功!"
                else:
                    print mColor.normal_Color + "[-]输入的信息保存进session文件失败"
                break
            if saveYN =='n' or saveYN =='':
                break
            print mColor.error_Color + "[-]请输入y,Y,n,N或者直接回车"

    pg=PasswordGenerator(PI)
    print mColor.normal_Color + "[+]正在生成字典文件，请耐心等待......"
    passwordslist=pg.generator()

    print "[+]生成成功,程序将把密码写入当前目录socialpass.dic"
    if os.path.exists("socialpass.dic")==True:
        if raw_input("[-]警告,当前目录有socialpass.dic,你希望覆盖吗?n|N,默认覆盖:").lower()=='n':
            exit()
    f=open("socialpass.dic",'w')
    for word in passwordslist:
        f.write(word+'\n')
    f.close()
    print "[+]写入成功!!socialpass.dic是最后的密码文件"


    checkYourPassword()
    
    

def main():
    reload(sys)
    sys.setdefaultencoding("utf8")
    if sys.stdout.encoding == 'cp936':
        sys.stdout = UnicodeStreamFilter(sys.stdout)

    parser = argparse.ArgumentParser(description="* 关于本工具更多说明或者有任何疑惑，请查阅README或者github wki")
    parser.add_argument('-f','--file',type=str,default=None,help="对密码文件进行各种处理",dest='file')
    parser.add_argument('-i','--interactive',help="交互式生成密码字典",action="store_true")
    parser.add_argument('-s','--session',help="管理保存输入信息的session文件",action="store_true")
    parser.add_argument('-d','--download',help="下载作者维护的密码字典",action="store_true")
    parser.add_argument('-v','--version',help="查看Logo和显示工具版本",action="store_true")

    args = parser.parse_args()
    if args.version:
        print_version()
        tag()
    if args.download:
        download()
        tag()
    if args.session:
        ManageSession()
        tag()
    if args.interactive:
        interactive()
        tag()
    if args.file!=None:
        HandleFile(args)
        tag()
        



if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\n[-]It's implite to interrupt me!:("










