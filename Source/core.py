from realation_connector.some_connector import tunnel, sql_connect, sql_connect_error_catcher
from data_puller.data_puller import get_rows, get_rows_count, get_custom_rows, get_table_names, join_custom_rows
from data_distributor.data_distributor import distribute
from data_pusher.data_pusher import insert_into_table, insert_many_tables, trigger_check

tunnel.start()

connection, cur = sql_connect_error_catcher(sql_connect())

cur.execute('SELECT CURDATE()')

row = cur.fetchone()

print(f"Date - {row}")

row = get_table_names(cur)
print(row)


def foo():
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


foo()


cur.execute('DESCRIBE sys;')
row = cur.fetchall()
for el in row:
    print(el)

foo()


print(get_rows_count('sys', cur))


tables_rows = get_rows('sys', cur, get_rows_count('sys', cur))

platforms_table = []
customers_table = []
suppliers_table = []
services_table = []
locations_table = []

distribute(tables_rows, platforms_table, customers_table, suppliers_table, services_table, locations_table)

print(platforms_table)
print(customers_table)
print(suppliers_table)
print(services_table)
print(locations_table)


foo()


cur.execute('USE friendship')

insert_into_table('platforms', cur, platforms_table)
connection.commit()

insert_many_tables(cur, 4, customers_table, suppliers_table, services_table, locations_table,
                   'customers', 'suppliers', 'services', 'locations')
connection.commit()


foo()

trigger_check(cur)


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

foo()

custom_rows = get_custom_rows(cur, 'suppliers', 'supplier_name', 'fsdfds', 'fsdfsf')
print(custom_rows)


join_custom_rows(cur, 'LEFT JOIN', 'suppliers', 'services', 'supplier_name', 'supplier_name',
                       ['supplier_id', 'supplier_name', 'supplier_details'])

print(cur.fetchall())

connection.close()
tunnel.close()

