"""
Prerequisite :
* Nested Function
* Functions are first class citizen or objects


Closure :
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 

"""

# Python program to illustrate
# closures
def outerFunction(text):
	text = text

	def innerFunction():
		print(text)

	# Note we are returning function
	# WITHOUT parenthesis
	return innerFunction

if __name__ == '__main__':
	myFunction = outerFunction('Hey!')
	myFunction()



"""
As observed from the above code, closures help to invoke functions outside their scope.
The function innerFunction has its scope only inside the outerFunction. 
But with the use of closures, we can easily extend its scope to invoke a function outside its scope.




When and why to use Closures:

1. As closures are used as callback functions, they provide some sort of data hiding.
 This helps us to reduce the use of global variables.

2.  When we have few functions in our code, closures prove to be an efficient way.
 But if we need to have many functions, then go for class (OOP).
"""