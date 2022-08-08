class Node:
	def __init__(self,data,nextNode=None):
		self.data = data
		self.nextNode = nextNode


class LinkedList:
	def __init__(self,head=None):
		self.head = head

	def insert(self,data):
		node = Node(data)
		if self.head is None:
			self.head = node
			return
		currentNode = self.head
		while True:
			if currentNode.nextNode is None:
				currentNode.nextNode = node
				break
			currentNode = currentNode.nextNode

	def insert_values(self,data_list):
		for value in data_list:
			self.insert(value)

	def get_length(self):
		count = 0
		currentNode = self.head
		while currentNode:
			count += 1 
			currentNode =currentNode.nextNode
		return count

	def remove_at(self,index):
		if index<0 or index >= self.get_length():
			raise Exception("invalid index")

		if index == 0:
			self.head = self.head.nextNode
			return

		count = 0
		currentNode = self.head
		while currentNode:
			if count == index-1:
				currentNode.nextNode = currentNode.nextNode.nextNode
				break
			currentNode = currentNode.nextNode
			count += 1


	def insert_at(self,index,data):
		if index<0 or index >= self.get_length():
			raise Exception("invalid index")

		if index == 0:
			self.insert(data)
			return

		count = 0
		currentNode = self.head
		while currentNode:
			if count == index-1:
				node = Node(data,currentNode.nextNode)
				currentNode.nextNode = node 
				break

			currentNode = currentNode.nextNode
			count += 1





	def printLinkedList(self):
		currentNode = self.head
		while currentNode is not None:
			print(currentNode.data)
			currentNode = currentNode.nextNode
		return None

l = LinkedList()

l.insert_values(['mango','banana','orange'])

print(l.get_length())

l.insert_at(1,'tal')




l.printLinkedList()





