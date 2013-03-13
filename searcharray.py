from dcarray import *
from copy import *

class SearchArray(DCArray):
    """a class for testing search methods

    contains search methods to use on DCArray, as well as methods to refresh
    the store of the array to research the same list."""


    def __init__(self,capacity):
        self._store = [0] * capacity
        self._capacity = capacity
        self._factor = 2
        self._size = 0
        self._startIndex = 0
        self._endIndex = 0

        self._default = None

    def mark(self):
        self._default = deepcopy(self._store)

    def refresh(self):
        if self._default is not None:
            self._store = deepcopy(self._default)
        else:
            return 1

def selectionsort(inlist):
    # for each value in the list
    for i in range(len(inlist)):
        minimum = i
        # for each value in the rest of the list
        for j in range(i+1,len(inlist)):
            # if this value is less than the minimum value,
            if inlist.get(j) < inlist.get(minimum):
                # then it is the new minimum
                minimum = j

        # move the new minimum to the front.
        if(minimum != i):
            tmp = inlist.get(i)
            inlist.set(i,inlist.get(minimum))
            inlist.set(minimum,tmp)

        return inlist
    
def insertionsort(inlist):
    # set a marker for the sorted section after the first number in the list
    # select the first unsorted number
    for i in range(1,len(inlist)):
        # swap to the left until it's in the right spot
        j = i
        while(inlist.get(j) < inlist.get(j-1) and j > 0):
            tmp = inlist.get(j)
            inlist.set(j,inlist.get(j-1))
            inlist.set(j-1,tmp)
            j -= 1
        # advance
    return inlist

def quicksort(inlist,start,length):
    #pick a pivot element
    if(len(inlist) <= 1):
        return inlist
    pivot = int(len(inlist)/2)
    lessers = SearchArray(len(inlist))
    greaters = SearchArray(len(inlist))

    for i in range(len(inlist)):
        if(i == pivot):
            pass
        elif(inlist.get(i) > inlist.get(pivot)):
            greaters.backadd(inlist.get(i))
        else:
            lessers.backadd(inlist.get(i))

    lessers = quicksort(lessers)
    greaters = quicksort(greaters)
    outlist = SearchArray(len(inlist))

    for i in range(len(lessers)):
        outlist.backadd(lessers.get(i))
    outlist.backadd(inlist.get(pivot))
    for i in range(len(greaters)):
        outlist.backadd(greaters.get(i))

    return outlist


def mergesort(inlist,low,mid,aux):
    if (low - mid) <= 1:
        return inlist
    #split the list in half
    middle = int((low - mid)/2)

    #mergesort the two halves
    inlist = merge(mergesort(inlist,low,mid,aux),mergesort(inlist,mid,len(inlist),aux))


def merge(inlist,low,mid,high,aux):
    i = low
    j = mid
    k = 0
    while(i < mid and j < high):
        if(inlist[i] < inlist[j]):
            aux[k] = inlist[i]
            i += 1
            k += 1
        else:
            aux[k] = inlist[j]
            j += 1
            k += 1
    while(i < mid):
        aux[k] = inlist[i]
        i += 1
        k += 1
    while(j < high):
        aux[k] = inlist[j]
        j += 1
        k += 1
    return aux
"""
def mergesort(inlist):
    if len(inlist) <= 1:
        return inlist
    middle = int(len(inlist)/2)

    left = SearchArray(middle)
    for i in range(0,middle):
        left.backadd(inlist.get(i))

    right = SearchArray(middle)
    for i in range(middle,len(inlist)):
        right.backadd(inlist.get(i))

    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    result = SearchArray(len(right) + len(left) + 1)
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left.get(i) <= right.get(j):
            result.backadd(left.get(i))
            i += 1
        else:
            result.backadd(right.get(j))
            j += 1

    while(i < len(left)):
        result.backadd(left.get(i))
        i += 1
    while(j < len(right)):
        result.backadd(right.get(j))
        j += 1

    return result

def testsort(inlist):
    for i in (range(1,len(inlist))):
        if(inlist.get(i-1) > inlist.get(i):
            return False
    return True
"""