
import matplotlib.pyplot as plt 

#5
def normalizeData(df):
	x = df.copy()
	sumList = []

	for i, row in x.iterrows():
		row.drop(labels = ["Poll", "Date", "Sample", "Spread"], inplace = True)
		print(row) 
		sumList.append(100-sum(row))

	x["Undecided"] = sumList

	print(x)
#7 for caniddate in df.columns:
# if candidate not in ["poll" etc]
def plotCandidate(candidate,df):
	plt.scatter(y = df[candidate], x=df["Poll"]) #variables no quotes
	plt.title(candidate + "Polling")
	plt.ylim(0) # so the bottom is 0
	plt.show()

#9
def statsPerCandidate(candidate,df):
		return df[candidate].mean()

#10
def cleanSample(df):
	sampleType = []
	sampleSize = []
	for i, row in df.iterrows():
		if "RV" in row["Sample"]:
			sampleType.append("RV")
			sampleSize.append(row["Sample"].replace(" RV", ""))
		elif "LV" in row["Sample"]:
			sampleType.append("LV")
			sampleSize.append(row["Sample"].replace(" LV", ""))
	for size in range(len(sampleSize)):
		if "RV" not in sampleSize[size] and "LV" not in sampleSize[size]: int(sampleSize[size])
		else:sampleSize[size] = 0
	df["Sample Type"] = sampleType
	df["Sample Size"] = sampleSize

	return df

#12
def computePollWeight(df,poll):
	x = (df["poll"]== poll)
	xsum = sum(x["sampleSize"])
	y = sum(df["sampleSize"])

	return xsum/y


#13
def weightedStatsPerCandidate(candidate,df):
	weightedAverages = []
	for poll in df["poll"].unique():
		x = sum(df[df["poll"] == poll][candidate])
		y = computePollWeight(df, poll)
		weightedAverages.append(x*y)
	return sum(weightedAverages)/len(weightedAverages)

#15.
def computeCorrelaton(candidate1, candidate2, df):
	return df[candidate1].corr(df[candidate2])

#16.

#17.
def superTuesday(df, candidates):
	BidenST = []
	SandersST = []
	
	for i, row in dataset.iterrows():

		BidenCount = row["Biden"]
		SandersCount = row["Sanders"]
		for candidate in candidates:

			if candidate != "Biden" and candidate != "Sanders":
				BidenCorr = computeCorrelaton("Biden", candidate, df)
				SandersCorr = computeCorrelaton("Sanders", candidate, df)

				if abs(BidenCorr) > abs(SandersCorr):
					BidenCount += row[candidate]
				else:
					sanderCount += row[candidate]
		
		BidenST.append(BidenCount)
		SandersST.append(SandersCount)

	dataset["BidenST"] = BidenST
	dataset["SandersST"] = SandersST

#18.

#19
def getConfidenceInterval(datacolumn):
	npArray = 1.0 * np.array(data)
	stdErr = scipy.stats.sem(npArray)
	n = len(datacolumn)
	return stdErr* scipy.stats.t.ppf((1+.95)/2.0, n-1)

#20
def runTTest(d1, d2):
	return scipy.stats.ttest_ind(d1, d2)












