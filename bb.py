
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
print(len(x1))
rng = np.random.default_rng() # insi
start = tm.time()
x2 = rng.random(size=M)
print(tm.time()-start)  # as usual, build in functions are much quicker

start = tm.time()
x2 = MCRNG(seed, A, C, M)
print(tm.time()-start)

x_shuffle = np.array(x1)[x2]

plt.figure()
plt.scatter(x_shuffle[:-1], x_shuffle[1:],
            c=np.arange(len(x_shuffle[:-1])))
plt.colorbar()

plt.figure()
plt.scatter(x1[:-1], x1[1:], c=np.arange(len(x1[:-1])))
plt.colorbar()
plt.xlabel('$x_i$')
plt.ylabel('$x_{i+1}$')

plt.figure()
plt.scatter(x_shuffle[:-1], x_shuffle[1:],
            c=np.arange(len(x_shuffle[:-1])))
plt.xlabel('$x_i$')
plt.ylabel('$x_{i+1}$')
plt.colorbar()


plt.figure()
plt.scatter(x2[:-1], x2[1:], c=np.arange(len(x2[:-1])))
plt.colorbar()
plt.xlabel('$x_i$')
plt.ylabel('$x_{i+1}$')

p = 0.3
bern1 = np.where(np.array(x2/np.max(x2))<p, 1, 0)

_ = plt.hist(bern1)

# consider a multiple choice test with N=15 questions with four answers each, of which only one is correct.
# How many correct answers will you get, if you randomly choose answers (p=1/4)

from scipy.special import comb
# https://stackoverflow.com/questions/26560726/python-binomial-coefficient

N = 16
p = 0.25

def Fails(p):
    
    count = 0
    
    while rng.random()>p:
        count += 1
    
    return count
p = 0.3

ints = np.arange(20)

k_geo = np.array([Fails(p) for i in range(num)])
k_geo2 = rng.geometric(p, size=num)-1  # python defines it as numbers of trials to run until success,
# while we consider number of failures before success, which is one less

_ = plt.hist(k_geo, bins = ints-0.5, density=True)
_ = plt.hist(k_geo2, bins = ints-0.5, density=True, histtype='step')

prob =  p * (1-p)**ints[:-1]

print(prob)

_ = plt.plot(ints[:-1], prob, '*')

def TakeTheTest(N, p):
    
    answers = rng.uniform(size=N)
    
    return np.sum(np.where(answers<p, 1, 0))
    
num = 2048

ks = np.array([TakeTheTest(N, p) for i in range(num)])
ks2 = rng.binomial(N, p, size=num)

ints = np.arange(15)

_ = plt.hist(ks, bins = ints-0.5, density=True)
_ = plt.hist(ks2, bins = ints-0.5, density=True, histtype='step')

prob = comb(N, ints[:-1])* p**ints[:-1] * (1-p)**(N-ints[:-1])

print(prob)

_ = plt.plot(ints[:-1], prob, '*')

lam = 5

t = rng.exponential(scale=1/lam, size=num)

t2 = -1./lam * np.log(1-rng.uniform(size=num))

bins = np.linspace(0, 1.6, num=15)

_ = plt.hist(t, density=True, bins=bins)
_ = plt.hist(t2, density=True, histtype='step', bins=bins)

from scipy.stats import poisson
# Poisson, average number of goals per football match nave = 2.5

# binomial for N--> inf and p*N = n expected = constant



nave = 2.5
ngoals = rng.poisson(nave, size=1000)

n = np.arange(12)

fact_n = np.array([np.math.factorial(x) for x in n])

pdf = nave**n * np.exp(-nave) / fact_n
# attention, goals are not independent events, so -- in principle -- a poission distribution might not be the
# correct description!!

plt.figure()
_ = plt.hist(ngoals, bins=n-0.5, density=True)
plt.plot(n, pdf, '*')


# central limit theorem

mu = 0.5

reps = 1000
N = 2000

var = 1/12/reps

# we leave it to the reader to show that for x ~ U(0,1), <x> = 0.5 and Var[x] = 1/12 --> Homework!!!

x = rng.uniform(size=(reps, N))
u = np.mean(x, axis=0)

plt.figure()
_ = plt.hist(x.flatten(), density=True)

plt.figure()
_ = plt.hist(u, density=True)

xx = np.linspace(0.45, 0.55)

_ = plt.plot(xx, 1./np.sqrt(2*np.pi*var)*np.exp(-0.5*(xx-mu)**2/var))

N = 400
rng = np.random.default_rng()

cauchy_points = rng.standard_cauchy(size=(N, N, N))
cauchy_mean = np.mean(cauchy_points, axis=0)
cauchy_mean_mean = np.mean(cauchy_mean, axis=0)

print(cauchy_points.shape, cauchy_mean.shape, cauchy_mean_mean.shape)
bins = np.linspace(-10, 10)
pdf = 1/np.pi * 1/(1+bins**2)
fig, ax = plt.subplots(1, 3, figsize=(10, 5))
_ = ax[0].hist(cauchy_points.flatten(), density=True, bins=bins)
_ = ax[0].plot(bins, pdf)
_ = ax[1].hist(cauchy_mean.flatten(), density=True, bins=bins)
_ = ax[1].plot(bins, pdf)
_ = ax[2].hist(cauchy_mean_mean, density=True, bins=bins)
_ = ax[2].plot(bins, pdf)
