import sqlite3

def fetch_userdata(username):

    # connect to database
    conn = sqlite3.connect('redbubble.db')

    # create a cursor
    cursor = conn.cursor()

    # query the database
    cursor.execute("SELECT * FROM redbubble_user WHERE username = (?)", (username,))
    # WHERE 
    items = cursor.fetchall()

    return(items)

    conn.commit()
    #close our connection
    conn.close()

