#!/usr/bin/env python


class Bin:
	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.isStored = 0

class Box:
	def __init__(self, binId, maxw, maxh):
		self.binId = binId
		self.maxw = maxw
		self.maxh = maxh
		self.occW = 0
		self.occH = 0
		self.subsets = []
		
	def addBin(self, b):
		if len(self.subsets) is 0:
			if b.w + self.occW <= self.maxw and b.h + self.occH <= self.maxh:
				self.occW += b.w
				self.occH += b.h
				
				return True
			else:
				return False


if __name__ == "__main__":
	idc = 0		# idCounter
	bc = 0		# Box counter
	L=[[]]
	mw = 100
	mh = 100
	
	L[bc] = Box(idc, mw, mh)
	idc += 1
	while(True):
		w = int(raw_input('Insert bin w: '))
		h = int(raw_input('Insert bin h: '))
			
				
