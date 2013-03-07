from dcarray import *
from searcharray import *
from scanner import *
from makeIntegers import genInts,swap 
import sys
import datetime
import gnuplotter
import random

REPEATS = 10000

def main(args):
    if(4 > len(args)):
        print('Usage: python3',args[0],'lowbound datapoints distance sorted/unsorted',file=sys.stderr)
        return 1

    lowbound = args[1]
    datapoints = args[2]
    stepsize = args[3]
    sorting = args[4]

    #we need a number of items equal to the number of datapoints times
    #the distance between each
    count = datapoints * stepsize

    #sorted or unsorted
    if(sorting[0] == "s" or sorting[0] == "S"):
        values = genInts(count,lowbound,stepsize,0)
        outfile = "Sorted"
    elif(sorting[0] == "u" or sorting[0] == "U"):
        values = genInts(count,lowbound,stepsize,count)
        outfile = "Unsorted"
    else:
        # error out if not one of these things
        return 1

    results = []
    #test the searches datapoints times
    for i in range(datapoints):

        # build and fill the array
        array = SearchArray(i*stepsize)
        for j in range(i*stepsize):
            array.backadd(values[j])
            
        # the first column of the results row is the number of items
        results.append([len(array)])

        print("performing selection sort...")
        # execute the sort REPEATS times, storing each execution on the end of bulktime
        bulktime = [] 
        for j in range(REPEATS):
            start = datetime.datetime.now()
            selectionsort(array)
            end = datetime.datetime.now()
            bulktime.append((end - start).microseconds)
        results[i].append(sum(bulktime)/len(bulktime))

        print("performing insertion sort...")
        # execute the sort REPEATS times, storing each execution on the end of bulktime
        bulktime = [] 
        for j in range(REPEATS):
            start = datetime.datetime.now()
            insertionsort(array)
            end = datetime.datetime.now()
            bulktime.append((end - start).microseconds)
        results[i].append(sum(bulktime)/len(bulktime))

        print("performing merge sort...")
        # execute the sort REPEATS times, storing each execution on the end of bulktime
        bulktime = [] 
        for j in range(REPEATS):
            start = datetime.datetime.now()
            mergesort(array)
            end = datetime.datetime.now()
            bulktime.append((end - start).microseconds)
        results[i].append(sum(bulktime)/len(bulktime))

        print("performing quick sort...")
        # execute the sort REPEATS times, storing each execution on the end of bulktime
        bulktime = [] 
        for j in range(REPEATS):
            start = datetime.datetime.now()
            quicksort(array)
            end = datetime.datetime.now()
            bulktime.append((end - start).microseconds)
        results[i].append(sum(bulktime)/len(bulktime))
    #at the end, there's a massive 2D array of execution times for various amounts of data

    # build the outfile using buildtable from gnuplotter
    gnuplotter.buildtable(results,outfile)

if __name__ == '__main__':
    main(['main.py',0,10,1,'u'])
