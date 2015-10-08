#coding: utf-8
# A dictionary of movie critics and their ratings of a small
# set of movies

from math import sqrt

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}



#person1 与 person2 之间的欧几里得距离的相似度评价

def sim_distance(prefs, person1, person2):
	#得到双方都曾评价过得的东西的列表
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	
	#如果两者没有共同之处则返回0；
	if len(si) == 0:  return 0
	
	#计算所有差值的平方和
	sum_of_squres = sum([pow(prefs[person1][item] - prefs[person2][item],2)
					for item in prefs[person1] if item in prefs[person2]])
	
	return 1 / (1 + sqrt(sum_of_squres))

#p1 与 p2 之间的皮尔逊相关系数

def sim_pearson(prefs,p1,p2):
	#得到双方都曾评价过得的东西的列表
	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item] = 1
		
	n = len(si)
	
	#如果两者没有共同之处则返回0；
	if n == 0: return 0
	
	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])
	
	sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
	
	pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
	
	num = pSum - (sum1 *sum2 / n)
	denSq = abs(sum1Sq - pow(sum1,2)/n) * abs(sum2Sq - pow(sum2,2)/n)
	den = sqrt(denSq)
	
	if den == 0: return 0
	
	r = num/den
	return r
	
def topMatches(prefs,person,n=5,similarity = sim_pearson):
	scores = [(similarity(prefs,person,other),other) for other in prefs if other!=person]
	#对列表进行排序，评价值最高者排在最前面
	scores.sort()
	scores.reverse()
	return scores[0:n]

def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		#不和自己进行比较
		if other == person: continue
		sim = similarity(prefs,person,other)
		
		#忽略评价值为零或者小于零的情况
		if sim <= 0: continue
		for item in prefs[other]:
			#只对自己还未看过的影片进行评价
			if item not in prefs[person] or prefs[person][item] == 0:
				#相似度 * 评价值
				totals.setdefault(item,0)
				totals[item] += prefs[other][item]*sim
				#相似度之和
				simSums.setdefault(item,0)
				simSums[item]+=sim
		
	#建立一个归一化的列表
	ranking = [(total/simSums[item],item) for item,total in totals.items()]
	
	#排序
	ranking.sort()
	ranking.reverse()
	return ranking

	
def transformPrefs(prefs):
	result = {}
	for person in prefs:
		print person
		for item in prefs[person]:
			result.setdefault(item,{})
			#将物品和人员进行对调
			result[item][person] = prefs[person][item]

	return result
	
def calculateSimilarItems(prefs,n = 10):
	result = {}
	
	#以物品为中心对偏好矩阵实施倒置处理
	itemPrefs = transformPrefs(prefs)
	c = 0
	
	for item in itemPrefs:
		c += 1
		if c%100 == 0: print "%d / %d" % (c ,len(itemPrefs))
		#寻找相近的物品
		scores = topMatches(itemPrefs,item,n = n,similarity = sim_distance)
		result[item] = scores
	return result

def getRecommendedItems(prefs,itemMatch,user):
	userRating = prefs[user]
	scores = {}
	totalSim = {}
	
	#循环遍历由当前用户评分的物品
	for (item, rating) in userRating.items():
		#循环遍历与当前物品相近的物品
		for (similarity, item2) in itemMatch[item]:
			
			#如果该用户已经对当前物品做过评价，则将其忽略
			if item2 in userRating: continue
			#评价值与相似度的加权之和
			scores.setdefault(item2,0)
			scores[item2] += similarity * rating
			
			#全部相似度之和
			totalSim.setdefault(item2,0)
			totalSim[item2] += similarity
	
	rankings = [ (score/totalSim[item],item) for item,score in scores.items()]
	
	rankings.sort()
	rankings.reverse()
	return rankings
	
def loadMovieLens(path='./data'):
	movies = {}
	for line in open(path+'/u.item'):
		(id, title) = line.split('|')[0:2]
		movies[id] = title
	
	#加载数据
	prefs = {}
	for line in open(path+'/u.data'):
		(user, movieid, rating, ts) = line.split('\t')
		prefs.setdefault(user,{})
		prefs[user][movies[movieid]] = float(rating)
	return prefs


######################################## homeworks  ###########################################

def sim_tanimoto(prefs, p1, p2):
	

