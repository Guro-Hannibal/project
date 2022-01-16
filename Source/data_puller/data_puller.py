def get_rows_count(table_name, cursor):
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    tuple_result = cursor.fetchone()
    return int(tuple_result[0])


def get_rows(table_name, cursor, count):
    cursor.execute(f'SELECT * FROM {table_name}')
    tuple_result = cursor.fetchall()
    print(tuple_result)
    return tuple_result


def get_custom_rows(cursor, table_name, name, *args):
    rows = []
    for el in args:
        exe_str = (
            f"SELECT * FROM {table_name} WHERE {name}='{el}'"
                   )
        cursor.execute(exe_str,)
        rows.append(cursor.fetchone())
    return rows
