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

    
    #running :
    #simpan_data(555555,"Pointer",125000,20)
    simpan_dataBanyak()
    tampil_data()
            
        
except Error as e :
    print('Terjadi kesalahan : ', e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
