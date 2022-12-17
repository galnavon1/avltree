# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

import random

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields.
	@type value: str
	@param value: data of your node
	"""

	def __init__(self, value=None, left=None, right=None, parent=None, height=-1, size=0):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.size = size
		self.bf = 0

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

	def getLeft(self):
		return self.left if self.height != -1 else None  # include virtual child

	"""returns the right child
	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

	def getRight(self):
		return self.right if self.height != -1 else None  # include virtual child

	"""returns the parent 
	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

	def getParent(self):
		return self.parent

	"""return the value
	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""

	def getValue(self):
		return self.value

	"""returns the height
	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

	def getHeight(self):
		return self.height

	def getSize(self):
		return self.size

	"""sets left child
	@type node: AVLNode
	@param node: a node
	"""

	def setLeft(self, node):
		self.left = node

	"""sets right child
	@type node: AVLNode
	@param node: a node
	"""

	def setRight(self, node):
		self.right = node

	"""sets parent
	@type node: AVLNode
	@param node: a node
	"""

	def setParent(self, node):
		self.parent = node

	"""sets value
	@type value: str
	@param value: data
	"""

	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node
	@type h: int
	@param h: the height
	"""

	def setHeight(self, h):
		self.height = h

	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

	def isRealNode(self):
		return self.height != -1


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
	"""
	Constructor, you are allowed to add more fields.
	"""

	def __init__(self):
		self.size = 0
		self.root = AVLNode()
		self.min = None
		self.max = None

	# add your fields here

	'''
	returns whether the node is a left child or right child
		@rtype: bool
		@returns: True if the node is left child, False otherwise
	'''

	def left_child(self, node):
		if node.parent == None:
			return None
		else:
			return node == node.parent.left

	"""returns whether the list is empty
	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

	def empty(self):
		return True if self.size == 0 else False

	'''
	perform right rotation and fix the attributes of the updated nodes
	@rtype: void
	'''

	def RR(self, node):
		temp = node
		T = node.left.right
		node = node.left
		node.setParent(temp.parent)
		if temp.parent is not None:
			temp.parent.setLeft(node) if self.left_child(temp) else temp.parent.setRight(node)
		else:
			self.root = node
		node.setRight(temp)
		node.right.setLeft(T)
		T.setParent(node.right)
		node.right.setParent(node)
		# update the attributes of the new right son
		node.right.size = node.right.left.size + node.right.right.size + 1
		node.right.height = max(node.right.left.height, node.right.right.height) + 1
		node.right.bf = node.right.left.height - node.right.right.height
		# update the attributes of the new subtree root
		node.size = node.left.size + node.right.size + 1
		node.height = max(node.left.height, node.right.height) + 1
		node.bf = node.left.height - node.right.height

	'''
		perform left rotation and fix the attributes of the updated nodes
		@rtype: void
	'''

	def LL(self, node):
		temp = node
		T = node.right.left
		node = node.right
		node.setParent(temp.parent)
		if temp.parent is not None:
			temp.parent.setLeft(node) if self.left_child(temp) else temp.parent.setRight(node)
		else:
			self.root = node
		node.setLeft(temp)
		node.left.setRight(T)
		T.setParent(node.left)
		node.left.setParent(node)
		# update the attributes of the new left son
		node.left.size = node.left.right.size + node.left.left.size + 1
		node.left.height = max(node.left.right.height, node.left.left.height) + 1
		node.left.bf = node.left.right.height - node.left.left.height
		# update the attributes of the new subtree root
		node.size = node.left.size + node.right.size + 1
		node.height = max(node.left.height, node.right.height) + 1
		node.bf = node.left.height - node.right.height

	'''
		perform right rotation and than left rotation (and fix the attributes of the updated nodes)
		@rtype: void
	'''

	def RL(self, node):
		self.RR(node.right)
		self.LL(node)

	'''
		perform left rotation and than right rotation (and fix the attributes of the updated nodes)
		@rtype: void
	'''

	def LR(self, node):
		self.LL(node.left)
		self.RR(node)

	'''
	fix the tree after insertion or deletion and count the rotations number
	@rtype: int
	@returns: number of rebalancing operations  
	'''

	def fix_the_tree(self, node):
		counter = 0  # counter for rebalancing
		if node is None:
			return counter
		while node is not None:
			node.height = max(node.left.height, node.right.height) + 1
			node.bf = node.left.height - node.right.height
			if abs(node.bf) < 2:
				node.size = node.left.size + node.right.size + 1
			else:  # rotation is needed
				counter += 1
				if node.bf == 2 and (node.left.bf == 1 or node.left.bf == 0):  # right rotation situation
					self.RR(node)
				elif node.bf == 2 and node.left.bf == -1:  # left-right rotation situation
					self.LR(node)
					counter += 1
				elif node.bf == -2 and (node.right.bf == -1 or node.right.bf == 0):  # left rotation situation
					self.LL(node)
				elif node.bf == -2 and node.right.bf == 1:  # right-left rotation situation
					self.RL(node)
					counter += 1
			node = node.parent
		return counter

	"""the select func returns the node in rank k+1, select_rec her recursive implementation"
	@type k: int
	@pre: 0 < k <= self.length()
	@param k: rank of a node
	@rtype: AVLnode
	"""

	def select_rec(self, x, k):
		r = x.left.size + 1
		if k == r:
			return x
		elif k < r:
			return self.select_rec(x.left, k)
		else:
			return self.select_rec(x.right, k - r)

	def select(self, k):
		return self.select_rec(self.root, k)

	"""retrieves the value of the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
	"""

	def retrieve(self, i):
		if i >= self.size or i < 0:
			return None
		n = self.select(i + 1)
		return n.value

	'''
	finds the predecessor if the node has real left child
	@rtype: AVLnode
	'''

	def predecessor_has_left(self, n):
		predecessor = n.left
		while AVLNode.isRealNode(predecessor.right):
			predecessor = predecessor.right
		return predecessor

	'''
	finds the predecessor if the node has no real left child
	@rtype: AVLnode
	'''

	def predecessor_no_left(self, n):
		if self.left_child(n) == None:
			return None
		if not self.left_child(n):
			return n.parent
		else:  # n is left child
			while self.left_child(n.parent) is True:
				n = n.parent
			if not self.left_child(n):
				return n.parent
			return None

	"""inserts val at position i in the list
	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def insert(self, i, val):
		n = AVLNode(val, AVLNode(), AVLNode(), None, 0, 1)
		n.left.setParent(n)
		n.right.setParent(n)
		if i == self.size:
			if self.size == 0:
				self.root = n
				self.max = n
				self.min = n
				self.size += 1
				return 0
			else:
				self.max.setRight(n)
				n.setParent(self.max)
				self.max = n
		else:  # i < self.size
			if i == 0:
				self.min = n
			cur = self.select(i + 1)
			if not AVLNode.isRealNode(cur.left):  # cur has no left child
				cur.setLeft(n)
				n.setParent(cur)
			else:  # cur has left child
				predecessor = self.predecessor_has_left(cur)
				predecessor.setRight(n)
				n.setParent(predecessor)
		# fixing the tree after insertion
		rebalance_num = self.fix_the_tree(n.parent)
		self.size += 1
		return rebalance_num

	'''
	deleting the node if it has one child at most and connecting his parent to his son
	@rtype = void 
	'''

	def one_child_del(self, child, par):
		bool = self.left_child(par)
		if bool == None:  # cur is the root
			self.root = child
		elif bool:  # cur is the left child
			par.parent.left = child
		else:  # cur is the right child
			par.parent.right = child

	def append(self, val):
		num = self.insert(self.length(), val)
		return num

	'''
	@pre: n.right != None
	finds the successor if the node has a right child
	'''

	def successor_right_child(self, n):
		n = n.right
		while AVLNode.isRealNode(n.left):
			n = n.left
		return n

	def successor_no_right(self, n):
		if self.left_child(n) is None:
			return None
		if self.left_child(n):
			return n.parent
		else:  # n is right child
			while self.left_child(n.parent) is False:  # go up and left as we can
				n = n.parent
			if self.left_child(n):
				return n.parent
			return None

	"""deletes the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def delete(self, i):
		if self.size == 0:
			return -1
		if i == self.size - 1:  # update the max attribute
			if AVLNode.isRealNode(self.max.left):
				self.max = self.predecessor_has_left(self.max)
			else:
				self.max = self.predecessor_no_left(self.max)
		if i == 0:  # update the min attribute
			if AVLNode.isRealNode(self.min.right):
				self.min = self.successor_right_child(self.min)
			else:
				self.min = self.successor_no_right(self.min)
		cur = self.select(i + 1)  # the required node to delete
		if cur.height == 0:  # cur is a leaf
			temp = cur.parent
			self.one_child_del(AVLNode(), cur)
			if temp is not None:
				temp.left.setParent(temp)
				temp.right.setParent(temp)
		else:  # cur is inner node
			if not AVLNode.isRealNode(cur.left):  # cur has only a right child
				temp = cur.right
				temp.setParent(cur.parent)
				self.one_child_del(temp, cur)
			elif not AVLNode.isRealNode(cur.right):
				temp = cur.left
				temp.setParent(cur.parent)
				self.one_child_del(temp, cur)
			else:  # cur has two real childs
				direct_son = False  # if successor is a direct son of cur
				if cur.right.left.height == -1:
					direct_son = True
				successor = self.successor_right_child(cur)
				temp = successor.parent  # temp is the starting node for going up and fixing the tree
				self.one_child_del(successor.right, successor)  # deleting the original successor from the tree
				# replacing cur (deleted node) with his successor
				temp.left.setParent(temp)
				successor.setParent(cur.parent)
				successor.setLeft(cur.left)
				successor.setRight(cur.right)
				cur.right.setParent(successor)
				cur.left.setParent(successor)
				if cur.parent is None:  # if the deleted node is the root
					self.root = successor
				else:
					cur.parent.setLeft(successor) if self.left_child(cur) else cur.parent.setRight(successor)
				if direct_son:  # if successor was direct son of cur before the changes, temp should
					# point to the changed successor
					temp = successor
		# fixing the tree after deletion
		rebalance_num = self.fix_the_tree(temp)
		self.size -= 1
		return rebalance_num

	"""returns the value of the first item in the list
	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""

	def first(self):
		if self.min is None:
			return None
		else:
			return self.min.value

	"""returns the value of the last item in the list
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

	def last(self):
		if self.max is None:
			return None
		else:
			return self.max.value

	''' recursive function for listToArray, in-order scan
	@rtype: void
	'''

	def recListToArray(self, node, lst):
		if not AVLNode.isRealNode(node):
			return
		self.recListToArray(node.left, lst)
		lst.append(node.value)
		self.recListToArray(node.right, lst)

	"""returns an array representing list 
	@rtype: list
	@returns: a list of strings representing the data structure
	"""

	def listToArray(self):
		lst = []
		self.recListToArray(self.root, lst)
		return lst

	"""returns the size of the list 
	@rtype: int
	@returns: the size of the list
	"""

	def length(self):
		return self.size

	"""sort the info values of the list
	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""

	def sort(self):
		lst = self.listToArray()
		if self.size > 1:
			lst.sort()
		tree = AVLTreeList()
		for i in range(len(lst)):
			tree.insert(i, lst[i])
		return tree

	"""permute the info values of the list 
	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""

	def permutation(self):
		lst = self.listToArray()
		random.shuffle(lst)
		tree = AVLTreeList()
		for i in range(len(lst)):
			tree.insert(i, lst[i])
		return tree

	"""concatenates lst to self
	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

	def concat(self, lst):
		if lst.size == 0:
			return self.root.height + 1
		if self.size == 0:
			self.root = lst.root
			self.size = lst.size
			self.min = lst.min
			self.max = lst.max
			return self.root.height + 1
		h1 = self.root.height
		h2 = lst.root.height
		if h1 <= h2:
			x = lst.min
			lst.delete(0)  # delete the minimum from the higher tree
			node = lst.root
			# find the lst node that has the same height has self
			while node.height > h1 and node.left.isRealNode():
				node = node.left
			x.setRight(node)
			x.setLeft(self.root)
			self.root.setParent(x)
			x.setParent(node.parent)
			if node.parent is not None:
				node.parent.setLeft(x)
			node.setParent(x)
			if lst.root.parent is None:
				self.root = lst.root
			else:
				self.root = x
		else:
			x = self.max
			self.delete(self.size - 1)
			node = self.root
			while node.height > h2 and node.right.isRealNode():
				node = node.right
			x.setRight(lst.root)
			x.setLeft(node)
			lst.root.setParent(x)
			x.setParent(node.parent)
			if node.parent is not None:
				node.parent.setRight(x)
			node.setParent(x)
			if self.root.parent is not None:
				self.root = x
		self.fix_the_tree(x)
		self.size = self.root.size
		self.max = lst.max
		return max(h2, h1) - min(h2, h1)

	'''
	returns the rank of a given node
	@rtype: int
	'''

	def myrank(self, node):
		counter = node.left.size + 1
		while node.parent is not None:
			if not self.left_child(node):
				counter += node.parent.left.size + 1
		return counter

	"""searches for a *value* in the list
	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""

	def search(self, val):
		lst = self.listToArray()
		for i in range(len(lst)):
			if lst[i] == val:
				return i
		return -1

	"""returns the root of the tree representing the list
	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""

	def getRoot(self):
		return None if self.size == 0 else self.root

	def getTreeHeight(self):
		return self.root.height

	def printt(self):
		out = ""
		for row in self.printree(self.root):  # need printree.py file
			out = out + row + "\n"
		print(out)

	def printree(self, t, bykey=True):
		# for row in trepr(t, bykey):
		#        print(row)
		return self.trepr(t, False)

	def trepr(self, t, bykey=False):
		if t == None:
			return ["#"]
		thistr = str(t.key) if bykey else str(t.getValue())
		return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

	def conc(self, left, root, right):
		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)
		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]
		ls = self.leftspace(left[0])
		rs = self.rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
					  " " + "\\" + rs * "_" + (rwid - rs) * " ")
		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "
			row += (rootwid + 2) * " "
			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "
			result.append(row)
		return result

	def leftspace(self, row):
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1

	def rightspace(self, row):
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1

		return i

'''
	def leftspace(self, row):
		"""helper for conc"""
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1

	def rightspace(self, row):
		"""helper for conc"""
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1
		return i

	def conc(self, left, root, right):
		"""Return a concatenation of textual represantations of
		a root node, its left node, and its right node
		root is a string, and left and right are lists of strings"""

		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)

		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

		ls = self.leftspace(left[0])
		rs = self.rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "

			row += (rootwid + 2) * " "

			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "

			result.append(row)

		return result

	def printree(self, t):
		"""Print a textual representation of t"""
		for row in self.trepr(t):
			print(row)
		return self.trepr(t)

	def trepr(self, t):
		"""Return a list of textual representations of the levels in t"""
		if t is None:
			return ["#"]

		thistr = str(t.value)

		return self.conc(self.trepr(t.left), thistr, self.trepr(t.right))
'''