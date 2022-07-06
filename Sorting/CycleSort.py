
# Version 1: Uses while loop to make sure start doesn't increment
def CycleSort(arr):

    start = 0

    # Only goes through n times. We swap the value based on its correct index in a sorted array.
    # In a sorted array, index = value - 1. So we can take advantage of that here: as long as our first element
    # is not in the correct position, we keep putting it into its correct position 
    for start in range(len(arr)):

        while arr[start] - 1 != start:
            # Val is where the index we need to move it to (since index = value - 1) + 
            val = arr[start]-1
            arr[start],arr[val] = arr[val],arr[start]
    
# Version 2: Uses if/else statement to move start. The key behind this is still the same: we only move our pointer
# once our current index is in the right place. Otherwise, we keep moving elements to their correct index 
def CycleSort2(arr):

    start = 0
    while start < len(arr):
        val = arr[start]-1
        if arr[start] - 1 != start:
            arr[start],arr[val] = arr[val],arr[start]   
        else:
            start+=1 
        print(arr)

def main():
    #Update comment on cylic sort 
    arr = [6,3,4,1,2,5]
    #arr1 = [1,2,3,4,5]
    end = len(arr)
    #CycleSort(arr)
    CycleSort2(arr)
    #print(arr)


if __name__ == "__main__":
    main()