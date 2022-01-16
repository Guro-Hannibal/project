def insert_into_table(data, cursor, table_name):
    if table_name == 'platfroms':
        str_data = (
            "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
        )
    elif table_name == 'suppliers':
        str_data = (
            "INSERT INTO suppliers (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
        )
    elif table_name == 'services':
            str_data = (
                "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
            )
    elif table_name == 'locations':
        str_data = (
            "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
        )
    elif table_name == 'customers':
        str_data = (
            "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
        )
    else:
        return print('Not enough data: table_name doesnt much')
    cursor.executemany(str_data, data)


def insert_many_tables(cursor, *args):
