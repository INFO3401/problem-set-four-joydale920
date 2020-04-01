import pandas as pd
import matplotlib.pyplot as plt 
import scipy.stats
import statsmodels.api as sm 
from statsmodels.formula.api import ols


def loadAndCleanData(filename):
	data = pd.read_csv(filename)
	fixed_data = data.fillna(0)
	return fixed_data

def computerPDF(sD,data):
	data[sD].plot.kde()
	plt.show()

	# generate KDE plot for each feature in data
	# [sD] access specific column in the dataframe
	# call my graph 
	# data[sD].plot.kde()
	# show my graph
	# plt.show()


def viewDistribution(column,data):
	data[column].plot.hist()
	plt.show()

#def viewLogDistribution --> help

def computeBins(column, data):
	dfcut = pd.qcut(data[column],q=3, duplicates = "drop")
	catList = dfcut.cat.categories.tolist()
	return catList


def computeDefaultRisk(column,bin,sD,data):
	data = data[(data[sD] >= bin[0]) & (df[feature] <=bin[1])]
	rating_probs = data.groupby(column).size().div(len(data))
	print(rating_probs)

def computerConfidenceInterval(data):
	npArray = 1.0 *np.array(data)
	stdErr = scipy.stats.sem(npArray)
	n = len(data)
	#return (stdErr * scipy.stats.t.ppf((1+.95))/2.0, n-1)

def getEffectSize(d1, d2):
	m1 = d1.mean()
	m2 = d2.mean()
	s1 = d1.std()
	s2 = d2.std()

	return (m1 - m2) / math.sqrt((math.pow(s1, 3) + math.pow))


def runANOVA(dataframe, vars):
	model = ols(vars, data=dataframe).fit()
	aov_table = sm.stats.anova_lm(model, typ=2)
	return aov_table




# Office hours for 11-18 =(


	
