

# Iteratively, the loop will end when start < end. We use j as a pointer to iterate through the array
# to the last element. We are pushing the biggest value up to the end. When the loop ends, we decrease the 
# size of the end element by 1. Why? Because the last element already has the biggest element. It does not 
# make sense to still compare the last element 

def BubbleSortIteratively(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        j = start
        # Boolean value in case the array is sorted. If no swapping occurs, just break out of the loop. This time complexity
        # is O(n) because the j loop will not run after n times since no swapping occured 
        swapped = False
        while j < end:

            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j], arr[j+1]
                j+=1
                swapped = True
            else:
                j+=1 
            print(arr)
        
        if swapped == False:
            print("It is sorted")
            break

        end -= 1
    
def BubbleSortRecursively(arr,start,end):
    if start >= end:
        return
    j = start
    swapped = False
    while j < end:
        if arr[j] > arr[j+1]:
            arr[j+1],arr[j] = arr[j], arr[j+1]
            j+=1
            swapped = True
        else:
            j+=1
    if swapped == False:
        print("It is sorted")
        return
    BubbleSortRecursively(arr,start,end-1)

def main():

    arr = [3,1,8,9,2,3,5]
    arr1 = [1,2,3,4,5]
    #BubbleSortIteratively(arr1)
    end = len(arr)-1
    
    BubbleSortRecursively(arr,0,end)
    # print(arr)



if __name__ == "__main__":
    main()