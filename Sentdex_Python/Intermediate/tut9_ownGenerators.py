# writing our own generators]
import timeit

def generate_names():
	yield 'Devid'
	yield 'Raj'
	yield 'Third eye clicks'


for i in generate_names():
	print(i)






for i in range(10):
	for j in range(10):
		if i == 5:
			break
		print(i,j)

TEST_NUMBER = (2, 5, 3)
def generate_number_tuple():
	for i in range(10):
		for j in range(10):
			for k in range(10):
				yield (i, j, k)
for i, j, k in generate_number_tuple():
	if (i, j, k)  == TEST_NUMBER:
		print(i, j, k)

# indentation will also be considered in the code 
print(timeit.timeit('''TEST_NUMBER = (2, 5, 3) 
def generate_number_tuple():
	for i in range(10):
		for j in range(10):
			for k in range(10):
				yield (i, j, k)
for i, j, k in generate_number_tuple():
	if (i, j, k)  == TEST_NUMBER:
		print(i, j, k)
''', number = 10))
