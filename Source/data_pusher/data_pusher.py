
def insert_into_table(table_name, data, cursor):
    for row in data:
        i = 0
        exe_string = f'INSERT INTO {table_name} (*) VALUES'
        for el in row:
            if i < len(row):
                exe_string += f' {el},'
            else:
                break
        cursor.execute(f'INSERT INTO {table_name} (*) VALUES')
