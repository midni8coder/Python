# zip function 

x= [1, 2, 3, 4]

y= [5, 26, 7, 8]

z=  ['a', 'b', 'c', 'd']


for a, b, c in zip(x, y, z):
	print(a, b, c)

print(zip(x, y, z)) # zip objects

for i in  zip(x, y, z):
	print(i) # (1, 5, 'a')  (2, 26, 'b')


print(list(zip(x, y, z))) # list of zip tuples [(1, 5, 'a'), (2, 26, 'b'), (3, 7, 'c'), (4, 8, 'd')]

print(dict(zip(x, y))) # list of zip tuples {1: 5, 2: 26, 3: 7, 4: 8}

[print(a, b, c) for a, b, c in zip(x, y, z)]

for x,y in zip(x, y): # x value will be overridden
	print(x, y)
print(x) # prints last saved value