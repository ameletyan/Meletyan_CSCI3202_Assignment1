# GitHub Account: ameletyan

from Queue import *

# stack class
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

# binary tree class
class BinTree:
	x = 0

# graph class
class Graph:
	x = 0

def testQueue():
	# add 10 integers to the queue
	# dequeue them and print the values
	return 0

def testStack():
	print "\n\nTesting stack..."
	
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
	
	# pop them and print the values
	while(stack.checkSize() > 0):
		print "\nPopping the integer at the top of the stack..."
		print stack.pop()
		print "Successfully popped the top integer from the stack!"
	
	print "\nSuccessfully tested stack!  It works!"
	
def testBinTree():
	# add 10 integers as nodes to te tree
	# print the tree
	# delete 2 integers from the tree
	# print the tree
	return 0

def testGraph():
	# add 10 integers as vertices to the graph
	# add 20 edges to the graph
	# find 5 vertices
	return 0

# MAIN
# runs all tests

testStack()
