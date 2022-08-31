import sqlite3

def delete_all():

    # connect to database
    conn = sqlite3.connect('redbubble.db')

    # create a cursor
    cursor = conn.cursor()

    # query the database
    cursor.execute("DELETE FROM redbubble_user")
    items = cursor.fetchall()

    for item in items:
        print(item)

    conn.commit()
    #close our connection
    conn.close()

delete_all()
