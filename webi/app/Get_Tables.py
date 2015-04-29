import MySQLdb


def get_users():
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()

    cursor.execute("show columns from User")
    x0 = ""
    x1 = ""
    x2 = ""
    i = 0
    for x in cursor.fetchall():
        if i == 0:
            x0 = x[0]
        elif i == 1:
            x1 = x[0]
        else:
            x2 = x[0]
        i += 1
    ret = [(x0, x1, x2)]

    cursor.execute("select * from User")
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]


def get_bills():
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()

    cursor.execute("show columns from Bill")
    x0 = ""
    x1 = ""
    x2 = ""
    i = 0
    for x in cursor.fetchall():
        if i == 0:
            x0 = x[0]
        elif i == 1:
            x1 = x[0]
        else:
            x2 = x[0]
        i += 1
    ret = [(x0, x1, x2)]

    cursor.execute("select * from Bill")
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]


def get_times():
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()

    cursor.execute("show columns from Time")
    x0 = ""
    x1 = ""
    x2 = ""
    i = 0
    for x in cursor.fetchall():
        if i == 0:
            x0 = x[0]
        elif i == 1:
            x1 = x[0]
        else:
            x2 = x[0]
        i += 1
    ret = [(x0, x1, x2)]

    cursor.execute("select * from Time")
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]


def get_transactions():
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()

    cursor.execute("show columns from Transactions")
    x0 = ""
    x1 = ""
    x2 = ""
    x3 = ""
    i = 0
    for x in cursor.fetchall():
        if i == 0:
            x0 = x[0]
        elif i == 1:
            x1 = x[0]
        elif i == 2:
            x2 = x[0]
        else:
            x3 = x[0]
        i += 1
    ret = [(x0, x1, x2, x3)]

    cursor.execute("select * from Transactions")
    return ret + [(x[0], x[1], x[2], x[3]) for x in cursor.fetchall()]


def get_users_ids():
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()

    cursor.execute("select UserID from User")
    return [(x[0]) for x in cursor.fetchall()]