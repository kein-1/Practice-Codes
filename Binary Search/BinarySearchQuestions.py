
#Q1: Find the ceiling of a target number in a sorted array.
#A ceiling is defined as the smallest number equal to or greater 
# than the target
def ceiling(arr,target):

    start = 0
    end = len(arr)-1
    if arr[end] < target:
        print("Error")
        return -1
    #Continue until they are not equal. 
    while start <= end:
        middle = (start+end)//2
        print(start,end,middle)
        if arr[middle] == target:
            return arr[middle]
        elif arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1

# At this point the middle is not our target AND the loop broke. 
# Why do we return start? Before the loop breaks, the middle element is equal to start. That 
# Is the last time the loop will run. If our target element is NOT start (which is middle), the loop
# Will break and start = end + 1
# In a sorted array, this must mean the next item is our next largest integer 
    print(start,end,middle)
    return arr[start]



#Q2: Find the floor of a number. A floor is the greatest smallest number that is less than or equal to our target

def floor(arr,target):

    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start+end)//2

        if arr[middle] == target:
            return arr[middle]
        elif arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    
    #Same as above but instead of returning start, we return end 
    return arr[end]

    

def main():
    
    list1 = [14,16,17,19,20]
    print(ceiling(list1,15))
    # print(floor(list1,15))
    # print(floor(list1,7))
    
if __name__ == "__main__":
    main()


