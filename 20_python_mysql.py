import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_asset2025"
    )

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM divisis")
        hasil = cursor.fetchall()

        for row in hasil:
            print(row)

except Error as e:
    print("Terjadi error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
