def distribute(rows):
    for row in rows:
        platform_table.append(row[0:4])
        customer_table.append(row[4:9])
        supplier_table.append(row[9:12])
        service_table.append(row[12:15])
        location_table.append(row[15:])
    return


distribute(tables_rows)

print(platform_table)
print(customer_table)
print(supplier_table)
print(service_table)
print(location_table)