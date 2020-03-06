import numpy as np
import networkx as nx
import csv
import sys
import os
from convertingMATtoCSV import getData

dataDict = getData('brainnetworks/')
firstKey = list(dataDict.keys())[3]

m = dataDict[firstKey][-1]

#make a networkx graph from the sim matrix
def makeGraph(m):
	G=nx.Graph()
	maxVal = np.max(m)
	for i in range(len(m)):
		for j in range(len(m[i])):
			#0 technically isn't a connection so we don't add it
			if m[i,j] != 0:
				normalizedWeight = maxVal - m[i,j]
				G.add_edge(i, j, weight=normalizedWeight)
	return G

def removeNewCSVs():
	os.remove('csv/EBC.csv')
	os.remove('csv/NBC.csv')
	os.remove('csv/C.csv')
	os.remove('csv/PR.csv')
	os.remove('csv/all.csv')

def writeRowToCSV(subjectID, G, EBC, NBC, C, PR, x):
	bigRow=subjectID + ','

	#EBC writing, need to handle cases for edges that may exist
	#in one graph but not another, set to 0 --- 2416 entries... not sure how
	row=subjectID + ','
	for i in range(0, 70):
		for j in range(i+1, 70):
			if((i, j) in EBC):
				row += str(EBC[(i, j)]) + ","
				#bigRow += str(EBC[(i, j)]) + ","
			else:
				row += "0,"
				#bigRow += "0,"
	row = row[:-1] + '\n'
	with open('csv/EBC.csv', 'a') as File:
		File.write(row)
	
	#NBC writing --- 70 entries
	row=subjectID + ','
	for i in range(len(NBC)):
		row += str(NBC[i]) + ','
		bigRow += str(NBC[i]) + ','
	row = row[:-1] + '\n'
	with open('csv/NBC.csv', 'a') as File:
		File.write(row)

	#COM writing ---  entries
	#row=''
	#for i in range(len(list(COM.keys()))):
	#	for j in range(len(COM[i])):
	#		row += str()

	#Clustering coefficients  --- 70 entries
	row=subjectID + ','
	for i in range(len(C)):
		row += str(C[i]) + ','
		bigRow += str(C[i]) + ','
	row = row[:-1] + '\n'
	with open('csv/C.csv', 'a') as File:
		File.write(row)

	#Page Rank --- 70 entries
	row=subjectID + ','
	for i in range(len(PR)):
		row += str(PR[i]) + ','
		bigRow += str(PR[i]) + ','
	row = row[:-1] + '\n'
	with open('csv/PR.csv', 'a') as File:
		File.write(row)

	#the one that we're doing outside of paper
	#right now its second order centrality
	row=subjectID + ','
	for i in range(len(x)):
		row += str(x[i]) + ','
		bigRow += str(x[i]) + ','
	row = row[:-1] + '\n'
	with open('csv/SOC.csv', 'a') as File:
		File.write(row)

	bigRow = bigRow[:-1] + '\n'
	with open('csv/all.csv', 'a') as File:
		File.write(bigRow)



removeNewCSVs()
for subject in dataDict:
	m = dataDict[subject][-1]

	G=makeGraph(m)
	EBC = nx.edge_betweenness_centrality(G, normalized=False)
	NBC = nx.betweenness_centrality(G, normalized=False)
	#COM = nx.communicability(G)	
	C = nx.clustering(G)
	PR = nx.pagerank(G)
	x = nx.second_order_centrality(G)


	writeRowToCSV(subject, G, EBC, NBC, C, PR, x)
