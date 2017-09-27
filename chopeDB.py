import pymysql
from util import VPrinter


class MySQLConnector:
    """
        jadi kalo mau connect ke db tinggal MySQLConnector(namadb)
        terus di assign ke variable mis:
        db = MySQLConnector("apalah")
        
        terus pas misal mau insert tinggal
        db.insert('tablename', arguments)
        coba liat trial-mysql.py kalo mo coba" 
        makasih :)
    """
    def __init__(self, database):
        self.connection = pymysql.connect(
            host='bebong.id',
            user='u7728567_chope',
            password='bunuakumz578%&*',
            db=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def close(self):
        self.connection.close()

    def update(self, table, conditions):
        pass

    def delete(self, table, conditions):
        pass

    def insert(self, table, data=[]):
        """
        insert documentation
        table: string
        data: list of tuples (colname, type, value)
            e.g. ('favCartoonCharacter', 's', 'Donald Duck')
            's' denotes string
            'd' denotes decimal (number)
            'f' denotes float
            et cetera.
        """
        v = VPrinter(True)

        colName = ', '.join([('`' + elm[0] + '`') for elm in data])
        v.vprint(colName)
        colType = ', '.join([("%" + elm[1]) for elm in data])
        v.vprint(colType)

        statement = (
            "INSERT INTO " + table
            + " (" + colName + ") "
            + "VALUES (" + colType + ")")
        v.vprint(statement)

        args = tuple([elm[2] for elm in data])
        v.vprint(args)

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(statement, args)
            self.connection.commit()
        finally:
            pass

    def select(self, table, columns):
        pass
