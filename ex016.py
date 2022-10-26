""" Grafico de vendas """

import matplotlib.pyplot as plt
import numpy as np

n = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(n,y)
plt.show()