import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#objects = ('America', 'India', 'Africa', 'UK', 'UAE','Iran')
objects = ('Brazil', 'Italy', 'Canada', 'France', 'UK','India','Germany','Japan','China','USA')
y_pos = np.arange(len(objects))
performance=[1.80,2.00,2.10,2.80,3.30,3.50,4.10,4.80,19.80,24.10]

plt.barh(y_pos, performance, align='center', alpha=1)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Top 10 Economies of the World in 2022')

plt.show()
