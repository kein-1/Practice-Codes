

# Q1: Determine if an array is sorted or not
from re import A


def sortedOrNot(arr,start,end):


    if start == end:
        return True
    if arr[start] > arr[start+1]:
        return False
    return sortedOrNot(arr,start+1,end)


# Q2: Return an array of indicies as to where our target element exists
# i.e if our array is [1,2,3,4,4,8], we return [3,4] since that is our indicies 
# Method 1: Creating the list in reverse: basically we are adding the elements WHEN we are returning. 
# Each function call 
def atIndices(arr,start,target):

    dupp = []
    
    if start >= len(arr):
        return []
    
    if arr[start] == target:
        dupp.append(start)
    return dupp + atIndices(arr,start+1,target)
    
# Method 2: Passing in the list as an argument
# Edit: This works since ans is passed as by reference 
def atIndices2(arr,start,target,ans):

    if start >= len(arr) - 1:
        return 
    
    if arr[start] == target:
        ans.append(start)
    return atIndices2(arr,start+1,target,ans)


def main():
    # arr = [6,3,4,1,2,5]
    # arr1 = [1,2,3,4,5]
    # print(sortedOrNot(arr,0,len(arr)-1))
    # print(sortedOrNot(arr1,0,len(arr1)-1))

    arr = [1,2,3,4,4,8]
    arr2 = [1,2,3,4]
    ans = []
    
    print(atIndices(arr,0,4))
    # atIndices2(arr,0,4,ans)
    # print(ans)
    

if __name__=="__main__":
    main()