from collections import deque

class Queue:
	def __init__(self):
		self.buffer = deque()


	def endeque(self, val):
		self.buffer.appendleft(val)

	def dequeue(self,val):
		return self.buffer.pop()

	def is_empty(self):
		return len(self.buffer==0)

	def size(self):
		return len(self.buffer)



queue1 = Queue()

queue1.endeque(2)
queue1.endeque(3)
queue1.endeque(4)
