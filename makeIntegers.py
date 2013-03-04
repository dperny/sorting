import sys
import random

def main(args):
    # make sure we have enough args
    if(len(args) < 5):
        print("USAGE: python3 {0} <count> <start> <step> <swaps>".format(args[0]))
        return 1
    #call genInts, which returns the list of integers
    ints = genInts(int(args[1]), int(args[2]), int(args[3]), int(args[4]))
    #print out the integers, 1 line no spaces
    for i in ints:
        print(str(i),end=" ")
    # newline characters, for your health
    print()

    return

def genInts(count,start,step,swaps):
    # make a list by making a range
    # make a range from start to end (defined as count*step) with step
    array = list(range(start,(count*step),step))
    # swap the values swaps times
    i = 0
    while(i < swaps):
        array = swap(array)
        i += 1

    return array

def swap(array):
    #initialize a random thing
    random.seed()
    # two random points between the beginning and then of the list
    i = random.randint(0,len(array)-1)
    j = random.randint(0,len(array)-1)
    # if the points are the same, get a new j
    while(j == i): 
        j = random.randint(0,len(array)-1)
    # swap the values
    array[i],array[j] = array[j],array[i]

    return array

if __name__ == '__main__':
    sys.exit(main(sys.argv))
