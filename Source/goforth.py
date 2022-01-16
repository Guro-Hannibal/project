from mysql.connector import connect, Error
import sshtunnel

tunnel = sshtunnel.SSHTunnelForwarder(
    ssh_username='ag3131',
    ssh_password='GoForthGo',
    ssh_address_or_host='192.168.0.66',
    ssh_port=22,
    remote_bind_address=('127.0.0.1', 3306)
)


tunnel.start()

global connection

try:

    connection = connect (
        host='localhost',
        user='root',
        passwd='Science',
        database='data_source',
        port=tunnel.local_bind_port
    )

except Error:
    print(f'Ошибка -  {Error}')


cur = connection.cursor()

cur.execute('SELECT CURDATE()')

row = cur.fetchone()

print(f"Date - {row}")
#
# #
# cur.execute('USE logical_data_model;')
cur.execute('DESCRIBE sys;')
row = cur.fetchall()
for el in row:
    print(el)


def get_tables_count(table_name):
    cur.execute(f'SELECT COUNT(*) FROM {table_name}')
    tuple_result = cur.fetchone()
    return int(tuple_result[0])


print(get_tables_count('sys'))


def get_rows(table_name, count):
    cur.execute(f'SELECT * FROM {table_name}')
    tuple_result = cur.fetchall()
    print(tuple_result)
    return tuple_result


rows = get_rows('sys', get_tables_count('sys'))


def distribute(rows):
    push_row = []
    for row in rows:
        service_row = row[0:3]
        
        for el in row[0:3]:
            print(str(el) + '   abc', end='    ')
            push_row.append(el)
        print()
        for item in row[3:6]:
            print(str(item) + '   abc', end='    ')
        print()
        for item in row[6:9]:
            print(str(item) + '   abc', end='    ')
        print()
        for item in row[9:12]:
            print(str(item) + '   abc', end='    ')
        print()
        for item in row[12:15]:
            print(str(item) + '   abc', end='    ')
        print()
        for item in row[15:18]:
            print(str(item) + '   abc', end='    ')
        print()
    print(testr)
    return push_row


anything = distribute(rows)


print(anything)









connection.close()

tunnel.close()

