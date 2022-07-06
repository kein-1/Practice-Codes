
def QuickSort(arr,low,high):

    # We use s and e because these will be our pointers. Since this is a recursive algorithm 
    # we cannot just decrement low and high. If we do, we will lose track of our list 
    s = low
    e = high

    # Pick a pivot. All numbers to the left of pivot should be less than pivot 
    # While all numbers to the right of pivot should be greater than pivot 
    pivValue = (arr[low] + arr[high])//2

    if low >= high:
        return
    while s < e:

        print(f"Before: {s}, {e}, {pivValue}")
        # We start until we find an element that is greater than pivot
        while arr[s] < pivValue:
            s+=1
        
        # We start until we find an element that is less than pivot
        while arr[e] > pivValue:
            e-=1
        if s <= e:
        #Swap the two, then decrement s and e
            arr[e], arr[s] = arr[s], arr[e]
            s+=1
            e-=1
        print(f"After: {s}, {e}")
        print(arr)
        
    print("=====")
    print(arr)

    #Recursive call on the left side will be low to e, because e is constantly moving left 
    QuickSort(arr,low,e)

    #Recursive call on the right side will be s to high, because s is constantly moving right
    QuickSort(arr,s,high)

def main():
    arr = [9,3,7,5,6,4,8,2]
    # arr = [9,2,7,8,1,3,10,4,5,6]

    print(arr)
    QuickSort(arr,0,7)
    print(arr)
    # print(arr)
    

if __name__=="__main__":
    main()