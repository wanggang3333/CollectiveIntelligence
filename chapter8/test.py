import numpredict
import optimization
#print numpredict.wineprice(95.0, 3.0)
#data = numpredict.wineset1()
#print data[0],data[1]
#print numpredict.knnestimate(data,(99.0,50),k = 1)
#print numpredict.knnestimate(data,(99.0,50))
#print numpredict.weightedknn(data,(99.0,5.0))
#print numpredict.crossvalidate(numpredict.knnestimate,data)
#data = numpredict.wineset2()

#costf = numpredict.createcostfunction(numpredict.knnestimate, data)
#print optimization.annealingoptimize(numpredict.weightdomain, costf, step = 2)
data = numpredict.wineset3()
#print numpredict.probguess(data, [99,20],40,80)
numpredict.probabilitygraph(data, (99,30), 120)