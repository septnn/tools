import pymysql
from w3lib.html import remove_tags
import re

class fangDb:

    def f(self, value):
        # 移除标签
        content = remove_tags(value)
        # 移除空格 换行
        return re.sub(r'[\t\r\n\s]', '', content)

    def insertUrl(self, url, name, community, layout, tag, total, unit):
        sql = "INSERT INTO `fang_list` SET `url` = %s, `name` = %s, `community` = %s, `layout` = %s, `tag` = %s, `total` = %s, `unit` = %s;"
        return self.exec(sql, [url, name, community, layout, tag, total, unit]);           

    def insertDetail(self, url, fkey, name, total, unit, house_loyout, house_turn, house_area, house_build, community, area, base_detail, transaction, special, house_img):
        sql = "INSERT INTO `fang_detail` SET `url` = %s, `fkey` = %s, `name` = %s, `total` = %s, `unit` = %s, `house_loyout` = %s, `house_turn` = %s, `house_area` = %s, `house_build` = %s, `community` = %s, `area` = %s, `base_detail` = %s, `transaction` = %s, `special` = %s, `house_img` = %s;"
        return self.exec(sql, [url, fkey, name, total, unit, house_loyout, house_turn, house_area, house_build, community, self.f(area), self.f(base_detail), self.f(transaction), self.f(special), house_img]);
        # return self.exec(sql, [url, fkey, name, total, unit, house_loyout, house_turn, house_area, house_build, community, area, base_detail, transaction, special, house_img]);
    
    def truncate(self):
        sql = "TRUNCATE `fang_list`;"
        self.exec(sql, [])
        sql = "TRUNCATE `fang_detail`;"
        return self.exec(sql, [])

    def exec(self, sql, val):
        try:
            with self.conn().cursor() as cursor: # with 自动关闭cursor.close()
                return cursor.execute(sql, val)
        finally:
            self.conn().close()
        return False

    def conn(self):
        return pymysql.connect( host="192.168.31.224",
                                user="test",
                                password="123456",
                                database="fang",
                                charset="utf8",
                                autocommit=True)

# def main():
#     urls = ['https://tj.ke.com/ershoufang/19121111410100123994.html', 'https://tj.ke.com/ershoufang/19121111410100122481.html', 'https://tj.ke.com/ershoufang/19121111410100120751.html', 'https://tj.ke.com/ershoufang/19121111410100119335.html', 'https://tj.ke.com/ershoufang/19121111410100114921.html', 'https://tj.ke.com/ershoufang/19121111410100118920.html', 'https://tj.ke.com/ershoufang/19121111410100118521.html', 'https://tj.ke.com/ershoufang/19121111410100116525.html', 'https://tj.ke.com/ershoufang/19121111410100118885.html', 'https://tj.ke.com/ershoufang/19121111410100115098.html', 'https://tj.ke.com/ershoufang/19121111410100117243.html', 'https://tj.ke.com/ershoufang/19121111410100119959.html', 'https://tj.ke.com/ershoufang/19121111410100114838.html', 'https://tj.ke.com/ershoufang/19121111410100112381.html', 'https://tj.ke.com/ershoufang/19121111410100113598.html', 'https://tj.ke.com/ershoufang/19121111410100114771.html', 'https://tj.ke.com/ershoufang/19121111410100112440.html', 'https://tj.ke.com/ershoufang/19121111410100111931.html', 'https://tj.ke.com/ershoufang/19121111410100110639.html', 'https://tj.ke.com/ershoufang/19121111410100110228.html', 'https://tj.ke.com/ershoufang/19121111410100109227.html', 'https://tj.ke.com/ershoufang/19121111410100108450.html', 'https://tj.ke.com/ershoufang/19121111410100108368.html', 'https://tj.ke.com/ershoufang/19121111410100106570.html', 'https://tj.ke.com/ershoufang/19121111410100108698.html', 'https://tj.ke.com/ershoufang/19121111410100102423.html', 'https://tj.ke.com/ershoufang/19121111410100107550.html', 'https://tj.ke.com/ershoufang/19121111410100106141.html', 'https://tj.ke.com/ershoufang/19121111410100103919.html', 'https://tj.ke.com/ershoufang/19121111410100102576.html']
#     urlInsert(urls)

# if __name__ == '__main__':
#     main()
