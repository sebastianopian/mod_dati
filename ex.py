import numpy as np
array_1= np.random.randint(0,25,(20))
array_2= b=np.random.randint(0,2,(20))
array_20 = np.where( array_2==0, 0.001,0)
array_200= array_2+array_20
print(array_1/array_200)
i= np.where(np.isinf(array_1/array_2)==True)
print(i)