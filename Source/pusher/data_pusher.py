class DataPusher:




    supplier_trigger = False

    service_trigger = False

    def insert_into_table(self, table_name, cursor, data):
        if table_name == 'platforms':
            sql_str = (
                "INSERT INTO platforms (platform_id, platform_name, platform_details, acces_variables) VALUES(%s, %s, %s, %s)"
            )
        elif table_name == 'suppliers':
            supplier_trigger = True
            __suppliers_last_push = data
            sql_str = (
                "INSERT INTO suppliers (supplier_id, supplier_name, supplier_details) VALUES(%s, %s, %s)"
            )
        elif table_name == 'services':
            services_trigger = True
            __services_last_push = data
            sql_str = (
                    "INSERT INTO services (service_code, service_name, supplier_name) VALUES(%s, %s, %s)"
                )
        elif table_name == 'locations':
            sql_str = (
                "INSERT INTO locations (location_id, location_name, location_details) VALUES(%s, %s, %s)"
            )
        elif table_name == 'customers':
            sql_str = (
                "INSERT INTO customers (customer_name, customer_id, title, gender, customers_details) VALUES(%s, %s, %s, %s, %s)"
            )
        else:
            return print('Not enough data: table_name doesnt much')
        cursor.executemany(sql_str, data)

    def insert_many_tables(self, cursor, count, *args):
        for el in args[:count]:
            print(args[count])
            self.insert_into_table(args[count], cursor, el)
            count += 1

    def trigger_check(self, cursor):
        table_name = 'suppliers_service_join'
        data = []
        if supplier_trigger and service_trigger:
            for row, elem in __services_last_push, __suppliers_last_push:
                service_id = row[0]
                supplier_id = elem[0]
                service_name = row[1]
                supplier_name = elem[1]
                data.append((service_id, supplier_id, service_name, supplier_name))
            self.insert_into_table(table_name, cursor, data)

