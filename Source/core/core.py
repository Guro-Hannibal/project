from relation_connector import tunnel, sql_connect, sql_connect_error_catcher
from data_puller import DataPuller
from data_distributor import Distributor
from data_pusher import DataPusher

tunnel.start()

a, b = sql_connect_error_catcher(sql_connect())

relay, interface = a, b




class Core:

    def __init__(self, source_database, friendship_project, relay, interface):
        self.source_database = source_database
        self.friendship_project = friendship_project
        self.interface = interface
        self.relay = relay


class UI(Core, DataPusher, DataPuller, Distributor):

    def __init__(self, source_database, friendship_project, relay, interface):
        super().__init__(source_database, friendship_project, relay, interface)
        self.source_database = source_database
        self.friendship_project = friendship_project
        self.inner = interface
        self.relay = relay


console = UI('source_database', 'friendship', relay, interface)


# with open('core.sql', 'r') as data:
#     with connection.cursor() as sql_runner:
#         sql_runner.execute("DROP DATABASE IF EXISTS friendship")
#         sql_runner.execute(data.read(), multi=True)
#     connection.commit()

interface.execute('SELECT CURDATE()')

row = interface.fetchone()

print(f"Date - {row}")

row = console.get_table_names(interface)
print(row)


def foo():
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


foo()

interface.execute('DESCRIBE sys;')
row = interface.fetchall()
for el in row:
    print(el)

foo()


print(console.get_rows_count('sys', interface))


tables_rows = console.get_rows('sys', interface, console.get_rows_count('sys', interface))

platforms_table = []
customers_table = []
suppliers_table = []
services_table = []
locations_table = []

console.distribute(tables_rows, platforms_table, customers_table, suppliers_table, services_table, locations_table)

print(platforms_table)
print(customers_table)
print(suppliers_table)
print(services_table)
print(locations_table)


foo()


interface.execute('USE friendship')


console.insert_into_table('platforms', interface, platforms_table)
relay.commit()

console.insert_many_tables(interface, 4, customers_table, suppliers_table, services_table, locations_table,
                   'customers', 'suppliers', 'services', 'locations')
relay.commit()


foo()

if console.supplier_trigger and console.service_trigger:
    console.trigger_check(interface)


tables = []
interface.execute('SELECT * FROM platforms')
tables.append(interface.fetchall())
interface.execute('SELECT * FROM customers')
tables.append(interface.fetchall())
interface.execute('SELECT * FROM suppliers')
tables.append(interface.fetchall())
interface.execute('SELECT * FROM services')
tables.append(interface.fetchall())
interface.execute('SELECT * FROM locations')
tables.append(interface.fetchall())
for el in tables:
    print(el)

foo()

custom_rows = console.get_custom_rows(interface, 'suppliers', 'supplier_name', 'fsdfds', 'fsdfsf')
print(custom_rows)


console.join_custom_rows(interface, 'LEFT JOIN', 'suppliers', 'services', 'supplier_name', 'supplier_name',
                       ['supplier_id', 'supplier_name', 'supplier_details'])

row = interface.fetchall()

print(row)

console.union_custom_rows(interface, "suppliers", "services", ['supplier_id', 'supplier_name', 'supplier_details'],
                  ['service_code', 'service_name', 'supplier_name'], [], 'supplier_id')

print(interface.fetchall())


relay.close()
tunnel.close()

