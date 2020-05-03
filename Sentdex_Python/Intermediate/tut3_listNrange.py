# # List comprehensions  and generator expressions


# #for i in  range(5):#generates a stream in a range of 0-4

# #list is fast because it uses more memory  - already loaded into main memory
# #generators  are slow as compared to list - uses less memory  - don't store the values in memory, it generates dynamically

# # **  lists 
# xyz = [i for i in range(5)]
# print(xyz)
# xyz = []
# for i in range(5):
# 	xyz.append(i)

# print(xyz)


# # ** generators expressions
# xyz = (i for i in range(5))  
# print(xyz) #<generator object <genexpr> at 0x0000007A327F1570>

# for i in xyz:
# 	print('generators',i)

# #xyz = [i for i in range(500000000)]
# print('done')
# #xyz = (i for i in range(500000000))  
# print(xyz)



[[print(i,ii)  for ii in range(5) ] for i in range(5)]  # one liner 2 level for loop 

xyz = (((i,ii)  for ii in range(5) ) for i in range(5))

# print(xyz)

# for i in xyz:
# 	print(i)

for i in xyz:
	for ii in i:
		print(ii) #(4, 1)(4, 2)(4, 3)

print([i for i in range(5)]) # output - [0, 1, 2, 3, 4]
[print(i) for i in range(5)] # 0 newline 1 newline 2 newline etc





