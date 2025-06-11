import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # kosong kalau pakai XAMPP default
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
                
        def simpan_data(sku, nama_item, harga, stok):
            sql = "INSERT INTO items(sku,nama_item,harga,stok) VALUES(%s,%s,%s,%s)"
            val = (sku,nama_item,harga,stok)
            cursor.execute(sql,val)
            conn.commit()
            print("Data Berhasil disimpan")
            
            
        #running :
        simpan_data(444444,"mouse",100000,15)
        tampil_data()
except Error as e:
    print("Terjadi kesalahan:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
