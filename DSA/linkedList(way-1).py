# Make Nodes

# data = anything like string number etc
# nextNode = ther pointer of next node 


#Creating Node class
class Node():
	def __init__(self,data,nextNode=None):
		self.data = data
		self.nextNode = nextNode


#Creating node object and assing data to each node
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)


print(node1.data,node1.nextNode)


#assign next node reference to Each node
node1.nextNode = node2
node2.nextNode = node3


print(node1.data,id(node1.nextNode))



#Traversing the node

currentNode = node1
while True:
	print(currentNode.data)
	if currentNode.nextNode is None:
		break
	currentNode = currentNode.nextNode