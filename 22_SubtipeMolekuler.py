import matplotlib.pyplot as plt

# Data subtipe molekuler
subtipe_labels = ['Luminal A', 'Luminal B', 'HER2+', 'TNBC']
subtipe_values = [33.3, 46.67, 8.89, 11.11]

# Data status ER
er_labels = ['ER+', 'ER−']
er_values = [80, 20]

# Membuat 2 pie chart berdampingan
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart subtipe molekuler
axs[0].pie(subtipe_values, labels=subtipe_labels, autopct='%1.1f%%',
           startangle=90, colors=plt.cm.Pastel1.colors)
axs[0].set_title('Subtipe Molekuler (Pasien Kanker)')

# Pie chart status ER
axs[1].pie(er_values, labels=er_labels, autopct='%1.1f%%',
           startangle=90, colors=plt.cm.Pastel2.colors)
axs[1].set_title('Status ER')

plt.tight_layout()
plt.show()
