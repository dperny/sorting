from dcarray import *
from copy import *

def selectionsort(inlist):
    for i in range(len(inlist)):
        mini = i
        for j in range(i+1,len(inlist)):
            #if value is less than mini
            if inlist[j] < inlist[mini]:
                mini = j

        if(mini != i):
            inlist[mini],inlist[i] = inlist[i],inlist[mini]

    return inlist
    
def insertionsort(inlist):
    # set a marker for the sorted section after the first number in the list
    # select the first unsorted number
    for i in range(1,len(inlist)):
        j = i
        while(inlist[j] < inlist[j-1] and j > 0):
            inlist[j],inlist[j-1] = inlist[j-1],inlist[j]
            j -= 1
        # advance
    return inlist

def quicksort(inlist,left = 0,right = None):
    # if the rightmost value is none, then it's the len of the list
    if right == None: right = len(inlist)
    # if the list is larger than size 1
    if (right - left) > 1:
        #pivot is the middle value
        pivot = int((left + right - 1)/2)

        # partition the list, return the point of partition
        newpivot = partition(inlist,left,right,pivot)

        quicksort(inlist,left,newpivot)
        quicksort(inlist,newpivot+1,right)

    return inlist

def partition(inlist,left,right,pivot):
    # pivotValue is the value of the item at pivot
    pivotValue = inlist[pivot]
    # move the pivotValue to the rightmost element being partitioned
    inlist[pivot],inlist[right-1] = inlist[right-1],inlist[pivot]
    # store is the leftmost index
    store = left
    # for the range from left to right, exclusive
    for i in range(left,right):
        # if i is less than the pivotvalue
        if inlist[i] < pivotValue:
            # swap i and the store
            inlist[i],inlist[store] = inlist[store],inlist[i]
            # increment store
            store += 1
    # swap the pivotvalue back in with the store
    inlist[store],inlist[right-1] = inlist[right-1],inlist[store]
    #return the location of the store
    return store


def mergesort(inlist,low=0,high=None):
    if high is None:
        high = len(inlist)

    if (high - low) <= 1:
        return inlist
    #split the list in half
    mid = int((high + low)/2)

    #mergesort the two halves
    mergesort(inlist,low,mid)
    mergesort(inlist,mid,high)

    #merge the two mergesorted halves
    merge(inlist,low,mid,high)

    return inlist


def merge(inlist,low,mid,high):
    # ok, we can use append in python. It performs in constant time
    i = low
    j = mid
    k = 0
    aux = []

    while(i < mid and j < high):
        if(inlist[i] < inlist[j]):
            aux.append(inlist[i])
            i += 1
        else:
            aux.append(inlist[j])
            j += 1
    while(i < mid):
        aux.append(inlist[i])
        i += 1
    while(j < high):
        aux.append(inlist[j])
        j += 1

    for k in range(len(aux)):
        inlist[k+low] = aux[k]

    return inlist
