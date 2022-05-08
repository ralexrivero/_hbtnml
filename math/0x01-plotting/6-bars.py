#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

labels = ['Farrah', 'Fred', 'Felicia']
width = 0.5

fig, ax = plt.subplots()

print(fig)
print(ax)
print(fruit)
print(fruit[0])

ax.bar(labels, fruit[0], width, label='apples', color='r')
ax.bar(labels, fruit[1], width, label='bannanas', color='y')
ax.bar(labels, fruit[2], width, label='orange', color='#ff8000')
ax.bar(labels, fruit[3], width, label='peaches', color='#ffe5b4')

plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
ax.legend()
plt.show()
