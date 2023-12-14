import numpy as np
import matplotlib.pyplot as plt 
import time as tm
from scipy.stats import norm, lognorm
import pandas as pd
import emcee
from scipy.optimize import minimize
import pygtc

data = pd.read_csv('Esercizio3.csv')
data

def log_prior(theta):
    m, s = theta
    if s>0:
        return 0.0
    return -np.inf

def log_likelihood(theta, y, yerr):
    m, s = theta
    sigma2 = s*2+yerr*2
    return -0.5 * np.sum((y - m) ** 2 / sigma2 + np.log(sigma2))

def log_posterior(theta, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, y, yerr)

np.random.seed(42)
nll = lambda *args: -log_posterior(*args)
initial = np.array([170, 1.])*(1+ 0.1 * np.random.randn(2))
soln = minimize(nll, initial, args=(data.Altezza, data.Errore))
m_bf, s_bf = soln.x
soln.x

pos = soln.x *(1+ 1e-4 * np.random.randn(32, 2))
nwalkers, ndim = pos.shape

sampler = emcee.EnsembleSampler(
    nwalkers, ndim, log_posterior, args=(data.Altezza, data.Errore)
)
sampler.run_mcmc(pos, 2000, progress=True);

fig, axes = plt.subplots(2, figsize=(10, 7), sharex=True)
samples = sampler.get_chain()
labels = ["$mu$", "$sigma$"]
for i in range(ndim):
    ax = axes[i]
    ax.plot(samples[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(samples))
    ax.set_ylabel(labels[i])
    ax.yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel("step number");
plt.show()
tau = sampler.get_autocorr_time()
print(tau)

flat_samples = sampler.get_chain(discard=100, flat=True)
print(flat_samples.shape)

GTC = pygtc.plotGTC(chains=flat_samples,
                    paramNames=['$mu$','$sigma$'],
                    chainLabels=['Altezza maschile'],
                    figureSize='MNRAS_page')