import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="papacakep22",
        database="db_retail"
    )

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        hasil = cursor.fetchall()

        for row in hasil:
            print(row)

except Error as e:
    print("Terjadi error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

