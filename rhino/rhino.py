import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
import re


def cor_id(m):
    if m == '应用程序':
        d_id = 'd4'
    elif m == '图块':
        d_id = 'd59'
    elif m == '曲线':
        d_id = 'd82'
    elif m == '尺寸标注':
        d_id = 'd198'
    elif m == '文档':
        d_id = 'd237'
    elif m == '几何':
        d_id = 'd257'
    elif m == '物件操作点':
        d_id = 'd286'
    elif m == '群组':
        d_id = 'd302'
    elif m == '填充图案':
        d_id = 'd319'
    elif m == '图层':
        d_id = 'd336'
    elif m == '灯光':
        d_id = 'd366'
    elif m == '直线':
        d_id = 'd391'
    elif m == '直线类型':
        d_id = 'd402'
    elif m == '材质':
        d_id = 'd407'
    elif m == '网格':
        d_id = 'd424'
    elif m == '物件':
        d_id = 'd469'
    elif m == '平面':
        d_id = 'd527'
    elif m == '点和向量':
        d_id = 'd546'
    elif m == '选取':
        d_id = 'd579'
    elif m == '曲面':
        d_id = 'd603'
    elif m == '工具列':
        d_id = 'd696'
    elif m == '变换':
        d_id = 'd712'
    elif m == '用户数据':
        d_id = 'd734'
    elif m == '用户界面':
        d_id = 'd745'
    elif m == '工具':
        d_id = 'd773'
    elif m == '视图':
        d_id = 'd791'
    else:
        d_id = 'd999'

    return d_id


def function_name(html, path):
    # 二级标题
    title_two = html.xpath('//div[@id="d3"]/div/nobr/a[@target="content"]/span/text()')
    for m in title_two:
        print(m)
        path1 = path + '/' + m
        is_exists = os.path.exists(path1)
        if not is_exists:
            os.makedirs(path1)

        title_three = html.xpath('//div/div[@id="' + str(cor_id(m)) + '"]/div/nobr/a[@target="content"]/span/text()')
        for i in title_three:
            print(i)
            source = 'http://bbs.rhino3d.asia/pythonhelp/scr/Functions/' + str(i) + '.htm'
            content = requests.get(source)
            content.encoding = 'utf-8'
            content_html = content.text

            h1 = BeautifulSoup(content_html, 'lxml').findAll('h1')[0].text
            if h1 == '404 Not Found':
                source = 'http://bbs.rhino3d.asia/pythonhelp/scr/Functions/' + str(i.lower()) + '.htm'
                content = requests.get(source)
                content.encoding = 'utf-8'
                content_html = content.text

            d1 = re.compile(r'<script language="JavaScript" type="text/JavaScript">[^>]+</script>', re.S)
            main_text = BeautifulSoup(d1.sub('', content_html), 'lxml')

            body_text = main_text.findAll('body')[0].text

            f = open(path1+'/'+str(i)+".text", 'wb')
            f.write(body_text.encode('utf-8'))
            f.close()

    print('数据获取结束')


def rhino():
    # 数据目录
    res = requests.get('http://bbs.rhino3d.asia/pythonhelp/webhelpcontents.htm')
    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    result = etree.tostring(html)

    # 一级标题
    title_one = html.xpath('//div/nobr/a[@target="content"]/span/text()')
    for n in title_one:
        # 创建文件夹
        path = 'function/' + n
        is_exists = os.path.exists(path)
        if not is_exists:
            os.makedirs(path)

        if n == 'Rhino/Python':
            print('')
        if n == '说明':
            print('')
        if n == '脚本示例':
            print('')
        if n == 'rhinoscript 函数库':
            print(n)
            function_name(html, path)


if __name__ == "__main__":
    rhino()