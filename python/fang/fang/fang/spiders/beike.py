import scrapy;
import fang.spiders.fangDb as fangDb;

class beike(scrapy.Spider):
    name = "beike"

    def start_requests(self):
        urls = [];
        for num in range(100):
            t = 'https://tj.ke.com/ershoufang/' + "pg" + str(num) + "co32/"
            urls.append(t)
        urls = [
            'https://tj.ke.com/ershoufang/pg3co32/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath('//a[@class="img VIEWDATA CLICKDATA maidian-detail"]/@href').getall()
        urls = [
            'https://tj.ke.com/ershoufang/19121411410100117140.html'
        ]
        for url in urls:
            # fangDb.insertUrl(url)
            self.detail(url)

        # filename = 'quotes.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s ' % filename)
    def detail(self, url):
        scrapy.Request(url=url, callback=self.parse)
    def detailCallback(self, response):
        fkey = response.xpath('//head/title/text()').get()
        name = response.xpath('//h1[@class="main"]/@title').get()
        total = response.xpath('//span[@class="total"]/text()').get()
        unit = response.xpath('//span[@class="unitPrice"]/text()').get()
        house_loyout = response.xpath('//div[@class="room"]/div[@class="mainInfo"]/text()').get()
        house_turn = response.xpath('//div[@class="type"]/div[@class="mainInfo"]/text()').get()
        house_area = response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').get()
        house_build = response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').get()
        community = response.xpath('//div[@class="communityName"]/a[@class="info no_resblock_a"]/text()').get()
        area = response.xpath('//div[@class="areaName"]/a"]/text()').getAll() # 多个
        base_detail = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li').getall() # 多个
        transaction = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li').getall() # 多个
        special = response.xpath('//div[@class="introContent showbasemore"]//a/text()').getall() # 多个
        house_img = response.xpath('//div[@class="imgdiv"]/@data-img').get() # 多个
        fangDb.insertDetail(fkey,
                            name,
                            total,
                            unit,
                            house_loyout,
                            house_turn,
                            house_area,
                            house_build,
                            community,
                            area,
                            base_detail,
                            transaction,
                            special,
                            house_img)
