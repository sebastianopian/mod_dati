import numpy as np
import matplotlib.pyplot as mpl
import scipy.optimize as sopt

a= np.array([2,5,6,9,12,18,21])
mia=np.min(a)
maxa=np.max(a)
media=np.mean(a)
std=np.std(a)

print('min = {}, max = {}, mean= {}, std={}' .format(mia, maxa, media, std))

xv= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
yv=np.array([1,3,2,5,6,4,8,9,6,3,4,7])

mpl.plot(xv, color='red', marker='o', linestyle='dashed', linewidth='2', markersize=12, label='x')
mpl.plot(yv, color='blue', marker='o', linestyle='dashed', linewidth='2', markersize=9, label='x')
mpl.show()

mu=2
sigma=1.2
my_data=np.ranndom.normal(mu,sigma,10000)
gauss_hist= np.histogram(my_data, bins=50, density=True)
def gaus_for_fit(xvals,mu,sigma):
    px=(1./np.sqrt(2*np.pi*sigma**2))*np.exp(-(((xvals - mu)**2)/(2*sigma**2)))
    return px
_ = mpl.hist(gauss_hist, bins='auto') 
mpl.title("Histogram with 'auto' bins")
mpl.show()