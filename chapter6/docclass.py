#coding:utf-8
from pysqlite2 import dbapi2 as sqlite
import re
import math

def getwords(doc):
	splitter = re.compile('\\W*')
	#根据非字母字符进行单词划分
	words = [s.lower() for s in splitter.split(doc) if len(s)>2 and len(s)<20]
	#只返回一组不重复的单词
	return dict([(w,1) for w in words])

class classifier:
	def __init__(self, getfeatures, filename = None):
	#统计特征、分类组合的数量
	self.fc = {}
	#统计每个分类中的文档数量
	self.cc = {}
	self.getfeatures = getfeatures
	
	#增加对特征、分类组合的计数值
	def incf(self, f, cat):
		self.fc.setdefault(f, {})
		self.fc[f].setdefault(cat, 0)
		self.fc[f][cat] += 1
		
	#增加对某一分类的计数值
