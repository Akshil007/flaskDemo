import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "akshil99",
)

myCursor = mydb.cursor()

myCursor.execute("create database test")
