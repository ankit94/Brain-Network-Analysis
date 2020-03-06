import sys
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression




classifiers = {
	"MLP": MLPClassifier(alpha=0.0001, max_iter=1000),
	"RFC": RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0)
}



#wrapper class for classifier models
class ClassifierModel:

	m = None

	def __init__(self, modelType):
		if modelType not in classifiers:
			print("Error: Could not find given model: {}".format(modelType))
			sys.exit()
		self.m = classifiers[modelType]

	#might have to tweak for some classifiers that don't have fit method
	def fit(data, targets):
		self.m.fit(data, targets)

	def score(data, targets):
		score = self.m.score(data, targets)
		return score

	def k_fold_fit_and_score(data, targets):
		#do algorithm for paritioning data to test lots
		return None




regression = {
	'LR': LinearRegression()
}


class RegressionModel:

	m = None

	def __init__(self, modelType):
		if modelType not in classifiers:
			print("Error: Could not find given model: {}".format(modelType))
			sys.exit()
		self.m = regression[modelType]

	#might have to tweak for some classifiers that don't have fit method
	def fit(data, targets):
		self.m.fit(data, targets)

	#make score work for all 5 personality traits
	def score(data, targets):
		score = 0
		return score

	def k_fold_fit_and_score(data, targets):
		#do algorithm for paritioning data to test lots
		return None