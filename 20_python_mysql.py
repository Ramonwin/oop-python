import mysql.connector

# Koneksi ke database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Ganti dengan password MySQL kamu
    database="db_asset2025"
)

cursor = conn.cursor()

# Eksekusi query
cursor.execute("SELECT * FROM divisis")

# Ambil semua data
hasil = cursor.fetchall()

# Tampilkan data
for row in hasil:
    print(f"ID: {row[0]}, Nama: {row[1]}")

# Tutup koneksi
cursor.close()
conn.close()
