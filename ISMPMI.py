import quandl
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = quandl.get('ISM/MAN_PMI', authtoken='XPC5T_rCEEd5aNnys5rn')

print(df.tail(5))

df.plot()
plt.title('ISM')
plt.show()
