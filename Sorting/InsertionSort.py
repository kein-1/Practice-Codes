



# Idea behind insertion sort is we sort each partial subarray, starting from 0. 
# Counter is used so we move from right to left, but we are sorting starting from 0 to 1,
# 0 to 2 etc
def InsertionSortIteratively(arr):

    start = 0
    counter = 1
    steps = 0

    while counter < len(arr):
        j = counter 
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
                j-=1
                steps+=1
            else:
                j-=1
        print(arr)
        counter +=1
        
def main():

    arr = [3,1,8,9,2,3,5]
    #arr1 = [1,2,3,4,5]
    end = len(arr)
    InsertionSortIteratively(arr)
    #print(arr)


if __name__ == "__main__":
    main()