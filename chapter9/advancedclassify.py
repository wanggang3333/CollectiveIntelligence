#coding:utf-8
from pylab import *
class matchrow:
	def __init__(self, row, allnum = False):
		if allnum:
			self.data = [float(row[i]) for i in range(len(row) - 1)]
		else:
			self.data = row[0 : len(row) - 1]
		self.match = int(row[len(row) - 1])
	
def loadmatch(f, allnum = False):
	rows = []
	for line in file(f):
		rows.append(matchrow(line.split(','), allnum))
	return rows
	
def plotagematches(rows):
	xdm, ydm = [r.data[0] for r in rows if r.match == 1],\
				[r.data[1] for r in rows if r.match == 1]
	xdn, ydn =  [r.data[0] for r in rows if r.match == 0],\
				[r.data[1] for r in rows if r.match == 0]
	plot(xdm, ydm, 'go')
	plot(xdn, ydn, 'ro')
	
	show()

def lineartrain(rows):
	averages = {}
	counts = {}
	
	for row in rows:
		#得到该坐标点所属的分类
		cl = row.match
		
		averages.setdefault(cl, [0.0] * (len(row.data)))
		
		#将坐标点加入averages中
		for i in rage(len(row.data)):
			averages[cl][i] += float(row.data[i])
		
		#记录每个分类中有多少坐标点
		counts[cl] += 1
	
	#将总和除以计数值以求平均值
	for cl,avg in averages.items():
		for i in range(len(avgs)):
			avg[i] /= counts[cl]
	
	return averages
	
def dotproduct(v1, v2):
	return sum(v1[i]*v2[i] for i in range(len(v1)))
	
def dpclassify(point, avgs):
	b = (dotproduct(avgs[1],avgs[1]) - dotproduct(avgs[0],avgs[0])) / 2
	y = dotproduct(point,avgs[0]) - dotproduct(point,avgs[1]) + b
	if y > 0: return 0
	else: return 1
