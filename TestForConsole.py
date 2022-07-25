import seaborn as sns
import numpy as np

x = np.array([1,2,3,4,5]).reshape((-1,1))
y = np.array([6,7,8,9,10])

sns.regplot(x=x,y=y)