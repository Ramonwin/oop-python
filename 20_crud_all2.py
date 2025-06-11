import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(
<<<<<<< HEAD
        host="localhost",
        user="root",
        password="",  # kosong kalau pakai XAMPP default
        database="db_retail"
=======
        host = "localhost",
        username = "root",
        password = "papacakep22",
        database = "db_retail"
>>>>>>> 8770d975347099c7fb665e84468db16eebf03659
    )
    if conn.is_connected():
        cursor = conn.cursor()
<<<<<<< HEAD
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
=======

    def tampil_data():
        sql = "SELECT * FROM items"
        cursor.execute(sql)
        hasil = cursor.fetchall()
        for data in hasil:
            print(data)

    def simpan_data(sku, nama_item, harga, stok):
        sql = "INSERT INTO items(sku, nama_item, harga, stok) values(%s,%s,%s,%s)"
        val = (sku, nama_item, harga,stok)
        cursor.execute(sql,val)
        conn.commit()
        print("Data Berhasil disimpan")

    
    #running :
    simpan_data(555555,"Pointer",125000,20)
    tampil_data()
            
        
except Error as e :
    print('Terjadi kesalahan : ', e)
>>>>>>> 8770d975347099c7fb665e84468db16eebf03659
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
