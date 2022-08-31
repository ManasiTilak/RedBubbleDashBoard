"""
Get all the data from the db
"""
import sqlite3

def show_all():

    # connect to database
    conn = sqlite3.connect('redbubble.db')

    # create a cursor
    cursor = conn.cursor()

    # query the database
    cursor.execute("SELECT * FROM redbubble_user")
    items = cursor.fetchall()

    for item in items:
        print(item)

    conn.commit()
    #close our connection
    conn.close()

show_all()