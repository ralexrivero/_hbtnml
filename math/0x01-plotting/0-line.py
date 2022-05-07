#!/usr/bin/env python3
""" Plot a line """
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(np.arange(0, 11), y, 'r')
plt.show()
