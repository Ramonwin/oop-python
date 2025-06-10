import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "papacakep22",
        database = "db_retail"
    )

    if conn.is_connected():
        cursor = conn.cursor()

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
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
