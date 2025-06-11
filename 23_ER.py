import matplotlib.pyplot as plt
import numpy as np

# Data dari Tabel 4.1
er_labels = ['ER+', 'ER-']
er_values = [80, 20]  # Persentase

stage_labels = ['Stage I', 'Stage II', 'Stage III', 'Stage IV']
stage_values = [4.44, 33.33, 37.78, 24.44]  # Persentase

# Warna khusus onkologi
er_colors = ['#2ecc71', '#e74c3c']  # Hijau untuk ER+, Merah untuk ER-
stage_colors = ['#3498db', '#9b59b6', '#f1c40f', '#e67e22']  # Warna berbeda tiap stadium

# Buat figure dengan 2 subplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Karakteristik Kanker Payudara', fontsize=16, fontweight='bold')

# --- Diagram 1: Status ER ---
ax1.bar(er_labels, er_values, color=er_colors, edgecolor='black', width=0.6)
ax1.set_title('Status Reseptor Estrogen (ER)', pad=15, fontsize=14)
ax1.set_ylabel('Persentase (%)', fontsize=12)
ax1.set_ylim(0, 100)

# Tambahkan nilai di atas bar
for i, v in enumerate(er_values):
    ax1.text(i, v + 2, f"{v}%", ha='center', fontweight='bold')

# --- Diagram 2: Stadium Kanker ---
bars = ax2.bar(stage_labels, stage_values, color=stage_colors, edgecolor='black', width=0.7)
ax2.set_title('Distribusi Stadium', pad=15, fontsize=14)
ax2.set_ylim(0, 50)

# Custom label untuk stadium
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}%', ha='center', va='bottom', fontweight='bold')

# Atur grid dan layout
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust untuk suptitle

plt.savefig('er_stage_combined.png', dpi=300, bbox_inches='tight')
plt.show()