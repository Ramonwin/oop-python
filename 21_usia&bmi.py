import matplotlib.pyplot as plt
import numpy as np

labels = ['Kanker Payudara', 'Kontrol Sehat']
usia_means = [53.84, 36.89]
usia_std = [10.79, 13.84]
bmi_means = [25.35, 25.01]
bmi_std = [4.82, 4.40]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8,6))
rects1 = ax.bar(x - width/2, usia_means, width, yerr=usia_std, 
                label='Usia (tahun)', color='skyblue')
rects2 = ax.bar(x + width/2, bmi_means, width, yerr=bmi_std,
                label='BMI (kg/m²)', color='salmon')

ax.set_ylabel('Nilai')
ax.set_title('Perbandingan Usia dan BMI')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.savefig('usia_bmi_comparison.png', dpi=300)
plt.close()