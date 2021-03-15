import sys
import xlrd

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.cluster import SpectralClustering


xlsNameToNumber = {
	"Cores": 1,
 	"Rmax": 2,
	"Rpeak": 3,
	"Power": 5
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
		
	ret = np.array(ret)
	return ret


# returns a 2D np.array from top500_data, given a time interval (inclusive) and 2 parameters
# and the 2 np arrays corresponding to the specified parameters
# currently:
#	min year = 2010
#	max year = 2020
# 	params = ["Rpeak", "Rmax", "Cores", "Power"]
def getNPArrays( paramX, paramY, startYear = 2010, endYear = 2020, log = False):
	x = createTab(startYear, endYear, paramX)
	y = createTab(startYear, endYear, paramY)
 
	if log:
		for index in range(0, len(x)):
			x[index] = np.log(x[index])
			y[index] = np.log(y[index])
	
	return createMatrix(x, y), np.array(x), np.array(y)



tab, x, y = getNPArrays("Cores", "Rpeak", 2019, 2019)
tab2, x2, y2 = getNPArrays("Cores", "Rpeak", 2019, 2019, log=True)


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



kmeans = KMeans(n_clusters=2)
kmeans.fit(tab2)
plt.scatter(tab2[:,0],tab2[:,1], c=kmeans.labels_, cmap='rainbow', s=2)
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.savefig("img/kmeans.png", bbox_inches = "tight") 

plt.clf()

data = np.vstack([x2, y2]).T
model = GaussianMixture (n_components=2).fit(data)
plt.scatter(x2, y2, c=model.predict(data), s=2)
plt.savefig("img/regression", bbox_inches = "tight") 

plt.clf()

clustering = SpectralClustering(n_clusters=2, assign_labels="discretize", random_state=0).fit_predict(tab2)
plt.scatter(tab2[:,0],tab2[:,1], label="True Position", c = clustering, s=2)
plt.savefig("img/spectral.png", bbox_inches = "tight") 