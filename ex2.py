import numpy as np
import matplotlib.pyplot as mpl
import pandas as pa

b_y= np.loadtxt("data.txt", usecols=8, dtype='float') 
Mass= np.loadtxt("data.txt", usecols=4, dtype='float') 
age= np.loadtxt("data.txt", usecols=12, dtype='float') 

a= mpl.scatter(b_y , Mass , c= age, marker='.', s=3)
mpl.colorbar(a)    
mpl.show()