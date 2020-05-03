#strings  - concatenations, format 


names  = ['Devid','Raj', 'Samantha']

#for name in names:
	#print('Hello..!! ' + name)
#	print(' '.join(['Hello there ', name]))

print(', '.join(names))
import os
path = 'F:\\Devid'
file_name = 'SQLServer.txt'
full_file_path = path +'\\'+file_name

with open(os.path.join(path,file_name))  as file:
	print(file.read())


# eating 1 apple a day keeps your Doctor away
num= 2
person = 'Girlfriend'
string = 'eating '+str(num)+' apple a day keeps your '+person+' away'
print(string)
print('eating {} apple a day keeps your {} away'.format(num,person))
print('eating {1} apple a day keeps your {0} away'.format(num,person))
print(f'eating {0} apple a day keeps your {1} away',num,person)