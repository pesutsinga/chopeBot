import pymysql


class MySQLConnector:
    def __init__(self):
        self.table = ''
        self.connection = pymysql.connect(
            host='bebong.id',
            user='u7728567_chope',
            password='bunuakumz578%&*',
            db='u7728567_chopebot',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def close(self):
        self.connection.close()

    def update(self, table, conditions):
        pass

    def delete(self, table, conditions):
        pass

    def insert(self, table, values):
        """
        Documentation:
        table: string
        values: list of tuples
        """
        cols = ', '.join([('`' + elm[0] + '`') for elm in values])
        print(cols)

        types = ', '.join([("%" + elm[1]) for elm in values])
        print(types)

        statement = (
            "INSERT INTO " + table
            + " (" + cols + ") "
            + "VALUES (" + types + ")")
        print(statement)

        args = tuple([elm[2] for elm in values])
        print(args)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(statement, args)
            self.connection.commit()
        finally:
            pass

    def select(self, table, ext='', **columns):
        pass
