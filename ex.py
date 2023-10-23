import numpy as np
import matplotlib.pyplot as mpl

b_y= np.loadtxt("data.txt", usecols=8, dtype='float') 
Mass= np.loadtxt("data.txt", usecols=4, dtype='float') 
age= np.loadtxt("data.txt", usecols=12, dtype='float') 
i=0
for i in range(len(age)):
    if (age[i]>0 and age[i]<1):
       mpl.scatter(b_y[i], Mass[i], c= 'purple', marker='.', s=3)
    elif (age[i]>1 and age[i]<2):
       mpl.scatter(b_y[i], Mass[i], c= 'blue', marker='.', s=3)
    elif (age[i]>2 and age[i]<3):
       mpl.scatter(b_y[i], Mass[i], c= 'deepskyblue', marker='.', s=3)
    elif (age[i]>3 and age[i]<4):
       mpl.scatter(b_y[i], Mass[i], c= 'aquamarine', marker='.', s=3)
    elif (age[i]>4 and age[i]<5):
       mpl.scatter(b_y[i], Mass[i], c= 'lime', marker='.', s=3)
    elif (age[i]>5 and age[i]<6):
       mpl.scatter(b_y[i], Mass[i], c= 'darkgreen', marker='.', s=3)
    elif (age[i]>6 and age[i]<7):
       mpl.scatter(b_y[i], Mass[i], c= 'yellow', marker='.', s=3)
    elif (age[i]>7 and age[i]<8):
       mpl.scatter(b_y[i], Mass[i], c= 'gold', marker='.', s=3)
    elif (age[i]>8 and age[i]<9):
       mpl.scatter(b_y[i], Mass[i], c= 'darkorange', marker='.', s=3)
    elif (age[i]>9 and age[i]<10):
       mpl.scatter(b_y[i], Mass[i], c= 'sienna', marker='.', s=3)
    elif (age[i]>10 and age[i]<11):
       mpl.scatter(b_y[i], Mass[i], c= 'red', marker='.', s=3)
    elif (age[i]>11 and age[i]<12):
       mpl.scatter(b_y[i], Mass[i], c= 'grey', marker='.', s=3)
    elif (age[i]>12 and age[i]<13):
        mpl.scatter(b_y[i], Mass[i], c= 'black', marker='.', s=3)
    i=i+1
    
    
mpl.show()