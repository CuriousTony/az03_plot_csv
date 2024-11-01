import pandas as pd
import matplotlib.pyplot as plt
import time

# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны
df = pd.read_csv('data_to_df.csv')
df['Цена'] = df['Цена'].str.replace(' ', '').astype(int)
print(f"Средняя цена в файле - {df['Цена'].mean()}")

prices = df['Цена']
plt.hist(prices, bins=10, edgecolor='black')
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()
time.sleep(5)
plt.close()
