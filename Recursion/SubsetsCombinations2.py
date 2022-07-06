

# Q1: Find all subsets of the given text
# This is like merge sort calls, quick sort calls, Binary Search Tree BFS and DFS recursion calls in that
# Each function call will have two separate calls 

# How it works is we pass the string each time. Instead of creating it in the call, we 
# pass it as a parameter that gets updated with each function call. This is top-down approach whereas
# if we build it in the function, it will be a bottom-up approach (like what we did with the string 
# questions earlier)
def subsets(text,emptyString):

    
    if len(text) <= 0:
        print(emptyString)
        return
    
    # How to add and how to ignore? 

    temp = text[0]

    subsets(text[1:],emptyString+temp)
    subsets(text[1:],emptyString)

#Q1A: Return a list of subset strings instead of printing by passing the list as parameter (easy)
def subsets2(text,emptyString,newList):

    
    if len(text) <= 0:
        newList.append(emptyString)
        return
    
    # How to add and how to ignore? 

    temp = text[0]

    subsets2(text[1:],emptyString+temp,newList)
    subsets2(text[1:],emptyString,newList)

#Q2: Return a list of subset strings WITHOUT passing the list as a parameter (like above in 1A)
def subsets3(text,emptyString):

    
    if len(text) <= 0:
        
        return [emptyString]
    
    # This part was very tricky with the return. Basically the function calls return the TWO subsequent function calls
    # Thus each function is returning a list [], as noted in the base condition 

    temp = text[0]
    return subsets3(text[1:],emptyString+temp) + subsets3(text[1:],emptyString)
    



def main():
    
    word = "abc"
    subsS = []
    #subsets(word,"")
    #subsets2(word,"",subsS)
    #print(subsS)
    newDups = subsets3(word,"")
    print(newDups)


if __name__=="__main__":
    main()
