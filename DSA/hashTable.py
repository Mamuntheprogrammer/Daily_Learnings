class HashTable:
	def __init__(self):
		self.MAX = 100
		self.arr = [None for i in range(self.MAX)]

	def get_hashvalue(self,key):
		h=0
		for char in key:
			h += ord(char)
		return h%self.MAX

	# def add(self,key,val):
	# 	h = self.get_hashvalue(key)
	# 	self.arr[h]=val

	# def get(self,key):
	# 	h = self.get_hashvalue(key)
	# 	return self.arr[h]

	# above two method are implimented in builtin

	def __setitem__(self,key,val):
		h = self.get_hashvalue(key)
		self.arr[h]=val

	def __getitem__(self,key):
		h = self.get_hashvalue(key)
		return self.arr[h]

	def __delitem__(self,key):
		h = self.get_hashvalue(key)
		self.arr[h] = None


t = HashTable()

t["age"] = 30

# t.add("age",30)

print(t.arr)


print(t["age"])
# print(t.get("age"))