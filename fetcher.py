import sys
import xlrd

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.cluster import SpectralClustering
from sklearn.linear_model import LinearRegression
from scipy.cluster.hierarchy import dendrogram, linkage


xlsNameToNumber = {
	"Cores": 1,
 	"Rmax": 2,
	"Rpeak": 3,
	"Power": 5 # 2008+
}



# returns a python array from top500_data
def createTab(startYear, endYear, param):
	retour = []
	columnIndex = xlsNameToNumber[param]
 
	for year in range(startYear, endYear+1):
		file = xlrd.open_workbook("xls/TOP500_" + str(year) + "06.xls")
		sheet = file.sheet_by_index(0)
		retour += sheet.col_values(columnIndex, 1)
		file = xlrd.open_workbook("xls/TOP500_" + str(year) + "11.xls")
		sheet = file.sheet_by_index(0)
		retour += sheet.col_values(columnIndex, 1)
		
	return retour


# returns a 2D np.array out of 2 native python arrays of the same size
def createMatrix(xTab, yTab):
	
	if len(xTab) != len(yTab):
		sys.exit("Different parameters size: cannot compute matrix")
	
	ret = []
	
	for i in range(1, len(xTab)):
		ret.append([xTab[i], yTab[i]])
  

	# ret2 = [[0 for x in range(len(ret))] for y in range(len(ret))] 
	
	# for i in range(len(ret)):
		# for j in range(len(ret)):
			# ret2[i][j] = np.sqrt((ret[j][0] - ret[i][0])**2 + (ret[j][1] - ret[i][1])**2)


	# ret2 = np.array(ret2)
	# ret2 = np.exp(- ret2** 2 / (2. * 1 ** 2))
	# print(ret2)

	print("Matrix created")
	return np.array(ret)



def purgeTabs(x, y):
	
	x1 = []
	y1 = []
	
	toAdd = True
	
	for i in range(len(x)):
		for j in range(len(x1)):
			if(x1[j] == x[i] and y1[j] == y[j]):
				toAdd = False
				break
		if toAdd:
			x1.append(x[i])
			y1.append(y[i])
		else:
			toAdd = True
			
	print("Removed", len(x) - len(x1), "duplicates")
	return x1, y1


# returns a 2D np.array from top500_data, given a time interval (inclusive) and 2 parameters
# and the 2 np arrays corresponding to the specified parameters
# currently:
#	min year = 2000
#	max year = 2020
# 	params = ["Rpeak", "Rmax", "Cores", "Power"]
def getNPArrays(paramX, paramY, startYear = 2010, endYear = 2020, log = False):
	x = createTab(startYear, endYear, paramX)
	y = createTab(startYear, endYear, paramY)

	x, y = purgeTabs(x, y)

	if log:
		for index in range(0, len(x)):
			x[index] = np.log(x[index])
			y[index] = np.log(y[index])

	return createMatrix(x, y), np.array(x), np.array(y)



tab, x, y = getNPArrays("Cores", "Rpeak", 2020, 2020, log=True)

plt.scatter(tab[:,0], tab[:,1], label="True Position", s=2)
plt.savefig("img/points_log2.png", bbox_inches = "tight")


plt.clf()

#####
# https://www.datatechnotes.com/2020/12/spectral-clustering-example-in-python.html
#####


clustering = SpectralClustering(n_clusters=2, assign_labels="kmeans", eigen_solver='amg', affinity="nearest_neighbors").fit(tab)
plt.scatter(tab[:,0],tab[:,1], label="True Position", c = clustering.labels_, s=2)
plt.savefig("img/spectral.png", bbox_inches = "tight") 



"""

labels = range(1, 11)

for label, x, y in zip(labels, tab[:, 0], tab[:, 1]):
	plt.annotate(
		label,
		xy=(x, y), xytext=(-3, 3),
		textcoords='offset points', ha='right', va='bottom')

linked = linkage(tab1, 'single')

labelList = range(1, len(tab1)+1)

plt.figure(figsize=(10, 7))
dendrogram(linked,
			orientation='top',
			labels=labelList,
			distance_sort='descending',
			show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('sample index or (taille du cluster)')
plt.ylabel('distance')
plt.savefig("img/hierarchy.png", bbox_inches = "tight") 
plt.clf()


plt.scatter(tab[:,0], tab[:,1], label="True Position", s=2)
plt.savefig("img/points_lin.png", bbox_inches = "tight")

plt.clf()

plt.yscale("log")
plt.xscale("log")

plt.scatter(tab[:,0], tab[:,1], label="True Position", s=2)
plt.savefig("img/points_log.png", bbox_inches = "tight")

plt.clf()

plt.scatter(tab2[:,0], tab2[:,1], label="True Position", s=2)
plt.savefig("img/points_log2.png", bbox_inches = "tight")

plt.clf()



kmeans = KMeans(n_clusters=4)
kmeans.fit(tab1)
plt.scatter(tab[:,0],tab[:,1], c=kmeans.labels_, cmap='rainbow', s=2)
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.savefig("img/kmeans.png", bbox_inches = "tight") 

plt.clf()



data = np.vstack([x, y]).T
model = GaussianMixture (n_components=2).fit(data)
plt.scatter(x2, y2, c=model.predict(data), s=2)
plt.savefig("img/regression", bbox_inches = "tight") 

plt.clf()




plt.clf()

clustering = SpectralClustering(n_clusters=2, assign_labels="discretize", random_state=0, affinity="precomputed").fit_predict(tab2)
plt.scatter(tab[:,0],tab[:,1], label="True Position", c = clustering, s=2)
plt.savefig("img/spectral.png", bbox_inches = "tight") 




x = x.reshape(-1,1)

reg = LinearRegression()
predict_space = np.linspace(min(x), max(x)).reshape(-1,1)
reg.fit(x,y)
predicted = reg.predict(predict_space)
plt.plot(predict_space, predicted, color='red', linewidth=2)
plt.scatter(x=x,y=y, s=2)
plt.xlabel('pelvic_incidence')
plt.ylabel('sacral_slope')
plt.savefig("img/linreg.png", bbox_inches = "tight") 



"""

