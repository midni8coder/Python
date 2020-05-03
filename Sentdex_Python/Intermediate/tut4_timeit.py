# Time it module 

import timeit


print(timeit.timeit('xyz= [i for i in range(1000)]',number=1))
print(timeit.timeit('xyz= [i for i in range(1000)]',number=300))