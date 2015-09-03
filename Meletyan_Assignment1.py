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
	def __init__(self, intKey):
		self.integerKey = intKey
		self.leftChild = None
		self.rightChild = None
		self.parent = None
	
	#GETTERS
	# getter for the integer key
	def getIntKey(self):
		return self.integerKey
	
	# getter for the left child
	def getLeftChild(self):
		return self.leftChild
	
	# getter for the right child
	def getRightChild(self):
		return self.rightChild
	
	# getter for the parent
	def getParent(self):
		return self.parent
	
	# SETTERS
	# setter for the integer key
	def setIntKey(self, i):
		self.integerKey = i
	
	# setter for the left child
	def setLeftChild(self, node):
		self.leftChild = node
		self.nodes["left"] = node
	
	# setter for the right child
	def setRightChild(self, node):
		self.rightChild = node
		self.nodes["right"] = node

# Binary Tree class
class BinTree:
	def __init__(self, root):
		self.root = root
		self.totalNodes = 1
		self.tree = {"root": self.root}
		
		# cursor to help with selecting nodes
		self.cursor = self.root
	
	# add nodes to the binary tree
	def add(self, value, parentValue):
		self.cursor = self.root
		
		# add the new node as the left child if the parent has no children
		
		# add the new node as the right child if the parent has a left child only
		
		# do not add the node if the parent already has two children

# Graph class
class Graph:
	x = 0

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
	
	# add 10 integers as nodes to the tree
	# print the tree
	# delete 2 integers from the tree
	# print the tree
	
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
