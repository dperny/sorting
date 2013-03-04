from dcarray import *
from scanner import *
from makeIntegers import *
import sys
import datetime
import gnuplotter
from copy import *

def main(args):
	if(4 > len(args)):
		print('Usage: python3',args[0],'searchtype timevalue datafile',file=sys.stderr)
		return 1

	values = 1 
	stringout = ""
	values = makeIntegers(start,stop,step,swap)
	while(values <= 100):
		# make the master array, which we will sort many, many times
		original = DCArray(values)

		#this fills the master with the requested number of elements
		i = 0
		while(i < values):
			original.backadd(values[i])
			i += 1

		# first, do selection sort
		if(args[1][0] == 's' or args[1][0] == 'S'): 
			print("running selection sort")
			time = []
			for i in range(len(10000)):
				# make a copy of the original, to sort same data every time
				array = deepcopy(original)

				start = datetime.datetime.now()
				array.ssort()
				end = datetime.datetime.now()
				# add the elapsed time the giant array we're going to later average
				time.append((end - start).microseconds)

			averageTime = sum(time)/len(time)

		else:
			print("Invalid searchtype",file=sys.stderr)
			return 1

		# time = end - start
		# elapsedTime = time.microseconds
		stringout = stringout + str(values) + ' ' + str(averageTime) + '\n'

		values += 5

	outfile = args[1] + '.out'
	with open(outfile,"w") as out:
		out.write(stringout)

	gnuplotter.buildgraph(args[1],args[2])

	return

if __name__ == '__main__':
	main(sys.argv)