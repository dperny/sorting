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

def quicksort(inlist,left,right):
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

def quicksort(inlist,left,right):
    #pick a pivot element
    if left < right:
        pivot = int((left+right)/2)

        

def partition(inlist,left,right,pivot):
    pivotValue = inlist[pivot]
    inlist[pivot],inlist[right] = inlist[right],inlist[pivot]
    store = left
    for i in range(left,right):
        if inlist[i] > pivotValue:
            inlist[i],inlist[store] = inlist[store],inlist[i]
            store += 1
        inlist[store],inlist[right] = inlist[right],inlist[store]


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
