from logging.config import valid_ident
import matplotlib.pyplot as plt
from random import randint, sample
"""year = [2015, 2017, 2019, 2021, 2022]
pop = [3.45, 4.22, 4.69, 5.01, 5.56]
ans = [64, 65, 66.8, 68, 70]
#plt.plot(year,ans)
#plt.scatter(year,pop)
plt.show()"""
values = []
#v = sample(range(0,15),12)
for i in range(13):
    n = randint(0,15)
    values.append(n)
print(f" The values are : {values}")
plt.hist(values, bins=3)
plt.show()
