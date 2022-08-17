
class TreeNode:
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None


	def add_child(self,child):
	 	child.parent = self
	 	self.children.append(child)

	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level += 1
			p = p.parent
		return level 


	def print_tree(self):
		space = " " * self.get_level()*3
		prefix = space + "|--" if self.parent else ""
		print(prefix + self.data)
		if self.children:
			for child in self.children:
				child.print_tree()




def build_tree():
	root = TreeNode("Electronics")
	laptop = TreeNode("laptop")

	laptop.add_child(TreeNode("mac"))
	laptop.add_child(TreeNode("surface"))
	laptop.add_child(TreeNode("thinkpad"))

	root.add_child(laptop)



	print(root.print_tree())

if __name__ == '__main__':
    build_tree()
    pass