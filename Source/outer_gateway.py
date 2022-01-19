
import mysql.connector
import sshtunnel

tunnel = sshtunnel.SSHTunnelForwarder(
        ssh_username='ag3131',
        ssh_password='GoForthGo',
        ssh_address_or_host='192.168.0.66',
        ssh_port=22,
        remote_bind_address=('127.0.0.1', 3306)
)

tunnel.start()



from tkinter import *
root = Tk()
root.title("2.24")

root.geometry("1200x1200")

service_id = Entry(root, width=50).grid(column=1, row=1)
service_name = Entry(root, width=50).grid(column=1, row=4)
service_owner = Entry(root, width=50).grid(column=1, row=8)
service_details = Entry(root, width=50).grid(column=1, row=11)
service_id_label = Label(root, text='service_id_label').grid(column=1, row=3)
service_name_label = Label(text='service_name_label').grid(column=1, row=6)
service_owner_label = Label(text='service_owner_label').grid(column=1, row=9)
service_details_label = Label(text='service_details_label').grid(column=1, row=12)

platform_id = Entry(root, width=50).grid(column=24, row=1, columnspan=10, ipadx=24)
platform_name = Entry(root, width=50).grid(column=24, row=4, columnspan=10, ipadx=24)
platform_vars = Entry(root, width=50).grid(column=24, row=8, columnspan=10, ipadx=24)
platform_id_label = Label(text='platform_id_label').grid(column=24, row=3, columnspan=10, ipadx=24)
platform_name_label = Label(text='platform_name_label').grid(column=24, row=6, columnspan=10, ipadx=24)
platform_vars_label = Label(text='platform_vars_label').grid(column=24, row=9, columnspan=10, ipadx=24)

my_love_i = Entry(root, width=50).grid(column=24, row=161, columnspan=10, ipadx=24)
my_love_letter = Entry(root, width=50).grid(column=24, row=163, columnspan=10, ipadx=24)
my_love_you = Entry(root, width=50).grid(column=24, row=165, columnspan=10, ipadx=24)
my_love_name = Entry(root, width=50).grid(column=24, row=167, columnspan=10, ipadx=24)
my_love_hug = Entry(root, width=50).grid(column=24, row=169, columnspan=10, ipadx=24)
my_love_i_l = Label(text='I').grid(column=24, row=160, columnspan=10, ipadx=24)
my_love_letter_l = Label(text='LOVE').grid(column=24, row=162, columnspan=10, ipadx=24)
my_love_you_l = Label(text='YOU').grid(column=24, row=164, columnspan=10, ipadx=24)
my_love_name_l = Label(text='VIKTORIYA BUCHTIYCHOOK').grid(column=24, row=166, columnspan=10, ipadx=24)
my_love_hug_l = Label(text='HUG').grid(column=24, row=168, columnspan=10, ipadx=24)

event_owner = Entry(root, width=50).grid(column=160, row=1)
event_id = Entry(root, width=50).grid(column=160, row=4)
event_code = Entry(root, width=50).grid(column=160, row=8)
event_datatime = Entry(root, width=50).grid(column=160, row=1)
event_owner_label = Label(text='event_owner_label').grid(column=160, row=2)
event_id_label = Label(text='event_id_label').grid(column=160, row=5)
event_code_label = Label(text='event_code_label').grid(column=160, row=7)
event_datatime_label = Label(text='event_datatime_label').grid(column=160, row=10)



def seter():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Science',
        database='data_source',
        port=tunnel.local_bind_port)

    interface = conn.cursor()

    sql_str = "INSERT INTO My_Love VALUES My_Love.(%love, %love, %love, %love, %love),"\ \\
              { '"my_love_i'": my_love_i.get()\
                \'"my_love_you'": my_love_letter.get()\
                \"'my_love_you'": my_love_you.get()\
                \'"my_love_name"": my_love_name.get()\
                \'"my_love_hug"": my_love_hug.get()\
              }





    print(sql_str)
    interface.execute(sql_str)
    conn.close()
    tunnel.close()


send = Button(root, text='send more data, even more data!', activebackground='red',
                                background='blue', command=seter())
send.grid(column=66, row=200, columnspan=10, ipadx=24)

root.mainloop()






