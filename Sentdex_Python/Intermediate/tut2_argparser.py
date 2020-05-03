# Argparse for CLI 
import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x', type=float, default=1.0,
						help='x value')
	parser.add_argument('--y', type=float, default=1.0,
						help='y value')
	parser.add_argument('--operation', type=str, default='add',
						help='operation(mul,div,sub,add)')
	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))

def calc(args):
	operation = args.operation
	x= args.x
	y= args.y
	if operation == 'add':
		return x+y
	if operation == 'mul':
		return x*y
	if operation == 'sub':
		return x-y
	if operation == 'div':
		return x/y

main()
#if __name__ == '__main__':
	#main()