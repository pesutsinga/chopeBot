import pymysql


class MySQLConnector:
    table = ''

    def __init__(self):
        self.table = ''
        self.db = pymysql.connect(
            host='bebong.id',
            user='u7728567_chope',
            password='bunuakumz578%&*',
            db='u7728567_chopebot',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def set_table(tablename):
        self.table = str(tablename)

    def update(**conditions, **values):
        pass

    def delete(**condition):
        pass

    def insert(**values):
        pass

    def select(**columns, **conditions, ext=''):
        pass
