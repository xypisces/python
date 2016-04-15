

def find_start_imooc(fname):
	f = open(fname)
	for line in f:
		if line.startswith('imooc'):
			print (line)
find_start_imooc('imooc.txt')