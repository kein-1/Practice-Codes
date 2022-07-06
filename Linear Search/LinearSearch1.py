
#Q1: Search for a specific char in a string
from re import L


def searchString(word,targetChar):

    if word.length() == 0:
        return False
    if targetChar.lower() in word.lower():
        return True
    return False


#Q2: Search in the range of two indexes
def searchRange(list,target,start,end):
    
    for i in range(start,end+1):
        if list[i] == target:
            return True
    return False

#Q3: Min Number
def searchMin(list):

    if len(list) == 0:
        print("EMPTY LIST")
        return 0
    min = list[0]
    for i in range (len(list)):
        if list[i] < min:
            min = list[i]
    return min

def main():
    #Q1 Tests
    # print(searchString("Mochi","m"))
    # print(searchString("Mochi","z"))


    #Q2 Tests
    # arr = [1,2,3,4,5,6]
    # print(searchRange(arr,4,1,4))

    #Q3 Tests
    arr = [3,-2,1,20,-9]
    print(searchMin(arr))



if __name__=="__main__":
    main()