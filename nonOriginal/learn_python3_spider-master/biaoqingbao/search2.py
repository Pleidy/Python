#-*- coding:UTF-8 -*-
import itchat
import requests
from itchat.content import TEXT
from itchat.content import *
import time
import json
# from itchat.content import TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO

# 微信登录
# itchat.auto_login(hotReload=True)
# itchat.auto_login(enableCmdQR=True)
# itchat.auto_login(enableCmdQR=0)
# friends = itchat.get_friends(update=True)
# itchat.send('11111', toUserName="filehelper")



# 自动回复消息设置
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    friends = itchat.get_friends(update=True)
    for friend in friends:
        if msg['FromUserName'] == friend['UserName']:
            return '【暂时不在线】' + robotText(msg['Text'])
            # if friend['RemarkName']:
            #     return '收到' + friend['RemarkName'] + '发来的消息：' + msgText
            # else:
            #     return '收到' + friend['NickName'] + '发来的消息：' + msgText

# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     friends = itchat.get_friends(update=True)
#     for friend in friends:
#         if msg['FromUserName'] == friend['UserName']:
#             t0 = time.localtime()[4]
#             while True:
#                 t1 = time.localtime()[4]
#
#                 if t1 - t0 >= 1:  # 1分钟
#                     # *********判断APP上是否已经回复过了*********
#                     itchat.send_msg('自动回复：有事不在，晚点回复', msg['FromUserName'])
#                     break


# @itchat.msg_register(itchat.content.TEXT)
# def tuling_reply(msg):
#     defaultReply = 'I received: ' + msg['Text']
#     reply = get_response(msg['Text'])
#     return reply or defaultReply


# def get_response(_info):
#     api_url = 'http://www.tuling123.com/openapi/api'   # 图灵机器人网址
#     data = {
#         'key': 'b59a4fecfa104f578b922ec6638266be',     # 如果这个 apiKey 如不能用，那就注册一次
#         'info': _info,                                 # 这是我们从好友接收到的消息 然后转发给图灵机器人
#         'userid': 'wechat-robot',                      # 这里你想改什么都可以
#     }
#     try:
#         r = requests.post(api_url, data=data).json()   # 把data数据发
#         print(r)
#         return r.get('text')
#     except:
#         return


# 青云客智能聊天机器人
def robotText(msg):
    api_url = 'http://api.qingyunke.com/api.php'  # 智能聊天接口地址

    content = {'key': 'free', 'appid': 0, 'msg': msg}
    r = requests.get(url=api_url, params=content)

    return json.loads(r.text).get('content')


# 微信好友、群组数量
def number(friends, groups):
    print("群数量:", len(groups))
    for i in range(0, len(groups)):
        print(i + 1, "--", groups[i]['NickName'], groups[i]['MemberCount'], "人")
    print("好友数量", len(friends) - 1)
    for f in range(1, len(friends)):
        # 优先使用好友的备注名称，没有则使用昵称
        if friends[f]['RemarkName']:
            user_name = friends[f]['RemarkName']
        else:
            user_name = friends[f]['NickName']
        # 打印对应性别
        if friends[f]['Sex'] == 2:
            print(f, "--", user_name, '女')
        else:
            print(f, "--", user_name, '男')

# 微信公众号数据信息
def pub(mpsList):
    print("公众号数量:", len(mpsList))
    for it in mpsList:
        print(it['NickName'] + ':' + it['Signature'])




# itchat.auto_login()
itchat.auto_login(hotReload=True)
# itchat.auto_login(enableCmdQR=True)  # 命令行显示登陆二维码

# 获取微信好友列表
# friends = itchat.get_friends(update=True)
# 获取微信群组列表
# groups = itchat.get_chatrooms(update=True)
# 获取微信公众号信息
# mpsList = itchat.get_mps(update=True)[1:]



# 对应功能函数
# number(friends, groups)
# pub(mpsList)

itchat.run()
# itchat.send(u'测试消息发送', 'filehelper') # 发送文件传输助手信息

