def insert_into_table(table_name, cursor, data):
    if table_name == 'platforms':
        sql_str = (
            "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
        )
    elif table_name == 'suppliers':
        sql_str = (
            "INSERT INTO suppliers (supplier_id, supplier_name, supplier_details) VALUES(%s, %s, %s)"
        )
    elif table_name == 'services':
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
