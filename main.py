import mysql.connector 
from pprint import pprint
import sys

queryFetch = lambda reference_code: f'''
SELECT ps_product_lang.description, ps_stock_available.quantity FROM ps_product_lang, ps_stock_available, ps_product
WHERE ps_product_lang.id_product = ps_stock_available.id_product
AND ps_product.id_product = ps_stock_available.id_product
AND ps_product.reference = "{reference_code}";
'''


queryChange = lambda new_description, reference_code: f'''
UPDATE ps_product_lang, ps_stock_available, ps_product 
SET ps_product_lang.description = "{new_description}" 
WHERE ps_product_lang.id_product = ps_stock_available.id_product 
AND ps_product.id_product = ps_stock_available.id_product 
AND ps_product.reference = "{reference_code}" 
'''


def fetch_data(db_info, reference_code):
    '''
    fetchuje tabelke z bazy danych

    :param db_info: dane bazy danych w formie słownika
    :reference_code: kod produktu
    :return: całą tabelke wyciągniętą z pliku
    '''
    cnx = mysql.connector.connect(
        user=db_info['user'],
        password=db_info['password'],
        host=db_info['host'],
        database=db_info['database']
    )
    cur = cnx.cursor()
    cur.execute(queryFetch(reference_code))
    date = cur.fetchall()
    
    cur.close()
    cnx.close()

    return date


def change_table(db_info, reference_code, data):
    '''
    podmienia wartość dla quantity w bazie danych

    :param db_info: dane bazy danych w formie słownika
    :param data: dane wyciągnięte z poprzedniej tabeli
    :reference_code: kod produktu
    '''

    raw = data[0]
    description = raw[0]
    ammount = raw[1]
    # print(ammount)
    # print(raw)
    description += f'\n<p>stan magazynowy: {ammount}</p>'
    # description += '\n' + str(raw[1])
    print(description)

    cnx = mysql.connector.connect(
        user=db_info['user'],
        password=db_info['password'],
        host=db_info['host'],
        database=db_info['database']
    )
    cur = cnx.cursor()
    cur.execute(queryChange(description, reference_code))
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

    reference_code = ''
    data = []
    try:
        reference_code = sys.argv[1]
    except:
        print("BŁĄD: poprawna składnia: main.py kod_produktu")
        exit()
    
    try:
        data = fetch_data(db_info, reference_code)
    except Exception as e:
        print('BŁĄD: nie można wyciągnąć danych:')
        raise e
    
    try:
        change_table( db_info, reference_code, data )
    except Exception as e:
        print('BŁĄD: nie można zmienić komórki:')
        raise e


if __name__ == '__main__':
    main()
else:
    print("Run from import")
