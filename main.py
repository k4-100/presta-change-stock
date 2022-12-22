import mysql.connector 
from pprint import pprint
import sys

queryFetch = '''
SELECT ps_stock_available.quantity FROM ps_stock_available, ps_product
WHERE ps_stock_available.id_product =  ps_product.id_product
AND ps_product.reference = "food_2";
'''


queryChange = lambda new_stock, reference_code: f'''
UPDATE ps_stock_available, ps_product
SET ps_stock_available.quantity = {new_stock}
WHERE ps_stock_available.id_product = ps_product.id_product
AND ps_product.reference = "{reference_code}";
'''


# def fetch_table(db_info):
#     '''
#     fetchuje tabelke z bazy danych

#     :param db_info: dane bazy danych w formie słownika
#     :return: całą tabelke wyciągniętą z pliku
#     '''
#     cnx = mysql.connector.connect(
#         user=db_info['user'],
#         password=db_info['password'],
#         host=db_info['host'],
#         database=db_info['database']
#     )
#     cur = cnx.cursor()
#     cur.execute(queryFetch)
#     table = cur.fetchall()
#     
#     cur.close()
#     cnx.close()

#     return table


def change_table(db_info, reference_code, new_stock):
    '''
    podmienia wartość dla quantity w bazie danych

    :param db_info: dane bazy danych w formie słownika
    '''
    cnx = mysql.connector.connect(
        user=db_info['user'],
        password=db_info['password'],
        host=db_info['host'],
        database=db_info['database']
    )
    cur = cnx.cursor()
    cur.execute(queryChange(new_stock, reference_code))
    cnx.commit()

    cur.close()
    cnx.close()



def main():
    db_info = {
        "user": "root",
        "password": "",
        "host": "127.0.0.1",
        "database": "prestashop_1_6"
    }
    
    try:
        change_table(db_info, sys.argv[1], sys.argv[2])
    except:
        print("BŁĄD: poprawna składnia: main.py kod_produktu nowa_ilość")


if __name__ == '__main__':
    main()
else:
    print("Run from import")
