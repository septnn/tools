import pymysql

class fangDb:

    def insertUrl(self, url):
        sql = "INSERT INTO `fang_list` SET `url` = %s;"
        print(sql)
        return ''
        return self.exec(sql, (url));           

    def insertDetail(self, fkey, name, total, unit, house_loyout, house_turn, house_area, house_build, community, area, base_detail, transaction, special, house_img):
        sql = "INSERT INTO `fang_detail` SET `fkey` = %s, `name` = %s, `total` = %s, `unit` = %s, `house_loyout` = %s, `house_turn` = %s, `house_area` = %s, `house_build` = %s, `community` = %s, `area` = %s, `base_detail` = %s, `transaction` = %s, `special` = %s, `house_img` = %s;"
        print(sql)
        return ''
        return self.exec(sql, (fkey, name, total, unit, house_loyout, house_turn, house_area, house_build, community, area, base_detail, transaction, special, house_img));

    def exec(self, sql, val):
        try:
            with self.conn().cursor() as cursor: # with 自动关闭cursor.close()
                return cursor.execute(sql, val)
        finally:
            self.conn().close()
        return False

    def conn(self):
        return pymysql.connect( host="60.205.202.6",
                                user="dev",
                                password="ewDKkdQO",
                                database="test_dawei",
                                charset="utf8",
                                autocommit=True)

# def main():
#     urls = ['https://tj.ke.com/ershoufang/19121111410100123994.html', 'https://tj.ke.com/ershoufang/19121111410100122481.html', 'https://tj.ke.com/ershoufang/19121111410100120751.html', 'https://tj.ke.com/ershoufang/19121111410100119335.html', 'https://tj.ke.com/ershoufang/19121111410100114921.html', 'https://tj.ke.com/ershoufang/19121111410100118920.html', 'https://tj.ke.com/ershoufang/19121111410100118521.html', 'https://tj.ke.com/ershoufang/19121111410100116525.html', 'https://tj.ke.com/ershoufang/19121111410100118885.html', 'https://tj.ke.com/ershoufang/19121111410100115098.html', 'https://tj.ke.com/ershoufang/19121111410100117243.html', 'https://tj.ke.com/ershoufang/19121111410100119959.html', 'https://tj.ke.com/ershoufang/19121111410100114838.html', 'https://tj.ke.com/ershoufang/19121111410100112381.html', 'https://tj.ke.com/ershoufang/19121111410100113598.html', 'https://tj.ke.com/ershoufang/19121111410100114771.html', 'https://tj.ke.com/ershoufang/19121111410100112440.html', 'https://tj.ke.com/ershoufang/19121111410100111931.html', 'https://tj.ke.com/ershoufang/19121111410100110639.html', 'https://tj.ke.com/ershoufang/19121111410100110228.html', 'https://tj.ke.com/ershoufang/19121111410100109227.html', 'https://tj.ke.com/ershoufang/19121111410100108450.html', 'https://tj.ke.com/ershoufang/19121111410100108368.html', 'https://tj.ke.com/ershoufang/19121111410100106570.html', 'https://tj.ke.com/ershoufang/19121111410100108698.html', 'https://tj.ke.com/ershoufang/19121111410100102423.html', 'https://tj.ke.com/ershoufang/19121111410100107550.html', 'https://tj.ke.com/ershoufang/19121111410100106141.html', 'https://tj.ke.com/ershoufang/19121111410100103919.html', 'https://tj.ke.com/ershoufang/19121111410100102576.html']
#     urlInsert(urls)

# if __name__ == '__main__':
#     main()