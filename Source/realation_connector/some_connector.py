from mysql.connector import connect, Error
import sshtunnel

tunnel = sshtunnel.SSHTunnelForwarder(
    ssh_username='ag3131',
    ssh_password='GoForthGo',
    ssh_address_or_host='192.168.0.66',
    ssh_port=22,
    remote_bind_address=('127.0.0.1', 3306)
)


def sql_connect():
    connection = connect(
        host='localhost',
        user='root',
        passwd='Science',
        database='data_source',
        port=tunnel.local_bind_port)
    cur = connection.cursor()
    return connection, cur


def sql_connect_error_catcher(foo):
    try:
        relay, cur = sql_connect()
        return relay, cur
    except Error:
        print(f'Ошибка -  {Error}')



# cur.execute('SELECT CURDATE()')
#
# row = cur.fetchone()
#
# print(f"Date - {row}")


