# !/usr/bin/python3
import pymysql


class Conn_server:
    # 数据库连接
    def __init__(self, host, user, password, database, port, charset):
        """
        :param host: 访问服务端的ip
        :param user: 访问服务端的用户
        :param password: 访问服务端的用户密码
        :param database: 访问服务端的数据库
        :param port: 端口号
        :param charset: 访问时采用的编码方式
        """
        self.ht = host
        self.ur = user
        self.pd = password
        self.de = database
        self.pt = port
        self.ct = charset

        # 连接数据库服务端
        self.conn = pymysql.connect(host=self.ht, user=self.ur, password=self.pd, database=self.de, port=self.pt, charset=self.ct)

        # 创建游标，使用cursor()方法获取操作游标
        self.Cursor = self.conn.cursor()

    # 数据库查询
    def getData(self, sel):
        # execute()执行单条sql语句
        self.Cursor.execute(sel)

        # 查询cursor的rowcount属性获得查询结果条数
        if self.Cursor.rowcount != 0:
            # fetchall()接收全部的返回结果行.
            results = self.Cursor.fetchall()
            print(results)


cur = Conn_server("36.110.79.162", "test001", "smzycc", "ddz_user_data", 3306, "UTF8")
cur.getData('SELECT * FROM admin WHERE uid =1')

