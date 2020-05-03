# Multiprocessing 

import multiprocessing


def test(num):
	print('Testing {0}'.format(num))

if __name__ == '__main__':
	for i in range(10): # 500 to see 100% CPU utilization
		p = multiprocessing.Process(target = test, args=(i,))
		p.start()
		#p.join() # wait for the process to complete the execution 


