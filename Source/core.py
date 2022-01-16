from realation_connector.some_connector import tunnel, sql_connect, sql_connect_error_catcher
from data_puller.data_puller import get_rows, get_tables_count
from data_distributor.data_distributor import distribute
from data_pusher.data_pusher import insert_into_table, insert_many_tables

tunnel.start()

connection, cur = sql_connect_error_catcher(sql_connect())

cur.execute('SELECT CURDATE()')

row = cur.fetchone()

# print(f"Date - {row}")

cur.execute('DESCRIBE sys;')
row = cur.fetchall()
for el in row:
    print(el)


get_tables_count('sys', cur)


# print(get_tables_count('sys', cur))


tables_rows = get_rows('sys', cur, get_tables_count('sys', cur))

platforms_table = []
customers_table = []
suppliers_table = []
services_table = []
locations_table = []

print('333333333333333')


distribute(tables_rows, platforms_table, customers_table, suppliers_table, services_table, locations_table)

print(platforms_table)
print(customers_table)
print(suppliers_table)
print(services_table)
print(locations_table)

cur.execute('USE friendship')

# insert_into_table('platforms', cur, platforms_table)
connection.commit()
# str_data = (
#         "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
#     )
# cur.executemany(str_data, platforms_table)
insert_many_tables(cur, 5, platforms_table, customers_table, suppliers_table, services_table, locations_table, 'platforms', 'customers', 'suppliers', 'services', 'locations')
connection.commit()

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

cur.execute('SELECT * FROM platforms')
print(cur.fetchall())
connection.close()

tunnel.close()

