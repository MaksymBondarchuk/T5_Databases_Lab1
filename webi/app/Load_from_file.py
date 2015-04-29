import json
import MySQLdb


def load_from_file(file_name, table):
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()

    file = open("files/" + file_name)
    data = json.load(file)
    cursor.execute("delete from transactions")

    if table == "Users":
        cursor.execute("delete from user")
        for i in data:
            cursor.execute("insert into user (UserID, Name, comment) values ('"+str(i["UserID"])+"', '"+str(i["Name"])+"', '"+str(i["Comment"])+"')")
    elif table == "Bills":
        cursor.execute("delete from bill")
        for i in data:
            cursor.execute("insert into bill (BillID, Amount, Average_amount_for_month) values ('"+str(i["BillID"])+"', '"+str(i["Amount"])+"', '"+str(i["Average_amount_for_month"])+"')")
    elif table == "Times":
        cursor.execute("delete from time")
        for i in data:
            cursor.execute("insert into time (TimeID, DateTime, At_day_time) values ('" + str(i["TimeID"]) + "', '"+str(i["DateTime"])+"', '"+str(i["At_day_time"])+"')")

    file.close()
    db.commit()