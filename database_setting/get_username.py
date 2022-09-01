"""
Get all the data from the db
"""
import sqlite3

def get_usernames():

    # connect to database
    conn = sqlite3.connect('redbubble.db')

    # create a cursor
    cursor = conn.cursor()

    # query the database
    cursor.execute("SELECT username FROM redbubble_user")
    items = cursor.fetchall()
    return (items)

    # for item in items:
    #     print (type(item[0]))

    conn.commit()
    #close our connection
    conn.close()

get_usernames()