'''created by fwk
   2018/3/15
   parser lexer's result
'''


import os
path = os.path.join(os.path.basename(__file__), '../')
def parse():
	f = open(os.path.join(path, 'fwk.txt'), 'r')
	token = []
	for i in f.readlines()[1:]:
		token.append(i.split(',')[0].split('=')[1])

	f.close()
	return ''.join(token)

if __name__ == '__main__':
	print parse()