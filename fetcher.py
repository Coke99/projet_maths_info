from sklearn.cluster import SpectralClustering
import numpy as np
import matplotlib.pyplot as plt
import sys 

from data import *


# returns a python array from top500_data
def createTab(startYear, endYear, param):
	ret = []
 
	for year in range(startYear, endYear+1):
		ret += top500_data[str(year)]["june"][param]
		ret += top500_data[str(year)]["nov"][param]

	return ret


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
# currently:
#	min year = 2011
#	max year = 2020
# 	params = ["Rpeak", "Cores"]
def getNPArray(startYear, endYear, paramX, paramY):
	x = createTab(startYear, endYear, paramX)
	y = createTab(startYear, endYear, paramY)
	
	return createMatrix(x, y)


tab = getNPArray(2011, 2020, "Cores", "Rpeak")