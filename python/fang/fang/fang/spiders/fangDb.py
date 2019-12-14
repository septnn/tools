import pymysql


def urlInsert(url):
    sql = "INSERT INTO `fang_list` SET `url` = %s;";
    try:
        with conn().cursor() as cursor: # with 自动关闭cursor.close()
            cursor.execute(sql, (url))
    finally:
        conn().close()            
        

def conn():
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