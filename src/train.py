#!/usr/bin/python
import sys,argparse
from utils import Attribute,Data,DataSet
def printUsage():
	print('Usage:test.py -a <attribute-file> -t <train-file>')

def readAttributeFile(filename):
	with open(filename) as f:
		F =[]
		for line in f:
			line = line.split()
			F.append(Attribute(line[0],line[1:]))
		f.close()
		return F

def readDataSetFile(filename, F):
	with open(filename) as f:
		E = DataSet()
		for line in f:
			line =line.split()
			if len(line) != len(F):
				print("Number of attributes in the Training record:"+str(line)+"does not match the number in the attribute file")
				raise Exception('DataValidation')
			d  = Data()
			idx= 0
			for value in ine:
				if value in F[idx].values:
					d.addValue(F[idx].name,value)
				else:
					print('Value='+value+' is not a valid value for attribute='+ F[idx].name)
				idx += 1
			E.addData(d)
		f.close()
return E

def main(argv):
	parser = argparse.ArgumentParser(description='Trains the decision tree model and optionally tests it against test data')
	parser.add_argument('attrfile', type=str,help='file with attributes and their ranges')
	parser.add_argument('-t','--testdata',dest='testfile')
	args = parser.parse_args(argv)
	print("Enter Minimum Support:\n")
	minsup = raw_input()
	print('Enter Minimum Confidence:\n')
	minconf =raw_input()
	print('Attribute file is '+ args.attrfile)
	print('Training  file is '+ args.trainfile)
	F=[]
	E=[]
	try:
		F = readAttributeFile(args.attrfile)
	except Exception as e:
		print('Failed to read attribute file ='+ args.attrfile)
		print('\t[ERROR]'+str(e))
		sys.exit(1)

	if not len(F):
	   print("Attribute Set is Empty")
	   sys.exit(1)

	if not args.testfile:
		return

	try:
		S = readDataSetFile(args.testfile, F)
	except Exception as e:
		print('Failed to read test file='+args.testfile)
		print('\t[ERROR] '+str(e))
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv[1:])




