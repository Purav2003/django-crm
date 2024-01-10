import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

cursorObjet = dataBase.cursor()

cursorObjet.execute("CREATE DATABASE crm")
print("Database Created")