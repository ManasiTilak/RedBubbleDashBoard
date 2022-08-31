"""
Create databse with a table redbubble user
"""
import sqlite3

# connect to database
conn = sqlite3.connect('redbubble.db')

# create a cursor
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE redbubble_user(
    username TEXT,
    email TEXT,
    password TEXT,
    folder TEXT,
    excel_sheet TEXT
)""")

#commit the connection - IMPORTANT
conn.commit()

#close our connection
conn.close()