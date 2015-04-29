import MySQLdb


def remove_transaction(transaction_id):
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()
    command = "select TransactionID from transactions where TransactionID='" + str(transaction_id) + "';"
    cursor.execute(command)

    if cursor.fetchone():   # If we find
        command = "delete from transactions where TransactionID='" + str(transaction_id) + "';"
        cursor.execute(command)
        db.commit()


def add_transaction(transaction_id):
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()
    command = "select TransactionID from transactions where TransactionID='" + str(transaction_id) + "';"
    cursor.execute(command)

    if not cursor.fetchone():   # If no transaction with that ID
        command = "INSERT INTO transactions (TransactionID) VALUES ('" + str(transaction_id) + "');"
        cursor.execute(command)
        db.commit()


def change_transaction(transaction_id, field, new):
    db = MySQLdb.connect(host="localhost", user="root", passwd="5131", db="lab1")
    cursor = db.cursor()
    cursor.execute("select TransactionID from transactions where TransactionID='" + str(transaction_id) + "';")

    if cursor.fetchone():   # If we find
        if field == "TransactionID":
            cursor.execute("select TransactionID from transactions where TransactionID='" + str(new) + "';")
            if not cursor.fetchone():
                cursor.execute("UPDATE transactions SET TransactionID='" + str(new) + "' WHERE TransactionID='" + str(transaction_id) + "';")
        elif field == "BillID":
            cursor.execute("select BillID from Bill where BillID='" + str(new) + "';")
            if cursor.fetchone():
                cursor.execute("UPDATE transactions SET BillID='" + str(new) + "' WHERE TransactionID='" + str(transaction_id) + "';")
        elif field == "TimeID":
            cursor.execute("select TimeID from Time where TimeID='" + str(new) + "';")
            if cursor.fetchone():
                cursor.execute("UPDATE transactions SET TimeID='" + str(new) + "' WHERE TransactionID='" + str(transaction_id) + "';")
        elif field == "UserID":
            cursor.execute("select UserID from User where UserID='" + str(new) + "';")
            if cursor.fetchone():
                cursor.execute("UPDATE transactions SET UserID='" + str(new) + "' WHERE TransactionID='" + str(transaction_id) + "';")
        elif field == "Successful":
            cursor.execute("UPDATE transactions SET Successful='" + str(new) + "' WHERE TransactionID='" + str(transaction_id) + "';")
        db.commit()