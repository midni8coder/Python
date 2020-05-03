
s =  "   "+"  ".join([str(i)  for i in range(4)])
print([str(i)  for i in range(4)])
game = [[0 for i in range(4)] for i in range(4)]

print(game)
'''print('hello')

languages = "PYthon","Java","C#" # Tuple same as ("PYthon","Java","C#")

print(type(languages)) # type function returns type of object

for language in languages:
	print(language)



string = 'don\'t'
print(string)
'''

'''
import itertools
x = [1,2,3,4]

#for i in x:
#	print(i)

n = itertools.cycle(x)
#next(n)
for i in range(6):
	print(next(n))
print('#######')
c = iter(x) # convert list to iterable 
print(next(c))
print('***')
for i in c:
	print(i)

#print(game)
'''

'''
count = 0
for row in game:
	print(count,row)
	count +=1
	'''
#print(list(enumerate(game))) #[(0, [0, 0, 0]), (1, [0, 0, 0]), (2, [0, 0, 0])]
'''
def game_board(player=0, row=0,col=0, just_display=False):

	if not just_display:
		game[row][col] = player
	print('   a, b, c')
	for count,row in enumerate(game):
		print(count,row)

game_board(just_display=True)  
game_board(1,1,1) # game_board(player=1, row=1,col=1)
'''
''