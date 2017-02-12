# -*- coding: utf-8 -*-
from userinput.situationInput import situationInput
from userinput.informationCheck import *
from structure.structure import meaningColor

def inputClear(string):
    return string.strip()  #会去除二边的空格\r\n

def check_raw_input(prompt_string,mColor,check_func=None,error_message="格式错误",):
    while 1:
        content = raw_input(mColor.getInput_Color + prompt_string)
        content = inputClear(content)
        if check_func==None:
            return content
        if check_func(content):
            return content
        else:
            print mColor.error_Color + "[-]" + error_message
            continue

def explain(explain_string,mColor=None):
    mColor = mColor if mColor else meaningColor()
    print mColor.explain_Color + "[*]" + explain_string + "!"

def informationInput(PI,mColor):
    print mColor.normal_Color + "\r\n[+] 填写下面的信息以便生成字典,只允许可打印的美式键盘上的字符:"
    print "[+] 如果你不知道或者不想填写,直接回车一次\r\n"
    
    explain("全部名字包括目标现在的姓名,过去使用过的真实姓名(拼音格式书写,大小写不敏感,空格分开.如果有多个名字;分隔)")
    PI.fullnameList += check_raw_input(">目标全部的名字:", mColor).lower().split(';')
    
    explain("昵称此处大小写敏感,如果有中文的昵称,根据情况请自行决定是提供该昵称的英文名还是拼音,通常有比较" + \
        "直接和合理英文翻译,建议提供小写英文名.如果昵称含有不能输入的特殊字符,可以不考虑这个昵称(大小写不敏感,空格分开.如果有多个昵称;分隔)")
    PI.nicknameList += check_raw_input(">生活中的昵称(绰号):", \
        mColor).split(';')

    PI.nicknameList += check_raw_input(">各大社交软件上目标的昵称(没有特别可能包含在密码中的建议不填,多个昵称以;分隔):", \
        mColor).split(';')

    PI.qq += check_raw_input(">目标qq号(也可以输入目标爱人的qq号但这里只允许你输入一个):", \
        mColor,qqCheck,"qq必须全数字")

    explain("输入一个爱人的一个名字,每个words以空格分隔,此处大小写不敏感")
    PI.lovernameList += check_raw_input(">请输入目标爱人的名字拼音:", \
        mColor).lower().split(';')

    explain("允许输入多个昵称以;分隔,昵称内的words以空格分隔,大小写敏感")
    PI.nicknameList += check_raw_input(">请输入目标爱人的昵称:",mColor).split(";")

    PI.dateList += check_raw_input(">请输入目标生日,要求年月日共8位,比如19980405:", \
        mColor,dateCheck,"请按示例格式输入生日").split(";")

    explain("纪念日包括目标和爱人的结婚纪念日,目标爱人的生日,目标身边最重要的人的生日(没有特别重要的,建议不考虑这项)")
    PI.dateList += check_raw_input(">请输入其他与目标相关的重要纪念日期(多个以;分隔,要求年月日共8位,比如19980405):", \
        mColor,dateStringCheck,"请按示例格式输入正确的日期")

    explain("这里其实是希望你输入目标的手机号码,但是实际情况中,你的目标可能会使用他家人的某个手机号码," + \
        "如果有这种可能,这里可以填写多个手机号,不过还是强烈建议你从多个手机号中选择最可能的一个填入这里")
    PI.phoneList += check_raw_input(">目标的手机号码(填写多个手机号码以;分隔):", \
        mColor,phoneStringCheck,"输入电话号码必须全部数字").split(";")

    PI.oldpasswdList += check_raw_input(">你知道的目标使用过的旧密码(多个以;分隔):", \
        mColor).split(';')

    explain("这个机构可以是大范围和小范围的,比如校团委和教务处,那么你应该输入tuan wei或者jiao wu chu.同时也" +\
        "可以输入这个学校的名称.还有公司等等.对于你输入的每一个名称必须具备每个单词的第一个字母可以组成合" + \
        "理的缩写条件")
    PI.organizationList += check_raw_input(">目标所在机构的名称全称(大小写不敏感,英文或者中文拼音,多个;分隔):", \
        mColor).lower().split(';')

    #关键词和关键数字提取
    explain("这个部分需要你给出目标在密码中可能使用的关键词和关键数字(这里的关键词和关键数字都不是弱口令那种)" + \
        "，为了避免你不知道从何下手,这里将逐步引导你给出从目标的多个方面提取关键词和关键数字.以下关键词" + \
        "均大小写不敏感,每个关键词用;分隔,关键词内部每个words空格分隔.请不要有重复内容")
    pet_wordsList = check_raw_input(">与目标宠物或者喜欢的宠物相关的关键词,这些关键词可以是宠物英文名,宠物中文品名的全拼(没有养宠物或者喜欢的宠物请跳过):", \
        mColor).lower().split(';')

    pet_numbersList = check_raw_input(">与目标宠物或者喜欢的宠物相关的关键数字,可以是宠物的年龄,生日,死亡日期:", \
        mColor,numberStringCheck,"只允许输入数字").lower().split(';')

    star_wordsList = check_raw_input(">喜欢的明星相关的关键词,可以来自明星的名字,英文名等,也可以从目标最喜欢的明星的相关信息来推测,比如明星喜欢的东西,明星的发行唱片等:", \
        mColor).lower().split(';')

    star_numbersList = check_raw_input(">喜欢的明星相关的关键数字,这些数字通常都是能在网上搜到的:", \
        mColor,numberStringCheck,"只允许输入数字").lower().split(';')

    explain("特长这里包括二个部分,一是目标的业余爱好,二是目标的经常性习惯.")
    skill_wordsList = check_raw_input(">与目标特长相关的关键词:", \
        mColor).lower().split(';')

    skill_numbersList = check_raw_input(">与目标特长相关的关键数字:", \
        mColor,numberStringCheck,"只允许输入数字").lower().split(';')


    food_wordsList = check_raw_input(">目标最喜欢的食物相关的关键词,通常是事物中文或者英文或者专有名称:", \
        mColor).lower().split(';')

    food_numbersList = check_raw_input(">目标最喜欢的食物相关的关键数字(这里通常没有):", \
        mColor,numberStringCheck,"只允许输入数字").lower().split(';')

    location_wordsList = check_raw_input(">与目标家庭住址或者办公地址相关的关键词:", \
        mColor).lower().split(';')

    location_numbersList = check_raw_input(">与目标家庭住址或者办公地址相关的关键数字:", \
        mColor,numberStringCheck,"只允许输入数字").lower().split(';')

    explain("请不要和前面填写过得内容重复,如果没有特别可能包含在密码中的信息,请不要填写")
    relative_wordsList = check_raw_input(">与目标深爱的或者有重要意义的亲人相关的关键词:", \
        mColor).lower().split(';')

    relative_numbersList = check_raw_input(">与目标深爱的或者有重要意义的亲人相关的关键数字:", \
        mColor,numberStringCheck,"只允许输入数字").lower().split(';')

    explain("这里的图腾性质可以理解为目标大概率会使用的或者已经表现出经常使用的或者与目标相关的且有含义的使用" +\
        "会在密码中的关键词和关键数字")
    other_wordsList = check_raw_input(">其他你需要补充的具有图腾性质的关键词:", \
        mColor).lower().split(';')

    other_numbersList = check_raw_input(">其他你需要补充的具有图腾性质的关键数字:", \
        mColor,numberStringCheck,"只允许输入数字").lower().split(';')

    ##是否选择添加内置弱口令
    weakpasswd = check_raw_input(mColor.getInput_Color+">你想在最后的密码字典前面添加程序内置的弱口令密码?y|Y,默认不添加:", \
        mColor).lower()
    if weakpasswd=='y':
        print mColor.normal_Color+"[+]你选择了添加内置弱口令"
        weakpasswd=1
    else:
        print mColor.normal_Color+"[-]你没有选择添加内置弱口令"
        weakpasswd=0

    ##############增加场景输入，根据不同场景再获取更多信息并以字典形式保存给situation
    #这个字典至少有一个'mode'key,它的value指代这个字典来自的场景场景
    PI.situation=situationInput(mColor)
    ############

    PI.keywordsList = pet_wordsList+star_wordsList+skill_wordsList+food_wordsList+location_wordsList+relative_wordsList+other_wordsList
    PI.keynumbersList = pet_numbersList+star_numbersList+skill_numbersList+food_numbersList+location_numbersList+relative_numbersList+other_numbersList
    return PI






