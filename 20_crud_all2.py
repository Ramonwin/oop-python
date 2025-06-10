import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="papacakep22",  # kosong kalau pakai XAMPP default
        database="db_retail"
    )

    if conn.is_connected():
        cursor = conn.cursor()
        #cursor adalah objek perantara yang digunakan untuk menjalankan perintah SQL ke database dari Python.
        #commit() adalah perintah untuk menyimpan perubahan ke database secara permanen.

        def tampil_data():
            sql = "SELECT * FROM items"
            cursor.execute(sql)
            hasil = cursor.fetchall()
            for data in hasil:
                print(data)

    #running :
    tampil_data()

except Error as e:
    print("Terjadi error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
