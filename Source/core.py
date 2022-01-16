from realation_connector.some_connector import tunnel, sql_connect, sql_connect_error_catcher
from data_puller.data_puller import get_rows, get_rows_count
from data_distributor.data_distributor import distribute
from data_pusher.data_pusher import insert_into_table, insert_many_tables

tunnel.start()

connection, cur = sql_connect_error_catcher(sql_connect())

cur.execute('SELECT CURDATE()')

row = cur.fetchone()

print(f"Date - {row}")

cur.execute('DESCRIBE sys;')
row = cur.fetchall()
for el in row:
    print(el)


get_rows_count('sys', cur)


print(get_rows_count('sys', cur))


tables_rows = get_rows('sys', cur, get_rows_count('sys', cur))

platforms_table = []
customers_table = []
suppliers_table = []
services_table = []
locations_table = []

distribute(tables_rows, platforms_table, customers_table, suppliers_table, services_table, locations_table)

# print(platforms_table)
# print(customers_table)
# print(suppliers_table)
# print(services_table)
# print(locations_table)

cur.execute('USE friendship')

# insert_into_table('platforms', cur, platforms_table)
# connection.commit()

insert_many_tables(cur, 5, platforms_table, customers_table, suppliers_table, services_table, locations_table,
                   'platforms', 'customers', 'suppliers', 'services', 'locations')
connection.commit()

tables = []
cur.execute('SELECT * FROM platforms')
tables.append(cur.fetchall())
cur.execute('SELECT * FROM customers')
tables.append(cur.fetchall())
cur.execute('SELECT * FROM suppliers')
tables.append(cur.fetchall())
cur.execute('SELECT * FROM services')
tables.append(cur.fetchall())
cur.execute('SELECT * FROM locations')
tables.append(cur.fetchall())
for el in tables:
    print(el)

connection.close()
tunnel.close()

