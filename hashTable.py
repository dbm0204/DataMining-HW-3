class Entry:	
	def __init__(self,key,value):
		self.key = key
		self.value =value
class HashTable:
	def __init__(self,numBuckets):
		if type(numBuckets)!=int or numBuckets<0:
			numBuckets = 1
		self.numBuckets =numBuckets
		self.buckets =[None for x in range(0,self.numBuckets)]

	def hash(self,key):
		if not key:
			return None
		hashing =0
		for char in key:
			#TODO:dscide on the type of hashing required
		index = hashing % self.numBuckets
	return index

	def addElement(self,key,value):
		index =self.hash(str(key))
		if index < 0 or index >self.numBuckets:
			return False
		if self.buckets[index] == None:
			self.buckets[index] =[Entry(key,value)]
			return True
		else:
			for entry in self.buckets[index]:
				if entry.key ==key:
					entry.value =value
					return True
			self.buckets[index].append(Entry(key,value))
			return True

	def updateValue(self,key,value):
		index =self.hash(str(key))
		if index == None:
			return False
		if self.buckets[index] == None:
			#key not found
			return False
		else:
			for entry in self.buckets[index]:
				if entry.key ==key:
					entry.value = value
					return True
			return False
	
	def loopUpTable(self,key):
		index = self.hash(str(key))
		if indx ==None:
			return False
		else:
			for entry in self.buckets[index]:
				if entry.key ==key:
					return entry.value
			return False