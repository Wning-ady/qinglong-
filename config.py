# -*- coding: utf-8 -*-
# config
"""
new Env('xiaoym参数设置');
如需启用此处设置，需将文件重命名为config.py
"""

"""自定义ua"""
ua_list = [] # ['ua1','ua2']微信浏览器ua，至少配置一个，否则部分脚本无法运行，手机端电脑端均可

"""企业微信设置"""
qwbotkey=''  # 脚本优先从环境变量获取，没有获取到再从此处获取。已实装脚本：钢镚、每天赚

"""wxpusher设置"""
pushconfig = {"appToken":"","topicids":[]} 
"""脚本优先从环境变量获取，没有获取到再从此处获取，"topicids":["123456"],一对一推送无需设置toppicids。已实装脚本：钢镚、每天赚"""

"""元宝智慧星空内部互助设置"""
invite_info = {'name':'','code':''}  # 仓库脚本无需理会，收费项目专用
"""鱼儿设置"""
yu_config = {
        'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

        'txbz': 0.5,  # 设置提现标准 单位：元

        'sendable': 1,  # 企业微信推送开关 1开0关

        'pushable': 1,  # wxpusher推送开关 1开0关

        'delay_time': 20,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers

        'blacklist':[], # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

        'yuck':[], # ck设置，优先从环境变量中获取，[{'name':'德华','ck':'抓包的ck值'},{'name':'彦祖','ck':'抓包的ck值','uid':'UID_xxx'}]name值随意，方便自己辨认即可。uid是wxpusher一对一通知专属设置，其它情况不要填

    }
"""鱼儿设置完毕"""

"""可乐设置"""
kl_config={
    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'blacklist':[], # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

    'klck':[], # ck设置，优先从环境变量中获取，[{'name':'德华','ck':'抓包的ck值'},{'name':'彦祖','ck':'抓包的ck值','uid':'UID_xxx'}]name值随意，方便自己辨认即可。uid是wxpusher一对一通知专属设置，其它情况不要填
}
"""可乐设置完毕"""

"""点点赚设置"""
ddz_config={
    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'whitelist':[], # 提现白名单设置,白名单中的账号自动提现，填入ck中的name,['name1','name2']。

    'zfb_account': '', #支付宝账号
    
    'zfb_name': '', #支付宝名字

    'ddzck':[], # ck设置，优先从环境变量中获取，[{'name':'xxx','PHPSESSID':'xxx'},{'name':'xxx','PHPSESSID':'xxx','uid':'UID_xxxxx'}]name值随意，方便自己辨认即可。PHPSESSID是抓包数据。uid是wxpusher一对一通知专属设置，其它情况不要填
}
"""点点赚设置完毕"""

"""钢镚设置"""
czgm_config = {
    'printf': 1,  # 实时日志开关,1为开，0为关

    'debug': 1,  # debug模式开关,1为开,0为关

    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'upload': 0,  # 上传检测号信息到服务器设置，1为上传，相应地也可以从云端获取检测号字典；0为不上传， 相应地也不能从云端获取检测号字典

    'blacklist':[], # 提现黑名单设置,黑名单中的账号不进行自动提现，填入ck中的name,['name1','name2']。

    'czgmck':[], # ck设置，[{'name':'xxx','ck':'gfsessionid=xxx'},{'name':'xxx','ck':'gfsessionid=xxx','uid':'UID_xxxxx'}]name值随意，方便自己辨认即可。ck是抓包数据。uid是wxpusher一对一通知专属设置，其它情况不要填
}

"""每天赚设置"""
mtz_config = {
    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 2,  # 因为没有服务器验证是否点击链接的机制，建议线程设置为2.线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 40,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
    
    'blacklist':[],  # 黑名单中的账号不进行自动提现，填入ck中的name,['name1','name2']，未实名的辅助号专用，可到一定金额再实名提现
    
    'total_num': 19,  # 设置单轮任务最小数量"""设置为18即本轮数量小于18不继续阅读"""

    'mtzv2ck':'', #ck设置，建议填到环境变量或配置文件,多账号用&连接或创建多条变量。name=xxx;ck=share:xxxx&name=xxx;ck=share:xxxx;uid=UID_xxxx，微信和wxpusher群发不用填uid

}
"""智慧元宝设置"""
aio_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关

    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers

    'upload': 0,  # 上传检测号信息到服务器设置，1为上传，可以从云端获取检测号字典；0为不上传， 相应地也不能从云端获取检测号字典
    
    'blacklist':[],  # 黑名单中的账号不进行自动提现，填入ck中的name,['name1','name2']，未实名的辅助号专用，可到一定金额再实名提现

    'ybck':[], # 元宝ck，
    # 'zhck':[], # 智慧ck，
    # 'xkck':[], # 星空ck，
}
"""ck格式：[{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖','uid':'UID_xxx'},] 。uid是wxpusher一对一推送专属，其它无需配置。多账号添加大括号，注意不要漏逗号"""


"""人人帮设置"""
rrb_config = {
    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于5000，平台标准为5000 设置为5000，即为5毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers

    'rrbck':'', # ck设置，[{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖','uid':'UID_xxx'},] 。uid是wxpusher一对一推送专属，其它无需配置。多账号添加大括号，注意不要漏逗号
}
"""花花设置"""
hh_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关

    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 5000,  # 设置提现标准 不低于3000，平台标准为3000

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers

    'upload': 0,  # 上传检测号信息到服务器设置，1为上传，相应地也可以从云端获取检测号字典；0为不上传， 相应地也不能从云端获取检测号字典


    # 'hhck':'', # 花花ck，[{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖','uid':'UID_xxx'},] 。uid是wxpusher一对一推送专属，其它无需配置。多账号添加大括号，注意不要漏逗号
}
