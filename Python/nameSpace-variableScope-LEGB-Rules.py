"""
Namespace :

A namespace is a system that has a unique name for each and every object in Python. 
An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary.

Type of Namespace :

When Python interpreter runs solely without any user-defined modules, methods, classes, etc.
Some functions like print(), id() are always present, these are built-in namespaces.
When a user creates a module, a global namespace gets created, later the creation of local functions creates the local namespace.
The built-in namespace encompasses the global namespace and the global namespace encompasses the local namespace.

* Builtin Namespace
* Global Namespace
* Local Namespace 

The lifetime of a namespace :
 
A lifetime of a namespace depends upon the scope of objects, if the scope of an object ends, the lifetime of that namespace comes to an end.
Hence, it is not possible to access the inner namespace’s objects from an outer namespace.


** Check the namespace from the scope using DIR() builtin function 


LEGB Scope :
* Local
* Global
* Enclosed
* Builtin 

* global 
* nonlocal 

Note : * To chage the global variable value in local scope use global keyword with local scope variable
	   * To chage the enclosed variable value in local scope use nonlocal keyword with local scope variable



Resource :

Namespace : 
	https://www.geeksforgeeks.org/namespaces-and-scope-in-python/


"""


# LEGB EXAMPLE 




x = 0 # Global scope
print(x) # Built-in Scope
def outer():
	global x
	x = x + 3
	y = 5 # local scope
	print(x)
	def inner():
		nonlocal y
		y = y + 10 # enclosed scope
		print(y)
	inner()
outer()




