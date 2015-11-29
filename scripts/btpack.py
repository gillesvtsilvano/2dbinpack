#!/usr/bin/env python


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

	def add(self, block):
		node = self.findNode(self.root, block.w, block.h)
		if (node):
			block.fit = self.splitNode(node, block.w, block.h)

	def fit(self, blocks):
		print('Adding: {}'.format(blocks[0]))
		for n in blocks:
			block = n
			node = self.findNode(self.root, block.w, block.h)
			print('Found space at: {}'.format(node))
			if (node):
				block.fit = self.splitNode(node, block.w, block.h)
				return True
			else:
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
		print('Splited in: {} and {}'.format(node.down, node.right))
		return node

	def __repr__(self):
		return "{}\n{}\n{}".format(
				self.root, self.root.down, self.root.right)

if __name__ == "__main__":
	L = []
	L.append(Packer(100, 100))
	while(True):
		w = int(raw_input('Insert bin w: '))
		h = int(raw_input('Insert bin h: '))
		if (w is 0 and h is 0):
			print(len(L))
		else:
			for p in L:
				if (not p.fit([Node(0, 0, w, h)])):
					p = Packer(100, 100)
					p.fit([Node(0, 0, w, h)])
					L.append(p)
					break
				
