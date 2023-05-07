import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        database="metalife"
    )
    
    return db