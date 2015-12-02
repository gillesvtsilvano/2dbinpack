#!/usr/bin/env python

class ParseStates:
	END=0
	PCLASS=1
	NOFITEMS=2
	INSTANCENO=3
	MAXBINSIZE=4
	BINS=5
	


class Parser:
	
	States = ParseStates()

	def __init__(self, filepath):
		self.state=ParseStates.PCLASS
		self.l=[]
		self.MV2vpList = []
		self.filepath = filepath
		with open(filepath) as f:
			for line in f:
				self.l.append(line.split())
			f.close()

	def parse(self):
		p = MV2vp()
		for i in self.l:
			if self.state is ParseStates.END:
				p = MV2vp()
				self.state = ParseStates.PCLASS
			if self.state is ParseStates.PCLASS:
				p.pClass = int(i[0])
				self.state = ParseStates.NOFITEMS	
			elif self.state is ParseStates.NOFITEMS:
				p.nItems = int(i[0])
				self.state = ParseStates.INSTANCENO
			elif self.state is ParseStates.INSTANCENO:
				p.relativeInstanceNumber = int(i[0])
				p.absoluteInstanceNumber = int(i[1])
				self.state = ParseStates.MAXBINSIZE
			elif self.state is ParseStates.MAXBINSIZE: 
				p.maxH = int(i[0])
				p.maxW = int(i[1])
				self.state = ParseStates.BINS
			elif self.state is ParseStates.BINS: 
				if len(i) is not 0:
					p.addBin(int(i[0]), int(i[1]))
				else:
					self.MV2vpList.append(p)
					self.state = ParseStates.END
		print('We found %d instances' % len(self.MV2vpList))



class MV2vp:
	def __init__(self):
		self.bins = []
		self.pClass = 0
		self.nItems = 0
		self.relativeInstanceNumber = 0
		self.absoluteInstanceNumber = 0
		self.maxH = 0
		self.maxW = 0
	
	def addBin(self, w, h):
		b = Bin(w, h)
		if (len(self.bins) < self.nItems):
			self.bins.append(b)
	
	def __str__(self):
		s = '{Class: %d, nItems: %d}' % (self.pClass, self.nItems)
		for b in self.bins:
			s += '%s' % b
		return(s)

class Bin:
	def __init__(self, h, w):
		self.h = h
		self.w = w

	def __str__(self):
		return '{%d, %d}' % (self.h, self.w)


class Node:
	def __init__(self, x, y, w, h):
		self.used=False
		self.x=x
		self.y=y
		self.w=w
		self.h=h
	
	def __repr__(self):
		return "Node : {}x{}, {};{}, used: {}".format(
				self.w, self.h, self.x, self.y, self.used)


class Packer:
	def __init__(self, w, h):
		self.root = Node(0, 0, w, h)

	def fit(self, blocks):
		#print('Adding: {}'.format(blocks[0]))
		for n in blocks:
			#block = n
			node = self.findNode(self.root, n.w, n.h)
			
			if (node is not None):
				#print('Found space at: {}'.format(node))
				#print('{} stored on {}'.format(b, solutions.index(box)))
				node = self.splitNode(node, n.w, n.h)
				return True
			else:
				#print('No space left at: {}'.format(node))
				return False
		
	def findNode(self, root, w, h):
		if root.used:
			return self.findNode(root.right, w, h) or self.findNode(root.down, w, h)
		elif (w <= root.w) and (h <= root.h):
			return root
		else:
			return None
	
	def splitNode(self, node, w, h):
		node.used = True
		node.down = Node(node.x , node.y + h, node.w, node.h - h)
		node.right = Node(node.x + w, node.y, node.w - w, h)
		#print('Splited in: {} and {}'.format(node.down, node.right))
		return node

	def __repr__(self):
		return "{}\n{}\n{}".format(
				self.root, self.root.down, self.root.right)


if __name__ == "__main__":

	FILEPATH='/Users/gillessilvano/iCloud/UFRN - Mestrado/Otimizacao em Sistemas/2dbinpack/data/MV_2bp/Class_10.2bp'

	#FILEPATH='/Users/gillessilvano/iCloud/UFRN - Mestrado/Otimizacao em Sistemas/2dbinpack/class_test2.2bp'
	
	"""
		Read the file in filepath parsing all instances into a
		class structure for better manipulation of the bins
	"""

	parser = Parser(FILEPATH)
	parser.parse()

	
	
	
	"""
		Iterate on problem instances found in the file
	"""

	
	for instance in parser.MV2vpList:


		#print(instance)


		"""
			Initiate list solutions empty to store the amount of needed
			boxes to store all bins
		"""
		solutions = []

		"""
			Appending a box to our list of boxes. The values of
			the max boundaries are set here
		"""

		solutions.append(Packer(instance.maxW, instance.maxH))

		
		"""
			Iterate on bins found on problem instance
		"""

		for b in instance.bins:

			#print('Trying to find place for {}'.format(b))
			
			"""
				Iterate on boxes to find a box that the bin fits. if
				we can't find a box to store the bin, we create an empty
				one to put teh bin into
			"""
			for box in solutions:

				result = box.fit([Node(0, 0, b.w, b.h)])
				if result:
					#print('{} stored on {}'.format(b, solutions.index(box)))
					break
			if not result:
				bTmp = Packer(instance.maxW, instance.maxH)
				bTmp.fit([Node(0, 0, b.w, b.h)])
				solutions.append(bTmp)
				#print('{} Created.'.format(bTmp))
				#print('{} stored on {}'.format(b, solutions.index(bTmp)))
				
			#raw_input('')
		print(len(solutions))
