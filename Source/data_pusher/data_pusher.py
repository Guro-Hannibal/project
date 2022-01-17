from ..core import supplier_trigger, service_trigger, connection_database
from time import sleep

suppliers_last_push = None

services_last_push = None

def insert_into_table(table_name, cursor, data):
    if table_name == 'platforms':
        sql_str = (
            "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
        )
    elif table_name == 'suppliers':
        supplier_trigger = 1
        suppliers_last_push = data
        sql_str = (
            "INSERT INTO suppliers (supplier_id, supplier_name, supplier_details) VALUES(%s, %s, %s)"
        )
    elif table_name == 'services':
        services_trigger = 1
        services_last_push = data
        sql_str = (
                "INSERT INTO services (service_code, service_name, service_details) VALUES(%s, %s, %s)"
            )
    elif table_name == 'locations':
        sql_str = (
            "INSERT INTO locations (location_id, location_name, location_details) VALUES(%s, %s, %s)"
        )
    elif table_name == 'customers':
        sql_str = (
            "INSERT INTO customers (customer_name, customer_id, title, gender, customers_details) VALUES(%s, %s, %s, %s, %s)"
        )
    else:
        return print('Not enough data: table_name doesnt much')
    cursor.executemany(sql_str, data)


def insert_many_tables(cursor, count, *args):
    for el in args[:count]:
        print(args[count])
        insert_into_table(args[count], cursor, el)
        count += 1


def trigger_check(cursor):
    if not connection_database:
        return
    table_name = 'suppliers_service_join'
    data = []
    for row, elem in services_last_push, suppliers_last_push:
        service_id = row[0]
        supplier_id = elem[0]
        service_name = row[1]
        supplier_name = elem[1]
        data.append((service_id, supplier_id, service_name, supplier_name))
    print(data)
    if supplier_trigger == 1 and service_trigger == 1:
        insert_into_table(table_name, cursor, data)
    while connection_database:
        sleep(60)
        trigger_check()
