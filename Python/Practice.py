def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")












# # Decorator 

# def my_decorator(func):
#     def wrapper():
#         print("something will happen")
#         func()
#         print("decorator part done")
#     return wrapper

# @my_decorator
# def name():
#     print("I called from decorator")
# name()

















# def make_greetings(names):
#     funcs = []
#     for name in names:
#         funcs.append(lambda name=name: print('Hello', name))
#     return funcs
# # Try it
# a, b, c = make_greetings(['Guido', 'Ada', 'Margaret'])
# a() # Prints 'Hello Guido'
# b() # Prints 'Hello Ada'
# c() # Prints 'Hello Margaret'

# return funcs: After all names have been processed, the list funcs, containing the lambda functions, is returned from the make_greetings function.













# # High order functions can be
# # passed as arguments to other functions, placed in data structures, and returned by a
# # function as a result.
# import time
# def after(seconds, func):
#     time.sleep(seconds)
#     func()
# # Example usage
# def greeting():
#     print('Hello World')
# after(10, greeting)














# # One of the main uses of lambda is to define small callback functions. For example, you
# # may see it used with built-in operations such as sorted(). For example:

# words=['xyx','yyxj','x']

# # Sort a list of words by the number of unique letters
# result = sorted(words, key=lambda word: len(set(word)))
# print(result)













# # To return multiple value return a tuple 
# def retrunMv(*arg):
#     a,b,*c=arg
#     return (a,b,c)

# print(retrunMv(1,23,4,5))












# The args is in dictinary form
# def one(**args):
#     print(args)

# one(mamun=25,hasan=30)











# raise SystemExit() # Exit with no error message
# raise SystemExit("Something is wrong") # Exit with error


# import atexit






# Exceptions

# try:
#     div = 10/2
# except Exception as e:
#     print(f"From except block , The error is {e}")
# finally:
#     print("Done")



















#Done

# pairs = [('IBM', 125), ('ACME', 50), ('PHP', 40)]

# #Convert list to dictionary
# d = dict(pairs)

# #extract keys from dictionary
# syms = list(d) 
# #or
# syms = d.keys()

# print(d,syms)
















#Done
# from collections import Counter

# # Example portfolio data
# portfolio = [
#     ("AAPL", 100, 150.25),
#     ("GOOGL", 50, 2800.75),
#     ("AAPL", 75, 155.50),
#     ("MSFT", 200, 290.60),
#     ("GOOGL", 100, 2850.25)
# ]

# # Initialize Counter to track total shares
# total_shares = Counter()


# The reason your code is not working is because you are trying to directly access total_shares[name] before initializing it. In your code, you initialize total_shares as a regular dictionary using total_shares = dict(). Unlike the Counter object, a regular dictionary doesn't have default values for keys that do not exist, so attempting to access total_shares[name] when name doesn't yet exist in the dictionary will raise a KeyError.

# To fix this, you can initialize total_shares as a Counter object instead of a regular dictionary. The Counter object automatically initializes keys to zero when they are accessed for the first time. Here's the corrected version of your code using Counter:

# # Iterate over portfolio data and update total shares
# for name, shares, _ in portfolio:
#     # print(total_shares[name])
#     # total_shares[name] += shares
    
#     total_shares[name] = total_shares[name] + shares
#     print(total_shares)

    

# # Print the total shares for each stock
# for stock, shares in total_shares.items():
#     print(f"Total shares of {stock}: {shares}")













# Done
# a = {1,2,3}
# b = {3,4,5,6}

# a = t | s # Union 
# b = t & s # Intersection 
# c = t - s # Difference 
# d = s - t # Difference 
# e = t ^ s # Symmetric difference 

# print(a^b)














#Done
# with open('data.txt') as file:
#     while (chunk := file.read(10000)):
#     print(chunk, end='')

# The := operator used in this example assigns to a variable and returns its value so that it
# can be tested by the while loop to break out. When the end of a file is reached, read()
# returns an empty string. An alternate way to write the above function is using break:




















#Done
# def buildProfile(first,last, **otherInfo):
#     profile = {'first':first,'last':last}

#     for key, val in otherInfo.items():
#         profile[key]=val
#     return profile

# print(buildProfile('Saad', 'Abdullah', company='Aristopharma'))
















# Done
# def printer(printed,unprinted):
#     while unprinted:
#         printed.append(unprinted.pop())

# unprinted = ["doc","doc2","doc3"]
# printed = []

# printer(printed,unprinted) # this will modifying original list
# printer(printed,unprinted[:]) # This wont modify the original list
# print(printed,unprinted)











# Done
# def printInfo(name,age=None):
#     print(f"My name is {name}" + (f" And my age is {age}" if age is not None else ""))


# printInfo("Habib")
# printInfo("Ismail",25)