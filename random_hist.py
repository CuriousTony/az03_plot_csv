import numpy as np
import matplotlib.pyplot as plt

# Создай гистограмму для случайных данных, сгенерированных с помощью
# функции `numpy.random.normal`.

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)
plt.hist(data)
plt.title('Гистограмма случайных данных')
plt.xlabel('Ось Х')
plt.ylabel('Ось У')
plt.show()

# Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.

random_array1 = np.random.rand(5)
random_array2 = np.random.rand(5)
plt.scatter(random_array1, random_array2)
plt.title('Гистограмма рассеяния случайных данных')
plt.show()
