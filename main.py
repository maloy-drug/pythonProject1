import random
import scipy.optimze as opt
import matplotlib as plt
import numpy as np

x=np.linspace(0,30,30)
y=[]
for i in x:
    y.append(0.02*i**3-0.1*i**2+5*i+100*random.random()+50)
plt.plot(x,y,'*')
plt.show()




