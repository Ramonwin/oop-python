import matplotlib.pyplot as plt
import numpy as np

# Data dari Tabel 4.1
kategori = ['Kanker Payudara', 'Kontrol Sehat']
merokok = [5, 0]          # 11.11% dari 45 pasien
mantan_merokok = [8, 0]   # 17.78% dari 45 pasien
tidak_merokok = [32, 45]  # 71.11% dari 45 pasien

# Konversi ke persentase (opsional)
total = np.array([45, 45])  # Total pasien per kelompok
merokok_pct = np.array(merokok) / total * 100
mantan_pct = np.array(mantan_merokok) / total * 100
tidak_pct = np.array(tidak_merokok) / total * 100

# Warna untuk stacking
colors = ['#ff6b6b', '#ffa502', '#2ed573']  # Merah, Oranye, Hijau

# Plot Stacked Bar
fig, ax = plt.subplots(figsize=(8, 6))

# Stack bagian-bagian
ax.bar(kategori, merokok_pct, label='Merokok Saat Ini', color=colors[0])
ax.bar(kategori, mantan_pct, bottom=merokok_pct, 
       label='Mantan Perokok', color=colors[1])
ax.bar(kategori, tidak_pct, 
       bottom=merokok_pct + mantan_pct, 
       label='Tidak Pernah Merokok', color=colors[2])

# Customisasi
ax.set_title('Perbandingan Status Merokok', pad=20, fontweight='bold')
ax.set_ylabel('Persentase (%)')
ax.legend(loc='upper right')

# Tambahkan label nilai di atas bar
for i in range(len(kategori)):
    plt.text(i, merokok_pct[i]/2, f"{merokok_pct[i]:.1f}%", 
             ha='center', color='white', fontweight='bold')
    plt.text(i, merokok_pct[i] + mantan_pct[i]/2, f"{mantan_pct[i]:.1f}%", 
             ha='center', color='white', fontweight='bold')
    plt.text(i, merokok_pct[i] + mantan_pct[i] + tidak_pct[i]/2, 
             f"{tidak_pct[i]:.1f}%", ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('status_merokok_stacked.png', dpi=300, bbox_inches='tight')
plt.show()