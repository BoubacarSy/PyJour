import numpy as np
height = [1.45,1.85,1.95,1.80]
weight = [45,72,80,75]
np_height = np.array(height)
np_weight  =np.array(weight)

BMi = np_weight / np_height ** 2

print(BMi[1])
