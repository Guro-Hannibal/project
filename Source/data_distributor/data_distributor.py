def distribute(rows, *args):
    i = 0
    for row in rows:
        args[i].append(row[0:4])
        i += 1
        args[i].append(row[4:9])
        i += 1
        args[i].append(row[9:12])
        i += 1
        args[i].append(row[12:15])
        i += 1
        args[i].append(row[15:])
        i += 1
        i = 0
    return args
