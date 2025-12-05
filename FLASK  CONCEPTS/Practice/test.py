import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="9090",
        database="TESTED_DB"
    )
    if conn.is_connected():
        cursor=conn.cursor()
        cursor.execute("SELECT username FROM USERS")
        users=cursor.fetchall()
        for user in users:
            print(user)
    conn.close()
except Exception as e:
    print(" Error:", e)
