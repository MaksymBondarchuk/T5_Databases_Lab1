import MySQLdb


def search_bool(bool):
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

    cursor.execute("select * from Time where At_day_time=" + bool)
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]


def search_date(start, end):
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

    cursor.execute("select * from Time where date(DateTime) between '" + start + "' and '" + end + "'")
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]


def search_text_not_word(column, word):
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

    cursor.execute("select * from User where not match (" + column + ") against ('" + word + "' in boolean mode);")
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]


def search_phrase(column, phrase):
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

    cursor.execute("select * from User where match (" + column + ") against ('\"" + phrase + "\"' in boolean mode)")
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]


def search_bill(column, start, end):
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

    cursor.execute("select * from Bill where " + column + " between " + start + " and " + end)
    return ret + [(x[0], x[1], x[2]) for x in cursor.fetchall()]