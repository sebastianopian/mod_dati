import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Caricamento dei dati
data = np.loadtxt("/Users/sebastianopian/Desktop/mod_dati/dat.txt")

# Standardizzazione dei dati
scaler = StandardScaler()
data_std = scaler.fit_transform(data)

# PCA Full
pca_full = PCA(n_components=data.shape[1])
data_pca_full = pca_full.fit_transform(data_std)
data_reconstructed_full = scaler.inverse_transform(pca_full.inverse_transform(data_pca_full))
print("Explained variance by component:", pca_full.explained_variance_ratio_)
plt.plot(pca_full.explained_variance_ratio_)
plt.ylabel("$\sigma^2$")
plt.xlabel('Component')

# PCA Reduced
pca_reduced = PCA(n_components=6)
data_pca_reduced = pca_reduced.fit_transform(data_std)
data_reconstructed_reduced = scaler.inverse_transform(pca_reduced.inverse_transform(data_pca_reduced))


# Grafico dei dati originali
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(data[:, 8], data[:, 4], '.')
plt.title('Dati Originali')
plt.xlabel('$b-y$')
plt.ylabel('Mass')

# Grafico dei dati ricostruiti con PCA Full
plt.subplot(1, 3, 2)
plt.plot(data_reconstructed_full[:, 8], data_reconstructed_full[:, 4], '.')
plt.title('Dati Ricostruiti con PCA Full')
plt.xlabel('$b-y$')
plt.ylabel('Mass')

# Grafico dei dati ricostruiti con PCA Reduced
plt.subplot(1, 3, 3)
plt.plot(data_reconstructed_reduced[:, 8], data_reconstructed_reduced[:, 4], '.')
plt.title('Dati Ricostruiti con PCA Reduced')
plt.xlabel('$b-y$')
plt.ylabel('Mass')

plt.tight_layout()
plt.show()