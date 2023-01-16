import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Book.csv')

category = data['category']
sale = data['sale']

plt.title('Data Penjualan Produk Selama 1 Minggu')
plt.bar(category, sale)

plt.show()
