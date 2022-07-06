

# Utilized Python's max and idnex functions.
# Max returns the maximum value in the array. Index returns WHERE that max value is over a start to end range. 
# Each time the range becomes smaller since we are moving from right to left, putting the max at the end
# end is len(arr) and not len(arr)-1 because we want to include the last element in the index for max() and index(). It is
# not inclusive at the end so that is why we need to provide len(arr)
def SelectionSortIteratively(arr):

    start = 0
    end = len(arr)

    while start < end:
        
        # Finds the maw element of the array up to the last end index (since we are constanty putting
        # the last element at the end 
        maxVal = max(arr[:end])
        # Finds the max index of where maxVal is. This produces the first occurance 
        maxIndex = arr.index(maxVal,start,end)
        

        arr[end-1],arr[maxIndex] = arr[maxIndex],arr[end-1]
        end-=1

def SelectionSortRecursively(arr,end):

    start = 0

    #When arr shrinks till the end, we return. 
    if start >= end:
        return
    
    maxVal = max(arr[:end])
    maxIndex = arr.index(maxVal,start,end)
        
    arr[end-1],arr[maxIndex] = arr[maxIndex],arr[end-1]
    SelectionSortRecursively(arr,end-1)
def main():

    arr = [3,1,8,9,2,3,5]
    #arr1 = [1,2,3,4,5]
    end = len(arr)
    
    # SelectionSortIteratively(arr)
    SelectionSortRecursively(arr,end)
    print(arr)


if __name__ == "__main__":
    main()