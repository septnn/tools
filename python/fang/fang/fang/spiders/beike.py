import scrapy;
import fang.spiders.fangDb as fangDb;

class beike(scrapy.Spider):
    name = "beike"

    def start_requests(self):
        urls = [];
        for num in range(100):
            t = 'https://tj.ke.com/ershoufang/' + "pg" + str(num) + "co32/"
            urls.append(t)
        # urls = [
        #     'https://tj.ke.com/ershoufang/pg3co32/',
        # ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath('//a[@class="img VIEWDATA CLICKDATA maidian-detail"]/@href').getall()
        for url in urls:
            fangDb.urlInsert(url)
            self.detail(url)

        # filename = 'quotes.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s ' % filename)
    def detail(url):
        scrapy.Request(url=url, callback=self.parse)
    def detailCallback(self, response):
        urls = response.xpath('//a[@class="img VIEWDATA CLICKDATA maidian-detail"]/@href').getall()
