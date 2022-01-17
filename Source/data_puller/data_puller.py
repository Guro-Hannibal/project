def get_rows_count(table_name, cursor):
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    tuple_result = cursor.fetchone()
    return int(tuple_result[0])


def get_rows(table_name, cursor, count):
    cursor.execute(f'SELECT * FROM {table_name}')
    tuple_result = cursor.fetchall()
    return tuple_result


def get_table_names(cursor):
    cursor.execute('SHOW TABLES')
    return cursor.fetchall()


def get_custom_rows(cursor, table_name, condition, *args):
    __count = get_rows_count(table_name, cursor)
    result_rows = []
    for el in args:
        sql_str = (
        f"SELECT * FROM {table_name} WHERE {condition}='{el}'"
                    )
        cursor.execute(sql_str,)
        result_rows.append(cursor.fetchall())
    return result_rows


def join_custom_rows(cursor, join_type, join_table, joiner_table, condition, second_condition, list_of_args):
    sql_str = f"SELECT "
    for num, el in enumerate(list_of_args):
        if num >= len(list_of_args) - 1:
            sql_str += f"{join_table}.{el} "
            break
        sql_str += f"{join_table}.{el}, "
    result_sql_str = (
        sql_str +
        f"FROM {join_table} "
        f"{join_type} {joiner_table} ON {join_table}.{condition} = {joiner_table}.{second_condition};"
    )
    return cursor.execute(result_sql_str)

# tables_names and conditions must be dictionary and iterable,
# conditions must be iterable if more than 1 for a table put in another iterable argument
# for example tuples in list


