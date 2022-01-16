from mysql.connector import connect, Error
import sshtunnel

tunnel = sshtunnel.SSHTunnelForwarder(
    ssh_username='ag3131',
    ssh_password='GoForthGo',
    ssh_address_or_host='192.168.0.66',
    ssh_port=22,
    remote_bind_address=('127.0.0.1', 3306)
)


tunnel.start()

global connection

try:

    connection = connect (
        host='localhost',
        user='root',
        passwd='Science',
        database='data_source',
        port=tunnel.local_bind_port
    )

except Error:
    print(f'Ошибка -  {Error}')


cur = connection.cursor()

cur.execute('SELECT CURDATE()')

row = cur.fetchone()

print(f"Date - {row}")
#
# #
# cur.execute('USE logical_data_model;')
cur.execute('DESCRIBE sys;')
row = cur.fetchall()
for el in row:
    print(el)


def get_tables_count(table_name):
    cur.execute(f'SELECT COUNT(*) FROM {table_name}')
    tuple_result = cur.fetchone()
    return int(tuple_result[0])


print(get_tables_count('sys'))


def get_rows(table_name, count):
    i = 0
    cur.execute(f'SELECT * FROM {table_name}')
    tuple_result = cur.fetchall()
    while i < count:
        print(tuple_result[i])
        i += 1
    return


get_rows('sys', get_tables_count('sys'))
# cur.execute('USE logical_data_model;')

















connection.close()

tunnel.close()

