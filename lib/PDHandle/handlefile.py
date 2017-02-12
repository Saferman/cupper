# -*- coding:utf-8 -*-
import os
import re
from lib.PDHandle.passwordinfo import printpasslistinfo
from lib.PDHandle.passwordsort import passwordsort

def ReadStripFile(filenameext):
    lineslist=open(filenameext,'r').readlines()
    for i in xrange(0,len(lineslist)):
        lineslist[i]=lineslist[i].strip()
    return lineslist


def WriteToFile(filenameext,alist):
    f=open(filenameext,'w')
    for a in alist:
        f.write(a+'\n')
    f.close()


def AddSome(l=[],he='h',cover='c',s=''):#he只能为h或者e,cover为c或者a,返回列表
    if cover=='c':
        if he=='h':
            for i in xrange(0,len(l)):
                l[i] = s+l[i]
        else:
            for i in xrange(0,len(l)):
                l[i] = l[i]+s
    else:
        if he=='h':
            for i in xrange(0,len(l)):
                l.append(s+l[i])
        else:
            for i in xrange(0,len(l)):
                l.append(l[i]+s)
    return l
            
def Filter(l=[],choice='s',length='6'):
    if choice=='l':
        return [p for p in l if len(p)<=int(length)]
    else:#choice=='s'
        return [p for p in l if len(p)>=int(length)]
            
        

def HandleFile(args):#对args.file文件进行处理
    passfile=args.file
    while 1:
        if not os.path.exists(passfile):
            print "[-]file doesn't exist!"
            break
        
        print "\r\n[+]你的处理对象是: "+passfile+" ,目前版本支持的处理有:"
        print "1------检查密码文件并删除多余重复项"
        print "2------给每行密码开头或结尾添加自定义内容"
        print "3------过滤密码文件里小于或者大于你指定位数的密码"
        print "4------大小写转换"
        print "5------向该字典文件添加另一个字典文件的密码"
        print "6------得到密码文件内容的信息(总密码数,纯数字密码个数等)"
        print "7------按照一定规则对密码字典内密码进行排序以提高破解效率"
        print "99-----退出"
        handle=raw_input("\33[33m> 请输入你想进行的操作:\33[0m")

        if handle not in ['1','2','3','4','5','6','7','99']:
            print "[-]输入错误!!"
            raw_input(">Press any key is to input again:")
            continue

        if handle=='99':
            break
        
        passwordlist=ReadStripFile(passfile)
        
        if handle=='1':
            print "[+]正在删除原密码文件相同项,请稍等.........."
            passwordlist=list(set(passwordlist))
            WriteToFile(passfile,passwordlist)
            print "[+]去除重复项(只保留一个)成功,密码文件还是原文件"
            break

        if handle=="2":
            while 1:
                he=raw_input("\33[33m> 你想在每行密码开头或者结尾添加自定义字符?h|H开头,e|E结尾:\33[0m").lower()
                if he!="h" and he!="e":
                    print "[-]请输入h|H或者e|E"
                    continue
                else:
                    break
            string=raw_input("\33[33m> 请输入你想添加的字符:\33[0m")
            while 1:
                cover=raw_input("\33[33m> 你想把添加了字符的密码覆盖旧密码还是添至旧密码后面?c|C覆盖,a|A添加:\33[0m").lower()
                if cover!='c' and cover!='a':
                    print "[-]请输入c|C或者a|A"
                    continue
                else:
                    break
            print "[+]正在处理,请稍等......"
            passwordlist=AddSome(passwordlist,he,cover,string)
            WriteToFile(passfile,passwordlist)
            print "[+]添加成功!"
            break

        if handle=="3":
            while 1:
                filterchoice=raw_input(">你想过滤大于一定长度的密码(l|L)，还是小于一定长度的密码(s|S):").lower()
                if filterchoice!='l' and filterchoice != 's':
                    print "[-]请输入l|L或者s|S"
                    continue
                else:
                    break
            while 1:
                filterlength=raw_input(">请输入过滤长度(输入的值不含):")
                if re.search('^\d+$',filterlength)==None:
                    print "[-]请输入数字"
                    continue
                else:
                    break
            print "[+]正在过滤,请稍等......"
            passwordlist=Filter(passwordlist,filterchoice,filterlength)
            WriteToFile(passfile,passwordlist)
            print "[+]过滤完成"
            break

        if handle=='4':
            while 1:
                print "[-]你选择的数字不是1,2,3中的一个,请重新选择"
                print "1-------将所有密码中的所有字母转换为大写"
                print "2-------将所有密码中的所有字母转换为小写"
                print "3-------将所有密码第一位转换为大写(如果不是字母不会受到影响)"
                mo=raw_input("\33[33m> 请选择一项,输入数字即可:\33[0m")
                if mo not in ['1','2','3']:
                    print "[-]你只能输入1,2,3中的一个"
                    continue
                else:
                    break
            print "[+]正在处理大小写,请稍等.........."
            if mo=="1":
                passwordlist=[p.upper() for p in passwordlist]
            if mo=="2":
                passwordlist=[p.lower() for p in passwordlist]
            if mo=="3":
                passwordlist=[p.title() for p in passwordlist]
            WriteToFile(passfile,passwordlist)
            print "[+]大小写处理完成"
            break

        if handle=='5':
            while 1:
                anotherfile=raw_input(">请输入另一个密码文件绝对路径(含文件名后缀):")
                try:
                    anotherPL=ReadStripFile(anotherfile)
                except IOError:
                    print "\n[-]你输入的文件不存在!!"
                    continue
                except:
                    print "\n[-]出错,你选择的的文件无法程序无法正常打开!"
                    continue
                else:
                    break
            print '[+]即将把你选择的文件('+anotherfile+')添加至处理文件('+passfile+')后面'
            WriteToFile(passfile,passwordlist+anotherPL)
            print '[+]添加成功!'
            break
        if handle=='6':
            print "[+]正在获取文件关于密码的信息,请稍等........"
            printpasslistinfo(passwordlist)
            print "[+]获取信息完毕"
            break
            
        if handle=='7':
            print "[+]正在对密码文件内的密码进行排序"
            passwordlist = passwordsort(passwordlist)
            WriteToFile(passfile,passwordlist)
            print "[+]排序完毕"
            break


























            
            
    
