import MySQLdb

def remove_fact(transaction_id):
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="mydb")
    cursor = db.cursor()
    command = "select TransactionID from transactions where TransactionID='" + str(transaction_id) + "';"
    cursor.execute(command)

    if cursor.fetchone():   # If we find
        command = "delete from transactions where TransactionID='" + str(transaction_id) + "';"
        cursor.execute(command)
        db.commit()


def add_fact(transaction_id):
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="mydb")
    cursor = db.cursor()
    command = "select Transaction_id from f_transactions where Transaction_id='" + str(transaction_id) + "';"
    cursor.execute(command)

    if not cursor.fetchone():   # If no transaction with that ID
        command = "INSERT INTO f_transactions (Transaction_ID) VALUES ('" + str(transaction_id) + "');"
        cursor.execute(command)
        db.commit()

def change_fact(cursor, transaction_id, field, new):
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="mydb")
    cursor = db.cursor()
    cursor.execute("select Transaction_id from f_transactions where Transaction_id='" + str(transaction_id) + "';")

    if cursor.fetchone():   # If we find
        if field == "Transaction_ID":
            cursor.execute("select Transaction_id from f_transactions where Transaction_id='" + str(new) + "';")
            if not cursor.fetchone():
                cursor.execute("UPDATE f_transactions SET Transaction_ID='" + str(new) + "' WHERE Transaction_ID='" + str(transaction_id) + "';")
        elif field == "Bill_ID":
            cursor.execute("select Bill_ID from D_Bill where Bill_ID='" + str(new) + "';")
            if cursor.fetchone():
                cursor.execute("UPDATE f_transactions SET Bill_ID='" + str(new) + "' WHERE Transaction_ID='" + str(transaction_id) + "';")
        elif field == "Time_ID":
            cursor.execute("select Time_ID from D_Time where Time_ID='" + str(new) + "';")
            if cursor.fetchone():
                cursor.execute("UPDATE f_transactions SET Time_ID='" + str(new) + "' WHERE Transaction_ID='" + str(transaction_id) + "';")
        elif field == "User_ID":
            cursor.execute("select User_ID from D_User where User_ID='" + str(new) + "';")
            if cursor.fetchone():
                cursor.execute("UPDATE f_transactions SET User_ID='" + str(new) + "' WHERE Transaction_ID='" + str(transaction_id) + "';")
        elif field == "Successful":
            cursor.execute("UPDATE f_transactions SET Successful='" + str(new) + "' WHERE Transaction_ID='" + str(transaction_id) + "';")
        db.commit()