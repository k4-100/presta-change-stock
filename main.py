import mysql.connector 
from pprint import pprint

def fetch_table(db_info):
    '''

    '''
    cnx = mysql.connector.connect(
        user=db_info['user'],
        password=db_info['password'],
        host=db_info['host'],
        database=db_info['database']
    )
    cur = cnx.cursor()
    cur.execute('SELECT * FROM ps_stock_available')
    table = cur.fetchall()
    
    cnx.close()
    

    return table


def main():
    db_info = {
        "user": "root",
        "password": "",
        "host": "127.0.0.1",
        "database": "prestashop_1_6"
    }

    pprint( fetch_table(db_info) )


if __name__ == '__main__':
    main()
else:
    print("Run from import")
