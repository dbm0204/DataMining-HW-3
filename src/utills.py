#!/usr/bin/python
import math,sys

class Attribute:
	def __init__(self,name,values):
		self.name = name
		self.values = values

class Data:
	def __init__(self):
		self.values = {}
	
	def addValues(self, key, value):
		self.values[key] = value
	
	def getValues(self, key):
		return self.values[key]

class DataSet:
	def __init__(self):
		self.records = []

	def sortList(self):
		self.records.sort()

	def addData(self, data):
		self.records.append( data)

	def getSize(self):
		return len(self.records)

	def getClassLabel(self,attribute):
		if not len(self.records):
			return 'TODO_DEFAULT_LABEL'
	label = self.recods[0].getValue( attribute )
	for data in self.records:
		if data.getValue(attribute)	!= label:
			raise Exception ('Data not Homogenous')
	return label			