

# Q1: Find all subsets of the given text
# This is like merge sort calls, quick sort calls, Binary Search Tree BFS and DFS recursion calls in that
# Each function call will have two separate calls 

# How it works is we pass the string each time. Instead of creating it in the call, we 
# pass it as a parameter that gets updated with each function call. This is top-down approach whereas
# if we build it in the function, it will be a bottom-up approach (like what we did with the string 
# questions earlier)
def subsets(text,emptyString,start):

    
    if start >= len(text):
        print(emptyString)
        return
    
    # How to add and how to ignore? 

    temp = text[start]

    subsets(text,emptyString+temp,start+1)
    subsets(text,emptyString,start+1)

#Q1A: Return a list of subset strings instead of printing by passing the list as parameter (easy)
def subsets2(text,emptyString,start,newList):

    
    if start >= len(text):
        newList.append(emptyString)
        print(emptyString)
        return
    
    # How to add and how to ignore? 

    temp = text[start]

    subsets2(text,emptyString+temp,start+1,newList)
    subsets2(text,emptyString,start+1,newList)

#Q2: Return a list of subset strings WITHOUT passing the list as a parameter (like above in 1A)
def subsets3(text,emptyString,start):

    
    if start >= len(text):
        
        return [emptyString]
    
    # This part was very tricky with the return. Basically the function calls return the TWO subsequent function calls
    # Thus each function is returning a list [], as noted in the base condition 

    temp = text[start]
    return subsets3(text,emptyString+temp,start+1) + subsets3(text,emptyString,start+1)
    



def main():
    
    word = "abc"
    #subsS = []
    #subsets(word,"",0)
    #subsets2(word,"",0,subsS)
    newDups = subsets3(word,"",0)
    print(newDups)


if __name__=="__main__":
    main()
