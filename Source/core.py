from realation_connector.some_connector import tunnel, sql_connect, sql_connect_error_catcher
from data_puller.data_puller import get_rows, get_tables_count
from data_distributor.data_distributor import distribute

tunnel.start()

connection, cur = sql_connect_error_catcher(sql_connect())

cur.execute('SELECT CURDATE()')

row = cur.fetchone()

print(f"Date - {row}")

cur.execute('DESCRIBE sys;')
row = cur.fetchall()
for el in row:
    print(el)


get_tables_count('sys', cur)


print(get_tables_count('sys', cur))


tables_rows = get_rows('sys', cur, get_tables_count('sys', cur))

platform_table = []
customer_table = []
supplier_table = []
service_table = []
location_table = []

print('333333333333333')


distribute(tables_rows, platform_table, customer_table, supplier_table, service_table, location_table)

print(platform_table)
print(customer_table)
print(supplier_table)
print(service_table)
print(location_table)








connection.close()

tunnel.close()

