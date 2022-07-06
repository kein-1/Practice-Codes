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