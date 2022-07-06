def MergeSort(arr,low,high):
    
		#If we get down to only one element, return that element as an array
    if low == high:
        return [arr[low]]
    
    mid = (low + high)//2 
    
    tempArr1 = MergeSort(arr,low,mid)
    tempArr2 = MergeSort(arr,mid+1,high)
    
    return Merge(tempArr1,tempArr2)
        

def Merge(arr1,arr2):
    
    merged = []
    curr1 = curr2 = 0

    #Runs until we reach the end of either list
    while curr1 < len(arr1) and curr2 < len(arr2):
        if arr1[curr1] <= arr2[curr2]:
            merged.append(arr1[curr1])
            curr1+=1
        else:
            merged.append(arr2[curr2])
            curr2+=1

    #Appends the remaining elements in the list that is left. Only one of 
		#the loop below will run 
    while curr1 < len(arr1):
        merged.append(arr1[curr1])
        curr1+=1
    while curr2 < len(arr2):
        merged.append(arr2[curr2])
        curr2+=1
    
    return merged

def main():
    arr = [9,3,7,5,6,4,8,2]
    arr1 = [1,3,5,7,9]
    arr2 = [2,4,6,8,10]
    print(arr)
    #print(Merge(arr1,arr2))
    arr = MergeSort(arr,0,7)
    print(arr)

if __name__=="__main__":
    main()