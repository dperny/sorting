def main():
    sortedArr = [1,2,2,2,3,4,5,6,7,8,9]
    unsortedArr = [1,2,3,4,5,6,7,9,8]

    print('sortedArr is', isSorted(sortedArr))
    print('unsortedArr is', isSorted(unsortedArr))

    
def isSorted(arr):
    flag = True

##    i = 0
##    while ((flag==True) and (i<(len(arr)-1))):
##        if arr[i] > arr[i+1]:
##            flag = False
##        i+=1
##    
##        if not(arr[i] <= arr[i+1]):
##            flag = False
##        i+=1
##	
    for i in range(len(arr)-1):
        if arr[i] >arr[i+1]:
            flag = False
##        if not(arr[i] <= arr[i+1]):
##            flag = False

		
	
    return flag
            
main()
