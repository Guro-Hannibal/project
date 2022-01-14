from mysql.connector import connect, Error
import sshtunnel
import go
global tunnel

tunnel = sshtunnel.SSHTunnelForwarder(
    ssh_username='ag3131',
    ssh_password=go.codemore,
    ssh_address_or_host='192.168.0.66',
    ssh_port=22,
    ssh_pkey='',
    remote_bind_address=('127.0.0.1', 3306)
)


tunnel.start()

global connection

try:

    connection = connect (
        host='localhost',
        user='root',
        passwd='Science',
        port=tunnel.local_bind_port
    )

except Error:
    print(f'Ошибка -  {Error}')

cursor = connection.cursor()
#
# cursor.execute('SELECT CURDATE()')
#
# row = cur.fetchone()
#
# print(f"Date - {row}")

# cur.execute('DESCRIBE events;')
# row = cur.fetchall()
# for el in row:
#     print(el)
#
# cursor.execute('USE information_schema;')
# ox = 'location_history'
# db = 'information_schema'
# fdsfsdf = 'schema_name'
# cur.execute("""SELECT * FROM tables WHERE (ab LIKE %s{fgffname}% and lcname LIKE%{ffaf}%)""")%(ox,fdsfsdf)
# row = cur.fetchall()
#
# print(row)

dbcfname = 'table_name'

dbclname = 'schema_name'

dbcaddress = 'location_history'

dbccity = 'users'

dbcstate = 'vars'

dbczipcode = 'muhaha'

cursor.execute('SELECT * FROM information_schema.tables')

bcname = cursor.fetchall()

# cursor.execute(f"SELECT UNION(''s'', ''ys'') FROM '{(bcname, )}")
#
# bcname = cursor.fetchall()
#
# print(bcname)

for el in bcname:
    print(el)

connection.close()

tunnel.close()
