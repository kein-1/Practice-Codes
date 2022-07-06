# def bSearchIteratively(arr,target):
    
#     start = 0
#     end = len(arr)-1
    

#     while (start <= end):
#         middle = (start+end)/2
#         if arr[middle] == target:
#             return True
#         elif arr[middle] > target:
#             end = middle-1
#         else:
#             start = middle+1
    
#     return False


def bSearchRecursively(arr,start,end,target):
    
    middle = (start+end)//2
    
    if start > end:
        return False
    
    if arr[middle] == target:
        return True
    elif arr[middle] > target:
        return bSearchRecursively(arr,start,middle-1,target)
    else:
        return bSearchRecursively(arr,middle+1,end,target)


def orderDef(arr):
    
    if not arr:
        print("EMPTY ARRAY")
    

    start = 0
    end = len(arr)-1
    
    if arr[start] <= arr[end]:
        print("SORTED INCREASING")
    else:
        print("SORTED DECREASING")

    
    
    
def main():
    
    list1 = [0,1,2,3,4,5,6,7,8]
    list2 = [8,7,6,5,4,3,2,1,0]
    #print(bSearchIteratively(list1,2))
    #print(bSearchRecursively(list1,0,8,0))
    #print(bSearchRecursively(list1,0,8,222))
    orderDef(list1)
    orderDef(list2)
    #print("Hello")
    
if __name__ == "__main__":
    main()


