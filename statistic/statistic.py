import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

plt.figure()

data = pd.read_csv('data.csv')
data = data.astype(float)

print(stats.kstest('norm', 'norm', N=3))
print(stats.kstest('norm', 'norm', N=500))

print(stats.kstest(data, 'norm', (data.mean(), data.std()), N=len(data)))

data.plot(kind='bar', xlabel='Number of measure ', ylabel='Temperature, °C', title='Data')
data.plot.kde(xlabel='Number of measure ', title='Data')

plt.legend()
plt.show()


