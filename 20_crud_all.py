'''
┌──────────────┐
│   Python     │
└─────┬────────┘
      │
      ▼
┌──────────────┐
│ mysql.connector.connect()         ◀─── membuat koneksi ke DB
└─────┬────────┘
      │
      ▼
┌──────────────┐
│    db.cursor()                     ◀─── membuat cursor dari koneksi
└─────┬────────┘
      │
      ▼
┌─────────────────────────────┐
│ cursor.execute(SQL, params) ◀─── mengirim query ke server MySQL
└─────┬───────────────────────┘
      │
      ▼
┌───────────────────────┐
│    Server MySQL       │     ◀─── MySQL memproses perintahnya
└─────┬─────────────────┘
      │
      ▼
┌──────────────────────┐
│  (Jika SELECT)        │
│  cursor.fetchall()    │  ◀─── ambil hasil data dari DB
└────────┬──────────────┘
         │
         ▼
┌────────────────────────┐
│   Data siap digunakan  │
│   di Python (print, UI)│


pip install mysql-connector-python

jika muncul segmentation fault.. bukan dari python nya tapi dari library Mysql nya
rubah versi ke 
python -m pip install mysql-connector-python==8.0.20
'''

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
        #conn.commit() adalah perintah untuk menyimpan perubahan ke database secara permanen.
        def tampil_data():
            sql = "SELECT * FROM items"
            cursor.execute(sql)
            hasil = cursor.fetchall()
            for data in hasil:
                print(data)

        def simpan_data(sku, nama_item, harga, stok):
            sql = "INSERT INTO items (sku, nama_item, harga, stok) VALUES (%s,%s,%s,%s)"
            val = (sku, nama_item, harga, stok)
            cursor.execute(sql, val)
            conn.commit()
            print("Data berhasil ditambahkan.")

        def simpan_dataBanyak():
            sql = "INSERT INTO items(sku, nama_item, harga, stok) values(%s,%s,%s,%s)"
            val = [(666666, "Laptop 1", 5000000,10),
                    (777777, "Laptop 2", 5000000,10),
                    (888888, "Laptop 3", 5000000,10),
                    (999999, "Laptop 4", 5000000,10),
                    (121212, "Laptop 5", 5000000,10)]
            
            for data in val:
                cursor.execute(sql,data)
                conn.commit()
            
            print("Data Berhasil disimpan")

        def ubah_data(id, sku, nama_item, harga, stok):
            sql = "UPDATE items SET sku = %s, nama_item = %s, harga = %s, stok = %s WHERE id = %s"
            val = (sku, nama_item, harga, stok,id)
            cursor.execute(sql, val)
            conn.commit()
            print("Data berhasil diubah.")

        def hapus_data(id):
            sql = "DELETE FROM items WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            conn.commit()
            print("Data berhasil dihapus.")

        '''
        (id) = bukan tuple → hanya angka
        (id,) = tuple satu elemen
        Wajib pakai , untuk format parameter SQL yang benar
        '''

        #Running :
        
        #simpan_data(555555,"Pointer",150000,5)
        #ubah_data(9,555555,"mousepad",10000,12)
        #hapus_data(9)

        #simpan_dataBanyak()
        tampil_data()

except Error as e:
    print("Terjadi error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
