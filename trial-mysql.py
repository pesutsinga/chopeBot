from chopeDB import MySQLConnector


def main():
    db = MySQLConnector('u7728567_chopebot')
    argum = []
    argum.append(("TELEGRAMID", 's', 'apalahakuini' ))
    argum.append(("USERNAME", 's', 'gabisaapaapa'))
    argum.append(("PASSWORD", 's', 'mengalakepadatuhan'))
    db.insert("LIBCHOP", argum)
    db.close()
    

if __name__ == '__main__':
    main()
