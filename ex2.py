import numpy as np
import matplotlib.pyplot as mpl

b_y= np.loadtxt("data.txt", usecols=8, dtype='float') 
Mass= np.loadtxt("data.txt", usecols=4, dtype='float') 
age= np.loadtxt("data.txt", usecols=12, dtype='float') 
np.where(age>0 and age<1), mpl.scatter(b_y , Mass , c= 'purple', marker='.', s=3)
np.where(age >1 and age <2), mpl.scatter(b_y , Mass , c= 'blue', marker='.', s=3)
np.where(age >2 and age <3), mpl.scatter(b_y , Mass , c= 'deepskyblue', marker='.', s=3)
np.where(age >3 and age <4), mpl.scatter(b_y , Mass , c= 'aquamarine', marker='.', s=3)
np.where(age >4 and age <5), mpl.scatter(b_y , Mass , c= 'lime', marker='.', s=3)
np.where(age >5 and age <6), mpl.scatter(b_y , Mass , c= 'darkgreen', marker='.', s=3)
np.where(age >6 and age <7), mpl.scatter(b_y , Mass , c= 'yellow', marker='.', s=3)
np.where(age >7 and age <8), mpl.scatter(b_y , Mass , c= 'gold', marker='.', s=3)
np.where(age >8 and age <9), mpl.scatter(b_y , Mass , c= 'darkorange', marker='.', s=3)
np.where(age >9 and age <10), mpl.scatter(b_y , Mass , c= 'sienna', marker='.', s=3)
np.where(age >10 and age <11), mpl.scatter(b_y , Mass , c= 'red', marker='.', s=3)
np.where(age >11 and age <12), mpl.scatter(b_y , Mass , c= 'grey', marker='.', s=3)
np.where(age >12 and age <13), mpl.scatter(b_y , Mass , c= 'black', marker='.', s=3)
    
mpl.show()
