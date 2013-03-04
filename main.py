from dcarray import *
from scanner import *
import sys
import datetime
import gnuplotter
import random

def main(args):
    if(4 > len(args)):
        print('Usage: python3',args[0],'lowbound datapoints stepsize sorted/unsorted',file=sys.stderr)
        return 1

    # build the list of integers we're going to read from
    random.seed()
    start = random.randint(0,100)
    #we need a number of items equal to the number of datapoints times
    #the distance between each
    count = args[2] * args[3]
    step = random.randint(0,10)
    #sorted or unsorted
    if(args[4][0] = "s"):
        values = makeIntegers(count,start,step,0)
    elif(args[4][0] = "u"):
        values = makeIntegers(count,start,step,count)
    else:
        return 1

    results = []
    for i in range(count):

        data = SearchArray(i*steps)
        for j in range(len(data)):
            array.backadd(values[j])
        array.default()

        #test the searches count times

    #at the end, there's a massive 2D array of execution times for various amounts of data

    #use the buildtable function from gnuplotter to build a table of data and write out





if __name__ == '__main__':
    sys.exit(main(sys.argv))
