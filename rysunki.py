import matplotlib.pyplot as plt
from random import randint
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
for element in x:
    y.append(element**2)
z = [randint(10, 150) for z in range(10000)]


fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist(z, bins=100)

print(y)


ax2.plot(x, y)
plt.show()
