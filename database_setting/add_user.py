"""
Add user from data from the gui -NewUserRed_UI class
"""
import sqlite3

def add_new(new_username, new_email, new_password, new_folder, new_excel):
    conn = sqlite3.connect('redbubble.db')
    c = conn.cursor()
    c.execute("INSERT INTO redbubble_user VALUES(?, ?, ?, ?, ?)", (new_username, new_email, new_password, new_folder, new_excel))
    conn.commit()
    conn.close()