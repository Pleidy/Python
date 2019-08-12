import requests
from lxml import etree
from lxml import html
from lxml import etree as ElementTree
import time
import pymysql
import csv


# 定义函数抓取每页前30条商品信息
etree = html.etree
def crow_first(n):
    # 构造每一页的url变化
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page='+str(
        2 * n - 1)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=2&s=29&scrolling=y&log_id=1553997370.48777&tpl=3_M&show_items=100001172674,5089235,100001467225,100000651175,100000287145,8735304,6946605,7437564,100003332220,100000177756,100000349372,100000822981,100000773875,5089225,7081550,7920226,100003475378,100000287133,100000971366,6949475,7479810,5089273,8790521,100000820311,100003490442,100001364160,7651927,100000650837,7437786,100003936976',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=af4a92d694a5484d8c71efd3680f3f4d',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': '__jdu=2144065523; PCSYCityID=4; shshshfpa=fb96e5e7-9532-7619-ca05-d154e6d365b8-1553958792; shshshfpb=cQdnr5Sham%2FaQ9QVTXgAEFw%3D%3D; xtest=74.cf6b6759; ipLoc-djd=1-72-2799-0; qrsc=3; __jdc=122270672; ipLocation=%u5317%u4EAC; areaId=1; unpl=V2_ZzNtbUECEUVxXRRSLklbUGICQAhLX0BCcQBFXHIQXwBuBRUPclRCFX0UR1ZnG1wUZgsZWENcQRNFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHgZWQBmBBZZQVVzJXI4dmRzHl4EZQIiXHJWc1chVENWcxhdSGQDF1hDUEcRdgp2VUsa; __jda=122270672.2144065523.1552739118.1553994173.1553996458.4; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2dca5dc7da6d40cd892f59298824876c|1553996458170; shshshfp=79567a68de0261331ad4a4e1fe138e7a; rkv=V0400; 3AB9D23F7A4B3C9B=KD52ZZBUKOHXCD7EZ6VDJLMKTADTGGG4FXR5RX6B2FJDBH6KHBBMRJSCRWKCV5WAY4CIH5O7MDP2JSUB67I4TRHZ5I; __jdb=122270672.5.2144065523|4.1553996458; shshshsID=3e486e1a717c803e1f9d240196dc337c_5_1553998105495',
            }
    r = requests.get(url, headers=head)
    # 指定编码方式，不然会出现乱码
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    # 定位到每一个商品标签li
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    phone_data(datas)
# 定义函数抓取每页后30条商品信息
def crow_last(n):
    # 获取当前的Unix时间戳，并且保留小数点后5位
    a = time.time()
    b = '%.5f' % a
    url = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' + str(
        2 * n) + '&s=' + str(48 * n - 20) + '&scrolling=y&log_id=' + str(b)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=2&s=29&scrolling=y&log_id=1553997370.48777&tpl=3_M&show_items=100001172674,5089235,100001467225,100000651175,100000287145,8735304,6946605,7437564,100003332220,100000177756,100000349372,100000822981,100000773875,5089225,7081550,7920226,100003475378,100000287133,100000971366,6949475,7479810,5089273,8790521,100000820311,100003490442,100001364160,7651927,100000650837,7437786,100003936976',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=af4a92d694a5484d8c71efd3680f3f4d',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': '__jdu=2144065523; PCSYCityID=4; shshshfpa=fb96e5e7-9532-7619-ca05-d154e6d365b8-1553958792; shshshfpb=cQdnr5Sham%2FaQ9QVTXgAEFw%3D%3D; xtest=74.cf6b6759; ipLoc-djd=1-72-2799-0; qrsc=3; __jdc=122270672; ipLocation=%u5317%u4EAC; areaId=1; unpl=V2_ZzNtbUECEUVxXRRSLklbUGICQAhLX0BCcQBFXHIQXwBuBRUPclRCFX0UR1ZnG1wUZgsZWENcQRNFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHgZWQBmBBZZQVVzJXI4dmRzHl4EZQIiXHJWc1chVENWcxhdSGQDF1hDUEcRdgp2VUsa; __jda=122270672.2144065523.1552739118.1553994173.1553996458.4; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2dca5dc7da6d40cd892f59298824876c|1553996458170; shshshfp=79567a68de0261331ad4a4e1fe138e7a; rkv=V0400; 3AB9D23F7A4B3C9B=KD52ZZBUKOHXCD7EZ6VDJLMKTADTGGG4FXR5RX6B2FJDBH6KHBBMRJSCRWKCV5WAY4CIH5O7MDP2JSUB67I4TRHZ5I; __jdb=122270672.5.2144065523|4.1553996458; shshshsID=3e486e1a717c803e1f9d240196dc337c_5_1553998105495',
            }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    phone_data(datas)

def phone_data(datas):
    for data in datas:
        # 手机名
        p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')[0].split(',')[0]
        # 价格
        p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')[0]
        # 商品完整名称
        p_name1 = \
        data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')[0].split(',')[0].split(' ')[0].split('【')[0]
        data_sku = data.xpath('div/div[@class="p-focus"]/a/@data-sku')[0]
        commit_url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + str(data_sku)
        parameter_url = 'https://item.jd.com/' + data_sku + '.html'
        parameter_head = {
            'Host': 'blackhole.m.jd.com',
            'Origin': 'https://item.jd.com',
            'Referer': 'https://item.jd.com/41633722698.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.3'
        }
        # 获取评论量
        comments = requests.get(commit_url).json()['CommentsCount'][0]['CommentCountStr']
        parameter = requests.get(parameter_url, parameter_head)
        parameter_html = etree.HTML(parameter.text)
        for i in range(1, 14):
            phone_cs = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/h3/text()')[0]  # 获取手机参数
            if phone_cs == '主体':
                phone_brand = \
                parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[0].split('\n')[0]  # 获取品牌
                if not phone_brand:
                    phone_model = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[3]  # 获取型号
                    phone_net_model = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[7]  # 获取入网型号
                    list_year_time = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[8]  # 获取上市年份
                    list_month_time = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[9]  # 获取上市月份
                else:
                    phone_model = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[4]  # 获取型号
                    phone_net_model = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[8]  # 获取入网型号
                    list_year_time = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[9]  # 获取上市年份
                    list_month_time = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[10]  # 获取上市月份
            elif phone_cs == '操作系统':
                system = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl/dd/text()')[0]  # 获取操作系统
            elif phone_cs == '主芯片':
                cpu_kernel = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl[3]/dd/text()')[0]  # 获取处理器信息：核数
                cpu_model = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl[4]/dd/text()')[0]  # 获取处理器信息：型号
            elif phone_cs == '屏幕':
                screen_size = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl[1]/dd/text()')[0]  # 获取屏幕尺寸
                screen_resolution = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl[2]/dd/text()')[0]  # 获取屏幕分辨率
            elif phone_cs == '电池信息':
                capacity = parameter_html.xpath('//div[@class="tab-con"]/div[2]/div[1]/div[' + str(i) + ']/dl/dl[1]/dd/text()')[0]  # 获取电池大小
        list_time = list_year_time + list_month_time
        # print(phone_cs)
        # print(phone_brand)
        # print(phone_model)
        # print(phone_net_model)
        # print(list_year_time)
        # print(list_month_time)
        # print(system)
        # print(cpu_kernel)
        # print(cpu_model)
        # print(screen_size)
        # print(screen_resolution)
        # print(capacity)
        # print(comments)
        # exit()
        # 这个if判断用来处理那些价格可以动态切换的商品，比如上文提到的小米MIX2，他们的价格位置在属性中放了一个最低价
        if len(p_price) == 0:
            p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
        db = pymysql.connect("localhost", "root", "root", "jd")
        cursor = db.cursor()
        sql = "INSERT INTO jd_phone_data(name,phone_info,price,volum,phone_brand,phone_model,phone_net_model,list_time,phone_system,cpu_kernel,cpu_model,screen_size,screen_resolution,capacity) values ('" + str(
            p_name1) + "','" + str(p_name) + "'," + str(p_price) + ",'" + str(comments) + "','" + str(
            phone_brand) + "','" + str(phone_model) + "','" + str(phone_net_model) + "','" + str(
            list_time) + "','" + str(system) + "','" + str(cpu_kernel) + "','" + str(cpu_model) + "','" + str(
            screen_size) + "','" + str(screen_resolution) + "','" + str(capacity) + "')"
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()

if __name__ == '__main__':
    for i in range(1, 101):
        # 下面的print函数主要是为了方便查看当前抓到第几页了
        print('***************************************************')
        try:
            print('   First_Page:   ' + str(i))
            crow_first(i)
            print('   Finish')
        except Exception as e:
            print(e)
        print('------------------')
        try:
            print('   Last_Page:   ' + str(i))
            # exit()
            crow_last(i)
            print('   Finish')
        except Exception as e:
            print(e)