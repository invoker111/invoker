import re, urllib.request, os, base64
from bs4 import BeautifulSoup

same_patter = re.compile(r'a\sonclick="window.parent.location.href=.*?">(.*?)</a>')


# 找出一个关键词的类似9个关键词
def search_same(name):
    text = name.encode('gbk')
    text = 'https://m.baidu.com/recsys/ui/api/rs?query=' + urllib.request.quote(text) + '&title=arp&url=https%3A%2F%2Fzhidao.baidu.com%2Fsearch%3Fct%3D17%26pn%3D0%26tn%3Dikaslist%26rn%3D10%26fr%3Dwwwt%26word%3Darp&ak=ZQ4m31EXvKem1HPYzaK8Ekq6opqfhKFK&pc=1&charset=gbk&contentTitleText=%E5%8E%BB%E7%BD%91%E9%A1%B5%E6%90%9C%E7%B4%A2&entityNum=9&tn=SE_PcZhidaoqwyss_e1nmnxgw&random=0911'
    html = urllib.request.urlopen(text).read()
    soup = str(BeautifulSoup(html, 'html.parser', from_encoding='utf-8')).split('\n')
    soup = ''.join(soup)
    same_list = re.findall(same_patter, soup)
    return same_list


# 找出所有关键词
def create_list(lis, how):
    for name in lis:
        new_lis = search_same(name)
        for new_name in new_lis:
            if new_name not in lis:
                if len(lis) < how:
                    lis.append(new_name)
                else:
                    # 达到数量，return
                    return lis
    # 没达到数量就递归调用（广度遍历）
    create_list(lis, how)


def start(name, how):
    all_item = [name]
    new = create_list(all_item, how)
    print('所有相似的词：', new)
    # 依次执行所有爬虫
    # for name in new:
    #     sql = 'scrapy crawl zhidao_spider -a nam=%s' % name
    #     os.system(sql)
    os.chdir(r'C:\Users\qiang\Desktop\curl\bin')
    for name in new:
        bname = bytes(name, encoding='utf-8')

        sql = 'curl http://127.0.0.1:6800/schedule.json -d project=zhidao_spider -d spider=zhidao_spider -d nam=%s' \
              % base64.b64encode(bname).decode('utf-8')
        os.system(sql)
        print('关键词%s的爬虫部署成功！' % name)


if __name__ == '__main__':
    n = input('输入搜索开始关键词----->')
    h = input('请输入搜索类似关键词个数（自动寻找）----->')
    start(n, int(h))
