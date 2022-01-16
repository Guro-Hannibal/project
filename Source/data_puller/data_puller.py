def get_tables_count(table_name, cursor):
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    tuple_result = cursor.fetchone()
    return int(tuple_result[0])


def get_rows(table_name, cursor, count):
    cursor.execute(f'SELECT * FROM {table_name}')
    tuple_result = cursor.fetchall()
    print(tuple_result)
    return tuple_result
