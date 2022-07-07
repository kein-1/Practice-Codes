



def Bsearch(list,target,start,end):

    middle = int((start+end)/2)

    if start > end:
        return False

    if list[middle] == target:
        return True
    elif list[middle] > target:
        print(f"Searching from {list[start]} to {list[middle]}")
        return Bsearch(list,target,start,middle)
    else:
        print(f"Searching from {list[middle+1]} to {list[end]}")
        return Bsearch(list,target,middle+1,end)
    

def main():

    list1 = [0,1,2,3,4,5,6,7,8]
    length = len(list1)
    print(Bsearch(list1,0,0,length-1))
    print(Bsearch(list1,8,0,length-1))






if __name__ == "__main__":
    main()