
# Q1: Delete all characters as stated in a given string
# Note in python, strings are immutable. Need to create a new string 
# Basically at each function call we eithe return an empty char (if it is equal to target) OR 
# we return that char itself 

from unittest import skip


def deleteCharInString(stringstuff,start,target):

    temp=""
    if start >= len(stringstuff):
        return ""
    
    if stringstuff[start] != target:
        temp+=stringstuff[start]
    
    return temp + deleteCharInString(stringstuff,start+1,target)

# Q2: Skip a particular string 
# i.e if we are given "bcdapplefg" and we want to skip "apple", we should return "bcdfg"

def skipString(stringstuff,start,target):

    temp = ""
    
    if start >= len(stringstuff):
        return ""
    #If we found that string, we skip ahead based on the length of it
    if stringstuff[start:start+len(target)] == target:
        start+=len(target)-1
    else:
        temp+=stringstuff[start]
    
    print(stringstuff[start:start+len(target)])
    return temp + skipString(stringstuff,start+1,target)


def main():
    
    # word = "baccad"
    # newWord = deleteCharInString(word,0,'a')
    # print(newWord)
    string2 = "bcdapplefg"
    newString = skipString(string2,0,"apple")
    print(newString)

if __name__=="__main__":
    main()
