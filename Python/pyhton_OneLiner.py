'''
1.list comprehension

[ <expression> for <element> in <iterable> ]

[ <expression> for <element> in <iterable> if <condition> ]

Else can be used in List comprehension constructs, but be careful regarding the syntax. The if/else clauses should
be used before for loop, not after:

# When using if/else together use them before the loop

[x if x in 'aeiou' else '*' for x in 'apple']

#['a', '*', '*', '*', 'e']


'''

# ******************************* Example 1 ***********************************
# Example 1 : Iterating through a string Using for Loop

letters = []
for letter in 'List comprehension':
	letters.append(letter)
print(letters)


# Example 1 : Iterating through a string Using List comprehension

letters_LC = [letter for letter in 'List comprehension'] 

print(letters_LC)


# ******************************************************************************


# ******************************* Example  2 ***********************************
# Example 2 : Double the odds from given list of numbers using for loop

numbers = [1, 2, 3, 4, 5]

doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)
print(doubled_odds)


# Example 2 : Double the odds from given list of numbers list comprehension


doubled_odds_LC = [n * 2 for n in numbers if n % 2 == 1]

print(doubled_odds_LC)



# ******************************************************************************


# ******************************* Example  3 ***********************************





# ******************************************************************************


# ******************************* Example  4 ***********************************
# Example 4 : Find Vowel and replace consonant with * from a given word using for loop
result = []

for letter in 'apple':
	if letter in 'aeiou':
		result.append(letter)
	else:
		result.append('*')

print(result)


# Example 4 : Find Vowel and replace consonant with * from a given word using list comprehension


result = [ x if x in 'aeiou' else '*' for x in 'apple']

print(result)


# ******************************************************************************


# ******************************* Example  5 ***********************************
# Example 5 : # Organize letters in words in an alphabetical order using for loop

result = []
sentence = "Beautiful is better than ugly"
for word in sentence.split():
	result.append("".join(sorted(word,key = lambda x: x.lower())))
print(result)


# Example 5 : # Organize letters in words in an alphabetical order using list comprehension

result = ["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]
print(result)

# ******************************************************************************








#--------------------------------- Double Iteration or Nested ------------------
#							Inner loop first than outer loop

# ******************************* Example  6 ***********************************
# Example 6 : 

result = []

for i in range(1,3):
	result.append([])
	for j in range(4,7):
		result[i-1].append(i*j)

print(result)



# Example 6 :

result = [ [i*j for j in range(4,7)] for i in range(1,3) ]

print(result)


# ******************************************************************************


# ----------------- Using Map And Lambda Function ------------------------------



# ******************************* Example  7 ***********************************
# Example 7 : 

txt = ['lambda functions are anonymous functions.','anonymous functions dont have a name.','functions are objects in Python.']

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

print(list(mark))
# Example 7 :

# ******************************************************************************


# ******************************* Example  8 ***********************************
# Example 8 : 

price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
[9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
[8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
[7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
## One-Liner
sample = [line[::2] for line in price]

print(sample)

# Example 8 :

# ******************************************************************************

visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
'Safari', 'corrupted', 'Safari', 'corrupted',
'Chrome', 'corrupted', 'Firefox', 'corrupted']
## One-Liner
visitors[1::2] = visitors[::2]

print(visitors[1::2])



# ******************************* Example  zip ***********************************
''' Example 2 : Your data consists of the column names and the employee data
organized as list of tuples (rows). Assign the column names to
the rows and, thus, create a list of dictionaries. Each dictionary
assigns the column names to the respective data values '''

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
# Zip two lists together
zipped = list(zip(lst_1, lst_2))
print(zipped)
# [(1, 4), (2, 5), (3, 6)]
# Unzip to lists again
lst_1_new, lst_2_new = zip(*zipped)
print(list(lst_1_new))
print(list(lst_2_new))





## Data
column_names = ['name', 'salary', 'job']

db_rows = [('Alice', 180000, 'data scientist'),
('Bob', 99000, 'mid-level manager'),
('Frank', 87000, 'CEO')]


## One-Liner
db = [dict(zip(column_names, row)) for row in db_rows]

print(db)

# Example 2 :

# ******************************************************************************





#------------------------------ Dictionary Comprehension ----------------------




# ******************************* Example  1 ***********************************
# Example 1 : TO FIND TOP EARNERS USING LOOP

employees = {'Alice' : 100000,'Bob' : 99817,'Carol' : 122908,'Frank' : 88123,'Eve' : 93121}

top_earners = []

for key, val in employees.items():
	if val >= 100000:
		top_earners.append((key,val))

print(top_earners)



# Example 1 : TO FIND TOP EARNERS USING LIST COMPREHENSION

top_earners_LC = [(k, v) for k, v in employees.items() if v >= 100000]

print(top_earners_LC)
# ******************************************************************************

# ******************************* Example  2 ***********************************
# Example 2 : companies paying below your state’s minimum wage (< $9)

companies = {
'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}




# Example 2 :

## One-Liner
illegal = [x for x in companies if any(y<9 for y in companies[x].values())]

## Result
print(illegal)


# ******************************************************************************

# ******************************* Example  3 ***********************************
# Example 3 : swap the keys and values 5 different way



my_dict = {1: 'a', 2: 'b', 3: 'c'}


swapped = {v: k for k, v in my_dict.items()}
print(swapped)
swapped = dict(zip(my_dict.values(), my_dict))
print(swapped)
swapped = dict(zip(my_dict.values(), my_dict.keys()))
print(swapped)
swapped = dict(map(reversed, my_dict.items()))
print(swapped)



# Example 3 :

# ******************************************************************************
# ******************************* Example  3 ***********************************
# Example 3 : Merge Dictionary

dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}


{k: v for d in [dict1, dict2] for k, v in d.items()}

{**dict1, **dict2}


# Example 3 :

# ******************************************************************************






# ******************************* Example  2 ***********************************
# Example 2 : 





# Example 2 :

# ******************************************************************************