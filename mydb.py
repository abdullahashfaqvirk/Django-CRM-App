import mysql.connector


# Establishing a connection to the MySQL server
database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password'
)

# Creating a cursor object to interact with the MySQL database
cursor = database.cursor()

# Executing a query to create a new database named 'crm_db'
cursor.execute('CREATE DATABASE crm_db')
