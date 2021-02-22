# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 02:53:04 2021

@author: baraf
"""

" implementation methode de clustering hierachiaque "

import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

X = np.array([[50,30],[10,15],[40,12],[24,10],[10,30],
              [85,70],[30,30],[50,78],[60,55],[70,85]])

labels = range(1, 11)
plt.scatter(X[:,0],X[:,1], label='True Position')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
plt.show()

linked = linkage(X, 'single')

labelList = range(1, 11)

plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('sample index or (taille du cluster)')
plt.ylabel('distance')
plt.show()


" implementation methode de clustering centroide avec le k-Means "


import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[50,30],[10,15],[40,12],[24,10],[10,30],
              [85,70],[30,30],[50,78],[60,55],[70,85]])

plt.scatter(X[:,0],X[:,1], label='True Position')
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
#les nouvelles valeurs de centroïde
print("les coordonnées des centroïdes")
print( kmeans.cluster_centers_)
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')

##coloration des centroïdes de chaque cluster 
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.title('clustering centroide avec le k-Means')
plt.show()
