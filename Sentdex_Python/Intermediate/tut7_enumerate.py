# Enumerate 


list = ['length', 'right ', 'up', 'down']

for i in range(len(list)):
	print(i, list[i])

for i, j in enumerate(list):
	print(i,j)


new_dict = dict(enumerate(list))
print(new_dict)