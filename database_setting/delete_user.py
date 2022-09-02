import sqlite3

def delete_userdata(username):

    # connect to database
    conn = sqlite3.connect('redbubble.db')

    # create a cursor
    cursor = conn.cursor()

    # query the database
    cursor.execute("DELETE FROM redbubble_user WHERE username = (?)", (username,))
    # WHERE 
    items = cursor.fetchall()
    conn.commit()
    #close our connection
    
    return(items)
    conn.close()