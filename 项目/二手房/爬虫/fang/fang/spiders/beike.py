import scrapy;

from fang.spiders.fangDb import *

class beike(scrapy.Spider):
    name = "beike"
    def __init__(self):
        self.fangDb = fangDb()

    def start_requests(self):
        # 清空表
        self.fangDb.truncate()
        urls = [];
        for num in range(100):
            t = 'https://tj.ke.com/ershoufang/' + "pg" + str(num) + "mw1su1ty1bt2dp1sf1bp50ep150/"
            urls.append(t)
        # urls = [
        #     'https://tj.ke.com/ershoufang/pg2mw1su1ty1bt2dp1sf1bp50ep150/',
        # ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for li in response.xpath('//li[@class="clear"]'):
            url = li.xpath('./a/@href').get()
            name = li.xpath('./a/@title').get()
            community = li.xpath('./div/div[@class="address"]/div[@class="flood"]/div[@class="positionInfo"]/a/text()').get()
            layout = li.xpath('./div/div[@class="address"]/div[@class="houseInfo"]/text()').getall()[1]
            tag = ','.join(li.xpath('./div/div[@class="address"]/div[@class="tag"]/span/text()').getall())
            total = li.xpath('./div//div[@class="totalPrice"]/span/text()').get()
            unit = li.xpath('./div//div[@class="unitPrice"]/@data-price').get()
            # print([url,name,community,layout,tag,total,unit])
            print(self.fangDb.insertUrl(url,name,community,layout,tag,total,unit))
            yield scrapy.Request(url=url, callback=self.detailCallback)
            
    def detailCallback(self, response):
        url = response.url
        fkey = response.xpath('//head/title/text()').get()
        name = response.xpath('//h1[@class="main"]/@title').get()
        total = response.xpath('//span[@class="total"]/text()').get()
        unit = response.xpath('//span[@class="unitPriceValue"]/text()').get()
        house_loyout = response.xpath('//div[@class="room"]/div[@class="mainInfo"]/text()').get()
        house_turn = response.xpath('//div[@class="type"]/div[@class="mainInfo"]/text()').get()
        house_area = response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').get()
        house_build = response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').get()
        community = response.xpath('//div[@class="communityName"]/a[@class="info no_resblock_a"]/text()').get()
        area = ','.join(response.xpath('//div[@class="areaName"]').getall()) # 多个
        base_detail = ','.join(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li').getall()) # 多个
        transaction = ','.join(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li').getall()) # 多个
        special = ','.join(response.xpath('//div[@class="introContent showbasemore"]//a/text()').getall()) # 多个
        house_img = response.xpath('//div[@class="thumbnail"]//li[@data-desc="户型图"]/@data-pic').get()
        self.fangDb.insertDetail(url, fkey, name, total, unit, house_loyout, house_turn, house_area, house_build, community, area, base_detail, transaction, special, house_img)

        # filename = 'quotes.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s ' % filename)
