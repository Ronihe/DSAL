
# trie: used for dictionary, auto-completion, auto-query

"""
create a node class 
a node represents a single character in a string

root node is an empty node 



todo: make a function just type the top 3 letters and 

method: 

feed the trie,

get the word from the trie 


optional: connect to the local data base to get the trie 


"""
import copy
import json


print("just want to test if it is wotking!")

'''write the result into a file'''

class Node:
	''' the node has a value and a set of children'''

	def __init__(self, val: str ="abc", children: set #seem should just use list, since even the node contains the same the 
		= set(), 
		is_leaf: bool = False ) -> None:
		#  check if the value of the val is 
		self.value = val
		self.children = children
		self.is_leaf = is_leaf
		# todo: do I need a counter for the branch here

	def printval(self) -> None: # why the first param is self, python method the passed automatically, but not for receiving 
		print(f'this is the value: {self.value}')
		# print(f'this is the value: {self.valuef}')

# to test if the node with the same value and children considered 

def test(node: Node, set_node: set):
	set_node.add(node)
	# print(set_node)

node1 = Node("abc", set("abc"))
node2 = Node("abc", set("abc"))
copy_node1 = copy.deepcopy(node1)
print(f'the value of the copy value: {copy_node1.value}, what are the children {copy_node1.children}, is_leaf {copy_node1.is_leaf}')
node_set = set()
node_set.add(node1)
test(node2, node_set)
# change the node1 value here to see if the set would found it 
node1.value = "changed"
print(node1.value)
print("start")
for node in node_set:
	print(node.value)


print("success")
print(f'add the new node  with the same values to the set, the length should be 1, otherwise the length should be 2 {len(node_set)}') # if the set can check the value of a class should 

class Trie:
	''' 
	this is the trie class
	root node,
	method: add, find, print_trie

	'''
	def __init__(self, root : Node = Node(None)) :
		self.root = root

	def add():
		return None
		# check if the value 




node = Node(5, [3,4])
# node.printval



