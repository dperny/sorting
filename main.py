from dcarray import *
from scanner import *
import sys
import datetime
import gnuplotter

def main(args):
	if(4 > len(args)):
		print('Usage: python3',args[0],'searchtype timevalue datafile',file=sys.stderr)
		return 1

	values = 1 
	stringout = ""
	while(values <= 20):
		array = DCArray(values)
		s = Scanner(args[3])
		i = 0
		while(i < values):
			array.backadd(s.readint())
			i += 1

		if(args[1][0] == 'l' or args[1][0] == 'L'): 
			print("running linear search...")
			start = datetime.datetime.now()
			array.lsearch(30001)
			end = datetime.datetime.now()
		elif(args[1][0] == 'b' or args[1][0] == 'B'):
			print("running binary search...")
			start = datetime.datetime.now()
			array.bsearch(30001)
			end = datetime.datetime.now()
		else:
			print("Invalid searchtype",file=sys.stderr)
			return 1

		time = end - start
		elapsedTime = time.microseconds
		stringout = stringout + str(values) + ' ' + str(elapsedTime) + '\n'

		values += 1

	outfile = args[1] + '.out'
	with open(outfile,"w") as out:
		out.write(stringout)

	gnuplotter.buildgraph(args[1],args[2])

	return

if __name__ == '__main__':
	main(sys.argv)