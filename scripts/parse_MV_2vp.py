#!/usr/bin/env python

class ParseStates:
	END=0
	PCLASS=1
	NOFITEMS=2
	INSTANCENO=3
	MAXBINSIZE=4
	BINS=5
	


class MV2vpParser:
	
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
		p = MV_2vp()
		for i in self.l:
			if self.state is ParseStates.END:
				p = MV_2vp()
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
class MV_2vp:
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


if __name__ == "__main__":
	FILEPATH='/Users/gillessilvano/iCloud/UFRN - Mestrado/Otimizacao em Sistemas/2dbinpack/data/MV_2bp/Class_10.2bp'

	p = MV2vpParser(FILEPATH)
	p.parse()

