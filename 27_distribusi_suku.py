import matplotlib.pyplot as plt

# Data dari Tabel 4.1
labels = ['Jawa', 'Batak', 'Betawi', 'Sunda', 'Lainnya']
kanker = [57.78, 11.11, 13.33, 8.89, 8.89]    # Persentase kelompok kanker
kontrol = [22.22, 15.56, 15.56, 17.78, 28.89] # Persentase kelompok kontrol

# Warna untuk setiap suku (gunakan ColorBrewer palette)
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Buat figure dengan 2 subplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle('Distribusi Suku pada Kelompok Kanker Payudara vs Kontrol Sehat', 
            fontsize=14, fontweight='bold')

# Pie Chart Kanker Payudara
ax1.pie(kanker, labels=labels, autopct='%1.1f%%', startangle=90, 
        colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
ax1.set_title('Kanker Payudara (n=45)', pad=20, fontsize=12)

# Pie Chart Kontrol Sehat
ax2.pie(kontrol, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
ax2.set_title('Kontrol Sehat (n=45)', pad=20, fontsize=12)

# Atur layout dan simpan
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust untuk suptitle
plt.savefig('distribusi_suku_pie.png', dpi=300, bbox_inches='tight')
plt.show()