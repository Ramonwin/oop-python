import matplotlib.pyplot as plt

# Data stadium kanker (dalam persentase)
stadium_labels = ['Stadium I', 'Stadium II', 'Stadium III', 'Stadium IV']
stadium_values = [4.44, 33.33, 37.78, 24.44]

# Data grade histopatologi (dalam persentase)
grade_labels = ['Grade 1', 'Grade 2', 'Grade 3']
grade_values = [2.44, 55.56, 40.0]

# Buat 1 bar chart dan 1 pie chart berdampingan
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Diagram batang stadium kanker
axs[0].bar(stadium_labels, stadium_values, color='#ffcc99')
axs[0].set_title('Distribusi Stadium Kanker')
axs[0].set_ylabel('Persentase (%)')
axs[0].set_ylim(0, 50)

# Diagram pie grade histopatologi
axs[1].pie(grade_values, labels=grade_labels, autopct='%1.1f%%',
           startangle=90, colors=plt.cm.Set3.colors)
axs[1].set_title('Grade Histopatologi')

# Atur layout dan tampilkan
plt.tight_layout()
plt.show()
