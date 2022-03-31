"""
Defination :

Python has an interesting feature called decorators since it allows programmers to modify the behaviour of function or class.
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.


Related Topic you should know:
* Closure 
* In python Everything is Object
* Function are first class object / First class Fuction


Resource :

https://www.geeksforgeeks.org/decorators-in-python/
https://youtu.be/FsAPt_9Bf3U

"""

# Function Decorator

def str_upper(func):
	def inner():
		str1=func()
		return str1.upper()
	return inner

@str_upper          # one way of calling decorator
def print_str():
	return "hello world"

print(print_str())


# Another way of calling decorator

# a = str_upper(print_str)
# print(a())

#------------------------------------------------------------

# Decorator Using parameter

def outer(expr):
	def upper_d(func):
		def inner():
			return func()+ expr
		return inner
	return upper_d

@outer("mamun")
def ordinary():
	return "good morning "

print(ordinary())

# -----------------------------------------------------------

#  class decorators


class Decorator:
	def __init__(self,func):
		self.func = func

	def __call__(self):
		str1=self.func()
		return str1.upper()


@Decorator
def greet():
	return "Good morning"


print(greet())

# ------------------------------------------------------------------------
'''

  Three builtIn Decorator :
  	*	@property
  	*	@classmethod
  	*	@staticmethod

Resource :

https://youtu.be/5-S_B6nAzO8?list=PLzgPDYo_3xukWUakgF-OJvDOChq6drPG2


@property decorator use for use method as attribute and can set the attribute

'''

class Student:
	def __init__(self,name,grade):
		self.name = name
		self.grade = grade

	@property
	def msg(self):
		return self.name + " Got "+ self.grade

	@msg.setter
	def msg(self,msg):
		sent = msg.split(" ")
		self.name = sent[0]
		self.grade = sent[-1]

stud1 = Student("Mamun","B")
stud1.msg = "Mamun A+"

print(stud1.msg)





