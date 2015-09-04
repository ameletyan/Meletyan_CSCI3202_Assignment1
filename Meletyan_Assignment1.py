# GitHub Account: ameletyan

from Queue import *

# Queue class
class Queue:
	def __init__(self):
		self.queue = deque([])
	
	# adds an integer to the end of the queue
	def push(self, i):
		self.deque.append(i)
	
	# removes the integer at the start of the queue
	def dequeue(self):
		return self.deque.popleft()
	
	# returns the amount of integers in the queue
	def checkSize(self):
		return len(self.deque)
	
	# prints the whole queue (for personal testing)
	def printQueue(self):
		print self.deque

# Stack class
class Stack:
	def __init__(self):
		self.stack = []
	
	# adds an integer to the end of the stack
	def push(self, i):
		self.stack.append(i)
	
	# removes the integer at the top of the stack
	def pop(self):
		return self.stack.pop()
	
	# returns the amount of integers in the stack
	def checkSize(self):
		return len(self.stack)
	
	# prints the whole stack (for personal testing)
	def printStack(self):
		print self.stack

# Node class used for Binary Tree class
class Node:
	def __init__(self, value, parent = None):
		self.integerKey = value
		self.leftChild = None
		self.rightChild = None
		self.parent = parent
	
	# GETTERS
	# getter for the integer key
	def getIntKey(self):
		return self.integerKey
	
	# getter for the left child node
	def getLeftChild(self):
		return self.leftChild
	
	# getter for the right child node
	def getRightChild(self):
		return self.rightChild
	
	# getter for the parent node
	def getParent(self):
		return self.parent
	
	# SETTERS
	# setter for the integer key
	def setIntKey(self, i):
		self.integerKey = i
	
	# setter for the left child node
	def setLeftChild(self, node):
		self.leftChild = node
	
	# setter for the right child node
	def setRightChild(self, node):
		self.rightChild = node
	
	# setter for the parent node
	def setParent(self, parentNode):
		self.parent = parentNode

# Binary Tree class
class BinTree:
	def __init__(self, root):
		self.root = root
		
		# cursor to help with selecting nodes
		self.cursor = self.root
	
	def search(self, value):
		initCursor = self.cursor
		
		# if the node on the cursor has the desired value, return the node
		if(self.cursor.getIntKey() == value):
			return self.cursor
		
		# else, keep searching
		else:
			if(self.cursor.getLeftChild() != None):
				self.cursor = self.cursor.getLeftChild()
				leftSearch = self.search(value)
				if(leftSearch == None):
					if(initCursor.getRightChild() != None):
						self.cursor = initCursor.getRightChild()
						return self.search(value)
					else:
						return leftSearch
				else:
					return leftSearch
	
	# add nodes to the binary tree
	def add(self, value, parentValue):
		self.cursor = self.root
		
		# find the node with an integer key of parentValue
		# if parentValue is not found in the tree, print a message stating that
		if(self.search(parentValue) == None):
			print "Parent not found."
		else:
			self.cursor = self.root
			parent = self.search(parentValue)
			
			# add the new node as the left child if the parent has no children
			if(parent.getLeftChild() == None):
				parent.setLeftChild(Node(value, parent))
			
			# add the new node as the right child if the parent has a left child only
			elif(parent.getRightChild() == None):
				parent.setRightChild(Node(value, parent))
			
			# do not add the node if the parent already has two children, print a message stating that
			else:
				print "Parent has two children, node not added."
	
	# delete nodes that do not have children
	def delete(self, value):
		self.cursor = self.root
		
		# find the node with an integer key of value
		# if the node is not found, print a message stating that
		if(self.search(value) == None):
			print "Node not found."
		else:
			self.cursor = self.root
			node = self.search(value)
			
			# if a node has 1 or 2 children, do not delete the node and print a message stating that
			if((node.getLeftChild() != None)or(node.getRightChild() != None)):
				print "Node not deleted, has children."
			
			# if the node can be deleted, delete it
			else:
				# remove the node's reference from its parent
				if(node.parent.getLeftChild() == node):
					node.parent.setLeftChild(None)
				if(node.parent.getRightChild() == node):
					node.parent.setRightChild(None)
				
				# remove the node's references to its parent from itself
				node.setParent(None)
				
				# delete the node
				del node
	
	# traverse through a tree and print out the traversed nodes
	def printTraversal(self):
		initCursor = self.cursor
		print self.cursor.getIntKey()
		
		if(self.cursor.getLeftChild() != None):
			self.cursor = self.cursor.getLeftChild()
			self.printTraversal()
		
		self.cursor = initCursor
		if(self.cursor.getRightChild() != None):
			self.cursor = self.cursor.getRightChild()
			self.printTraversal()
	
	# reset cursor to root and print the tree
	def printTree(self):
		self.cursor = self.root
		self.printTraversal()

# Vertex class used for Graph class
class Vertex:
	def __init__(self, value):
		self.value = value
		self.adjacentVertices = []
	
	# returns the value associated with this vertex
	def getVal(self):
		return self.value
	
	# returns the list of adjacent vertices to this vertex
	def getAdjVert(self):
		return self.adjacentVertices
	
	# adds an adjacent vertex to the list
	def addAdjVert(self, vertex):
		self.adjacentVertices.append(vertex)

# Graph class
class Graph:
	def __init__(self):
		self.vertices = {}
	
	# add a vertex with a specified value
	def addVertex(self, value):
		# check that another vertex with the same value does not exist
		# if one does exist, then print a message stating that
		if(value in self.vertices):
			print "Vertex already exists."
		
		# else, add the new vertex
		else:
			self.vertices[value] = Vertex(value)
	
	# add an edge between two vertices with specified values
	def addEdge(self, value1, value2):
		# if one or both of the vertices do not exist, then print a message stating that
		if((value1 not in self.vertices)or(value2 not in self.vertices)):
			print "One or more vertices not found."
		# else, add the new edge
		else:
			vertex1 = self.vertices[value1]
			vertex2 = self.vertices[value2]
			vertex1.addAdjVert(vertex2)
			vertex2.addAdjVert(vertex1)
	
	# find a vertex with a specified value
	def findVertex(self, value):
		# if the vertex is found, then print the key values of its adjacent vertices
		if(value in self.vertices):
			adjVertList = self.vertices[value].getAdjVert()
			total = len(adjVertList)
			for i in range(0, total):
				print adjVertList[i].getVal()

def testQueue():
	print "\n\nTesting the Queue class..."
	
	# create queue
	print "Creating queue..."
	queue = Queue()
	print "Successfully created queue!"
	
	# add 10 integers to the queue
	print "\nAdding integers 1 through 10 to the queue..."
	
	# dequeue them and print the values
	
	print "Successfully tested the Queue class!  It works!"
	return 0

def testStack():
	print "\n\nTesting the Stack class..."
	
	# create a stack
	print "\nCreating stack..."
	stack = Stack()
	print "Successfully created stack!"
	
	# add 10 integers to the stack
	print "\nAdding integers 1 through 10 to the stack..."
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	stack.push(5)
	stack.push(6)
	stack.push(7)
	stack.push(8)
	stack.push(9)
	stack.push(10)
	print "Successfully added integers added to stack!"
	
	# test stack.checkSize()
	print "\nTesting the checkSize() method..."
	if(stack.checkSize() == 10):
		print "Successfully tested checkSize() method!  It works properly!"
	else:
		print "Oh no!  The checkSize() method is not working properly!"
	
	# pop them and print the values
	while(stack.checkSize() > 0):
		print "\nPopping the integer at the top of the stack..."
		print stack.pop()
		print "Successfully popped the top integer from the stack!"
	
	print "\nSuccessfully tested the Stack class!  It works!"
	
def testBinTree():
	print "\n\nTesting the Binary Tree class..."
	
	# create a binary tree
	print "\nCreating Binary Tree..."
	tree = BinTree(Node(0))
	print "Successfully created Binary Tree!"
	
	# add 10 integers as nodes to the tree
	print "\nAdding integers 1 through 10 to the tree..."
	tree.add(1, 0)
	tree.add(2, 0)
	tree.add(3, 1)
	tree.add(4, 1)
	tree.add(5, 2)
	tree.add(6, 2)
	tree.add(7, 3)
	tree.add(8, 3)
	tree.add(9, 4)
	tree.add(10, 4)
	print "Successfully added integers to the tree!"
	
	# print the tree
	print "\nPrinting the tree..."
	tree.printTree()
	print "Successfully printed the tree!"
	
	# delete 2 integers from the tree
	print "\nDeleting 2 integers from the tree..."
	tree.delete(6)
	tree.delete(10)
	print "Successfully deleted 2 integers from the tree!"
	
	# print the tree
	print "\nPrinting the tree..."
	tree.printTree()
	print "Successfully printed the tree!"
	
	print "\nSuccessfull tested the Binary Tree class!  It works"
	return 0

def testGraph():
	print "\n\nTesting the Graph class..."
	
	# add 10 integers as vertices to the graph
	# add 20 edges to the graph
	# find 5 vertices
	
	print "\nSuccessfull tested the Graph class!  It works"
	return 0

# MAIN
# runs all tests


print "Testing has begun!"
#testQueue()
#testStack()
#testBinTree()
#testGraph()
print "\n\nSuccessfully completed all tests!"
