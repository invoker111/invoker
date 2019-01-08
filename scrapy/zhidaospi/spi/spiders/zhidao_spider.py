# -*- coding: utf-8 -*-
import scrapy, base64
import re
from spi.items import SpiItem
from jieba.analyse import *
import urllib.request


class ZhidaoSpiderSpider(scrapy.Spider):
    name = 'zhidao_spider'

    def __init__(self, nam='软件', *args, **kwargs):
        # #####################传入参数#########################
        # nam = base64.b64decode(nam).decode('utf-8')
        super().__init__(name=nam)
        self.search_name = urllib.request.quote(nam)
        self.allowed_domains = ['zhidao.baidu.com']
        start_url = 'https://zhidao.baidu.com/search?word='+self.search_name
        self.start_urls = [start_url]
        self.finish_page = 0

    # 爬取主页面内容
    def parse(self, response):
        all_item = response.xpath("/html/body/div[3]/section/div/div/div/div[2]/div[1]/dl/dt/a/@href").extract()
        item_list = []
        if self.finish_page < 75:
            try:
                page = response.xpath('/html/body/div[3]/section/div/div/div/div[2]/div[2]/div/a[@class="pager-next"]/@href').extract_first()
                page = 'https://zhidao.baidu.com' + page
                self.finish_page += 1
                # 下一页，回调本身
                yield scrapy.Request(url=page, callback=self.parse)
            except:
                pass
        for i in all_item:
            if re.match('http://zhidao', i):
                item_list.append(i)
        for url in item_list:
            # item传给parse_main
            yield scrapy.Request(url=url, callback=self.parse_main)

    # 爬取item的信息
    def parse_main(self, response):
        answers = []
        title = response.xpath('/html/body/div[4]/div/section/article/div[1]/h1/span[@class="ask-title"]/text()').extract_first()
        try:
            best_answer = response.xpath("//*[starts-with(@id,'best-content')]").extract_first()
            best_answer = re.search(r'</div>\n</div>\n(.*)\n</div>', best_answer).group(1)
            best_answer = re.sub('<.*?>', '', best_answer)
        except:
            best_answer = 'None'
        answer = response.xpath("//div[@class='wgt-answers has-other  ']//div[@accuse='aContent']").extract()
        for ans in answer:
            try:
                ans = re.search(r'</div>\n</div>\n(.*)\n</div>', ans).group(1)
                ans = re.sub('<.*?>', '', ans)
            except:
                ans = 'None'
            answers.append(ans)
        answers = str(answers)
        word = ''
        for key, weight in textrank(answers+best_answer, withWeight=True):
            word += key
            word += '||'
        # ###############传给管道处理##############
        dic = SpiItem()
        dic['title'] = str(title)
        dic['best_answer'] = str(best_answer)
        dic['answers'] = str(answers)
        dic['word'] = str(word)
        yield dic
