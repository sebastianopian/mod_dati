import numpy as np
import matplotlib.pyplot as plt 
import time as tm
def MCRNG(seed, A, C, M):
    
    x = seed

    numbers = [ ]
    
    while True:
        x = ( A*seed + C )%M
        
        if (x in numbers):
            break
        else:
            numbers.append(x)
            seed = x
        
    return numbers
        
seed = 10
A = 36+1
C = 3
M = int(2**11)

start = tm.time()
x1 = np.array(MCRNG(seed, A, C, M))
print(tm.time()-start)
0.0572052001953125
print(len(x1))
2048
# lets see how we perform against python
rng = np.random.default_rng() # insi
start = tm.time()
x2 = rng.random(size=M)
print(tm.time()-start)  # as usual, build in functions are much quicker
0.00023317337036132812
start = tm.time()
x2 = MCRNG(seed, A, C, M)
print(tm.time()-start)

x_shuffle = np.array(x1)[x2]

plt.figure()
plt.scatter(x_shuffle[:-1], x_shuffle[1:], 
            c=np.arange(len(x_shuffle[:-1])))
plt.colorbar()