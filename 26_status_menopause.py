import matplotlib.pyplot as plt
import numpy as np

# Data dari Tabel 4.1 (dalam persentase)
kategori = ['Pre Menopause', 'Perimenopause', 'Postmenopause']
kanker = [24.44, 31.11, 44.44]    # Data kelompok kanker
kontrol = [71.11, 20.00, 8.89]    # Data kelompok kontrol sehat

x = np.arange(len(kategori))  # Posisi label
width = 0.35  # Lebar bar

fig, ax = plt.subplots(figsize=(10, 6))

# Buat grouped bars
rects1 = ax.bar(x - width/2, kanker, width, label='Kanker Payudara', 
                color='#ff7675', edgecolor='black')
rects2 = ax.bar(x + width/2, kontrol, width, label='Kontrol Sehat', 
                color='#74b9ff', edgecolor='black')

# Customisasi
ax.set_title('Perbandingan Status Menopause', pad=20, fontsize=14, fontweight='bold')
ax.set_xlabel('Status Menopause', fontsize=12)
ax.set_ylabel('Persentase (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(kategori)
ax.legend()

# Tambahkan nilai di atas bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

autolabel(rects1)
autolabel(rects2)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('status_menopause_grouped.png', dpi=300, bbox_inches='tight')
plt.show()