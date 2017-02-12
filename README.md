#Cupper V1.0 到来!
Cupper的名字含义是be better than common user passwords profiler(cupp).然而cupp作为一款早已过时的工具,仅仅超越这款工具是不够的。
从上一个版本到现在经过了3个月的时间,作者自身知识水平和见识有了提升,对该工具做出来许多改进。最后再次明确这款工具的目标---超越
作者接触过的每款开源社工密码生成工具。
#用途:
这款工具一个最重要的用途就是为渗透测试人员提供自身密码安全性的检测。
#使用环境和方法:
在这个版本中，暂时没考虑跨平台兼容性，推荐在kali linux系统中使用。
使用方法很简单: python cupper.py -h
#截图:
python cupper.py -v <br>
![Screenshot](https://github.com/Saferman/cupper/blob/master/images/version.png)
#支持的功能和介绍:
           ·交互式生成社工密码字典!这个功能也是这款工具的核心功能,将来也将在这个功能上花更多的时间
           ·下载作者上传的密码字典,和上个版本不同,这个版本的cupper可以动态更新密码字典
           ·多样的密码文件处理手段,包括密码大小写转换,添加字符至每行密码前面或者后面,拼接两个密码字典,过滤密码字典等
#展望:
在接下来的一个版本里,作者将强化旧密码分析引擎,并增加社工库查询功能,增加更多的目标信息获取处理功能,还有美观效果将在下一个版本大幅改进。<br>
敬请期待！
#其他:
1.在当前版本,为了尽可能减少缺少依赖带来的麻烦，作者尽可能使用python安装自带的模块。<br>
2.createpassword.py用类封装了算法,非常方便你直接调用(只是需要注意import进来的函数):<br>
           ·getpass=PasswordGenerator(传递目标信息)<br>
           ·print getpass.generate()<br>
