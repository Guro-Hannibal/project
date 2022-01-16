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
    cur.execute(f'SELECT * FROM {table_name}')
    tuple_result = cur.fetchall()
    print(tuple_result)
    return tuple_result


tables_rows = get_rows('sys', get_tables_count('sys'))

platform_table = []
customer_table = []
supplier_table = []
service_table = []
location_table = []

print('333333333333333')


def distribute(rows):
    for row in rows:
        platform_table.append(row[0:4])
        customer_table.append(row[4:9])
        supplier_table.append(row[9:12])
        service_table.append(row[12:15])
        location_table.append(row[15:])
    return


distribute(tables_rows)

print(platform_table)
print(customer_table)
print(supplier_table)
print(service_table)
print(location_table)








connection.close()

tunnel.close()

