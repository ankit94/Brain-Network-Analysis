import scipy.io
import numpy as np
from os import listdir
from os.path import isfile, join
import pandas as pd

#dictionary format:
#['<subjectID>']: [sex, age, FSIQ, Neuroticism, Extraversion, Openness, Agreeableness, Conscientiousness]
def getData(path):
	files = [f for f in listdir(path+'/smallgraphs') if isfile(join(path+'/smallgraphs', f))]
	
	dictionary = {}

	xls = pd.ExcelFile(path+"/metainfo.xls")

	sheetX = xls.parse(0) #2 is the sheet number
	sheetX = xls.parse(0).values
	fileIndex = -1
	for file in files:
		for i in range(len(sheetX)):
			if file[:9] == sheetX[i][0]:
				rowIndex = i
				break

		data = scipy.io.loadmat(path+'/smallgraphs/'+file)
		a = data['fibergraph'].toarray()
		for i in range(70):
		    for j in range(i, 70):
		        a[j][i] = a[i][j]

		dictionary[file[:9]] = [sheetX[i][2], sheetX[i][3], sheetX[i][5], sheetX[i][7], sheetX[i][8], sheetX[i][9], sheetX[i][10], sheetX[i][11], a]

	return dictionary


#example for how to get the data
dataDict = getData('brainnetworks/')

path = 'brainnetworks/'
files = [f for f in listdir(path+'/smallgraphs') if isfile(join(path+'/smallgraphs', f))]


