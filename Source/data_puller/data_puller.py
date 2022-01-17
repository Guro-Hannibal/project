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
    print()
    return cursor.execute(result_sql_str)


def union_custom_rows(cursor, union_table, unioner_table, args_list, atr_list, conditions_list, order = False):
    sql_str_top = f"SELECT "
    sql_str_bottom = f"SELECT "
    sql_str_universal = ''
    str_sql_obedient = ''
    for num, el in enumerate(args_list):
        if num >= len(args_list) - 1:
            sql_str_top += f"{union_table}.{el}"
            break
        sql_str_top += f"{union_table}.{el}, "
    for num, atr in enumerate(atr_list):
        if num >= len(atr_list) - 1:
            sql_str_bottom += f"{unioner_table}.{atr} FROM {unioner_table}"
            break
        sql_str_bottom += f"{unioner_table}.{atr}, "

    if len(conditions_list) == 0:
        sql_str_universal = f" FROM {union_table} "

    elif len(conditions_list) <= 2:
        sql_str_universal = f" FROM {union_table} ON {union_table}.{conditions_list[0]} " \
                         f"= {unioner_table}.{conditions_list[1]} " \
                            f""

    elif len(conditions_list) > 2:
        sql_str_universal = f" FROM {union_table} ON {union_table}.{conditions_list[0]} " \
                         f"= {union_table}.{conditions_list[0]}" \
                        f"{union_table} ON {union_table}.{conditions_list[0]} = {unioner_table}.{conditions_list} "

    if order:
        str_sql_obedient = f" ORDER BY {order}"
    master = (
        sql_str_top +
        sql_str_universal +
        "UNION " +
        sql_str_bottom +
        str_sql_obedient + ';'
    )
    print(master)
    cursor.execute(master)
# tables_names and conditions must be dictionary and iterable,
# conditions must be iterable if more than 1 for a table put in another iterable argument
# for example tuples in list


