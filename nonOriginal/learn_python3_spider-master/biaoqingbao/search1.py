#-*- coding:UTF-8 -*-
import itchat
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud
from snownlp import SnowNLP
import re
import jieba
from jieba import analyse
import numpy as np
from PIL import Image
import csv
from pyecharts.charts import Map, Geo

def analyseSex(firends):
    sexs = list(map(lambda x: x['Sex'], friends[1:]))
    counts = Counter(sexs).items()
    counts = sorted(counts, key=lambda x: x[0], reverse=False)
    counts = list(map(lambda x: x[1], counts))
    # 0未知 1男 2女
    labels = ['未知', '小哥哥', '小姐姐']
    colors = ['yellowgreen', 'darkslateblue', 'orangered']
    plt.figure(figsize=(8, 5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts,
            labels=labels,
            colors=colors,
            labeldistance=1.1,
            autopct='%3.1f%%',
            shadow=False,
            startangle=90,
            pctdistance=0.6
            )
    plt.legend(loc='upper right', )
    plt.title(u'%s的微信好友性别比例' % friends[0]['NickName'])
    plt.show()


def analyseSignature(friends):
    signatures = ''
    emotions = []
    for friend in friends:
        # 获取好友的签名
        if (friend['Signature'] != '罗德坤'):
            signature = friend['Signature']
            print(friend['Signature'])
        if (signature != None):
            # 过滤掉标签和表情
            signature = signature.strip().replace('span', '').replace('class', '').replace('emoji', '')
            signature = re.sub(r'1f(\d.+)', '', signature)

            if (len(signature) > 0):
                # 分析标签
                nlp = SnowNLP(signature)
                # 获取情绪值
                emotions.append(nlp.sentiments)
                # 结巴分析
                signatures += ' '.join(jieba.analyse.extract_tags(signature, 5))

    # Sinature WordCloud
    # back_coloring = np.array(Image.open('baseketball.jpg'))
    wordcloud = WordCloud(
        font_path='simfang.ttf',
        background_color="white",
        max_words=1200,
        # mask=back_coloring,
        max_font_size=75,
        random_state=45,
        width=960,
        height=720,
        margin=15
    )

    # 生成云词
    wordcloud.generate(signatures)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file('signatures.jpg')

    # Signature Emotional Judgment
    count_good = len(list(filter(lambda x: x > 0.66, emotions)))
    count_normal = len(list(filter(lambda x: x >= 0.33 and x <= 0.66, emotions)))
    count_bad = len(list(filter(lambda x: x < 0.33, emotions)))
    labels = [u'负能量', u'中性', u'正能量满满']
    values = (count_bad, count_normal, count_good)
    plt.rcParams['font.sans-serif'] = ['simHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel(u'情感判断')
    plt.ylabel(u'频数')
    plt.xticks(range(3), labels)
    plt.legend(loc='upper right', )
    plt.bar(range(3), values, color='rgb')
    plt.title(u'%s的微信好友签名信息情感分析' % friends[0]['NickName'])
    plt.show()


def analyseLocation(friends):
    keys = []
    values = []
    province = list(map(lambda x: x['Province'], friends[1:]))

    for i in set(province):
        keys.append(i)
        values.append(province.count(i))

    print(keys)
    print(values)
    maps = Map('中国地图', '中国地图', width=1200, height=600)
    maps.add("", keys, values, visual_range=[0, 50], maptype='china', is_visualmap=True, visual_text_color='#000')
    maps.show_config()
    maps.render(path="localtion.html")


if __name__ == '__main__':
    # 解决PIL乱码
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    # 微信登录
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)
    itchat.send('11111', toUserName="filehelper")
    # print(friends)
    # 分析性别
    # analyseSex(friends)
    # 分析个签
    # analyseSignature(friends)
    # 分析位置
    # analyseLocation(friends)
