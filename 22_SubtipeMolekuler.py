import matplotlib.pyplot as plt
labels = ['Luminal A', 'Luminal B', 'HER2+', 'TNBC']
sizes = [33.3, 46.67, 8.89, 11.11]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Subtipe Molekuler')
plt.show()