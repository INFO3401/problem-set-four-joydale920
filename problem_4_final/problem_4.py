#1. We all have our own biases and expectations 
#that may color the way that we interpret data. 
#Let's start by acknowledging those biases such that 
#we can actively consider them as we explore our data. 
#Who do you think will win the nomination? 
#Why do you think they will win? If you have not been 
#following the race, note that Ballotpedia 
#(https://ballotpedia.org/List_of_registered_2020_presidential_candidates 
#(Links to an external site.)) has a running 
#list of active candidates and details about those 
#candidates including their policy positions. 

# I think Joe Biden is going to win the election
# Why? He is winning most states right now 
# compared to Bernie Sanders.  Also, Bernie seems
# to get more young voters.  Young voters usually
# do not have as high of a turn out rate than older
# voters. 

from utils import *
from pollingData1 import *
import math
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt 

df = loadAndCleanData ("dems.csv")
#df = loadAndCleanData () 

print(df)

#5
normalizeData(df)

#7
for candidate in df.columns:
	if candidate not in ["Spread", "Date", "Poll", "Sample", "Undecided"]:
		plotCandidate(candidate,df)


#9
#print(statsPerCandidate("Sanders",df))

myCandidate = []
for candidate in df.columns:
	if candidate not in ["Spread", "Date", "Poll", "Sample"]:
		myCandidate.append(candidate)
		print(candidate.statsPerCandidate(candidate,df))
		# comma just means "put a space"


#10
df = cleanSample(df)
print(cleanSample)
#print(cleanSample(df))

#12
print(computePollWeight(df,"poll"))

#14
weightedStatsPerCandidate("Biden", df)
weightedStatsPerCandidate("Warren", df)
weightedStatsPerCandidate("Sanders", df)
weightedStatsPerCandidate("Biden", df)

#16
repeatList = []

for candidate1 in myCandidate:
	for candidate2 in myCandidate:
		if candidate1 != candidate2:
			if [candidate1, candidate2] not in repeatList and [candidate1, candidate2] not in repeatList:
				print(candidate1 + "vs " + candidate2 + ": " + computeCorrelaton(candidate1, candidate2, df))
				repeatList.append([candidate1, candidate2])

#print(computeCorrelaton(candidate1, candidate2, df)

#18
# Put for loop for problem 16 
#repeatList = []
#etc. etc.
#for candidate in myCans
superTuesday(df, myCandidate)
print("Biden Mean: " + df["BidenST"].mean())
print("Sanders Mean: " + df["SandersST"].mean())
print("Biden Weighted Mean: " + weightedStatsPerCandidate("BidenST", df))
print("Sanders Weighted Mean: " + weightedStatsPerCandidate("SandersST", df))
#weightedStatsPerCandidate(df,"candidate")

print("Biden and Klobuchar are the most correlated")
Print("Sanders and Steyer are the least correlated")

#print statement if doesnt work
#superTuesday(df, myCans)

#19 

getConfidenceInterval(df["BidenST"])
getConfidenceInterval(df["SandersST"])

#20

print("Numbers: " + runTTest(df["Biden"], df["Sanders"]))
print("Aggregated Numbers: " + runTTest(df["BidenST"], df["SandersST"]))











